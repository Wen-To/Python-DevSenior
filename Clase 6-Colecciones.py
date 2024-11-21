#COLECCIONES - LISTAS
nombres = ['Juan', 'Sebastian', 'Melissa', 'Xiomara']

print(nombres)
print(nombres[1])
print(nombres[-1])
print(nombres[2:3])

# Para conocer la cantidad de elementos de la lista
print("\nPara conocer la cantidad de elementos de la lista")
print(len(nombres))
# Para adicionar un elemento al final de la lista
print("\nPara adicionar un elemento al final de la lista")
nombres.append("Elizabeth")
print(nombres)
# Para insertar un elemento en una posición específica
print("\nInserto a María en la segunda posición de la lista")
nombres.insert(1, "María")  # Inserto a María en la segunda posición de la lista
print(nombres)
# Para eliminar un elemento de la lista
print("\nElimina el elemento especificado")
nombres.remove("Elizabeth")  # Elimina el elemento especificado
print(nombres)
print("\nElimina el último elemento de la lista")
nombres.pop()  # Elimina el último elemento de la lista
print(nombres)
print("\nElimina según el índice especificado")
del nombres[1]  # Elimina según el índice especificado
print(nombres)
nombres.pop(1)  # Elimina según el índice especificado
print(nombres)
nombres.clear() # limpiar la lista
print(nombres)
nombres.append("Elizabeth")
print(nombres)

#TUPLAS
paises = ('Colombia', 'Mexico', 'Ecuador', 'Venezuela')
print(paises)
print(len(paises))#Cuandos elementos tengo en la lista
print(paises[2])#Imprimir la posicion 2 de la lista
print(paises[-1])#Imprimir el ultimo en la lista
print(paises)
for pais in paises:
    print(pais)
paisesLista = list(paises)
paisesLista[1] = 'Argentina'
paises = tuple(paisesLista)
print(paises)

#SET
lenguajes = {'Java', 'Python', 'JavaScript'}
print(lenguajes)
print(len(lenguajes))
print('Java' in lenguajes)
lenguajes.add('Go')
print(lenguajes)
for lenguaje in lenguajes:
    print(lenguajes)
lenguajes.remove('Java')
print(lenguajes)
lenguajes.discard('Go')
print(lenguajes)
