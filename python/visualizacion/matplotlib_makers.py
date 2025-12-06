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
#%% Variables
layout = 'constrained'
figsize = (10,6)

#%%
# REFERENCIA COMPLETA: Personalización de Líneas y Marcadores
# https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/marker_reference.html
'''
=============================================================================
PARÁMETROS DE ax.plot() - REFERENCIA TÉCNICA
=============================================================================

ax.plot(
    x, y,                        # Datos: arrays o listas de coordenadas
    
    # --- PARÁMETROS DE LÍNEA ---
    color='r',                   # Color de la línea de conexión entre puntos
                                 # Formatos: nombre ('red'), abreviatura ('r'), hex ('#FF5733')
    linestyle='--',              # Estilo de línea: '-' (sólida), '--' (guiones),
                                 # '-.' (guión-punto), ':' (punteada)
    linewidth=2,                 # Grosor de la línea en puntos
    
    # --- PARÁMETROS DE MARCADORES ---
    marker='o',                  # Forma del marcador en cada punto de datos
                                 # Opciones comunes: 'o' (círculo), 's' (cuadrado),
                                 # '^' (triángulo arriba), 'v' (triángulo abajo),
                                 # 'D' (diamante), '*' (estrella), '+' (plus), 'x' (X)
    markersize=10,               # Tamaño del marcador en puntos
    
    # --- PARÁMETROS DE RELLENO DE MARCADORES ---
    markerfacecolor='blue',      # Color del RELLENO INTERIOR del marcador
                                 # Define QUÉ COLOR se usa para rellenar
    markerfacecoloralt='green',  # Color alternativo para fillstyle bicolor
                                 # Se usa para la parte NO especificada en fillstyle
    fillstyle='top',             # Estilo de relleno del marcador
                                 # Define QUÉ PARTE del marcador se rellena:
                                 # 'full' (completo - predeterminado)
                                 # 'left' (mitad izquierda)
                                 # 'right' (mitad derecha)
                                 # 'top' (mitad superior)
                                 # 'bottom' (mitad inferior)
                                 # 'none' (sin relleno, solo borde)
    
    # --- PARÁMETROS DE BORDE DE MARCADORES ---
    markeredgecolor='black',     # Color del BORDE/CONTORNO del marcador
    markeredgewidth=2,           # Grosor del borde del marcador en puntos
    
    # --- PARÁMETROS VISUALES GENERALES ---
    alpha=0.7,                   # Transparencia: 0 (completamente transparente)
                                 # a 1 (completamente opaco)
    label='Serie 1',             # Etiqueta para la leyenda del gráfico
    zorder=2                     # Orden de apilamiento visual (mayor = al frente)
                                 # Útil para controlar qué elementos se dibujan encima
)

=============================================================================
CONCEPTOS CLAVE: markerfacecolor vs fillstyle
=============================================================================

markerfacecolor: Define QUÉ COLOR se usa para rellenar el marcador
fillstyle:       Define QUÉ PARTE del marcador se rellena con ese color

Combinación: Ambos trabajan juntos para crear efectos visuales
             markerfacecolor proporciona el color, fillstyle define el área

=============================================================================
EJEMPLOS DE USO COMÚN
=============================================================================

# Marcador mitad lleno (bicolor con fillstyle)
marker='o', markerfacecolor='blue', markerfacecoloralt='red', fillstyle='left'
# Resultado: Mitad izquierda azul, mitad derecha roja

# Marcador sin relleno (solo contorno/borde)
marker='o', markerfacecolor='none', fillstyle='none', markeredgecolor='black'
# Resultado: Círculo hueco con borde negro

# Marcador completamente lleno (uso estándar)
marker='o', markerfacecolor='red', fillstyle='full'
# Resultado: Círculo completamente rojo

# Marcador con relleno parcial
marker='o', markerfacecolor='blue', fillstyle='top'
# Resultado: Solo la mitad superior del círculo rellena de azul

=============================================================================
MARCADORES DIRECCIONALES (sin necesidad de rotación)
=============================================================================

Para orientaciones básicas, usa marcadores con direcciones predefinidas:

'^'  → Triángulo apuntando hacia arriba
'v'  → Triángulo apuntando hacia abajo
'<'  → Triángulo apuntando hacia la izquierda  
'>'  → Triángulo apuntando hacia la derecha
'1'  → Tri-down marker
'2'  → Tri-up marker
'3'  → Tri-left marker
'4'  → Tri-right marker

Estos marcadores cubren el 90% de casos sin necesidad de rotación manual.

=============================================================================
NOTA IMPORTANTE: ROTACIÓN DE MARCADORES
=============================================================================

Los marcadores estándar de ax.plot() NO pueden rotarse directamente.

Para rotaciones personalizadas, necesitas usar MarkerStyle:

import matplotlib.markers as mmarkers

# Crear marcador rotado
marker_obj = mmarkers.MarkerStyle(marker='^')
marker_obj._transform = marker_obj.get_transform().rotate_deg(45)

# Usar con ax.scatter() (NO con ax.plot())
ax.scatter(x, y, marker=marker_obj, s=200)

Ver ejemplo completo en la última celda de este archivo.
'''
#%%

# Datos de ejemplo
X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [3, 4, 5, 3, 2, 4, 5, 7]

# Configuración
layout = 'constrained'
figsize = (14, 10)

# Crear figura con múltiples subplots para comparar
fig, axes = plt.subplots(2, 3, figsize=figsize, layout=layout)

