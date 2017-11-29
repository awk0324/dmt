#!/usr/bin/env python3
# See LICENSE file for copyright and license details.
"""
MIDI listener daemon for the Caller Station
"""

from subprocess import Popen
import mido

from config import (device_name)


def make_call():
    # DISPLAY=:0 xdotool key 1 2 3 Return
    print('Popping the mechanical turk')
    Popen(['xdotool', 'key', '1', '2', '3', 'Return'],
          env={'DISPLAY': ':0'})


def cancel_call():
    print('Popping the mechanical turk')
    Popen(['xdotool', 'key', 'Escape'],
          env={'DISPLAY': ':0'})

def main():
    print('Opening the MIDI input listener')
    midi_in = mido.open_input(device_name)
    for msg in midi_in:
        print('Got MIDI message!')
        #print('Type:', msg.type)
        #print('Time:', msg.time)
        #print('Velocity:', msg.velocity)
        #print('Note:', msg.note)
        #print('Channel:', msg.channel)
        #print('Bytes:', msg.bytes())
        #print('Bin:', msg.bin())
        #print('Hex:', msg.hex())
        print('Dict:', msg.dict())
        midi_dict = msg.dict()

        # a control change
        #mtype = midi_dict.get('type')
        #mtime = midi_dict.get('time')
        #mctl = midi_dict.get('control')
        #mval = midi_dict.get('value')
        #mchan = midi_dict.get('channel')

        # a note_on
        mtype = midi_dict.get('type')
        mtime = midi_dict.get('time')
        mnote = midi_dict.get('note')
        mvelo = midi_dict.get('velocity')
        mchan = midi_dict.get('channel')

        if mtype == 'note_on' and mtime == 0 and mnote == 60 \
                and mchan == 0:
            make_call()
            print('Got MIDI 60. Making call.')
        elif mtype == 'note_on' and mtime == 0 and mnote == 63 \
                and mchan == 0:
            cancel_call()
            print('Got MIDI 63. Cancelling call.')


        print('---')

    # Try this out too:
    #while True:
    #    for msg in midi_in.iter_pending():
    #        print(msg)


if __name__ == '__main__':
    main()
