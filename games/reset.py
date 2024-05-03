import buttons
import colors
import game

class Game:

  def start(self):
    buttons.set(buttons.left, colors.yellow)
    buttons.set(buttons.middle, colors.blue)
    buttons.set(buttons.right, colors.purple)
    # set image

  def left(self):
    game.current = game.start_spike()

  def middle(self):
    game.current = game.start_shift()

  def right(self):
    game.current = game.start_hintaro()
