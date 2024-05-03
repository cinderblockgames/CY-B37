#!/usr/bin/env python
import buttons
import colors
import game
import keybow
import time


buttons.setup()


cancel_left = False
cancel_right = False

def check_for_reset():
  global cancel_left, cancel_right
  if buttons.left.pressed and buttons.right.pressed:
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
