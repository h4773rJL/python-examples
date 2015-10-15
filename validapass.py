#! /usr/bin/python3
import re


def ismayor(a):
    if (len(a) < 8):
        print ('La contraseña debe contener al menos 8 caracteres', end='\n')
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



def ismenor(a):
    if (len(a) > 12):
        print ('El nombre de usuario no puede contener mas de 12 caracteres.', end='\n')
        return False
    return True


def alfanumeric(a):
    if (a.isalnum()):
        return True
    else:
        print ('No es Alfanumerica', end='\n')
        return False

#print ('Escriba una contraseña al menos 8 caracteres alfanumericos', end='\n')
paswd = str(input('User: '))
print ('pass: ', minus(paswd))
print ('pass: ', mayus(paswd))
print ('pass: ', unnum(paswd))