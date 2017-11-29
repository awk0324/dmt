# See LICENSE file for copyright and license details.
"""
MIDI handler configuration
"""

# The device we want to use for MIDI. Found using: mido.get_input_names()
#device_name = 'USB MS1x1 MIDI Interface:USB MS1x1 MIDI Interface MIDI 1 24:0'

# Uncomment this for hardcode
#device_name = 'USB MS1x1 MIDI Interface:USB MS1x1 MIDI Interface MIDI 1 20:0'

# Comment this out if you hardcode
import mido
device_name = mido.get_input_names()[1]
