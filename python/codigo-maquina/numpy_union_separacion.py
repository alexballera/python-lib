#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
#%%
import numpy as np
#%%
altura = np.array([1.74, 1.80, 1.78, 1.68, 1.78])

peso = np.array([91.40, 88.70, 87.30, 62.70, 81.60])
#%%
print(f'axis=0 por líneas = \n{np.stack((altura, peso), axis=0)}')
print(f'axis=1 por columnas = \n{np.stack((altura, peso), axis=1)}')
print(f'concatenate = \n{np.concatenate((altura, peso))}')
# %%
union = np.stack((altura, peso), axis=0)
print(union, type(union))
print()
separados = np.split(union, 2)
print(separados, type(separados))
#%%
union2 = np.stack((altura, peso), axis=1)
print(union2, type(union2))
print()
separados2 = np.split(union2, 5)
print(separados2, type(separados2))
# %%
