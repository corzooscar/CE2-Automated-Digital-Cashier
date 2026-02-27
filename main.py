Saldo = 1000
Cant_Operaciones = int(input(" --- ¡Bienvenido al Cajero Automático! ---\n ¿Cuántas operaciones desea realizar?:  "))

for i in range (Cant_Operaciones) :
    Conteo = i + 1
    Opcion = int(input(f"\n ------------ Menú Principal ------------#{Conteo}  \n 1 → Consultar saldo \n 2 → Retirar dinero \n 3 → Depositar dinero \n ➤ "))
    while Opcion < 1 or Opcion > 4:
        print("\nERROR: Por favor ingrese una opción válida")
        Opcion = int(input(f"\n ------------ Menú Principal ------------ | #{Conteo}  \n 1 → Consultar saldo \n 2 → Retirar dinero \n 3 → Depositar dinero "))
    if Opcion == 1:

        print("Tu saldo actual es: ", saldo )
        print("-"*30)
        print("\n") 
        
    elif Opcion == 2:
        try:
            monto_retirar = int(input("\ningrese el monto a retirar: "))
        except ValueError:
            print("\nMonto no válido. Por favor, ingrese un número entero.\n")
            continue
        while monto_retirar < 0:
            print("\nMonto no válido. Por favor, ingrese un monto positivo.\n")
            try:
                monto_retirar = int(input("ingrese el monto a retirar: "))
            except ValueError:
                print("\nMonto no válido. Por favor, ingrese un número entero.\n")
                continue
        if monto_retirar > saldo:
            print("\nFondos insuficientes\n")
        else:
            saldo -= monto_retirar
            print(F"\nRetiro exitoso. Su nuevo saldo actualizado es de: {saldo}\n")
            print("\nGracias por usar el cajero automático")

    if Opcion == 3:
        
        try: 
            deposito = int(input("Ingrese el monto a depositar: "))
            while deposito < 0:
                deposito=int(input("Error, ingrese un valor positivo: "))
        except ValueError:
            print("\nMonto no válido. Por favor, ingrese un número entero.\n")
            deposito = int(input("Ingrese el monto a depositar: ")) 

    if deposito > 0:
            print ("Su nuevo saldo es: ", saldo+deposito)


print(" Gracias por usar el cajero automatico")
