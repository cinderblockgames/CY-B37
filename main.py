#!/usr/bin/env python
import atexit
import buttons
import colors
import game
import keybow
import screens
import signal
import sounds
import subprocess
import sys
import time
from datetime import datetime
from threading import Lock
import RPi.GPIO as GPIO

buttons.setup()
sounds.setup()

color_pause = 0.1
sound_pause = 1.0
main_pause = 1.0 / 60.0 # 60 times a second

# ======== startup! ========
# set image

if buttons.show_lights:
  sounds.buzzer.play(sounds.Sounds.mode_3)
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
lock = Lock()
shutting_down = False
def shutdown(_):
  global lock, shutting_down
  if not shutting_down:
    with lock:
      if not shutting_down:
        shutting_down = True
        subprocess.call(['sudo', 'pkill', 'python'], shell=False) # shut down droid software

def off_subtitle():
  return 'cy-b37 casino table droid'

def exit_handler():
  sounds.buzzer.play(sounds.Sounds.disconnection) # game mode turning off
  buttons.clear()
  screens.clear()
  screens.replace_image(screens.images.get_image('off.bmp'))
  screens.set_subtitle_generator(off_subtitle)
  screens.show()
  time.sleep(sound_pause)
  subprocess.call(['sudo', 'shutdown', '-h', 'now'], shell=False) # shut down droid hardware

def kill_handler(*args):
  sys.exit(0)

atexit.register(exit_handler)
signal.signal(signal.SIGINT, kill_handler)
signal.signal(signal.SIGTERM, kill_handler)

GPIO.setwarnings(False) # we know
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(3, GPIO.RISING, callback=shutdown)
# ======== shutdown ========

sounds.buzzer.play(sounds.Sounds.connection)
game.current = game.start_reset()

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

@keybow.on()
def handle_key(index, state):
  pressed = buttons.pressed(index)
  if pressed == 0:
    left(state)
  if pressed == 1:
    middle(state)
  if pressed == 2:
    right(state)

while True:
  if buttons.show_lights:
    keybow.show()
  time.sleep(main_pause)