# 1. Marcador básico sin relleno especial
axes[0, 0].plot(X, Y, color='r', marker='o', markersize=12,
                markerfacecolor='b', markeredgecolor='black')
axes[0, 0].set_title('fillstyle="full" (predeterminado)')
axes[0, 0].grid(True, alpha=0.3)

# 2. Relleno solo arriba
axes[0, 1].plot(X, Y, color='r', marker='o', markersize=12,
                markerfacecolor='b', markeredgecolor='black',
                fillstyle='top')
axes[0, 1].set_title('fillstyle="top"')
axes[0, 1].grid(True, alpha=0.3)

# 3. Relleno solo abajo
axes[0, 2].plot(X, Y, color='r', marker='o', markersize=12,
                markerfacecolor='b', markeredgecolor='black',
                fillstyle='bottom')
axes[0, 2].set_title('fillstyle="bottom"')
axes[0, 2].grid(True, alpha=0.3)

# 4. Relleno solo izquierda
axes[1, 0].plot(X, Y, color='r', marker='o', markersize=12,
                markerfacecolor='b', markeredgecolor='black',
                fillstyle='left')
axes[1, 0].set_title('fillstyle="left"')
axes[1, 0].grid(True, alpha=0.3)

# 5. Relleno solo derecha
axes[1, 1].plot(X, Y, color='r', marker='o', markersize=12,
                markerfacecolor='b', markeredgecolor='black',
                fillstyle='right')
axes[1, 1].set_title('fillstyle="right"')
axes[1, 1].grid(True, alpha=0.3)

# 6. Sin relleno (solo borde)
axes[1, 2].plot(X, Y, color='r', marker='o', markersize=12,
                markerfacecolor='none', markeredgecolor='black',
                fillstyle='none', markeredgewidth=2)
axes[1, 2].set_title('fillstyle="none"')
axes[1, 2].grid(True, alpha=0.3)

fig.suptitle('Comparación de Estilos de Relleno (fillstyle)', 
             fontsize=16, fontweight='bold')

plt.show()
#%%
X = [1,2,3,4,5,6,7,8]
Y = [3,4,5,3,2,4,5,7]

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X,
        Y,
        color='r',
        marker='v',
        markersize=20,
        markerfacecolor='y',
        markerfacecoloralt='green',
        markeredgecolor='black',
        markeredgewidth=2,
        fillstyle='left',
        )

plt.show()
#%%
X = [1,2,3,4,5,6,7,8]
Y = [3,4,5,3,2,4,5,7]

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X,
        Y,
        color='r',
        marker=r'$\beta$', # con r'$\arg$' agregamos LaTex
        markersize=20,
        markeredgecolor='black',
        markeredgewidth=2,
        )

plt.show()
#%%
# Celda 6: Ejemplo simple con fillstyle
fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X,
        Y,
        color='r',
        marker='o',
        markerfacecolor='b',
        markersize=12,
        markeredgecolor='black',
        fillstyle='top'
        )

ax.set_title('Marcador con fillstyle="top"', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.show()

#%%
# Celda 7: ROTACIÓN DE MARCADORES con MarkerStyle
# Los marcadores estándar de ax.plot() NO pueden rotarse directamente.
# Para rotaciones personalizadas, usa MarkerStyle con ax.scatter()

import matplotlib.markers as mmarkers

# Datos de ejemplo
X_scatter = [1, 2, 3, 4, 5]
Y_scatter = [3, 4, 2, 5, 3]

# Crear figura
fig, ax = plt.subplots(figsize=(12, 8), layout='constrained')

# Crear múltiples marcadores con diferentes ángulos de rotación
angles = [0, 45, 90, 135, 180]
colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']

for i, (angle, color) in enumerate(zip(angles, colors)):
    # Crear objeto MarkerStyle con el marcador deseado
    marker_obj = mmarkers.MarkerStyle(marker='^')  # Triángulo hacia arriba
    
    # Aplicar rotación al marcador
    marker_obj._transform = marker_obj.get_transform().rotate_deg(angle)
    
    # Dibujar el marcador rotado usando scatter (NO plot)
    ax.scatter(i+1, 3, 
               marker=marker_obj,      # Marcador rotado
               s=400,                  # Tamaño (s = size en scatter)
               c=color,                # Color
               edgecolors='black',     # Color del borde
               linewidths=2,           # Grosor del borde
               alpha=0.8,
               label=f'{angle}°')
    
    # Agregar etiqueta con el ángulo
    ax.text(i+1, 2.5, f'{angle}°', 
            ha='center', va='top', fontsize=11, fontweight='bold')

# Agregar línea de referencia para comparación visual
ax.axhline(y=3, color='gray', linestyle='--', linewidth=1, alpha=0.5, zorder=0)

# Personalización del gráfico
ax.set_title('Rotación de Marcadores con MarkerStyle.rotate_deg()', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Posición', fontsize=12)
ax.set_ylabel('Valor', fontsize=12)
ax.set_xlim(0, 6)
ax.set_ylim(2, 4)
ax.legend(title='Ángulo de Rotación', loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')

# Nota explicativa
fig.text(0.5, 0.02, 
         'Nota: Los marcadores se rotan usando MarkerStyle._transform.rotate_deg() con ax.scatter(), NO con ax.plot()',
         ha='center', fontsize=10, style='italic', color='gray')

plt.show()