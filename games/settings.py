import colors
import paged_list
import settings

class Game:

  def __init__(self):
    self.external = None

  def _toggle_setting(self, name):
    settings.toggle_setting(name)
    self.paged_list.display()

  def start(self):
    self.paged_list = paged_list.PagedList([
        paged_list.Item(('Subtitles',), self._toggle_setting, 'subtitles'),
      ],
      [colors.light_pink, colors.deep_sky_blue, colors.grey])
    self.paged_list.start()

  def left(self):
    self.paged_list.left()

  def middle(self):
    self.paged_list.middle()

  def right(self):
    self.paged_list.next()
