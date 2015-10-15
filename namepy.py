#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import print_function
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#definimos la función que pondra el texto en la imagen
#(nombre a colocar, nombre del archivo)


def puttextimg(name, namefile):
        """usamos PIL para cargar la imagen del reconocimiento
...seleccionamos la fuente ttf, el color y la posición dentro de la imagen
...     y escribimos el nombre. by. h4773r
... """
    im = Image.open("reconocimiento.jpg")
     #archivo jpg del reconocimiento sin nombre
    outfile = namefile
     #juan te llamas.jpg

    pathfont = "DJB Angel Baby.ttf"
    font = ImageFont.truetype(pathfont, 145)
    text = name
     #nombre a colocar
    tcolor = (15, 21, 106)
     #color negro
    text_pos = (600, 1420)
     #coordenadas de donde se colocará el texto

    draw = ImageDraw.Draw(im)
    draw.text(text_pos, text, fill=tcolor, font=font)

    im.save(outfile, "JPEG")
     #guardamos el nuevo archivo
    return

f = open('nombres.csv', 'r')
 #abrimos el arhivo en opendata

for line in f:
    #Mientras existan lineas en el apuntador de lectura del archivo
    separated = line.split(',')
    #separamos nombre, apellido1, apellido2, email
    name = separated[0] + " " + separated[1] + " " + separated[2]
    namefile = "files/" + name + ".jpg"
    #se requiere capeta files
    email = separated[3]
    #el correo electronico
    puttextimg(name, namefile)
    #llamamos a la función para colocar texto
    print(name, email)
    #mostramos solo en mobre y el correo

f.close()