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
X = np.linspace(0.1, 6)
Y = np.sin(X)

plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(X, Y, linewidth=3, linestyle=(0, (6, 4)))

plt.show()
# %%
plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(X, Y, linewidth=3, linestyle='dashed') # solid, dashed, dashdot, dotted

plt.show()

# %%
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
ax.stem(X, Y, linefmt='r', label='stem plot', basefmt='green', markerfmt='b' )

ax.spines['left'].set_color('b')
ax.spines['left'].set_linewidth(3)
ax.spines['left'].set_linestyle('--')
ax.spines['top'].set_visible(False)

ax.grid(True, linewidth=2, linestyle=(0, (4,3)), color='g')

plt.legend()
plt.show()
# %%
