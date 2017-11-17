#!/usr/bin/env python3
# See LICENSE file for copyright and license details.
"""
HTTP API handler for the Caller Station
"""

from subprocess import Popen
from flask import Flask

from config import (cardno, mic_cap, mic_play)

APP = Flask(__name__)


@APP.route('/')
def main():
    """
    Main routine (noop)
    """
    return '\n'


@APP.route('/callanswered')
def callanswered():
    """
    Handler for the answered phone call.
    """
    print('Call answered')

    Popen(['amixer', '-c', cardno, 'cset', mic_play, '0'])
    Popen(['amixer', '-c', cardno, 'cset', mic_cap, '100'])

    return 'Call answered\n'


@APP.route('/callended')
def callended():
    """
    Handler for the ended phone call.
    """
    print('Call ended')

    Popen(['amixer', '-c', cardno, 'cset', mic_play, '100'])
    Popen(['amixer', '-c', cardno, 'cset', mic_cap, '0'])

    return 'Call ended\n'


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
