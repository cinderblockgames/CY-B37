import buttons
import colors
import screens

class Tracking:

  def __init__(self):
    self.positive = None
    self.target = None
    self.suit = None

class Game:

  def __init__(self):
    self.external = None
    self._small   = screens.fonts.get_regular_font(30)
    self._large   = screens.fonts.get_regular_font(40)
    self._suits   = screens.fonts.get_backup_font(70)
    self._symbols = screens.fonts.get_backup_font(45)
    self._target  = screens.fonts.get_regular_font(120)
    self._symbol  = screens.fonts.get_backup_font(190)
    self._small_y   = 251
    self._large_y   = 246
    self._suits_y   = 227
    self._symbols_y = 240
    self._target_y  = 50

  def _draw_boxes(self):
    # double-size legend
    screens.clear()
    screens._draw_button(((207, 235), (267, 295)))
    screens._draw_button(((271, 235), (331, 295)))
    screens._draw_button(((335, 235), (395, 295)))

  def start(self):
    buttons.set(buttons.left  , colors.red  )
    buttons.set(buttons.middle, colors.green)
    buttons.set(buttons.right , colors.white)
    self.tracking = Tracking()

    self._draw_boxes()
    screens.write_text('+', self._large, (227, self._large_y))
    screens.write_text('-', self._large, (291, self._large_y))
    screens.write_text('0', self._large, (351, self._large_y))
    screens.show()

  def pick_target(self):
    buttons.set(buttons.left  , colors.light_pink)
    buttons.set(buttons.middle, colors.hot_pink  )
    buttons.set(buttons.right , colors.grey      )

    self._draw_boxes()
    screens.write_text('5' , self._small, (228, self._small_y))
    screens.write_text('10', self._small, (279, self._small_y))
    screens.write_text('0' , self._small, (354, self._small_y))
    screens.show()

  def pick_suit(self):
    buttons.set(buttons.left  , colors.yellow)
    buttons.set(buttons.middle, colors.orange)
    buttons.set(buttons.right , colors.purple)

    self._draw_boxes()
    screens.write_text('●', self._suits, (217, self._suits_y))
    screens.write_text('▲', self._suits, (280, self._suits_y+1))
    screens.write_text('■', self._suits, (345, self._suits_y))
    screens.show()

  def play(self):
    buttons.set(buttons.left  , colors.off )
    buttons.set(buttons.middle, colors.off )
    buttons.set(buttons.right , colors.grey)

    # legend
    self._draw_boxes()
    screens.write_text('↺', self._symbols, (343, self._symbols_y))

    # target
    target = self.tracking.target
    if not self.tracking.positive:
      target *= -1
    value = str(target)
    x1 = 110 - 50*(len(value)-1)
    x2 = x1 + (50 if self.tracking.target == 10 else 30) + 70*len(value)
    screens.write_text(str(value), self._target, (x1, self._target_y))
    screens.write_text(
        self.tracking.suit,
        self._symbol,
        (x2, self._target_y - (46 if self.tracking.suit == '▲' else 52))
      )

    screens.show()

  def left(self):
    if self.tracking.positive == None:
      self.tracking.positive = True
      self.pick_target()
    elif self.tracking.target == None:
      self.tracking.target = 5
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "●"
      self.play()

  def middle(self):
    if self.tracking.positive == None:
      self.tracking.positive = False
      self.pick_target()
    elif self.tracking.target == None:
      self.tracking.target = 10
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "▲"
      self.play()

  def right(self):
    if self.tracking.target == None:
      self.tracking.positive = True
      self.tracking.target = 0
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "■"
      self.play()
    else:
      self.start()
