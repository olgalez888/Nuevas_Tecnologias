#casting de variable

num1=4.5
num2=int(4.5)
print(num2) #me muestra 4, pierde info

number="3"
number1=int("3")
print(number1) #aparece 3
print(type(number1)) #es de clase int

name=input("ingrese su nombre") #ponemos pepi en el ejecutador
print(name)
print("su nombre es:" +name) #con el simbolo + se debe dejar espacio
print("su nombre es:", name)
apellido=input("ingrese apellido")
id=input("ingrese id")
print("ver usuario:", name, apellido, id)
print("ingrese 1 o 0")
isOn=bool(1)
print(isOn)
isOn=bool(input("seleccione 1 si es casado?"))
print(type(isOn))
print(isOn) #me da true



