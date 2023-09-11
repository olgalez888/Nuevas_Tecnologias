#Python en visual studio code, por defecto todo en py es un objeto
#Que es tipado?
#python no tiene tipado, es dinamicamente tipado
#duplas son inmutables?
#casteo nivel de datos en la que esta, es cambiar tipo de variable
#lo que no se puede es csmbiar un entero por un byte, por eso casteo 
#hacia arriba
#si cambio de float a entero pierdo decimales, pierdo informacion

#Primer ejercicio
print("hola")
name="pepi"
salario="2000000"
note=4.5
isOn=True
fruits=["banana", "mango", "fresa"]
names=("carlos", "antoni", "wil")  #esto es una tupla
cars={"suv":"mazda cx30", "sedan":"kia rio"} #Esto es un diccionario
edades={19, 28, 35}  #esto es un conjunto o set
B=b"pepi" #esto es un byte

print(name)
print(type(name))
print(type(salario))
print(type(note))
print(type(isOn))
print(type(fruits))
print(type(names))
print(type(cars))
print(type(edades))



