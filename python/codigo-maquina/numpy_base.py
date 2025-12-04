#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
#%%
import numpy as np
#%%
lista = [1,2,3,4,5,6]
arreglo = np.array(lista)
arreglo2 = np.arange(1,7)
print(arreglo)
print(arreglo2)
# %%
lista = [1,2,3,4,5,6]
# dtype i = int por defecto int32 32 bits = 4 bytes
arreglo = np.array(lista, dtype='i') 
print(arreglo, arreglo.dtype, arreglo.itemsize)

# dtype i2 = int int16 16 bits = 2 bytes
arreglo = np.array(lista, dtype='i2')
print(arreglo, arreglo.dtype, arreglo.itemsize)

# dtype i4 = int32 32 bits = 4 bytes
arreglo = np.array(lista, dtype='i4')
print(arreglo, arreglo.dtype, arreglo.itemsize)

# dtype i8 = int64 64 bits = 8 bytes
arreglo = np.array(lista, dtype='i8')
print(arreglo, arreglo.dtype, arreglo.itemsize)