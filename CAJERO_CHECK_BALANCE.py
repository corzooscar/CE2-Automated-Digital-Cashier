import datetime
import time
saldo_inicial = 1000.0

opcion=int (input("cuantas operaciones desea relizar: "))
cant_opera=0
while True:
    print("menu de opciones: ")
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. depositar dinero")
    print("finalizar programa")
    opcion_2 = int(input("elija una opcion (1-4): "))
    cant_opera=+1
    
    # OPCION 1

    if opcion_2== 1:

        fecha_actual = datetime.date.today()
        hora_actual = time.strftime("%H:%M:%S")
        print("fecha: ",fecha_actual)
        print("hora: ",hora_actual)
        print("Tu saldo actual es: ", saldo_inicial )
        print("\n") 
        

    
    if opcion_2 == 2:
        retirar_dinero = float(input("cuanto desea retirar?:"))
        if retirar_dinero>saldo_inicial:
            print("no tienes fondos suficientes")
            cant_opera=+1
        else :
            saldo_inicial-=retirar_dinero
            print("su nuevo saldo es: ",saldo_inicial,"su monto retirado fue: ",retirar_dinero)
    if opcion_2 == 3:
            depositar=float(input("cuanto dinero desea depositar: "))
            if depositar>0:
                saldo_inicial+=depositar
                print("su nuevo saldo es: ",saldo_inicial)
    elif opcion_2 == 4:
        print("proceso finalizado")
        break

