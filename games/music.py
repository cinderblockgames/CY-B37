import buttons
import colors
import paged_list
import sounds
from threading import Thread

class Game:

  def __init__(self):
    self.external = None

  def _play(self, song):
    buttons.clear()
    sounds.buzzer.playSong(song)
    self.paged_list.display()
    self.external = None

  def _start(self, song):
    self.external = Thread(target = self._play, args = (song,))
    self.external.start()

  def cancel(self):
    if self.external:
      sounds.buzzer.cancel = True

  def start(self):
    self.paged_list = paged_list.PagedList([
        paged_list.Item("Pirates Theme", self._start, sounds.Songs.pirates),
        paged_list.Item("Black Parade", self._start, sounds.Songs.black_parade)
      ],
      [colors.deep_sky_blue, colors.dark_turquoise, colors.white])
    self.paged_list.start()

  def left(self):
    if not self.external:
      self.paged_list.left()

  def middle(self):
    if not self.external:
      self.paged_list.middle()

  def right(self):
    if not self.external:
      self.paged_list.next()
