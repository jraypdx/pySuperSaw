# todo:
#  - add a sub bass?
#  - add reverb?

import pyaudio
import numpy as np
from appJar import gui
# import matplotlib.pyplot as plt
import notes, saws

p = pyaudio.PyAudio()

volume = 1.00     # range [0.0, 1.0]
fs = 48000       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
#f = 440.0        # sine frequency, Hz, may be float

def play(samples):
    stream = p.open(format=pyaudio.paFloat32,
                        channels=2,
                        rate=fs,
                        output=True)
    stream.write(samples)
    stream.stop_stream()
    stream.close()



def press(button):
    if button == "Close":
        app.stop()
    else:
        waves = [] #format: Note, Octave, Voices, Detune
        for a in range (1,4+1):
            if (app.getScale("Volume " + str(a))):
                note = app.getOptionBox("Note " + str(a))
                octave = app.getOptionBox("Octave " + str(a))
                voices = app.getOptionBox("Voices " + str(a))
                detune = app.getEntry("Detune " + str(a))
                vol = app.getScale("Volume " + str(a))
                if detune == '':
                    detune = 0
                # print (str(a) + " det: " + str(detune))
                waves.append([note, octave, voices, detune, vol])
        if waves:
            play(saws.makeStereoWaves(waves))
        else:
            print("Please select at least one wave to use")

#I probably should have used a loop to make the gui...
app = gui(showIcon=False)
app.setTitle("pySuperSaw")
app.startFrame("frame 1", row=0, column=0)
#app.addCheckBox("Use 1")
app.addLabelScale("Volume 1")
app.showScaleValue("Volume 1")
app.addLabelOptionBox("Note 1", ["C", "C#/Db", "D",
                                 "D#/Eb", "E", "F", "F#/Gb", "G",
                                 "G#/Ab", "A", "A#/Bb", "B"])
app.addLabelOptionBox("Octave 1", ["2", "3", "4", "5", "6"])
# app.addScale("Detune 1", row=3, column=1)
app.addLabelOptionBox("Voices 1", ["1", "2", "3", "4"])
app.addLabel("Detune 1 (-100 to 100):")
app.addEntry("Detune 1")
app.stopFrame()

app.startFrame("frame 2", row=0, column=1)
# app.addCheckBox("Use 2")
app.addLabelScale("Volume 2")
app.showScaleValue("Volume 2")
app.addLabelOptionBox("Note 2", ["C", "C#/Db", "D",
                                 "D#/Eb", "E", "F", "F#/Gb", "G",
                                 "G#/Ab", "A", "A#/Bb", "B"])
app.addLabelOptionBox("Octave 2", ["2", "3", "4", "5", "6"])
app.addLabelOptionBox("Voices 2", ["1", "2", "3", "4"])
app.addLabel("Detune 2 (-100 to 100):")
app.addEntry("Detune 2")
app.stopFrame()

app.startFrame("frame 3", row=1, column=0)
app.addLabel("")
# app.addCheckBox("Use 3")
app.addLabelScale("Volume 3")
app.showScaleValue("Volume 3")
app.addLabelOptionBox("Note 3", ["C", "C#/Db", "D",
                                 "D#/Eb", "E", "F", "F#/Gb", "G",
                                 "G#/Ab", "A", "A#/Bb", "B"])
app.addLabelOptionBox("Octave 3", ["2", "3", "4", "5", "6"])
app.addLabelOptionBox("Voices 3", ["1", "2", "3", "4"])
app.addLabel("Detune 3 (-100 to 100):")
app.addEntry("Detune 3")
app.stopFrame()

app.startFrame("frame 4", row=1, column=1)
app.addLabel(" ")
# app.addCheckBox("Use 4")
app.addLabelScale("Volume 4")
app.showScaleValue("Volume 4")
app.addLabelOptionBox("Note 4", ["C", "C#/Db", "D",
                                 "D#/Eb", "E", "F", "F#/Gb", "G",
                                 "G#/Ab", "A", "A#/Bb", "B"])
app.addLabelOptionBox("Octave 4", ["2", "3", "4", "5", "6"])
app.addLabelOptionBox("Voices 4", ["1", "2", "3", "4"])
app.addLabel("Detune 4 (-100 to 100):")
app.addEntry("Detune 4")
app.stopFrame()

app.addLabel("  ")
app.addButtons(["Play", "Close"], press)

app.go()
p.terminate()