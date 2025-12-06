#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualización con Matplotlib
@author: Alex Ballera
"""
#%%
# Celda 1: Configuración
# %matplotlib widget
import matplotlib.pyplot as plt
import numpy as np

#%% https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
X = [1,2,3,4,5,6,7,8]
Y = [3,4,5,3,2,4,5,7]
Z = [1,3,2,5,5,7,4,6]

fig, ax = plt.subplots(figsize=(10,6))

ax.plot(X, Y, color='b', zorder=1)
ax.plot(X, Z, color='g', zorder=2)

plt.show()

#%%
X = ['A', 'B', 'C', 'D', 'E']
Y = [14, 7 ,18, 9, 10]

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(X, Y, color='b', edgecolor='r')

plt.show()
#%%