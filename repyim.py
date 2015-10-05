#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import print_function
import os, sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

im = Image.open("5.jpg")
outfile = "name.jpg"

font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf",145)
text = "José Luis Pérez Rendón"
tcolor = (0,0,0)
text_pos = (515,1320)

draw = ImageDraw.Draw(im)
draw.text(text_pos, text, fill=tcolor, font=font)

im.save(outfile,"JPEG")

