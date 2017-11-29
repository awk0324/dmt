#!/bin/sh
# See LICENSE file for copyright and license details.
# Creates a tmux session, starting all that is needed.

tmux start-server
tmux new-session -d -s dmt -n 'dmt'

# Start the HTTP API daemon
tmux send-keys "cd http-api && ./http_listener.py" C-m

# Start the MIDI handler daemon
tmux splitw -v -p 50
tmux send-keys "cd midi-handler && ./midi_handler.py" C-m

# Start the Asterisk log parsing daemon
tmux splitw -h -p 50
tmux send-keys "ssh -p2501 root@kunsthalpbx 'killall python3 ; killall tail ; cd dmt/freepbx-glue && tail -f /var/log/asterisk/full | ./freepbx_glue.py'" C-m

# Start Twinkle
tmux splitw -v -p 50
tmux send-keys "DISPLAY=:0 twinkle" C-m

# Attach to the session
tmux attach-session -t dmt
