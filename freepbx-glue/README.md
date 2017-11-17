freepbx-glue
============

freepbx-glue is a simple python daemon designed to parse logs output by
Asterisk/FreePBX.

It currently handles three states:

* The receiver is ringing
* The receiver has answered
* The receiver has hung up

Whenever a daemon enters one of these states, it will issue a callback
to an HTTP API running on the calling station.


Dependencies
------------

```
python3-requests
```


Deploying
---------

On the FreePBX machine, this daemon can be executed by running the
following command as root:

```
# tail -f /var/log/asterisk/full | ./freepbx_glue.py
```
