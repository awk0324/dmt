dmt
===

Description to be written.


Software dependencies
---------------------

This stack runs on two different machines: A FreePBX box, and a Caller
Station. Their setup is documented below.


### Caller Station

The Caller Station is a laptop running [Ubuntu Studio
17.10](https://ubuntustudio.org/). For our setup, we have removed
Pulseaudio by issuing:

```
# apt purge pulseaudio pulseaudio-utils pavucontrol
```

A reboot after removing Pulseaudio is necessary because it's integrated
in the desktop environment and this proved as the cleanest way to get
the system without it.

Once this is done, we can install the additional software needed to run
the part of the stack running on the Caller Station. Our SIP software of
choice is [Twinkle](http://www.twinklephone.com/), and our daemons are
written in Python 3, along with using some external libraries for it. We
can install all the dependencies by running the following:

```
# apt install git twinkle python3-flask xdotool tmux openssh-server openssh-client alsa-utils
```

Once we have our dependencies in place, we can clone this git repository
and proceed. The actual deployment is documented further on in this
readme.

```
$ git clone https://github.com/awk0324/dmt.git
```

For automation, it is also useful to generate an SSH key and copy it to
the FreePBX box's root user, which setup is explained below.


### FreePBX box

To be written.


Acknowledgments
---------------

Funkadelic's "Who Says a Funk Band Can't Play Rock?!" is copyright by
**Funkadelic/George Clinton/Walter Morrison/Michael Hampton**.

Funkadelic's "Maggot Brain" cover art is copyright by **Westbound
Records**.
