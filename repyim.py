#! /usr/bin/python
# -*- coding:utf-8 -*-


from __future__ import print_function
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

im = Image.open("reconocimiento.jpg")
outfile = "name.jpg"

font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSans-Bold.ttf",145)
text = "José Luis Pérez Rendón"
tcolor = (0, 0, 0)
text_pos = (715, 1440)

draw = ImageDraw.Draw(im)
draw.text(text_pos, text, fill=tcolor, font=font)

im.save(outfile, "JPEG")

