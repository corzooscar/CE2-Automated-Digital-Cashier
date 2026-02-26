saldo = 1000
print("Bienvenido al cajero Automatico")
operaciones = int(input("que operacion desea realizar:"))
for i in range(operaciones): int(input("\n 1.Consultar saldo \n 2.depositar dinero\n 3.retirar dinero"))
while operaciones <1 or operaciones >3:
    int(input("operacion invalida, ingrese nuevamente."))


    
    