import random

def GenerarClave():
    longitud = random.randrange(8,10)
    clave = []
    for x in range(longitud):
        clave.append(chr(random.randrange(33,126)))
    return "". join(clave)

h = GenerarClave()
print (h)
