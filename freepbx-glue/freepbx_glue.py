#!/usr/bin/env python3
# See LICENSE file for copyright and license details.
"""
FreePBX/Asterisk log parser and handler
"""

import sys
import requests

import globalvars
from config import (CALLER_ID, RECEIVER_ID, STATION_API)


def handle_line(logline):
    """
    Parses a single log line to make an according call
    """
    if not logline:
        return

    parsed = logline.split()

    # We wait for a ring.
    if parsed[4].split('-')[0] == RECEIVER_ID:
        # stackno = parsed[4].split('-')[1]
        if parsed[6] == 'ringing':
            globalvars.weareringing = True
            print('We are ringing')
            return

    # When a call is answered, the receiver stackno is +1 in hex than
    # the caller's.

    # The phone is ringing.
    if globalvars.weareringing:
        if parsed[3] == 'app_dial:' and parsed[5] == 'answered':
            globalvars.weareringing = False
            globalvars.wehaveanswered = True
            print('We have answered')
            resp = requests.get(STATION_API+'/callanswered')
            if resp.status_code != 200:
                print('Something went wrong with the API call.')
            return

    # The phone has been picked up.
    if globalvars.wehaveanswered:
        if parsed[3] == 'pbx.c:':
            if parsed[6].startswith('Hangup("' + CALLER_ID):
                globalvars.wehaveanswered = False
                print('We hung up.')
                print('---')
                resp = requests.get(STATION_API+'/callended')
                if resp.status_code != 200:
                    print('Something went wrong with the API call.')
                return


def main():
    """
    Main routine.
    Reads standard input line by line.
    """
    print('Tailing logfile...')
    while True:
        line = sys.stdin.readline()
        handle_line(line)


if __name__ == '__main__':
    main()
