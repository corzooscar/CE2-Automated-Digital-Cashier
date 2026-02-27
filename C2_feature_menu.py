saldo = 1000
Cant_Operaciones = int(input(" --- ¡Bienvenido al Cajero Automático! ---\n ¿Cuántas operaciones desea realizar?:  "))

for i in range (Cant_Operaciones) :
    Conteo = i + 1
    Opcion = int(input(f"\n ------------ Menú Principal ------------#{Conteo}  \n 1 → Consultar saldo \n 2 → Retirar dinero \n 3 → Depositar dinero \n 4 → Finalizar \n ➤ "))
    while Opcion < 1 or Opcion > 4:
        print("\nERROR: Por favor ingrese una opción válida")
        Opcion = int(input(f"\n ------------ Menú Principal ------------ | #{Conteo}  \n 1 → Consultar saldo \n 2 → Retirar dinero \n 3 → Depositar dinero \n 4 → Finalizar \n ➤ "))
