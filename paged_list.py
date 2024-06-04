import buttons
import math
import screens

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
    screens.clear()
    font = screens.fonts.get_regular_font(40)
    backup = screens.fonts.get_backup_font(50)
    x = (20, 80)
    y = (20, 100, 180)
    x2 = x[1] + 15
    y2 = (60, 140)

    name = self.list[self.current * 2].name
    screens.write_text('1.', font, (x[0], y[0]))
    screens.write_text(name[0], font, (x[1], y[0]))
    if len(name) > 1:
      screens.write_text(name[1], font, (x2, y2[0]))

    if len(self.list) > (self.current * 2) + 1:
      name = self.list[(self.current * 2) + 1].name
      screens.write_text('2.', font, (x[0], y[1]))
      screens.write_text(name[0], font, (x[1], y[1]))
      if len(name) > 1:
        screens.write_text(name[1], font, (x2, y2[1]))
    else:
      screens.write_text('2.', font, (x[0], y[1]))
      screens.write_text('→', backup, (x[1]-5, y[1]-14))

    screens.write_text('3.', font, (x[0], y[2]))
    screens.write_text('→', backup, (x[1]-5, y[2]-14))

    screens.add_legend('1', '2', '3')
    screens.show()

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
    if len(self.list) > (self.current * 2) + 1:
      item = self.list[(self.current * 2) + 1]
      item.action(*item.arguments)
    else:
      self.next()
