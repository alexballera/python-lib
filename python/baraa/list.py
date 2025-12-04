#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
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
# %%
