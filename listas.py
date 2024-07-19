mi_lista = ['a', 'b','c']

print(type(mi_lista))

otra_lista = ["hola", 55, 5, ['a', 'b', 'c']]

resultado = mi_lista[1]

print(resultado)

resultado = mi_lista[0:]
print(resultado) 

mi_lista2 = ['z', 'y', 'x']

print(mi_lista + mi_lista2)
mi_lista[0] = "hola"
print(mi_lista)

resultado = otra_lista[1:3]
print(resultado)

mi_lista2.sort()
print(mi_lista2)

