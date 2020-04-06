## brainsynth
### Control a synthesiser with your mind (and a Raspberry Pi)!  Look ma no hands!

This project uses a Python script to read brain waves from a Neurosky MindWave sensor (neurosky.com) and converts this into a control voltage that can be used on a synthesiser.  

There's two readings - attention and meditation - depending on which brain state you want to represent.  The code converts these readings into positive voltages that are output through the GPIO pins for onward use in the synth, so if you're controlling pitch using volts per octave (as most synths do) then a higher level of meditation will lead to a higher pitch for example.  (Eventually I'm going to add an inverse conversion for at least meditation, so if meditation level increases the note gets lower).  I've also got a couple of LEDs set up for a visual representation of the two readings.

Huge amount of thanks to these sites for getting me started with this:

Knights of Pi:  http://www.knight-of-pi.org/raspberry-pi-mindcontrol-neurosky-mindwave-as-simple-eeg-interface/

This was the jump off point for this project - if you can control an LED then you can control a synthesiser (and if you can dodge a wrench you can dodge a ball)

https://github.com/BarkleyUS/mindwave-python

This is the library for using the Mindwave sensor with Python.

Also to buy a Mindwave sensor:  http://neurosky.com
