# See LICENSE file for copyright and license details.
"""
HTTP API handler configuration
"""

# We are using the following USB sound card:
# input: GeneralPlus USB Audio Device as /devices/pci0000:00/0000:00:1a.0/usb1/1-1/1-1.2/1-1.2:1.3/0003:1B3F:2008.0003/input/input17
# hid-generic 0003:1B3F:2008.0003: input,hidraw0: USB HID v2.01 Device [GeneralPlus USB Audio Device] on usb-0000:00:1a.0-1.2/input3

# Card number (found in ALSA)
cardno = '1'

# Mic capture line (for amixer)
mic_cap = "numid=4,iface=MIXER,name='Mic Playback Volume'"

# Mic playback line (for amixer)
mic_play = "numid=8,iface=MIXER,name='Mic Capture Volume'"
