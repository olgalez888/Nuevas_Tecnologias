#examen 1

opc = 0
while opc < 3:

    opc = int(input("1. Registro\n 2. Tarjeta \n 3. Consultar usuarios\n 4. consultar lista prestamo\n 5. Registro\n"))

    if opc == 1:
        listaUsuario=[]

        for x in range(2):
            nombre=input("Ingrese Nombre")
            listaUsuario.append(nombre)

            apellido=input("Ingrese Apellido")
            listaUsuario.append(apellido)

            correo=input("Ingrese correo")
            listaUsuario.append(correo)

            numTarj=int(input("Ingrese numero tarjeta:"))
            listaUsuario.append(numTarj)
        print(listaUsuario)  



    elif opc == 2: 
        print("Tarjeta")
        listaNumTarjeta=[]
        for x in range(2):
            bicicletaNum=int(input("Ingrese Numero"))
            listaNumTarjeta.append(bicicletaNum)

            origen=input("Ingrese origen")
            listaNumTarjeta.append(origen)

            destino=input("Ingrese destino")
            listaNumTarjeta.append(destino)

            numTarjVal=int(input("Ingrese numero tarjeta:"))
            listaNumTarjeta.append(numTarj)   
        print(listaNumTarjeta)


        if nombre == "" or numTarj == "":
            print("Primero debe registrarse")

        elif numTarj == numTarjVal: 
            print("puede realizar prestamo de la bicicleta")
            
           
        else:
            print("nombre y numero tarjeta invalidos")



    elif opc == 3: 
            print("consultar usuario")

            nombre=input("Ingrese Nombre")
       
    if nombre in listaUsuario:
        print("nombre",nombre,"apellido",apellido, " correo: ", correo," numero de tarjeta: ", numTarj)



    elif opc == 4: 
        print("consultar prestamos",listaNumTarjeta)
   


    elif opc == 5: 
        print("salir")

    else:
        print("Seleccione una opcion Valida")  