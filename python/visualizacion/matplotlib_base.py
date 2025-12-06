#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualización interactiva con Matplotlib
@author: Alex Ballera
"""
#%%
# Celda 1: Configuración
# %matplotlib widget
import matplotlib.pyplot as plt
import numpy as np

#%% pyplot
# Celda 2: Gráfico interactivo
x, y = [1,2,3,4], [1,2,4,3]
plt.plot(x, y)
plt.show()
# %% POO
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

# %% Pyplot
X = np.linspace(0, 2, 100)

plt.figure(figsize=(10, 6), layout='constrained')
plt.plot(X, X, label='linear')
plt.plot(X, X**2, label='quadratic')
plt.plot(X, X**3, label='cubic')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('Simple Plot')
plt.legend()
plt.show()
#%% POO
X = np.linspace(0, 2, 100)

fig, ax = plt.subplots(figsize=(10,6), layout='constrained')

ax.plot(X, X, label='linear')
ax.plot(X, X**2, label='quadratic')
ax.plot(X, X**3, label='cubic')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
ax.set_title('Simple Plot')
ax.legend()
plt.show()
# %%
