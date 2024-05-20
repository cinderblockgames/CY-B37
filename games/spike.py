import buttons
import colors

class Game:

  def __init__(self):
    self.external = None

  def start(self):
    buttons.clear()
    # set image

  # If you press the current round button, reset to no round.
  # If you press a different round button, move to that round.

  def left(self):
    if buttons.left.color == colors.green and buttons.middle.color == colors.off and buttons.right.color == colors.off:
      self.start()
    else:
      buttons.set(buttons.left, colors.green)
      buttons.set(buttons.middle, colors.off)
      buttons.set(buttons.right, colors.off)

      # set image

  def middle(self):
    if buttons.middle.color == colors.green and buttons.right.color == colors.off:
      self.start()
    else:
      buttons.set(buttons.left, colors.green)
      buttons.set(buttons.middle, colors.green)
      buttons.set(buttons.right, colors.off)

      # set image

  def right(self):
    if buttons.right.color == colors.red:
      self.start()
    else:
      buttons.set(buttons.left, colors.green)
      buttons.set(buttons.middle, colors.green)
      buttons.set(buttons.right, colors.red)

      # set image
