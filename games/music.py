import buttons
import colors
import paged_list
import screens
import sounds
from threading import Thread

class Game:

  def __init__(self):
    self.external = None

  def _display_song_title(self, name):
    screens.clear()
    if len(name) == 1:
      screens.write_text(name[0], screens.fonts.get_italic_font(80), (20, 100))
    else:
      font = screens.fonts.get_italic_font(60)
      screens.write_text(name[0], font, (20, 80))
      screens.write_text(name[1], font, (35, 140))
    screens.show()

  def _play(self, song, name):
    buttons.clear()
    self._display_song_title(name)
    sounds.buzzer.playSong(song)
    self.paged_list.display()
    self.external = None

  def _start(self, song, name):
    self.external = Thread(target = self._play, args = (song,name,))
    self.external.start()

  def cancel(self):
    if self.external:
      sounds.buzzer.cancel = True

  def start(self):
    songs = [
        (('Pirates', 'Theme',), sounds.Songs.pirates),
        (('Black', 'Parade',), sounds.Songs.black_parade),
      ]
    self.paged_list = paged_list.PagedList([
        paged_list.Item(songs[0][0], self._start, songs[0][1], songs[0][0]),
        paged_list.Item(songs[1][0], self._start, songs[1][1], songs[1][0]),
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
