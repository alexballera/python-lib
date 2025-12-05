#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
#%%
import numpy as np
import pandas as pd
#%% Series
altura_cm = [178, 165, 155, 181, 176, 189, 190, 186]

altura = pd.Series(altura_cm)
altura.name = 'Alturas'
altura # type: ignore
#%% observo algunos elementos
altura.head() # primeros 5 elementos
altura.head(3) # la cantidad que quiero
altura.tail() # últimos 5
altura.tail(3) # los últimos que quiero
altura.sample() # muestra uno aleatorio
altura.sample(3) # n aleatorios
#%% ordenar
altura.sort_values() # ordena ascendente
altura.sort_values(ascending=False) # ordena descendente
altura.sort_index(ascending=False) # ordena por índice
#%% Estadísticas
print(f'Count (válidos): {altura.count()}')
print(f'Promedio:        {altura.mean()}')
print(f'Desvío Standard: {altura.std()}')
print(f'Suma:            {altura.sum()}')
print(f'Mínimo:          {altura.min()}')
print(f'Máximo:          {altura.max()}')
print(f'Mediana:         {altura.median()}')

print(f'\nDescriptivas: \n{altura.describe()}\n')
altura.info()

#%%
altura2 = altura_cm.copy()
altura2 = [float(num) for num in altura2]
altura2.append(np.nan )
altura2 = pd.Series(altura2)
altura2.name = 'Altura2'

print(f'Válidos: {altura2.count()}')
print(f'¿Todos Válidos?: {altura2.isna().all()}\n')
altura2.info()

#%% Filtros
alto = 170
mas_altos = [item for item in altura if item > alto] # Estilo programático python, retorna una lista
mas_altos = pd.Series(mas_altos) # Hay que hacer un paso más para convertir la lista a serie de pandas

condicion = altura.gt(alto) # gt = greater than alto (altura > alto) 
mas_altos2 = altura[condicion] # Estilo pandas (recomendable)
mas_altos2
#%%
