import pyaudio
import numpy as np
import notes

# p = pyaudio.PyAudio()

volume = 1.00     # range [0.0, 1.0]
fs = 48000       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
#f = 440.0        # sine frequency, Hz, may be float

#gen a saw wave
def genSaw(freq):
    samples = np.zeros(fs)
    dist = 2 / (fs / freq)
    samples[0] = -1.0
    for a in range(1, fs):
        if samples[a - 1] >= 1.0:
            samples[a] = -1.0
        else:
            samples[a] = samples[a - 1] + dist
    # print(samples[:120])
    return samples.astype(np.float32)

#gen a stereo saw wave (in progress)
def genStereoSaw(freq, voices):
    offset = 50 #how delayed one side is from the other (0 = mono, 100-2000 spread)
    if voices <= 0 or voices > 3: #currently supporting 1-3 voices
        voices = 1
    left = np.zeros(fs).astype(np.float32)
    right = np.zeros(fs).astype(np.float32)
    output = np.zeros(fs * 2).astype(np.float32)
    dist = 2 / (fs / freq)
    left[0] = -1.0
    for a in range(1, fs):
        if left[a - 1] >= 1.0:
            left[a] = -1.0
        else:
            left[a] = left[a - 1] + dist
    right[offset]
    for a in range(offset, fs):
        if right[a - 1] >= 1.0:
            right[a] = -1.0
        else:
            right[a] = right[a-1] + dist
    #combine the left and right channel
    count = 0
    for b in range(0, fs * 2):
        if b < 48000:
            if (b % 2 == 0):
                output[b] = left[count]
            else:
                output[b] = right[count]
            count += 1
    # print (output[:40])
    # play(output.tobytes())
    return output

def genRevSaw(freq):
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

#averages a list of stereo waves to play multiple notes at once
def addStereoWaves(waves):
    if not waves:
        return 0
    if len(waves) == 1:
        return waves[0]
    num = len(waves)
    output = np.zeros(fs*2).astype(np.float32)
    for a in waves:
        for b in range(0,fs*2):
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
    testWaves.append(genSaw(notes.getFreq2("E","4", 0)))
    testWaves.append(genSaw(notes.getFreq2("E","4", 0)))
    # testWaves.append(genSaw(notes.getFreq("G#/Ab","4"),0))
    testWaves.append(genSaw(notes.getFreq2("B","4", 0)))
    # testWaves.append(addSub(41.20))
    # samples = addWaves(testWaves)
    samples = panTest(testWaves)
    return samples

def makeStereoWaves(inList):
    testWaves = []
    for a in inList: #inList format: [note, octave, voices, detune]
        testWaves.append(genStereoSaw(notes.getFreq2(a[0], a[1], int(a[3])),int(a[2])))
    # testWaves.append(genStereoSaw(notes.getFreq2("E","3", 8),1))
    # testWaves.append(genStereoSaw(notes.getFreq2("E","3", -8),1))
    # testWaves.append(genStereoSaw(notes.getFreq2("E", "4", 12), 1))
    # testWaves.append(genStereoSaw(notes.getFreq2("E", "4", -12), 1))
    # testWaves.append(genStereoSaw(notes.getFreq2("A", "5", 0), 1))
    # play(addStereoWaves(testWaves))
    return addStereoWaves(testWaves)
#
# def play(samples):
#     stream = p.open(format=pyaudio.paFloat32,
#                         channels=2,
#                         rate=fs,
#                         output=True)
#     stream.write(samples)
#     stream.stop_stream()
#     stream.close()
#
# p.terminate()