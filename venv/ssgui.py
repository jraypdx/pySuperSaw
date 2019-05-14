def buildgui(app):
    app.setTitle("pySuperSaw")
    app.startFrame("frame1", row=0, column=0)
    app.addCheckBox("Use 1")
    app.addLabelOptionBox("Note 1", ["C", "C#/Db", "D",
                                     "D#/Eb", "E", "F", "F#/Gb", "G",
                                     "G#/Ab", "A", "A#/Bb", "B"])
    app.addLabelOptionBox("Octave 1", ["3", "4", "5"])
    app.addCheckBox("-", row=3, column=0)
    app.addScale("Detune 1", row=3, column=1)
    app.stopFrame()

    app.startFrame("frame2", row=0, column=1)
    app.addCheckBox("Use 2")
    app.addLabelOptionBox("Note 2", ["C", "C#/Db", "D",
                                     "D#/Eb", "E", "F", "F#/Gb", "G",
                                     "G#/Ab", "A", "A#/Bb", "B"])
    app.addLabelOptionBox("Octave 2", ["3", "4", "5"])
    # app.addScale()
    app.stopFrame()

    app.addButtons(["Play", "Cancel"], press)