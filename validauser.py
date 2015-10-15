#! /usr/bin/python3


def ismayor(a):
    if (len(a) < 6):
        print ('El nombre de usuario debe contener al menos 6 caracteres', end='\n')
        return False
    return True


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

print ('Escriba un nombre de usuario de 6 a 12 caracteres alfanumericos', end='\n')
salida = False
while salida is False:
    try:
        user = str(input('User: '))
        if (ismenor(user) and ismayor(user) and alfanumeric(user)):
            salida = True
            print (salida, end='\n')
        else:
            print ('Intente nuevamente...', end='\n')
    except (KeyboardInterrupt, EOFError):
        print ('Escriba un nombre de usuario de 6 a 12 caracteres alfanumericos', end='\n')