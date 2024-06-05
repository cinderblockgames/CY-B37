import buttons
import colors
import screens

class Game:

  def __init__(self):
    self.external = None

  def _generate_subtitle(self, round):
    text = 'round'
    if round > 0:
      text += ' ' + str(round)
    return text

  def _set_image(self, round):
    screens.clear()
    screens.write_text('round', screens.fonts.get_regular_font(86), (20, 10))
    if round > 0:
      screens.write_text(str(round), screens.fonts.get_bold_font(200), (130, 100))
    screens.add_legend(
        '↺' if round == 1 else '1',
        '↺' if round == 2 else '2',
        '↺' if round == 3 else '3'
      )
    screens.set_subtitle_generator(self._generate_subtitle, round)
    screens.show()

  def start(self):
    buttons.clear()
    self._set_image(0)

  # If you press the current round button, reset to no round.
  # If you press a different round button, move to that round.

  def left(self):
    if buttons.left.color == colors.green and buttons.middle.color == colors.off and buttons.right.color == colors.off:
      self.start()
    else:
      buttons.set(buttons.left, colors.green)
      buttons.set(buttons.middle, colors.off)
      buttons.set(buttons.right, colors.off)
      self._set_image(1)

  def middle(self):
    if buttons.middle.color == colors.green and buttons.right.color == colors.off:
      self.start()
    else:
      buttons.set(buttons.left, colors.green)
      buttons.set(buttons.middle, colors.green)
      buttons.set(buttons.right, colors.off)
      self._set_image(2)

  def right(self):
    if buttons.right.color == colors.red:
      self.start()
    else:
      buttons.set(buttons.left, colors.green)
      buttons.set(buttons.middle, colors.green)
      buttons.set(buttons.right, colors.red)
      self._set_image(3)
