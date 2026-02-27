saldo = 1000
accion = 0
   
#-------------------------------------------------------------------------------------------------------------
#OPCIONES 3 - DEPOSITAR DINERO
if accion == 3:

        deposito = int(input("Ingrese el monto a depositar: "))
        
        while deposito < 0:
         deposito=int(input("Error, ingrese un valor positivo: "))

         if deposito > 0:
            print ("Su nuevo saldo es: ", saldo+deposito)


print(" Gracias por usar el cajero automatico")
