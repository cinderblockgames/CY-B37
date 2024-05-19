import buttons
import colors

class Tracking:

  def __init__(self):
    self.external = None
    self.positive = None
    self.target = None
    self.suit = None

class Game:

  def start(self):
    buttons.set(buttons.left, colors.red)
    buttons.set(buttons.middle, colors.green)
    buttons.set(buttons.right, colors.white)
    self.tracking = Tracking()
    # set image

  def pick_target(self):
    buttons.set(buttons.left, colors.light_pink)
    buttons.set(buttons.middle, colors.hot_pink)
    buttons.set(buttons.right, colors.grey)
    # set image

  def pick_suit(self):
    buttons.set(buttons.left, colors.yellow)
    buttons.set(buttons.middle, colors.orange)
    buttons.set(buttons.right, colors.purple)
    # set image

  def play(self):
    buttons.set(buttons.left, colors.off)
    buttons.set(buttons.middle, colors.off)
    buttons.set(buttons.right, colors.grey)
    # set image

  def left(self):
    if self.tracking.positive == None:
      self.tracking.positive = False
      self.pick_target()
    elif self.tracking.target == None:
      self.tracking.target = 5
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "circle"
      self.play()

  def middle(self):
    if self.tracking.positive == None:
      self.tracking.positive = True
      self.pick_target()
    elif self.tracking.target == None:
      self.tracking.target = 10
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "triangle"
      self.play()

  def right(self):
    if self.tracking.target == None:
      self.tracking.positive = True
      self.tracking.target = 0
      self.pick_suit()
    elif self.tracking.suit == None:
      self.tracking.suit = "square"
      self.play()
    else:
      self.start()
