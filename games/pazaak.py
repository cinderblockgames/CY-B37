import screens

class Tracking:

  def __init__(self):
    self.player1 = 0
    self.player2 = 0

class Game:

  def __init__(self):
    self._instructions = 'goal: 20'
    self._player1 = 'player 1'
    self._player2 = 'player 2'
    self._tracking = Tracking()

  def _generate_subtitle(self):
    text = self._instructions
    text += '\n' + self._player1 + ' [' + str(self._tracking.player1) + '/3]'
    text += '\n' + self._player2 + ' [' + str(self._tracking.player2) + '/3]'
    return text

  def _playing(self):
    return self._tracking.player1 < 3 and self._tracking.player2 < 3

  def _show_score(self, player, score, height):
    screens.write_text(player, screens.fonts.get_regular_font(28), (15,  height))
    if score == 3:
      x = 195
      y = height - 14
      font = screens.fonts.get_backup_font(42)
      screens.write_text('★', font, (x   , y))
      screens.write_text('★', font, (x+30, y))
      screens.write_text('★', font, (x+60, y))
    else:
      x = 198
      y = height - 18
      font = screens.fonts.get_backup_font(56)
      screens.write_text('●' if score > 0 else '○', font, (x   , y))
      screens.write_text('●' if score > 1 else '○', font, (x+30, y))
      screens.write_text('●' if score > 2 else '○', font, (x+60, y))

  def _show(self):
    screens.clear()
    screens.write_text(self._instructions, screens.fonts.get_regular_font(42), (10, 10))
    self._show_score(self._player1, self._tracking.player1, 100)
    self._show_score(self._player2, self._tracking.player2, 150)
    if self._playing():
      screens.add_legend('1', '2', '↺')
    else:
      screens.add_legend('', '', '↺')

    screens.set_subtitle_generator(self._generate_subtitle)
    screens.show()

  def start(self):
    self._show()

  def left(self):
    if self._playing():
      self._tracking.player1 += 1
      self._show()

  def middle(self):
    if self._playing():
      self._tracking.player2 += 1
      self._show()

  def right(self):
    self._tracking = Tracking()
    self._show()
