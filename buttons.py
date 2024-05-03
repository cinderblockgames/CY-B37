import colors
import keybow
import button_state

# Keybow MINI is upside down in CY-B37.
# Keybow MINI goes 0-3-6, not 0-1-2.
left = button_state.ButtonState(9)
middle = button_state.ButtonState(6)
right = button_state.ButtonState(3)

def setup():
  keybow.setup(keybow.MINI)

def set(button, color):
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

# Keybow MINI is upside down in CY-B37.
list = [2, 1, 0]
def pressed(index):
  # Keybow MINI goes 0-3-6, not 0-1-2.
  return list[int(index / 3)]
