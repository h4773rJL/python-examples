#! /usr/bin/python3
import re

err = "La contraseña no es segura"
msg = "Escriba una contraseña al menos 8 caracteres alfanumericos"


def ismayor(a):
    if (len(a) < 8):
        return False
    return True


def minus(a):
    patron = ('[a-z]')
    flag = False
    for letra in a:
        if (re.match(patron, letra)):
            flag = True
    return flag


def mayus(a):
    patron = ('[A-Z]')
    flag = False
    for letra in a:
        if (re.match(patron, letra)):
            flag = True
    return flag


def unnum(a):
    patron = ('[0-9]')
    flag = False
    for letra in a:
        if (re.match(patron, letra)):
            flag = True
    return flag


def alfanumeric(a):
    if (a.isalnum()):
        return True
    else:
        return False



salida = False
while salida is False:
    try:
        print (msg, end='\n')
        paswd = str(input('passwd: '))
        if (ismayor(paswd)):
            if (alfanumeric(paswd)):
                if (minus(paswd) and mayus(paswd) and unnum(paswd)):
                    salida = True
                    print (salida, end='\n')
                else:
                    print (err, end='\n')
        else:
            print (err, end='\n')
    except (KeyboardInterrupt, EOFError):
        print (msg, end='\n')