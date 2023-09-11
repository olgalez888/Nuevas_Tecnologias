#listas son estructuras de datos lineales, se crean usando brackets ejemplo my_list=[]
#son listas ordenadas en el orden en que son ingresadas(orden de insersion)
#emplea metodos para manipular los items de la misma
#esto quiere decir que el ultimo dato ingresado ocupara la ultima posicion.
#como todas las listas la primer aposicion es cero
#permite items duplicados con indices diferentes
#las listas son mutables, podemos agregar actualizar o remover items
#puede contener distintos tipos de datos

#tuplas diccionarios set(conjunto). lista estan dentro de una estructura
#si quiero visualizar una lista va entre corchetes, cada elemen va ha tener un indice
#es dinamica es mutable puedo aregar elem nuevos, es ordenada, puedo remover tambien 
#puedo recorrer lalista con un for, puedo conocer su tamaño

nombres=["juan","pepito","maria","lisa"]
#el metodo len() valida el tamaño de la lista
print(len(nombres))
print(type(nombres))

listaDatos=["pepito","perez,",1000100100,1.80,True]
print(f"El numero de documento es:{listaDatos[2]}")
#slicing de datos
print(listaDatos[0:2])
print(listaDatos[1:4])
print(listaDatos[:4])
print(listaDatos[2:])

print(listaDatos[:-4])
print(listaDatos[:-3])
print(listaDatos[:-1])
print(listaDatos[:-2])
print(listaDatos[-1:-3])
print(listaDatos[-1:-4])
print(listaDatos[-4:-1])
print(listaDatos[1:4])





