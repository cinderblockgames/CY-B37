import colors
import game
import paged_list

class Game:

  def __init__(self):
    self.external = None

  def _replace(self, start):
    game.current = start()

  def start(self):
    self.paged_list = paged_list.PagedList([
        paged_list.Item(('Spike,','Kessel'), self._replace, game.start_spike),
        paged_list.Item(('Shift',), self._replace, game.start_shift),
        paged_list.Item(('Hintaro',), self._replace, game.start_hintaro),
        paged_list.Item(('Music',), self._replace, game.start_music),
        paged_list.Item(('Settings',), self._replace, game.start_settings),
      ],
      [colors.yellow, colors.blue, colors.purple])
    self.paged_list.start()

  def left(self):
    self.paged_list.left()

  def middle(self):
    self.paged_list.middle()

  def right(self):
    self.paged_list.next()
