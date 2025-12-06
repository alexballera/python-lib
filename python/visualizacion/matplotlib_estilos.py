#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualización con Matplotlib - Estilos de Líneas, Bordes y Cuadrículas
@author: Alex Ballera
"""
#%%
# REFERENCIA RÁPIDA: Estilos de Líneas y Personalización de Ejes
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# https://matplotlib.org/stable/api/spines_api.html
'''
=============================================================================
ESTILOS DE LÍNEA (linestyle)
=============================================================================

Formatos predefinidos (nombres):
    'solid' o '-'        → Línea continua (predeterminado)
    'dashed' o '--'      → Línea discontinua (guiones)
    'dashdot' o '-.'     → Línea con guión y punto alternados
    'dotted' o ':'       → Línea punteada

Formato personalizado (tupla):
    linestyle=(offset, (on_length, off_length))
    
    Ejemplos:
    (0, (6, 4))          → 6 puntos dibujados, 4 puntos en blanco
    (0, (1, 1))          → Punteado (1 dibujado, 1 en blanco)
    (0, (5, 2, 1, 2))    → Patrón complejo: 5 dibujados, 2 blancos, 
                            1 dibujado, 2 blancos (se repite)
    (5, (10, 3))         → offset=5: desplaza el inicio del patrón

=============================================================================
PERSONALIZACIÓN DE BORDES (ax.spines)
=============================================================================

Los "spines" son los bordes del área de graficación (top, bottom, left, right)

Cambiar color:
    ax.spines['left'].set_color('blue')

Cambiar grosor:
    ax.spines['left'].set_linewidth(3)

Cambiar estilo de línea:
    ax.spines['left'].set_linestyle('--')

Ocultar un borde:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

Posicionar en el centro (estilo cartesiano):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

=============================================================================
CUADRÍCULA (ax.grid)
=============================================================================

Activar cuadrícula básica:
    ax.grid(True)

Personalización completa:
    ax.grid(
        True,                       # Activar
        linewidth=2,                # Grosor de líneas
        linestyle='--',             # Estilo (también acepta tuplas)
        color='gray',               # Color
        alpha=0.5,                  # Transparencia
        which='major',              # 'major', 'minor', 'both'
        axis='both'                 # 'both', 'x', 'y'
    )

=============================================================================
STEM PLOT (Gráfico de Tallos)
=============================================================================

Un stem plot muestra datos como líneas verticales desde una línea base:

    ax.stem(x, y,
        linefmt='r',                # Formato de líneas verticales (color)
        markerfmt='bo',             # Formato de marcadores (color + forma)
        basefmt='k-',               # Formato de línea base
        label='Datos',              # Etiqueta para leyenda
        bottom=0                    # Altura de la línea base
    )

Casos de uso:
    - Señales discretas (procesamiento de señales)
    - Eventos temporales
    - Datos de frecuencia
    - Comparación de valores discretos

=============================================================================
LAYOUT Y ORGANIZACIÓN
=============================================================================

Layout constrained (recomendado):
    fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
    
    Ventajas:
    - Ajusta automáticamente espaciado
    - Evita superposición de etiquetas
    - Optimiza el uso del espacio

Múltiples subplots:
    fig, axs = plt.subplots(nrows, ncols, figsize=(width, height))
    
    Ejemplo con 2x2:
    fig, axs = plt.subplots(2, 2, figsize=(12, 10), layout='constrained')
    axs[0, 0].plot(...)  # Superior izquierdo
    axs[0, 1].plot(...)  # Superior derecho
    axs[1, 0].plot(...)  # Inferior izquierdo
    axs[1, 1].plot(...)  # Inferior derecho

=============================================================================
CASOS DE USO COMUNES
=============================================================================

1. Estilo académico (sin bordes superiores/derechos):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

2. Gráfico estilo cartesiano (ejes en el centro):
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

3. Énfasis en un borde específico:
    ax.spines['left'].set_color('blue')
    ax.spines['left'].set_linewidth(3)

4. Cuadrícula sutil para lectura:
    ax.grid(True, alpha=0.3, linestyle='--', color='gray')

'''

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

#%%
# Celda 4: Comparación de Estilos de Línea en Múltiples Subplots
# Demuestra diferentes estilos de línea en una sola figura

# Datos de ejemplo
X = np.linspace(0, 10, 100)
Y1 = np.sin(X)
Y2 = np.cos(X)
Y3 = np.sin(X) * np.exp(-X/10)
Y4 = np.cos(X) * np.exp(-X/10)

# Crear figura con 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10), layout='constrained')

# Superior izquierdo: Estilos predefinidos
axs[0, 0].plot(X, Y1, linestyle='solid', linewidth=2, label='solid', color='#e74c3c')
axs[0, 0].plot(X, Y1-0.5, linestyle='dashed', linewidth=2, label='dashed', color='#3498db')
axs[0, 0].plot(X, Y1-1, linestyle='dashdot', linewidth=2, label='dashdot', color='#2ecc71')
axs[0, 0].plot(X, Y1-1.5, linestyle='dotted', linewidth=2, label='dotted', color='#f39c12')
axs[0, 0].set_title('Estilos Predefinidos', fontsize=12, fontweight='bold')
axs[0, 0].legend(loc='upper right')
axs[0, 0].grid(True, alpha=0.3)
axs[0, 0].spines['top'].set_visible(False)
axs[0, 0].spines['right'].set_visible(False)

# Superior derecho: Estilos personalizados con tuplas
axs[0, 1].plot(X, Y2, linestyle=(0, (5, 5)), linewidth=2, label='(0, (5, 5))', color='#9b59b6')
axs[0, 1].plot(X, Y2-0.5, linestyle=(0, (3, 1, 1, 1)), linewidth=2, label='(0, (3, 1, 1, 1))', color='#e67e22')
axs[0, 1].plot(X, Y2-1, linestyle=(0, (1, 1)), linewidth=2, label='(0, (1, 1))', color='#1abc9c')
axs[0, 1].plot(X, Y2-1.5, linestyle=(5, (10, 3)), linewidth=2, label='(5, (10, 3))', color='#34495e')
axs[0, 1].set_title('Estilos Personalizados (Tuplas)', fontsize=12, fontweight='bold')
axs[0, 1].legend(loc='upper right', fontsize=9)
axs[0, 1].grid(True, alpha=0.3)
axs[0, 1].spines['top'].set_visible(False)
axs[0, 1].spines['right'].set_visible(False)

# Inferior izquierdo: Personalización de bordes (spines)
axs[1, 0].plot(X, Y3, linewidth=2, color='#e74c3c', label='Señal decreciente')
axs[1, 0].axhline(y=0, color='black', linewidth=0.8, linestyle='-', alpha=0.5)
axs[1, 0].set_title('Bordes Personalizados', fontsize=12, fontweight='bold')
axs[1, 0].spines['left'].set_color('#3498db')
axs[1, 0].spines['left'].set_linewidth(3)
axs[1, 0].spines['bottom'].set_color('#2ecc71')
axs[1, 0].spines['bottom'].set_linewidth(3)
axs[1, 0].spines['top'].set_visible(False)
axs[1, 0].spines['right'].set_visible(False)
axs[1, 0].legend(loc='upper right')
axs[1, 0].grid(True, alpha=0.3, linestyle='--')

# Inferior derecho: Stem plot con personalización
axs[1, 1].stem(X[::10], Y4[::10], 
               linefmt='#9b59b6', 
               markerfmt='o', 
               basefmt='#34495e',
               label='Muestras discretas')
axs[1, 1].set_title('Stem Plot (Gráfico de Tallos)', fontsize=12, fontweight='bold')
axs[1, 1].spines['top'].set_visible(False)
axs[1, 1].spines['right'].set_visible(False)
axs[1, 1].grid(True, alpha=0.3, linestyle=':', color='gray')
axs[1, 1].legend(loc='upper right')

# Título general
fig.suptitle('Comparación de Estilos de Línea y Personalización de Ejes', 
             fontsize=16, fontweight='bold', y=0.995)

plt.show()

#%%
# Celda 5: Ejemplo Avanzado - Estilo Cartesiano con Ejes en el Centro
# Útil para gráficos matemáticos y funciones trigonométricas

X_cart = np.linspace(-2*np.pi, 2*np.pi, 200)
Y_sin = np.sin(X_cart)
Y_cos = np.cos(X_cart)

fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')

# Graficar funciones
ax.plot(X_cart, Y_sin, linewidth=2.5, label='sin(x)', color='#e74c3c', alpha=0.8)
ax.plot(X_cart, Y_cos, linewidth=2.5, label='cos(x)', color='#3498db', alpha=0.8)

# Configurar ejes en el centro (estilo cartesiano)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Personalizar grosor de ejes
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# Configurar etiquetas en los ejes
ax.set_xlabel('x', fontsize=12, loc='right')
ax.set_ylabel('y', fontsize=12, loc='top', rotation=0)

# Configurar límites
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Agregar marcas en múltiplos de π
pi_ticks = [-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]
pi_labels = ['-2π', '-π', '0', 'π', '2π']
ax.set_xticks(pi_ticks)
ax.set_xticklabels(pi_labels)

# Cuadrícula sutil
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)

# Leyenda
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)

# Título
ax.set_title('Funciones Trigonométricas - Estilo Cartesiano', 
             fontsize=14, fontweight='bold', pad=20)

plt.show()
# %%
