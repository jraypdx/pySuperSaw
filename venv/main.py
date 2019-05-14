import pyaudio
import numpy as np
from appJar import gui
import matplotlib.pyplot as plt
import notes
import ssgui

p = pyaudio.PyAudio()

volume = 1.00     # range [0.0, 1.0]
fs = 48000       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
#f = 440.0        # sine frequency, Hz, may be float

#gen a saw wave
def genSaw(freq, detune):
    samples = np.zeros(fs)
    dist = 2 / (fs / freq)
    if detune:
        dist += (dist/1000 * detune)
    samples[0] = -1.0
    for a in range(1, fs):
        if samples[a - 1] >= 1.0:
            samples[a] = -1.0
        else:
            samples[a] = samples[a - 1] + dist
    # print(samples[:120])
    return samples.astype(np.float32)

def genRevSaw(freq, detune):
    samples = np.zeros(fs)
    dist = 2 / (fs / freq)
    samples[0] = 1.0
    for a in range(1, fs):
        if samples[a - 1] <= -1.0:
            samples[a] = 1.0
        else:
            samples[a] = samples[a - 1] - dist
    # print(samples[:120])
    return samples.astype(np.float32)

#averages a list of waves to play multiple notes at once
def addWaves(waves):
    num = len(waves)
    output = np.zeros(fs).astype(np.float32)
    for a in waves:
        for b in range(0,fs):
            output[b] = (output[b] + a[b])
    for o in output:
        o /= num
    return output.tobytes()

def panTest(waves):
    count = 0
    left = np.zeros(fs).astype(np.float32)
    right = np.zeros(fs).astype(np.float32)
    output = np.zeros(fs*2).astype(np.float32)
    for a in range(0,fs):
        left[a] = (waves[0][a] + (0.25 * waves[1][a])) / 2
        right[a] = (waves[0][a] + (1.5 * waves[1][a])) / 2
    for b in range(0,fs*2):
        if b < 48000:
            if (b % 2 == 0):
                output[b] = left[count]
            else:
                output[b] = right[count]
            count += 1
    # print (output[:40])
    return output.tobytes()

def addSub(freq):
    return (np.sin(2 * np.pi * np.arange(fs) * freq / fs)).astype(np.float32)

def makeWaves(inList):
    testWaves = []
    testWaves.append(genSaw(notes.getFreq("E","4"),5))
    testWaves.append(genSaw(notes.getFreq("E","4"),-5))
    # testWaves.append(genSaw(notes.getFreq("G#/Ab","4"),0))
    testWaves.append(genSaw(notes.getFreq("B","4"),3))
    # testWaves.append(addSub(41.20))

    # samples = addWaves(testWaves)
    samples = panTest(testWaves)
    return samples

def play(samples):
    stream = p.open(format=pyaudio.paFloat32,
                        channels=2,
                        rate=fs,
                        output=True)
    stream.write(samples)
    stream.stop_stream()
    stream.close()

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        samples = makeWaves(0)
        play(samples)

app = gui(showIcon=False)
ssgui.buildgui(app)

app.go()

# def press(button):
#     wave = app.getRadioButton("wave")
#     #freq = app.getEntry("Frequency")
#     vol = float(app.getScale("Volume") / 100)
#     #print (vol)
#     if button == "Cancel":
#         app.stop()
#     else:
#         freq = notes.getFreq(app.getOptionBox("Note"), str(app.getOptionBox("Octave")))
#         playSound(freq, wave, vol)

# app = gui()
# app.addLabelOptionBox("Note", ["C", "C#/Db", "D",
#                         "D#/Eb", "E", "F", "F#/Gb", "G",
#                         "G#/Ab", "A", "A#/Bb", "B"])
# app.addLabelOptionBox("Octave", ["3", "4", "5"])
# app.addButtons(["Play", "Cancel"], press)
# app.go()

p.terminate()