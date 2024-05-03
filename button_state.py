import colors

class ButtonState:

  def __init__(self, pixel):
    self.color = colors.off
    self.pressed = False
    self.pixel = pixel
