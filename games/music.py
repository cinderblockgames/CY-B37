import buttons
import colors
import paged_list
import sounds

class Game:

  def _play(self, song):
    buttons.clear()
    sounds.buzzer.playSong(song)
    self.paged_list.display()

  def start(self):
    self.paged_list = paged_list.PagedList([
        paged_list.Item("Pirates Theme", self._play, sounds.Songs.pirates),
        paged_list.Item("Black Parade", self._play, sounds.Songs.black_parade)
      ],
      [colors.deep_sky_blue, colors.dark_turquoise, colors.white])
    self.paged_list.start()

  def left(self):
    self.paged_list.left()

  def middle(self):
    self.paged_list.middle()

  def right(self):
    self.paged_list.next()
