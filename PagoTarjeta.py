#reciban por consola el valor de una compra
#que pueda ingresar el numero de cuotas con las que s eva ha pagar
#calcular el valor de la cuotas, (no vamos a calcular intereses)
#en un ciclo while queremos que muestre
#que imprima el plan de pago y le muestre el cupo liberado
#con cada pago
#cuota 1=1000
#cuota 2=1000
#cupo liberado=numero cuotas por valorcuota menos valor pagado
#agregarle un menu
#generar una funcionalidad
valorCompra=int(input("ingrese el valor compra"))
nroCuotas=int(input("ingrese las cuotas"))
valorCuota=valorCompra/nroCuotas
cuotActual=0
saldoActual=valorCompra
while cuotActual<nroCuotas:
    cuotActual+=1
    saldoActual-=valorCuota
    print("cuota",cuotActual,"=",valorCuota, " saldo: ", saldoActual)
      
# Generar un programa que permita hacer el registro e iniciar sesion dentro de while, 
# debe imprimir el menu usando la implementacion de if, elif , else (Selector multiple). 
# Cuando inicie sesion que implemente la solucion del calculo de cuotas creada en el reto anterio.           

    

   


