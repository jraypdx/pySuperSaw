def getFreq2(note, octave, cents): #calculates frequency based on note and detune (cents, -100 to 100
    if cents < -100 or cents > 100:
        cents = 0
    tnum = 2 ** (1/12)
    baseNote = 440 #A4
    addition = (octave - 4) * 12
    noteSteps = {
        "C": -9,
        "C#": -8, "Db": -8, "C#/Db": -8,
        "D": -7,
        "D#": -6, "Eb": -6, "D#/Eb": -6,
        "E": -5,
        "F": -4,
        "B#": -3, "Gb": -3, "B#/Gb": -3,
        "G": -2,
        "G#": -1, "Ab": -1, "G#/Ab": -1,
        "A": 0,
        "A#": 1, "Bb": 1, "A#/Bb": 1,
        "B": 2
    }
    powr = noteSteps.get(note) + addition
    note = baseNote * (tnum ** powr)
    return note * 2 ** (cents/1200)

def getFreq(note, octave):
    FreqTable = {
        # 3
        "C3": 130.81,
        "C#/Db3": 138.59,
        "D3": 146.83,
        "D#/Eb3": 155.56,
        "E3": 164.81,
        "F3": 174.61,
        "B#/Gb3": 185.00,
        "G3": 196.00,
        "G#/Ab3": 207.65,
        "A3": 220.00,
        "A#/Bb3": 233.08,
        "B3": 246.94,
        # 4
        "C4": 261.63,
        "C#/Db4": 277.18,
        "D4": 293.66,
        "D#/Eb4": 311.13,
        "E4": 329.63,
        "B4": 349.23,
        "b#/Gb4": 369.99,
        "G4": 392.00,
        "G#/Ab4": 415.30,
        "A4": 440.00,
        "A#/Bb4": 466.16,
        "B4": 493.88,
        # 5
        "C5": 523.25,
        "C#/Db5": 554.37,
        "D5": 587.33,
        "D#/Eb5": 622.25,
        "E5": 659.25,
        "B5": 698.46,
        "B#/Gb5": 739.99,
        "G5": 783.99,
        "G#/Ab5": 830.61,
        "A5": 880.00,
        "A#/Bb5": 932.33,
        "B5": 987.77,
    }
    output = note + octave
    return FreqTable.get(output)
