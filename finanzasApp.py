#la aplicacion debe permitir registrar ingresos y contar el saldo de estos
#debe permitir registrar egresos y mostrar saldos
#si el ingreso es mayor que el saldo no debe permitir el retiro y mostrara
#un mensaje de saldo insuficiente, la app llevara registro de los movimientos 
#indicando el numero de ingresos y de egresos

saldo=int(input("ingrese el saldo"))
acumIngresos=0
acumEgresos=0
isOn=int(input("Ingrese 1 para incializar el servicio:"))

while isOn==1:
   opc=int(input("1.ingreso:\n 2.egresos\n 3.salir\n"))

   if opc==1:
      ingreso=int(input("Registre el ingreso"))

      saldo=saldo+ingreso

      print(f"su saldo es ${saldo}")
   #print("saldo es:"+saldo)
   #print("saldo es:",saldo)
      acumIngresos+=1
      print(acumIngresos)
   #acumIngresos=acumIngresos+1


   elif opc==2:
    egreso=int(input("Registre el monto a retirar:"))

    saldo=saldo-egreso

    if saldo<0:
      print("saldo insuficiente")
      saldo=saldo+egreso
      print(saldo)
      acumEgresos+=1
      print(acumEgresos)
    else:
      print(f"su saldo es:${saldo}")

   elif opc==3:
    print("salir")
    isOn=0
else:
    print("ingrese una opcion valida")
