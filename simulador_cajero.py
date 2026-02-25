saldo_inicial = 1000.0
opcion=int (input("cuantas operaciones desea relizar: "))
for i in  range(opcion):
    print("menu de opciones: ")
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. depositar dinero")
    opcion_2 = int(input("elija una opcion (1-3): "))
    cant_opera=+1
if opcion_2 == 1:
    print("su saldo actual es: ",saldo_inicial)
if opcion_2 == 2:
    retirar_dinero = float(input("cuanto desea retirar?:"))
    if retirar_dinero>saldo_inicial:
        print("no tienes fondos suficientes")
    else :
        saldo_inicial-=retirar_dinero
        print("su nuevo saldo es: ",saldo_inicial,"su monto retirado fue: ",retirar_dinero)
if opcion_2 == 3:
        depositar=float(input("cuanto dinero desea depositar: "))
        if depositar>0:
            saldo_inicial+=depositar
            print("su nuevo saldo es: ",saldo_inicial)

