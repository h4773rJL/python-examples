#! /usr/bin/python3

<<<<<<< HEAD

=======
>>>>>>> 770336ef9b9d6f0247aea36f20d47fa963fe2dd3
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

<<<<<<< HEAD
print ('Escriba un nombre de usuario de 6 a 12 caracteres alfanumericos', end='\n')
=======
>>>>>>> 770336ef9b9d6f0247aea36f20d47fa963fe2dd3
salida = False
while salida is False:
    try:
        user = str(input('User: '))
<<<<<<< HEAD
        if (ismenor(user) and ismayor(user) and alfanumeric(user)):
            salida = True
            print (salida, end='\n')
        else:
            print ('Intente nuevamente...', end='\n')
    except (KeyboardInterrupt, EOFError):
        print ('Escriba un nombre de usuario de 6 a 12 caracteres alfanumericos', end='\n')
=======
        #print ('-< ', ismenor(user))
        #print ('-> ', ismayor(user))
        #print ('-a1 ', alfanumeric(user))
        if (ismenor(user) and ismayor(user) and alfanumeric(user)):
            print ('usuario correcto', end='\n')
            salida = True
        else:
            print ('nuevaente...')
    except (KeyboardInterrupt, EOFError):
        print ('Escriba un nombre de usuario de 6 a 12 caracteres alfanumericos')
>>>>>>> 770336ef9b9d6f0247aea36f20d47fa963fe2dd3
