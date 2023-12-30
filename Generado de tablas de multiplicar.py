#Hacer que un programa que realice la tabla de multiplicar que le pidamos
#hasta el 10. Debe imprimir en pantalla la tabla de multiplicar completa
#de la que se solicite.

num= int(input("Ingrese el numero del cual quiera saber la tabla: "))

for i in range(1,11):
    print(num,"x",i, "=", num*i)