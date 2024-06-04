import buttons
import screens

class Game:

  def __init__(self):
    self.external = None

  def start(self):
    buttons.clear()
    screens.replace_image(screens.images.get_image('hintaro.bmp'))
    screens.show()

  def left(self):
    # hintaro doesn't have any additional functionality
    pass

  def middle(self):
    # hintaro doesn't have any additional functionality
    pass

  def right(self):
    # hintaro doesn't have any additional functionality
    pass
