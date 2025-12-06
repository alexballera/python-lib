#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualización con Matplotlib - Configuración de Ejes
@author: Alex Ballera
"""
#%%
# REFERENCIA RÁPIDA: Configuración y Personalización de Ejes
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html
# https://matplotlib.org/stable/api/ticker_api.html
'''
=============================================================================
CONFIGURACIÓN BÁSICA DE EJES (ax.set)
=============================================================================

ax.set() permite configurar múltiples propiedades del eje simultáneamente:

ax.set(
    xlim=(0, 10),            # Límites del eje X (min, max)
    ylim=(0, 100),           # Límites del eje Y (min, max)
    xlabel='Eje X',          # Etiqueta del eje X
    ylabel='Eje Y',          # Etiqueta del eje Y
    title='Título',          # Título del gráfico
    xscale='linear',         # Escala: 'linear', 'log', 'symlog', 'logit'
    yscale='linear'          # Escala del eje Y
)

Métodos individuales (alternativa):
    ax.set_xlim(0, 10)       # Solo límites de X
    ax.set_ylim(0, 100)      # Solo límites de Y
    ax.set_xlabel('Eje X')   # Solo etiqueta X
    ax.set_ylabel('Eje Y')   # Solo etiqueta Y
    ax.set_title('Título')   # Solo título
    ax.set_xscale('log')     # Solo escala X

=============================================================================
ESCALAS DE EJES
=============================================================================

Escalas disponibles:

'linear'  → Escala lineal (predeterminada)
'log'     → Escala logarítmica (base 10)
            Útil para datos que varían varios órdenes de magnitud
            Ejemplo: 1, 10, 100, 1000

'symlog'  → Logarítmica simétrica (permite valores negativos)
'logit'   → Escala logit (para probabilidades entre 0 y 1)

Uso:
    ax.set_yscale('log')     # Eje Y logarítmico
    ax.set_xscale('log')     # Eje X logarítmico

=============================================================================
MARCAS DE EJES (TICKS)
=============================================================================

1. TICKS MANUALES (valores específicos):

    ax.set_xticks([0, 2, 4, 6, 8])           # Posiciones de las marcas
    ax.set_xticklabels(['A', 'B', 'C', 'D', 'E'])  # Etiquetas personalizadas
    
    # O en una sola línea:
    ax.set_xticks([0, 5, 10], ['Inicio', 'Medio', 'Final'])

2. TICKS MAYORES Y MENORES:

    Mayores: Marcas principales con etiquetas
    Menores: Marcas secundarias (subdivisiones)

    ax.set_yticks(np.arange(0, 11, 2))              # Mayores cada 2
    ax.set_yticks(np.arange(0, 11, 0.5), minor=True) # Menores cada 0.5

3. LOCATORS AUTOMÁTICOS (matplotlib.ticker):

    from matplotlib.ticker import MultipleLocator, AutoMinorLocator
    
    # Mayores cada N unidades
    ax.xaxis.set_major_locator(MultipleLocator(5))
    
    # Menores automáticos
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    
    # Menores cada N unidades
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))

=============================================================================
FORMATO DE ETIQUETAS (FORMATTERS)
=============================================================================

Personaliza cómo se muestran los números en los ejes:

Formato simple (string):
    ax.yaxis.set_major_formatter('{x:.1f} cm')  # 1 decimal + unidad
    ax.yaxis.set_major_formatter('{x:.0f}°')    # Sin decimales + símbolo
    ax.yaxis.set_major_formatter('{x:.2e}')     # Notación científica

Formato con función:
    ax.yaxis.set_major_formatter(lambda x, pos: f'${x:.0f}k')

Ejemplos de formato:
    '{x:.1f}'     → 3.1, 5.2, 7.8  (1 decimal)
    '{x:.0f}'     → 3, 5, 8         (sin decimales)
    '{x:.2e}'     → 3.14e+02        (científica)
    '{x:,.0f}'    → 1,000           (con comas)

=============================================================================
PERSONALIZACIÓN DE TICKS (ax.tick_params)
=============================================================================

Controla la apariencia de las marcas y etiquetas:

ax.tick_params(
    axis='both',          # 'x', 'y', 'both'
    which='major',        # 'major', 'minor', 'both'
    direction='in',       # 'in', 'out', 'inout'
    length=6,             # Largo de las marcas
    width=2,              # Grosor de las marcas
    color='black',        # Color de las marcas
    labelsize=12,         # Tamaño de las etiquetas
    labelcolor='blue',    # Color de las etiquetas
    labelrotation=45,     # Rotación de las etiquetas (grados)
    pad=10,               # Separación entre marca y etiqueta
    grid_color='gray',    # Color de la cuadrícula
    grid_alpha=0.5        # Transparencia de la cuadrícula
)

Ejemplos comunes:
    # Rotar etiquetas de X
    ax.tick_params(axis='x', labelrotation=45)
    
    # Cambiar tamaño de etiquetas mayores y menores
    ax.tick_params(axis='y', which='major', labelsize=12)
    ax.tick_params(axis='y', which='minor', labelsize=8)
    
    # Ocultar etiquetas pero mantener marcas
    ax.tick_params(axis='x', labelbottom=False)

=============================================================================
CASOS DE USO COMUNES
=============================================================================

1. Gráfico con escala logarítmica:
    ax.set_yscale('log')
    ax.set_ylim(1, 10000)

2. Etiquetas personalizadas en barras:
    categorias = ['A', 'B', 'C']
    ax.set_xticks([0, 1, 2], categorias)

3. Formato con unidades:
    ax.yaxis.set_major_formatter('{x:.1f} cm')

4. Ticks mayores y menores:
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))

5. Rotar etiquetas largas:
    ax.tick_params(axis='x', labelrotation=30)

'''

#%%
# Celda 1: Configuración
# %matplotlib widget
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

#%% Variables globales
layout = 'constrained'
figsize = (10, 6)
#%%
# Celda 2: ETIQUETAS PERSONALIZADAS Y ESCALAS
# Demuestra uso de set_xticks con etiquetas personalizadas

fig, ax = plt.subplots(figsize=figsize, layout=layout)

X = np.linspace(0, 20, 200)
Y = X**3

ax.plot(X, Y, linewidth=2, color='#3498db')

# Etiquetas personalizadas en posiciones específicas
ax.set_xticks([0, 5, 10, 15, 20], 
              ['Inicio', 'Primer\nCuarto', 'Mitad', 'Tercer\nCuarto', 'Final'])

# Configurar límites y etiquetas
ax.set_xlabel('Posición', fontsize=12)
ax.set_ylabel('Valor cúbico', fontsize=12)
ax.set_title('Etiquetas Personalizadas en Eje X', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.show()

#%%
# Celda 3: ESCALA LOGARÍTMICA
# Útil para datos con rangos muy amplios

fig, axs = plt.subplots(1, 2, figsize=(14, 6), layout=layout)

X = np.linspace(0.1, 20, 200)
Y = X**3

# Gráfico con escala lineal
axs[0].plot(X, Y, linewidth=2, color='#e74c3c')
axs[0].set_xlabel('X', fontsize=12)
axs[0].set_ylabel('Y = X³', fontsize=12)
axs[0].set_title('Escala Lineal', fontsize=13, fontweight='bold')
axs[0].grid(True, alpha=0.3)

# Gráfico con escala logarítmica en Y
axs[1].plot(X, Y, linewidth=2, color='#2ecc71')
axs[1].set_yscale('log')  # Escala logarítmica
axs[1].set_xlabel('X', fontsize=12)
axs[1].set_ylabel('Y = X³ (log)', fontsize=12)
axs[1].set_title('Escala Logarítmica', fontsize=13, fontweight='bold')
axs[1].grid(True, alpha=0.3, which='both')  # Cuadrícula en mayores y menores

fig.suptitle('Comparación: Escala Lineal vs Logarítmica', 
             fontsize=16, fontweight='bold', y=0.98)

plt.show()

#%%
# Celda 4: TICKS MAYORES Y MENORES (método simple)
# Usando set_yticks con parámetro minor

datos = {
    'campo': ['Inglés', 'Matemáticas', 'Lengua', 'Historia', 'Física', 'Biología'],
    'nivel': [6, 5, 4, 7, 5, 6]
}

df = pd.DataFrame(datos)

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.bar(df['campo'], df['nivel'], color='#3498db', edgecolor='black', alpha=0.8)

# Configurar ticks mayores (cada 2 unidades)
ax.set_yticks(np.arange(0, 11, 2))

# Configurar ticks menores (cada 0.5 unidades)
ax.set_yticks(np.arange(0, 11, 0.5), minor=True)

# Personalizar apariencia
ax.tick_params(axis='x', labelrotation=25, labelsize=11)
ax.tick_params(axis='y', which='major', labelsize=12)
ax.tick_params(axis='y', which='minor', length=3)  # Menores más cortos

ax.set_ylabel('Nivel de Competencia', fontsize=12)
ax.set_title('Evaluación por Materia - Ticks Mayores y Menores', 
             fontsize=14, fontweight='bold')
ax.grid(True, axis='y', alpha=0.3, which='both')

plt.show()

#%%
# Celda 5: LOCATORS Y FORMATTERS (control avanzado)
# Usando MultipleLocator y formatos personalizados

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.bar(df['campo'], df['nivel'], color='#e74c3c', edgecolor='black', alpha=0.8)

# Configurar rango del eje Y
ax.set_ylim(0, 10)

# TICKS MAYORES: cada 1 unidad con formato personalizado
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_formatter('{x:.1f} cm')  # Formato: 1 decimal + unidad
ax.tick_params(axis='y', which='major', labelsize=12, labelcolor='blue')

# TICKS MENORES: cada 0.5 unidades
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_formatter('{x:.1f}')
ax.tick_params(axis='y', which='minor', labelsize=9, labelcolor='gray')

# TICKS DE X: rotar etiquetas
ax.tick_params(axis='x', which='major', labelsize=11, labelrotation=30)

ax.set_ylabel('Altura (con unidades)', fontsize=12)
ax.set_title('Formato Personalizado con Locators y Formatters', 
             fontsize=14, fontweight='bold')
ax.grid(True, axis='y', alpha=0.3, which='major')

plt.show()

#%%
# Celda 6: COMPARACIÓN COMPLETA - Múltiples Técnicas
# Demuestra diferentes configuraciones en un solo gráfico

fig, axs = plt.subplots(2, 2, figsize=(14, 10), layout=layout)

# Subplot 1: Límites y etiquetas básicas
X1 = np.linspace(0, 4*np.pi, 200)
Y1 = 4 + np.cos(X1)
axs[0, 0].plot(X1, Y1, linewidth=2, color='#3498db')
axs[0, 0].set(xlim=(0, 4*np.pi), ylim=(0, 6),
              xlabel='Radianes', ylabel='Amplitud')
axs[0, 0].set_title('Límites con ax.set()', fontweight='bold')
axs[0, 0].grid(True, alpha=0.3)

# Subplot 2: Etiquetas personalizadas
X2 = [1, 2, 3, 4, 5]
Y2 = [23, 45, 56, 32, 67]
categorias = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie']
axs[0, 1].bar(X2, Y2, color='#e74c3c', alpha=0.8)
axs[0, 1].set_xticks(X2, categorias)
axs[0, 1].set_title('Etiquetas Categóricas', fontweight='bold')
axs[0, 1].grid(True, axis='y', alpha=0.3)

# Subplot 3: Ticks mayores y menores con formato
X3 = np.linspace(0, 10, 100)
Y3 = X3**2
axs[1, 0].plot(X3, Y3, linewidth=2, color='#2ecc71')
axs[1, 0].yaxis.set_major_locator(MultipleLocator(20))
axs[1, 0].yaxis.set_minor_locator(MultipleLocator(5))
axs[1, 0].yaxis.set_major_formatter('{x:.0f}')
axs[1, 0].tick_params(axis='y', which='major', labelsize=11, length=6)
axs[1, 0].tick_params(axis='y', which='minor', labelsize=8, length=3)
axs[1, 0].set_title('Locators con Formato', fontweight='bold')
axs[1, 0].grid(True, alpha=0.3, which='both')

# Subplot 4: Rotación y formato personalizado
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
ventas = [120, 150, 180, 160, 200, 190]
axs[1, 1].bar(meses, ventas, color='#9b59b6', alpha=0.8)
axs[1, 1].yaxis.set_major_formatter('{x:.0f}k')
axs[1, 1].tick_params(axis='x', labelrotation=45, labelsize=11)
axs[1, 1].tick_params(axis='y', labelsize=11)
axs[1, 1].set_title('Rotación + Formato Monetario', fontweight='bold')
axs[1, 1].grid(True, axis='y', alpha=0.3)

fig.suptitle('Técnicas de Configuración de Ejes - Guía Completa',
             fontsize=16, fontweight='bold', y=0.98)

plt.show()
# %%
