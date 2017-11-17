http-listener
=============

http-listener is a small Flask daemon acting as a HTTP API listening for
callbacks from the FreePBX log handler.

It offers callbacks for `/callanswered` and `/callended`.

The former will mute the playback of our sound input on the speakers and
enable it on the phone.

The latter will do the opposite.


Dependencies
------------

```
python3-flask
```


Deployment
----------

Deploy this by running `./http_listener.py` on the Caller Station.
