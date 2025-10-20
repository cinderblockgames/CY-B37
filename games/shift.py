import screens

class Tracking:

  def __init__(self):
    self.positive = None
    self.target = None
    self.suit = None

class Game:

  def __init__(self):
    self._small   = screens.fonts.get_regular_font(30)
    self._large   = screens.fonts.get_regular_font(40)
    self._suits   = screens.fonts.get_backup_font(70)
    self._symbols = screens.fonts.get_backup_font(45)
    self._target  = screens.fonts.get_regular_font(90)
    self._symbol  = screens.fonts.get_backup_font(160)
    self._small_y   = 351
    self._large_y   = 346
    self._suits_y   = 327
    self._symbols_y = 340
    self._target_y  = 50

  def _draw_boxes(self):
    # double-size legend
    screens.clear()
    screens._draw_button(((107, 335), (167, 395)))
    screens._draw_button(((171, 335), (231, 395)))
    screens._draw_button(((235, 335), (295, 395)))

  def start(self):
    self.tracking = Tracking()

    self._draw_boxes()
    screens.write_text('0', self._large, (124, self._large_y))
    screens.write_text('+', self._large, (191, self._large_y))
    screens.write_text('-', self._large, (254, self._large_y))
    screens.show()

  def pick_target(self):
    self._draw_boxes()
    screens.write_text('0' , self._small, (127, self._small_y))
    screens.write_text('5' , self._small, (191, self._small_y))
    screens.write_text('10', self._small, (243, self._small_y))
    screens.show()

  def pick_suit(self):
    self._draw_boxes()
    screens.write_text('●', self._suits, (117, self._suits_y))
    screens.write_text('▲', self._suits, (180, self._suits_y+1))
    screens.write_text('■', self._suits, (245, self._suits_y))
    screens.show()

  def play(self):
    # legend
    self._draw_boxes()
    screens.write_text('↺', self._symbols, (243, self._symbols_y))

    # target
    target = self.tracking.target
    if not self.tracking.positive:
      target *= -1
    value = str(target)
    x1 = 60 - 25*(len(value)-1)
    x2 = x1 + (70 if self.tracking.target == 10 else 50) + 40*len(value)
    screens.write_text(str(value), self._target, (x1, self._target_y))
    screens.write_text(
        self.tracking.suit,
        self._symbol,
        (x2, self._target_y - (44 if self.tracking.suit == '▲' else 50))
      )

    screens.show()

  def left(self):
    if self.tracking.target == None:
      self.tracking.positive = True
      self.tracking.target = 0
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "●"
      self.play()

  def middle(self):
    if self.tracking.positive == None:
      self.tracking.positive = True
      self.pick_target()
    elif self.tracking.target == None:
      self.tracking.target = 5
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "▲"
      self.play()

  def right(self):
    if self.tracking.positive == None:
      self.tracking.positive = False
      self.pick_target()
    elif self.tracking.target == None:
      self.tracking.target = 10
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "■"
      self.play()
    else:
      self.start()
