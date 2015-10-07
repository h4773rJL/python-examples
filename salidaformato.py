#! /usr/bin/python3

while True:
    entrada = input("-->")
    if entrada == "*":
        break
    else:
        print ("Caracter expresado en numero es [ %d ]" % ord(entrada))
