#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
#%%
import numpy as np
#%%
altura_y_pesos = np.array([[ 1.74, 91.40 ],
                           [ 1.80, 88.70 ],
                           [ 1.78, 87.30 ],
                           [ 1.68, 62.70 ],
                           [ 1.78, 81.60 ]])
#%%
# axis=0 Columnas; axis=1 Filas
print(f'\nMínimo: {altura_y_pesos.min(axis=0)}')
print(f'\nMáximo: {altura_y_pesos.max(axis=0)}')
print(f'\nPos Mínimo: {altura_y_pesos.argmin(axis=0)}')
print(f'\nPos Máximo: {altura_y_pesos.argmax(axis=0)}')
print(f'\nPromedio: {altura_y_pesos.mean(axis=0)}')
print(f'\nSuma: {altura_y_pesos.sum(axis=0)}')
# %%
