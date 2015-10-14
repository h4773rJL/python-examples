#! /usr/bin/python3

import math


def suma():
    while True:
        try:
            a = eval(input('primer valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    while True:
        try:
            b = eval(input('segundo valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')
    r = a + b
    return r


def resta():
    while True:
        try:
            a = eval(input('primer valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    while True:
        try:
            b = eval(input('segundo valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    r = a - b
    return r


def multi():
    while True:
        try:
            a = eval(input('primer valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    while True:
        try:
            b = eval(input('segundo valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    r = a * b
    return r


def divi():
    while True:
        try:
            a = eval(input('primer valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    while True:
        try:
            b = eval(input('segundo valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    try:
        r = a / b
    except ZeroDivisionError:
        print ('la división por cero no esta definia')
        r = 0
    return r


def expo():
    while True:
        try:
            a = eval(input('primer valor: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    while True:
        try:
            b = int(input('a la potencia: '))
            break
        except ValueError:
            print('Oops!  That was no int valid number.  Try again...')
    r = a ** b
    return r


def loga():
    while True:
        try:
            a = eval(input('Logaritmo base 10 de:  '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    r = math.log(a, 10)
    return r


def seno():
    while True:
        try:
            a = eval(input('seno:  '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')

    r = math.sin(a)
    return r


def coseno():
    while True:
        try:
            a = eval(input('coseno:  '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')
    r = math.cos(a)
    return r


def tangente():
    while True:
        try:
            a = eval(input('tangente:  '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')
    r = math.tan(a)
    return r


def aseno():
    while True:
        try:
            a = eval(input('calcular seno inverso: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')
    r = math.asin(a)
    return r


def acoseno():
    while True:
        try:
            a = eval(input('calcular coseno inverso: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')
    r = math.acos(a)
    return r


def atangente():
    while True:
        try:
            a = eval(input('calcular tangente inversa: '))
            break
        except NameError:
            print('Oops!  That was no valid number.  Try again...')
    r = math.tanh(a)
    return r

print ("Calculadora")
print ("1. suma", end='\n')
print ("2. resta", end='\n')
print ("3. multiplicación", end='\n')
print ("4. división", end='\n')
print ("5. x levado a la y", end='\n')
print ("6. Logaritmo base 10", end='\n')
print ("7. Exponencial", end='\n')
print ("8. seno", end='\n')
print ("9. coseno", end='\n')
print ("10. tangente", end='\n')
print ("11. arco seno", end='\n')
print ("12. arco coseno", end='\n')
print ("13. arco tangente", end='\n')
print (" ---", end='\n')
print ("20. Salir", end='\n')

se = eval(input('Selecciona: '))

if se < 0:
    print('Negative changed to zero')
elif se == 1:
    print('suma: ', suma())
elif se == 2:
    print('resta: ', resta())
elif se == 3:
    print('Multiplicacion: ', divi())
else:
    print('error')
