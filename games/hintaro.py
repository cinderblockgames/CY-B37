from PIL import Image, ImageDraw
import screens

class Game:
  def __init__(self):
    image = self._image = Image.new("1", (300, 400), 0xFF) # 1 for B/W, fill with white
    draw = ImageDraw.Draw(image)

    Xs = (5, 60, 115, 170, 225)
    Ys = (10, 70, 130, 190)

    text_args = { "font": screens.fonts.get_regular_font(48), "fill": 0x00 }
    for index in range(4):
      draw.text((Xs[0], Ys[index]), f"{index + 1}.", **text_args)

    kulro = screens.images.get_image("kulro.png")
    tukar = screens.images.get_image("tukar.png")
    hin   = screens.images.get_image("hin.png"  )
    taro  = screens.images.get_image("taro.png" )

    y = Ys[0] - 15
    image.paste(tukar, (Xs[1], y), tukar)
    image.paste(tukar, (Xs[2], y), tukar)
    image.paste(kulro, (Xs[3], y), kulro)
    image.paste(kulro, (Xs[4], y), kulro)

    y = Ys[1] - 15
    image.paste(kulro, (Xs[1], y), kulro)
    image.paste(kulro, (Xs[2], y), kulro)
    image.paste(kulro, (Xs[3], y), kulro)
    image.paste(kulro, (Xs[4], y), kulro)

    y = Ys[2] - 15
    image.paste(tukar, (Xs[1], y), tukar)
    image.paste(tukar, (Xs[2], y), tukar)

    y = Ys[3] - 15
    image.paste(kulro, (Xs[1], y), kulro)
    image.paste(kulro, (Xs[2], y), kulro)

    rect_args = { "outline": 0x00, "width": 3 }
    draw.rectangle([( 10,290), (150,360)], **rect_args)
    draw.rectangle([(150,290), (290,360)], **rect_args)
    image.paste(hin  , ( 15,290), hin)
    image.paste(tukar, ( 75,290), tukar)
    image.paste(taro , (155,290), taro)
    image.paste(kulro, (215,290), kulro)

    line_args = { "fill": 0x00, "width": 3 }
    y1, y2 = 295, 355
    x1, x2 = 85, 135
    draw.line([(x1,y1), (x2,y2)], **line_args)
    draw.line([(x1,y2), (x2,y1)], **line_args)
    x1, x2 = 225, 275
    draw.line([(x1,y1), (x2,y2)], **line_args)
    draw.line([(x1,y2), (x2,y1)], **line_args)

  def start(self):
    screens.replace_image(self._image)
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
