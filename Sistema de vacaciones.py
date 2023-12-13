print("*******************************")
print("Sistema de vacaciones de rapi")
print("******************************")


nombre = input("Cual es tu nombre?: ")
clave = int (input("Escrbia su clave: "))
Tiempo_Empresa= float(input("Tiempo que lleva en la empresa: "))

if clave == 1:
    print("Departamente de atencion al cliente")
    
    if Tiempo_Empresa >= 1 and Tiempo_Empresa < 2:
        print( "El empleado", nombre,  "Tiene derecho a 6 dias de vacaciones")
    elif Tiempo_Empresa >= 2 and Tiempo_Empresa<= 6:
        print("El empleado", nombre,"Tiene derecho a 14 dias de vacaciones")
    elif Tiempo_Empresa >=7:
        print("El empleado", nombre," tiene Derecho a 20 dias de vacaciones")
    else: 
        print("El empleado",nombre, "No tiene derecho a vacaciones")

elif clave==2:
    print("Logistica")
    if Tiempo_Empresa >=1 and Tiempo_Empresa<2:
        print("El empleado", nombre,"Tiene derecho a 7 dias de vacaciones")
    elif Tiempo_Empresa >=2 and Tiempo_Empresa<= 6:
        print("El empleado", nombre,"Tiene derecho a 15 dias de vacaciones")
    elif Tiempo_Empresa >= 7:
        print("El empleado", nombre,"Tiene derecho a 22 dias de vacaciones") 
    else: 
        print("El empleado",nombre, "No tiene derecho a vacaciones")

elif clave ==3:
    print("Gerencia")
    if Tiempo_Empresa>=1 and Tiempo_Empresa<2:
        print("El empleado", nombre,"Tiene derecho a 10 dias de vacaciones")
    elif Tiempo_Empresa >=2 and Tiempo_Empresa<= 6:
        print("El empleado", nombre,"Tiene derecho a 20 dias de vacaciones ")
    elif Tiempo_Empresa >=7: 
        print("El empleado", nombre,"TIene derecho a 30 dias de vacaciones")
    else: 
        print("El empleado",nombre, "No tiene derecho a vacaciones")
else:
    print("No existe esa clave")
