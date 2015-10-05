#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import print_function
import os, sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def puttextimg ( name, namefile ):
    im = Image.open("5.jpg")
    outfile = namefile

    font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf",145)
    text = name
    tcolor = (0 , 0 , 0)
    text_pos = (515 , 1320)

    draw = ImageDraw.Draw(im)
    draw.text(text_pos, text, fill=tcolor, font=font)

    im.save(outfile,"JPEG")
    return;


destiny = 'heatseeker.persa@gmail.com'

f = open('nombres.csv', 'r')

for line in f:
	separated=line.split(',')
	name = separated[0]+" "+separated[1]+" "+separated[2]
	namefile = name+".JPG"
	email = separated[3]
	puttextimg(name, namefile)
	print(name,email,end='')

f.close()
