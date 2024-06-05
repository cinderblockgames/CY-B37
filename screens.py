from display import epd4in2_V2
import os
from PIL import Image, ImageDraw, ImageFont
import queue
import settings
from threading import Thread
import time

class _Fonts:

  def __init__(self):
    dir = os.path.dirname(os.path.realpath(__file__))
    self._fonts = os.path.join(dir, 'display/fonts')
    self._regular = {}
    self._bold = {}
    self._italic = {}
    self._bold_italic = {}
    self._backup = {}

  def get_regular_font(self, size):
    if size not in self._regular:
      path = os.path.join(self._fonts, 'Aurebesh.otf')
      self._regular[size] = ImageFont.truetype(path, size)
    return self._regular[size]

  def get_bold_font(self, size):
    if size not in self._bold:
      path = os.path.join(self._fonts, 'Aurebesh Bold.otf')
      self._bold[size] = ImageFont.truetype(path, size)
    return self._bold[size]

  def get_italic_font(self, size):
    if size not in self._italic:
      path = os.path.join(self._fonts, 'Aurebesh Italic.otf')
      self._italic[size] = ImageFont.truetype(path, size)
    return self._italic[size]

  def get_bold_italic_font(self, size):
    if size not in self._bold_italic:
      path = os.path.join(self._fonts, 'Aurebesh Bold Italic.otf')
      self._bold_italic[size] = ImageFont.truetype(path, size)
    return self._bold_italic[size]

  def get_backup_font(self, size):
    if size not in self._backup:
      path = os.path.join(self._fonts, 'Font.ttc')
      self._backup[size] = ImageFont.truetype(path, size)
    return self._backup[size]

class _Images:

  def __init__(self):
    dir = os.path.dirname(os.path.realpath(__file__))
    self._images = os.path.join(dir, 'display/images')
    self._opened = {}

  def get_image(self, filename):
    if filename not in self._opened:
      path = os.path.join(self._images, filename)
      self._opened[filename] = Image.open(path)
    return self._opened[filename]

# Expose singleton-intended instances.
fonts = _Fonts()
images = _Images()

# Track output.
_epd = epd4in2_V2.EPD()
_epd.init_fast(_epd.Seconds_1_5S)
_image = None
_draw = None

_display_queue = queue.SimpleQueue()
def show(partial = True):
  buffer = _epd.getbuffer(_image)
  if partial:
    _display_queue.put((_epd.display_Partial, buffer))
  else:
    _display_queue.put((_epd.display_Fast, buffer))

def clear():
  global _image, _draw
  _image = Image.new(
      '1',                       # 1 for black and white, L for grayscale
      (_epd.width, _epd.height), # size (horizontal)
      _epd.GRAY1                 # clear with white
    )
  _draw = ImageDraw.Draw(_image)

def replace_image(image):
  _image.paste(image, (0, 0)) # overwrite the whole image

def write_text(text, font, location):
  _draw.text(location, text.lower(), font = font, fill = _epd.GRAY4)

def _draw_button(corners):
  _draw.rectangle((corners[0][0]  , corners[0][1]  , corners[1][0]  , corners[1][1]  ), outline = _epd.GRAY4)
  _draw.rectangle((corners[0][0]-2, corners[0][1]-2, corners[1][0]+2, corners[1][1]+2), outline = _epd.GRAY4)
  _draw.line((corners[0][0]-2, corners[0][1]-2, corners[0][0], corners[0][1]), fill = _epd.GRAY4)
  _draw.line((corners[1][0]+2, corners[0][1]-2, corners[1][0], corners[0][1]), fill = _epd.GRAY4)
  _draw.line((corners[0][0]-2, corners[1][1]+2, corners[0][0], corners[1][1]), fill = _epd.GRAY4)
  _draw.line((corners[1][0]+2, corners[1][1]+2, corners[1][0], corners[1][1]), fill = _epd.GRAY4)

def _write_button(text, location):
  if text:
    supported = True
    for char in text:
      if char not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$+-*/=%"\'#@&_(),.;:?!\{}<>[]`^':
        supported = False
        break

    if supported:
      write_text(text, fonts.get_regular_font(25), location)
    else:
      write_text(text, fonts.get_backup_font(25), (location[0]-4, location[1]-2)) # backup font needs better placement

def add_legend(left, middle, right):
  _draw_button(((297, 265), (327, 295)))
  _write_button(left, (304, 269))

  _draw_button(((331, 265), (361, 295)))
  _write_button(middle, (338, 269))

  _draw_button(((365, 265), (395, 295)))
  _write_button(right, (372, 269))

def set_subtitle_generator(subtitle_generator, *subtitle_generator_arguments):
  if settings.is_set('subtitles'):
    high_galactic = fonts.get_backup_font(20)
    write_text(subtitle_generator(*subtitle_generator_arguments), high_galactic, (5, 235))

def _display_loop():
  while True:
    display = _display_queue.get() # blocks until something in queue
    display[0](display[1])

_display_loop_thread = Thread(target=_display_loop)
_display_loop_thread.start()

clear() # initialize empty
show(False)
