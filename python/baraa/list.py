#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
#%%
import copy

#%%
vacia = []
print(vacia)
#%%
lista = [1,2,3,4,5,6]
print(lista[:3])
print(lista[7:])
print(lista[1:5])
#%%
# Deben coincidir las variables, si no se declaran todas las variables entonces usar el *resto
uno, dos, tres, *resto = lista
print(uno)
print(dos)
print(tres)
#%%
primero, *resto, ultimo = lista
print(primero)
print(resto)
print(ultimo)
#%% underscore obvia la declaración de esa variable
primero, _, _, cuatro, _ , *resto = lista
print(primero)
print(cuatro)
print(resto)
#%% *_ obvia el resto de las variables
primero, *_ = lista
print(primero)
#%%
max(lista)
#%%
min(lista)
#%%
sum(lista)
#%%
len(lista)
#%% % devuelve True si se cumplen TODOS
all(lista)
#%%
all([1,0,6])
#%
all(['s', '', 'y'])
#%% any devuelve True si cumple AL MENOS UNO
any(lista)
#%%
any(['s', '', 'y'])
#%%
lista.count(5)
#%% cuenta la cantidad de veces que se encuentra el elemento que se pasa por parámetro
lista.append(5)
lista.count(5)
# %%
print(9 in lista)
print(9 not in lista)
#%% sort / reverse cambia la lista original
letras = ['z', 'b', 'g', 'a']
print(letras)
letras.sort(reverse=True)
print(letras)
letras.sort()
print(letras)
letras.reverse()
print(letras)
# %%
matrix = [
    ['d', 't', 'a'],
    ['h', 'a', 'b'],
    ['p', 'x', 'b']
]
print(matrix)
matrix[1].sort()
print(matrix)
# %% sorted reversed no cambia la original
letras = ['h', 'z', 'b', 'g', 'a']

nueva_letras = sorted(letras)
print(nueva_letras)

nueva_letras = sorted(letras, reverse=True)
print(nueva_letras)

nueva_letras = list(reversed(letras))
print(nueva_letras)
print(letras)

#%% Asignación: comparten la referencia en la memoria, un cambio en una variable se observa en la otra variable
letras_copy = letras
#%%
letras.append('y')
#%%
print(letras)
print(letras_copy)

#%% Copy: copia la variable y cada una apunta a un espacio diferente de la memoria y tienen diferentes referencias
letras_copy = letras.copy()
letras.append('y')
print(letras)
print(letras_copy)

# %% Copy: los niveles inferiores comparten la referencia en la memoria
matrix_copy = matrix.copy()
matrix[1].append('z')
print(matrix)
# %% copy.deepcopy resuelve las referencias en los niveles inferiores
# matrix[1].pop()
matrix_copy = copy.deepcopy(matrix)
matrix[1].append('z')
print(matrix)
print(matrix_copy)
#%% asignacion
original = [
    ['a', 'b'],
    ['c', 'd']
]
copy1 = original
print(f'Misma lista? {copy1 is original}')

#%% Shallow copy
copy2 = original.copy()
print(f'Misma lista? {copy2 is original}')
print(f'Misma referencia? {copy2[0] is original[0]}')

#%% Deep copy
copy3 = copy.deepcopy(original)
print(f'Misma lista? {copy3 is original}')
print(f'Misma referencia? {copy3[0] is original[0]}')
# %%
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]
#%%
comb = letras + numeros
comb # type: ignore
# %%
numeros.extend(letras) # type: ignore
print(numeros)
print(letras)
# %%
letras = ['a', 'b', 'c']
numeros = [1, 2, 3, 4]

comb = list(zip(letras, numeros, 'hola'))
comb # type: ignore
#%% Iterador for, while / Iterable: listas, dicc, conjuntos
arr = []
for l in 'abracadabra':
    arr.append(l)

print(arr)  
palabra = ''
for l in arr:
    palabra += l

print(palabra)

#%%
pal = ''
for letra in (list(map(str.upper, palabra))):
    pal += letra

pal  # pyright: ignore[reportUnusedExpression]

#%% Filtros
letras = ['a', '', 'b', None, 'c', '23']
print(list(filter(None, letras))) # filtra quitando los None (falsos)
print(list(filter(bool, letras))) # filtra quitando los falsos

letras = ['a', '45', 'b', 'c', '23']
print(list(filter(str.isalpha, letras))) # se define cualquier función para filtrar

#%% Lambda
multiplicar = lambda x: x*2  # noqa: E731
print(multiplicar(3))

suma = lambda x, y: x + y  # noqa: E731
print(suma(3,7))
# %%
precios = [12, 234, 43, 456, 67]
print(list(filter(lambda x: x > 100, precios)))

#%% Listas por comprensión
# multiplicar * 2 los números menor a 50
precios = [1, 234, 43, 456, 49]

precios_mod = [p * 2 for p in list(filter(lambda p: p < 50, precios))]
print(precios_mod)

precios_mod2 = [p * 2 for p in precios if p < 50]
print(precios_mod2)

precios_new = []
for p in precios:
    while p < 1000:
        p *=2
    precios_new.append(p)

print(precios_new)
print(list(enumerate(precios_new)))
