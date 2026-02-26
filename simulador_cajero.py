saldo = 1000
operaciones = int(input("Introduce el numero de operaciones a realizar: "))

for i in range(operaciones):
    accion = int(input("Elija la accion a realizar: 1.Consultar saldo // 2.retirar dinero // 3.Depositar dinero: "))

    while accion < 1 or accion > 3:
        int(input("Opcion invalida, intentelo de nuevo: "))

#OPCION 1 - MOSTRAR SALDO
    if accion == 1:
        print ("Su saldo actual es de:" ,saldo)
#---------------------------------------------------------------------------------------------------------
#OPCION 2 - RETIRAR SALDO
    if accion == 2:
        valor_retirar = int(input("Ingrese el valor a retirar: "))
        while valor_retirar < 0:
            valor_retirar = int(input("Monto invalido, ingrese un valor positivo: "))

        if saldo < valor_retirar:
            print("Fondos insuficiente")

        if saldo >= valor_retirar:
             print("Retiro validado, nuevo saldo disponible: ",saldo-valor_retirar)
#-------------------------------------------------------------------------------------------------------------
#OPCIONES 3 - DEPOSITAR DINERO
    if accion == 3:
        saldo = saldo-valor_retirar
        deposito = int(input("Ingrese el monto a depositar: "))
        while deposito < 0:
            deposito = int(input("Error, ingrese un valor positivo: "))

        if deposito > 0:
            print ("Su nuevo saldo es: ", saldo+deposito)


print(" Gracias por usar el cajero automatico")