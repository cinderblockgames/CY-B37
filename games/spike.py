import screens

class Game:
  def __init__(self):
    self._round = 0

  def _generate_subtitle(self):
    text = 'round'
    if self._round > 0:
      text += ' ' + str(self._round)
    return text

  def _set_image(self):
    screens.clear()
    screens.write_text('round', screens.fonts.get_regular_font(68), (10, 10))
    if self._round > 0:
      x = 86 if self._round == 1 else 85
      screens.write_text(str(self._round), screens.fonts.get_bold_font(200), (x, 100))
    screens.add_legend(
        '↺' if self._round == 1 else '1',
        '↺' if self._round == 2 else '2',
        '↺' if self._round == 3 else '3'
      )
    screens.set_subtitle_generator(self._generate_subtitle)
    screens.show()

  def start(self, round=0):
    self._round = round
    self._set_image()

  # If you press the current round button, reset to no round.
  # If you press a different round button, move to that round.

  def left(self):
    self.start(0 if self._round == 1 else 1)

  def middle(self):
    self.start(0 if self._round == 2 else 2)

  def right(self):
    self.start(0 if self._round == 3 else 3)
