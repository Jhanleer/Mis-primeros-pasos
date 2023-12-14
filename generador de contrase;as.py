import random
from werkzeug.security import generate_password_hash

minus= "abcdefghijklmnopqrstuvwxyz"
mayus= minus.upper()
numeros= "0123456789"
simbolos= "[]{}()*;/,._-"

base= minus + mayus + numeros + simbolos
longitud= 20

for _ in range(10):
    muestra= random.sample(base, longitud)
    #el .join() convierte una lista en un string
    password= "".join(muestra)
    password_encripato= generate_password_hash(password)
    print("{} , {}" .format(password, password_encripato))