#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Ballera
"""
#%%
import numpy as np
import pandas as pd
#%% ======================================================================
# Series
altura_cm = [178, 165, 155, 181, 176, 189, 190, 186]

altura = pd.Series(altura_cm)
altura.name = 'Alturas'
altura # type: ignore
#%% observo algunos elementos
print(f'\nAlturas primeros 5: \n{altura.head()}') # primeros 5 elementos
print(f'\nAlturas primeros 3: \n{altura.head(3)}') # la cantidad que quiero
print(f'\nAlturas últimos 5: \n{altura.tail()}') # últimos 5
print(f'\nAlturas últimos 3: \n{altura.tail(3)}') # los últimos que quiero
print(f'\nAlturas uno aleatorio: \n{altura.sample()}') # muestra uno aleatorio
print(f'\nAlturas 3 aleatorios: \n{altura.sample(3)}') # n aleatorios
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
print(f'¿altura tiene algún valor NaN?: {altura.hasnans}\n')
print(f'¿altura2 tiene algún valor NaN?: {altura2.hasnans}\n')
altura2.info()
altura2[8]

#%% Filtros
alto = 170
mas_altos = [item for item in altura if item > alto] # Estilo programático python, retorna una lista
mas_altos = pd.Series(mas_altos) # Hay que hacer un paso más para convertir la lista a serie de pandas

condicion = altura.gt(alto) # gt = greater than alto (altura > alto) 
mas_altos2 = altura[condicion] # Estilo pandas (recomendable)
mas_altos2
#%% ======================================================================
# DataFrames
datos = {
    "nombre": ['Erika', 'Elías', 'Miguel', 'Karla', 'Gabriela'],
    "edad": [23, 24, 21, 25, 22],
    "altura": [173, 194, 165, 154, 176],
    "peso": [83.2, 65.4, 71.1, 67.9, 71.8]
}
#%%
amigos = pd.DataFrame(datos)
amigos
#%%
amigos.describe()
#%%
amigos.info()
#%% Filtros 
# edad < 23
edad = 23
condicion = amigos['edad'] < edad
filtrado = amigos[condicion]
print(f'Filtrado: \n {filtrado}')
print(f'\nDescribe: \n {filtrado.describe()}')
print(f'\n Edad máxima: {filtrado['edad'].max()}')
#%% creamos nuevo df amigos desde archivo excel
amigos = pd.read_excel('./amigos.xlsx', index_col='Id')
amigos
#%%
amigos.describe()
#%%
amigos.info()
#%%
print(f'¿Todos los valores son válidos? {'Sí' if bool(amigos.all().all()) else 'No'}')
#%% Amigos con edad < 21 años
edad = 21
condicion = amigos['Edad'] < edad

filtro = amigos[condicion]
filtro
# %% creamos df universidad desde archivo excel
universidad = pd.read_excel('./universidad.xlsx', index_col='Id Persona', parse_dates=['Inscripción'])
universidad
#%%
universidad.head()
#%%
universidad.describe(include=['object'])
# universidad.value_counts()
#%%
universidad.describe(include=['number'])
#%%
universidad.info()
#%%
print(f'¿Todos los datos son válidos? {'Sí' if (universidad != pd.Timestamp(0)).all().all() else 'No'}')
#%% Trabajamos con Ambos DF
estudiantes = amigos.merge(universidad, left_on='Id', right_on='Id Persona')
estudiantes
#%%
estudiantes.head()
#%%
estudiantes.tail()
#%%
estudiantes.info()
#%%
estudiantes.describe(include=['number'])
#%%
estudiantes.describe(include=['object'])
#%%
estudiantes.loc[:,'Num Control'] = estudiantes.loc[:,'Num Control'].str.upper()
estudiantes.head()
#%%
estudiantes.loc[:,'Carrera'] = estudiantes.loc[:,'Carrera'].str.title()
estudiantes.head()
#%%
estudiantes['Año'] = estudiantes['Inscripción'].dt.year # type: ignore
estudiantes.head()
#%%
estudiantes['Año/mes'] = estudiantes['Inscripción'].dt.strftime('%Y/%m')  # type: ignore
estudiantes.head()
#%% Licenciados
licenciados = estudiantes[estudiantes.loc[:,'Carrera'].str.contains('Lic.')]
licenciados.head()
#%% Ingenieros
ingenieros = estudiantes[estudiantes.loc[:,'Carrera'].str.startswith('Ing.')]
ingenieros.head()
#%%
grupo = estudiantes.groupby('Carrera')['Edad'].mean()
grupo
#%%
grupo2 = estudiantes.groupby('Carrera')[['Edad', 'Altura', 'Peso']].agg(['mean', 'min', 'max'])
print(grupo2)
#%%
grupo2 = estudiantes.groupby('Carrera')[['Edad']].describe()
print(grupo2)
#%%
lic_ano = licenciados.groupby('Año').size()
lic_ano
#%%
import matplotlib.pyplot as plt
#%%
lic_ano.plot(kind='bar')
plt.tight_layout()
plt.title('Licenciados por año')
plt.show()
#%% Pivot
pivot = licenciados.pivot_table(index=['Año'], columns=['Carrera'], values='Edad', aggfunc='count', fill_value=0)
print(pivot)
# %%
pivot.plot(kind='bar')
plt.tight_layout()
plt.title('Carreras por año')
plt.show()
