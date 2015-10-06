#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import print_function
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def puttextimg(name, namefile):
    im = Image.open("reconocimiento.jpg")
    outfile = namefile

    font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSans-Bold.ttf", 145)
    text = name
    tcolor = (0, 0, 0)
    text_pos = (715, 1540)

    draw = ImageDraw.Draw(im)
    draw.text(text_pos, text, fill=tcolor, font=font)

    im.save(outfile, "JPEG")
    return


destiny = 'heatseeker.persa@gmail.com'

f = open('nombres.csv', 'r')

for line in f:
    separated = line.split(',')
    name = separated[0] + " " + separated[1] + " " + separated[2]
    namefile = name + ".jpg"
    email = separated[3]
    puttextimg(name, namefile)
    print(name, email)

f.close()
