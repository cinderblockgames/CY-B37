import buttons
import math

class Item:

  def __init__(self, name, action, *arguments):
    self.name = name
    self.action = action
    self.arguments = arguments

class PagedList:

  def __init__(self, list, colors):
    self.list = list
    self.colors = colors
    self.current = 0
    self.last = math.ceil(len(list) / 2) - 1

  def _generate_image(self):
    pass

  def display(self):
    buttons.set(buttons.left, self.colors[0])
    buttons.set(buttons.middle, self.colors[1])
    buttons.set(buttons.right, self.colors[2])
    self._generate_image()

  def start(self):
    self.current = 0
    self.display()

  def next(self):
    self.current += 1
    if self.current > self.last:
      self.current = 0
    self.display()

  def left(self):
    item = self.list[self.current * 2]
    item.action(*item.arguments)

  def middle(self):
    item = self.list[(self.current * 2) + 1]
    item.action(*item.arguments)
