#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualización con Matplotlib - Textos, Anotaciones y Leyendas
@author: Alex Ballera
"""
#%%
# REFERENCIA RÁPIDA: Textos, Anotaciones y Leyendas
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html
# https://matplotlib.org/stable/users/explain/axes/legend_guide.html
'''
=============================================================================
AGREGAR TEXTO (ax.text)
=============================================================================

Agrega texto en coordenadas específicas del gráfico:

ax.text(
    x, y,                    # Coordenadas donde ubicar el texto
    s='Texto',               # String o texto a mostrar
    fontsize=12,             # Tamaño de fuente (o 'small', 'large', etc.)
    color='black',           # Color del texto (o 'c')
    ha='center',             # Alineación horizontal: 'left', 'center', 'right'
    va='center',             # Alineación vertical: 'top', 'center', 'bottom'
    rotation=0,              # Rotación en grados o 'vertical', 'horizontal'
    alpha=1.0,               # Transparencia (0=transparente, 1=opaco)
    fontfamily='sans-serif', # 'serif', 'sans-serif', 'monospace', 'cursive'
    fontstyle='normal',      # 'normal', 'italic', 'oblique'
    fontweight='normal',     # 'normal', 'bold', 'light', o 0-1000
    bbox=dict(...)           # Cuadro decorativo alrededor del texto
)

Formato de bbox (cuadro decorativo):
    bbox=dict(
        facecolor='white',   # Color de fondo
        edgecolor='black',   # Color del borde
        boxstyle='round',    # Estilo: 'square', 'round', 'circle', 'sawtooth'
        alpha=0.8,           # Transparencia
        pad=0.5,             # Espaciado interno
        linewidth=1          # Grosor del borde
    )

LaTeX en textos:
    s=r'$\alpha = 45°$'      # Símbolos matemáticos
    s=fr'Valor: $\beta = {variable}$'  # Con f-string

=============================================================================
ANOTACIONES CON FLECHAS (ax.annotate)
=============================================================================

Señala un punto específico con texto y flecha:

ax.annotate(
    text='Anotación',        # Texto de la anotación
    xy=(x, y),               # Punto a señalar (coordenadas)
    xytext=(x_text, y_text), # Ubicación del texto
    fontsize=12,             # Tamaño de fuente
    ha='center',             # Alineación horizontal
    va='center',             # Alineación vertical
    arrowprops=dict(...),    # Propiedades de la flecha
    bbox=dict(...)           # Cuadro decorativo (opcional)
)

arrowprops - Estilos simples:
    arrowprops=dict(
        arrowstyle='->',     # '->', '-[', '-|>', 'fancy', 'simple', 'wedge'
        color='black',       # Color de la flecha
        linewidth=2,         # Grosor de la línea
        shrink=0.05          # Separación del punto (0-1)
    )

arrowprops - Control detallado:
    arrowprops=dict(
        width=3,             # Ancho del cuerpo de la flecha
        headwidth=10,        # Ancho de la punta
        headlength=10,       # Largo de la punta
        facecolor='red',     # Color de relleno
        edgecolor='black',   # Color del borde
        linewidth=1          # Grosor del borde
    )

Estilos de flecha (arrowstyle):
    '->'     : Flecha simple
    '-['     : Corchete
    '-|>'    : Flecha con base
    'fancy'  : Flecha decorativa (requiere facecolor/edgecolor)
    'simple' : Flecha básica
    'wedge'  : Cuña triangular

=============================================================================
LEYENDAS (ax.legend / fig.legend)
=============================================================================

Muestra etiquetas de las series graficadas:

ax.legend(
    loc='best',              # Ubicación: 'best', 'upper right', 'lower left'
                            # 'outside upper right', etc.
    fontsize=10,            # Tamaño de fuente
    title='Título',         # Título de la leyenda
    frameon=True,           # Mostrar marco (True/False)
    shadow=True,            # Agregar sombra (True/False)
    fancybox=True,          # Esquinas redondeadas (True/False)
    facecolor='white',      # Color de fondo
    edgecolor='black',      # Color del borde
    framealpha=0.9,         # Transparencia del marco (0-1)
    ncol=1,                 # Número de columnas
    markerscale=1.0,        # Escala de marcadores (1.0 = tamaño original)
    bbox_to_anchor=(1, 1)   # Posición precisa (x, y) para colocar fuera
)

Ubicaciones comunes (loc):
    'best'               → Matplotlib elige la mejor ubicación
    'upper right'        → Esquina superior derecha (dentro)
    'upper left'         → Esquina superior izquierda
    'lower right'        → Esquina inferior derecha
    'center'             → Centro del gráfico

Diferencia entre ax.legend() y fig.legend():
    ax.legend()  → Leyenda para un eje específico
    fig.legend() → Leyenda compartida para toda la figura (múltiples subplots)
                   Solo fig.legend() acepta loc='outside ...'

Colocar leyenda FUERA del gráfico:

    Opción 1 - Con ax.legend() usando bbox_to_anchor:
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        # (1.05, 1) = fuera a la derecha, arriba
        # (0.5, -0.15) = abajo centrado
        # (-0.1, 0.5) = izquierda centrado
    
    Opción 2 - Con fig.legend() (para toda la figura):
        fig.legend(loc='outside upper right')
        fig.legend(loc='outside lower center')

=============================================================================
CASOS DE USO COMUNES
=============================================================================

1. Texto simple en el gráfico:
    ax.text(5, 5, 'Punto máximo', fontsize=12, ha='center')

2. Texto con cuadro decorativo:
    ax.text(3, 7, 'Importante', bbox=dict(facecolor='yellow', alpha=0.5))

3. Anotación básica con flecha:
    ax.annotate('Mínimo', xy=(2, 1), xytext=(4, 3),
                arrowprops=dict(arrowstyle='->', color='red'))

4. Leyenda fuera del gráfico:
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

5. Leyenda con formato personalizado:
    ax.legend(title='Series', shadow=True, fancybox=True, 
              facecolor='lightgray', framealpha=0.9)

6. Leyenda compartida para toda la figura:
    fig.legend(loc='outside upper right', fontsize=10)

'''

#%%
# Celda 1: Configuración
# %matplotlib widget
import matplotlib.pyplot as plt
import numpy as np

#%% Variables
layout = 'constrained'
figsize = (10, 6)

# Datos de ejemplo
X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y = np.array([3, 4, 5, 3, 2, 4, 5, 7])
Z = np.array([5, 8, 12, 2, 1, 5, 8, 9])

#%% 
# Celda 2: TEXTO SIMPLE - Ejemplo básico de ax.text()

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X, Y, 'o-', linewidth=2, markersize=8, color='#3498db')

# Texto simple sin decoración
ax.text(x=5, y=5, s='Punto de interés', 
        fontsize=14, color='red', ha='center', va='bottom')

# Texto con formato básico
ax.text(x=2, y=3.5, s='Mínimo local',
        fontsize=12, color='green', ha='left', 
        style='italic', weight='bold')

ax.set_title('Texto Simple en Gráficos', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()

#%%
# Celda 3: TEXTO CON CUADRO DECORATIVO - bbox personalizado

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X, Y, 'o-', linewidth=2, markersize=8, color='#e74c3c')

# Definir cuadro decorativo
bbox_destacado = dict(
    facecolor='yellow',      # Color de fondo
    edgecolor='red',         # Color del borde
    boxstyle='round,pad=0.5', # Estilo con esquinas redondeadas
    alpha=0.8,               # Transparencia
    linewidth=2              # Grosor del borde
)

# Texto con cuadro
ax.text(x=4, y=6, s='Máximo: 7', 
        fontsize=13, color='black', 
        ha='center', va='center',
        bbox=bbox_destacado)

# Texto con LaTeX
alfa = 45
ax.text(x=2, y=2, s=fr'$\alpha = {alfa}°$',
        fontsize=16, color='purple',
        bbox=dict(facecolor='white', alpha=0.7))

ax.set_title('Texto con Cuadros Decorativos', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()

#%%
# Celda 4: ANOTACIONES CON FLECHAS - Señalar puntos específicos

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X, Y, 'o-', linewidth=2, markersize=8, color='#2ecc71')

# Anotación con flecha simple
ax.annotate(
    text='Mínimo\nY = 2',
    xy=(5, 2),              # Punto a señalar
    xytext=(6.5, 4),        # Ubicación del texto
    fontsize=12,
    ha='center',
    arrowprops=dict(
        arrowstyle='->',
        color='red',
        linewidth=2
    ),
    bbox=dict(facecolor='white', edgecolor='red', alpha=0.8)
)

# Anotación con flecha fancy
ax.annotate(
    text='Máximo\nY = 7',
    xy=(8, 7),
    xytext=(6, 6.5),
    fontsize=12,
    ha='center',
    arrowprops=dict(
        arrowstyle='fancy',
        facecolor='orange',
        edgecolor='black',
        linewidth=1.5
    )
)

ax.set_title('Anotaciones con Flechas', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_ylim(0, 8)

plt.show()

#%%
# Celda 5: LEYENDAS - Comparación de series

fig, ax = plt.subplots(figsize=figsize, layout=layout)

# Graficar múltiples series con etiquetas
ax.plot(X, Y, 'o-', linewidth=2, markersize=8, 
        color='#3498db', label='Serie Y')
ax.plot(X, Z, 's--', linewidth=2, markersize=8, 
        color='#e74c3c', label='Serie Z')
ax.plot(X, (Y+Z)/2, '^:', linewidth=2, markersize=8,
        color='#2ecc71', label='Promedio')

# Leyenda con formato personalizado
ax.legend(
    loc='upper left',
    fontsize=11,
    title='Series de Datos',
    shadow=True,
    fancybox=True,
    framealpha=0.9
)

ax.set_title('Leyendas en Gráficos', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_xlabel('X')
ax.set_ylabel('Valores')

plt.show()

#%%
# Celda 6: EJEMPLO COMPLETO - Combinando todo en múltiples subplots

fig, axs = plt.subplots(2, 2, figsize=(14, 10), layout='constrained')

# Subplot 1: Texto con diferentes estilos
axs[0, 0].plot(X, Y, 'o-', linewidth=2, color='#3498db')
axs[0, 0].text(2, 5, 'Fuente sans-serif', fontfamily='sans-serif', fontsize=11)
axs[0, 0].text(2, 4.3, 'Fuente monospace', fontfamily='monospace', fontsize=11)
axs[0, 0].text(2, 3.6, 'Texto en cursiva', fontstyle='italic', fontsize=11)
axs[0, 0].text(2, 2.9, 'Texto en negrita', fontweight='bold', fontsize=11)
axs[0, 0].set_title('Estilos de Fuente', fontweight='bold')
axs[0, 0].grid(True, alpha=0.3)

# Subplot 2: Cuadros decorativos con diferentes estilos
axs[0, 1].plot(X, Z, 'o-', linewidth=2, color='#e74c3c')
estilos_bbox = ['round', 'square', 'circle', 'sawtooth']
colores = ['yellow', 'lightblue', 'lightgreen', 'pink']
for i, (estilo, color) in enumerate(zip(estilos_bbox, colores)):
    axs[0, 1].text(2 + i*1.5, 10 - i*1.5, estilo,
                   bbox=dict(boxstyle=estilo, facecolor=color, alpha=0.7),
                   fontsize=10, ha='center')
axs[0, 1].set_title('Estilos de Cuadros (boxstyle)', fontweight='bold')
axs[0, 1].grid(True, alpha=0.3)

# Subplot 3: Diferentes tipos de flechas
axs[1, 0].plot(X, Y, 'o-', linewidth=2, color='#2ecc71')
arrow_styles = ['->', '-[', '-|>', 'fancy']
y_positions = [6, 5, 4, 3]
for i, (style, y_pos) in enumerate(zip(arrow_styles, y_positions)):
    axs[1, 0].annotate(
        style,
        xy=(4, y_pos - 0.3),
        xytext=(6, y_pos),
        arrowprops=dict(arrowstyle=style, color='red', linewidth=1.5),
        fontsize=10,
        bbox=dict(facecolor='white', alpha=0.8)
    )
axs[1, 0].set_title('Estilos de Flecha (arrowstyle)', fontweight='bold')
axs[1, 0].grid(True, alpha=0.3)
axs[1, 0].set_ylim(1, 7)

# Subplot 4: Leyenda fuera del gráfico con bbox_to_anchor
axs[1, 1].plot(X, Y, 'o-', label='Serie 1', linewidth=2)
axs[1, 1].plot(X, Z, 's--', label='Serie 2', linewidth=2)
axs[1, 1].plot(X, Y*1.5, '^:', label='Serie 3', linewidth=2)
axs[1, 1].plot(X, Z*0.8, 'D-.', label='Serie 4', linewidth=2)
# bbox_to_anchor=(1.05, 1) coloca la leyenda fuera, a la derecha
axs[1, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left', 
                 fontsize=10, title='Datos', shadow=True,
                 framealpha=0.9)
axs[1, 1].set_title('Leyenda Fuera del Gráfico', fontweight='bold')
axs[1, 1].grid(True, alpha=0.3)

# Título general
fig.suptitle('Textos, Anotaciones y Leyendas - Guía Completa',
             fontsize=16, fontweight='bold')

plt.show()
# %%