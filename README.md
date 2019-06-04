Course Project Writeup
Python Super Saw
Intro:
A super saw is a group of detuned saw waves that is very commonly used in EDM tracks.  It can be made with pretty much any synthesizer that supports multiple saw waves and detuning.  It’s common to use several detuned saw waves at different octaves for each not of a chord.  It’s incredibly easy to make a super saw, but much harder to make one that sounds good.
My project was to create a super saw in python.  The idea was to create a very basic synthesizer that had multiple saw waves, with the option to choose the note that each places, as well as the octave and detune level that each wave plays at.  Another option was to choose the number of voices, (1-4) that each wave uses.  1 being mono, and each additional voice adding another offset saw wave to one side of the channel (L/R) to create a stereo effect.  This would allow the user to implement more of the stereo field in the super saw.

Outcome:
The project went about as well as I expected.  I was able to implement everything that I had expected to, but didn’t have time to go above and beyond like I had hoped.  It doesn’t sound very good, though.  It is definitely saw waves, and it works as anticipated, but no one is going to be using it in any songs any time soon.  I think that VST synthesizers people usually use must have a lot more going on under the hood.
All of the options seen on the screenshot on the right are fully functioning.  You can select a volume level for each wave (0 means the wave is never computer), a note, octave, and voice count for each wave, as well as the detune level in cents for each wave.  
After all of the selections are made by the user, the play button will play one second of audio from the selection.  It takes a few seconds to render the audio, I am not sure if this is purely due to python or just due to me not programming in an efficient way for audio.  I used a lot of loops.
I would have like to be able to use the computer keyboard to play different notes, or at least to be able to select how long the sound was played, but didn’t get that far.  Another idea that I had was to make some kind of a way to load a text document that would save data for the setup of the synth, so that you could load it and play several different notes/setups in succession. 

Conclusion:
Really the only thing that didn’t go as well as expected was how it sounds.  It doesn’t sound nearly as good as I had expected, but I bet with a bunch more work I could get it sounding decent.  This project has definitely made me want to try making a VST effect, but it has also made me weary of how hard efficient audio processing is.
