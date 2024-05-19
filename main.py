#!/usr/bin/env python
import buttons
import colors
import game
import keybow
import sounds
import time

buttons.setup()
sounds.setup()

# ======== startup! ========
sounds.buzzer.play(sounds.Sounds.connection)
# set image
sleep = 0.10
for color in colors.cycle:
  buttons.set(buttons.left, color)
  keybow.show()
  time.sleep(sleep)
  buttons.set(buttons.middle, color)
  keybow.show()
  time.sleep(sleep)
  buttons.set(buttons.right, color)
  keybow.show()
  time.sleep(sleep)
# ======== /startup ========

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
  keybow.show()
  time.sleep(1.0 / 60.0)
