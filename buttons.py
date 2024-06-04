import colors
import keybow
import button_state
from spidev import SpiDev

show_lights = False

# Keybow MINI goes 0-3-6, not 0-1-2.
left = button_state.ButtonState(3)
middle = button_state.ButtonState(6)
right = button_state.ButtonState(9)

def setup():
  keybow.setup(keybow.MINI)

def set(button, color):
  global show_lights
  if show_lights:
    keybow.set_led(button.pixel, color[0], color[1], color[2])
  button.color = color

def flip(button, color):
  if button.color == colors.off:
    set(button, color)
  else:
    set(button, colors.off)

def clear():
  set(left, colors.off)
  set(middle, colors.off)
  set(right, colors.off)

def pressed(index):
  return index # apparently it's now going 0-1-2, i dunno man
  # Keybow MINI goes 0-3-6, not 0-1-2.
  # Also, doing the if check here because wires can trigger other "keys" to be "pushed."
  if index % 3 == 0 and index <= 6:
    return int(index / 3)
