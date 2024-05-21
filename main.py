#!/usr/bin/env python
import atexit
import buttons
import colors
import game
import keybow
import signal
import sounds
import subprocess
import sys
import time
from datetime import datetime

buttons.setup()
sounds.setup()

color_pause = 0.1
sound_pause = 1.0
main_pause = 1.0 / 60.0 # 60 times a second

# ======== startup! ========
sounds.buzzer.play(sounds.Sounds.connection)
# set image
for color in colors.cycle:
  buttons.set(buttons.left, color)
  keybow.show()
  time.sleep(color_pause)
  buttons.set(buttons.middle, color)
  keybow.show()
  time.sleep(color_pause)
  buttons.set(buttons.right, color)
  keybow.show()
  time.sleep(color_pause)
# ======== /startup ========

# ======== shutdown ========
def exit_handler():
  buttons.clear()
  time.sleep(sound_pause)
  sounds.buzzer.play(sounds.Sounds.sleeping)
  sounds.buzzer.play(sounds.Sounds.sleeping)
  sounds.buzzer.play(sounds.Sounds.sleeping)
  time.sleep(sound_pause)
  subprocess.call(['sudo', 'shutdown', '-h', 'now'], shell=False) # shut down the droid

def kill_handler(*args):
  sys.exit(0)

atexit.register(exit_handler)
signal.signal(signal.SIGINT, kill_handler)
signal.signal(signal.SIGTERM, kill_handler)
# ======== shutdown ========

game.current = game.start_reset()
sounds.buzzer.play(sounds.Sounds.mode_3)

cancel_left = False
cancel_right = False

def check_for_reset():
  global cancel_left, cancel_right
  if buttons.left.pressed and buttons.right.pressed:
    if game.current.external:
     game.current.cancel()
    else:
      game.current = game.start_reset()
    cancel_left = True
    cancel_right = True

def left(state):
  global cancel_left
  buttons.left.pressed = state
  if state:
    check_for_reset()
  elif cancel_left:
    cancel_left = False
  else:
    game.current.left()

def middle(state):
  buttons.middle.pressed = state
  if not state:
    game.current.middle()

def right(state):
  global cancel_right
  buttons.right.pressed = state
  if state:
    check_for_reset()
  elif cancel_right:
    cancel_right = False
  else:
    game.current.right()

hit = None
def shutdown(state):
  if not state: # only on up
    global hit
    if hit and (datetime.now() - hit).total_seconds() < 3: # hit the button twice within three seconds to shut down
      sounds.buzzer.play(sounds.Sounds.disconnection) # game mode turning off
      buttons.clear()
      time.sleep(sound_pause)
      subprocess.call(['sudo', 'pkill', 'python'], shell=False) # shut down the droid
    else:
      hit = datetime.now()
      sounds.buzzer.play(sounds.Sounds.button_pushed)

@keybow.on()
def handle_key(index, state):
  pressed = buttons.pressed(index)
  if pressed == 0:
    left(state)
  if pressed == 1:
    middle(state)
  if pressed == 2:
    right(state)
  if index == 11: # shutdown button
    shutdown(state)

while True:
  keybow.show()
  time.sleep(main_pause)
