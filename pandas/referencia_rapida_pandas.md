# 📋 Referencia Rápida de Pandas

Guía de consulta rápida para las operaciones más comunes en pandas.

---

## 🔧 Importación y Configuración

```python
import pandas as pd
import numpy as np

# Configuración básica
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
pd.set_option('display.width', None)        # Sin límite de ancho
```

---

## 📊 Creación de Estructuras de Datos

### DataFrames
```python
# Desde diccionario
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd'],
    'C': [1.1, 2.2, 3.3, 4.4]
})

# Desde listas
df = pd.DataFrame(data, columns=['col1', 'col2'], index=['fila1', 'fila2'])

# Desde archivo
df = pd.read_csv('archivo.csv')
df = pd.read_excel('archivo.xlsx')
```

### Series
```python
# Serie básica
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# Serie desde diccionario
s = pd.Series({'a': 1, 'b': 2, 'c': 3})
```

---

## 🎯 Selección y Filtrado

### Selección Básica con Corchetes `df[]`
```python
# COLUMNAS
df['columna']                    # Una columna (Serie)
df[['col1', 'col2']]            # Múltiples columnas (DataFrame)

# FILAS (solo con slicing)
df[0:3]                         # Posición numérica (0 a 2)
df['inicio':'fin']              # Rango de índice (ambos incluidos)
df[-3:]                         # Últimas 3 filas
df[condicion_booleana]          # Filtrado por condición
```

### Selección por Etiquetas con `.loc[]`
```python
# FILAS
df.loc['etiqueta']              # Una fila (Serie)
df.loc['inicio':'fin']          # Rango de etiquetas
df.loc[['etiq1', 'etiq2']]      # Filas específicas

# FILAS Y COLUMNAS
df.loc[:, 'columna']            # Todas las filas, una columna
df.loc[:, ['col1', 'col2']]     # Todas las filas, columnas específicas
df.loc['fila', 'columna']       # Valor específico
df.loc[condicion, ['col1']]     # Filtrado con columnas específicas

# ACCESO RÁPIDO
df.at['fila', 'columna']        # Más rápido para un valor
```

### Selección por Posición con `.iloc[]`
```python
# FILAS
df.iloc[0]                      # Primera fila (Serie)
df.iloc[0:3]                    # Rango de posiciones (0 a 2)
df.iloc[[0, 2, 4]]              # Filas específicas por posición
df.iloc[-1]                     # Última fila

# FILAS Y COLUMNAS
df.iloc[:, 0]                   # Todas las filas, primera columna
df.iloc[:, 0:3]                 # Todas las filas, columnas 0 a 2
df.iloc[0, 1]                   # Valor en posición específica
df.iloc[[1, 3], [0, 2]]         # Filas y columnas específicas

# ACCESO RÁPIDO
df.iat[fila, columna]           # Más rápido para un valor
```

---

## 🔍 Filtrado con Condiciones

### Filtros Básicos
```python
# Filtro simple
df[df['columna'] > valor]

# Múltiples condiciones
df[(df['A'] > 0) & (df['B'] < 10)]      # Y lógico
df[(df['A'] > 0) | (df['B'] < 10)]      # O lógico
df[~(df['A'] > 0)]                      # NO lógico

# Valores específicos
df[df['columna'].isin(['valor1', 'valor2'])]
df[~df['columna'].isin(['valor1'])]     # Excluir valores
```

### Filtros Avanzados
```python
# Query (más legible)
df.query('A > 0 and B < 10')
df.query('A > @variable')               # Variables externas

# Valores nulos
df[df['columna'].notna()]               # No nulos
df[df['columna'].isna()]                # Nulos
df[df.isnull().any(axis=1)]            # Filas con algún nulo
df[df.notnull().all(axis=1)]           # Filas sin nulos
```

---

## 📈 Estadísticas y Agregación

### Estadísticas Básicas
```python
# Por columna (axis=0, por defecto)
df.mean()                       # Media
df.median()                     # Mediana
df.std()                        # Desviación estándar
df.var()                        # Varianza
df.min()                        # Mínimo
df.max()                        # Máximo
df.sum()                        # Suma
df.count()                      # Conteo de no-nulos

# Por fila (axis=1)
df.mean(axis=1)                 # Media por fila
df.sum(axis=1)                  # Suma por fila

# Solo columnas numéricas
df.mean(numeric_only=True)
```

### Valores Extremos
```python
df.min()                        # Valores mínimos
df.max()                        # Valores máximos
df.idxmin()                     # Índice del mínimo
df.idxmax()                     # Índice del máximo
df.nlargest(n, 'columna')       # n valores más grandes
df.nsmallest(n, 'columna')      # n valores más pequeños
```

### Percentiles y Cuartiles
```python
df.quantile(0.25)               # Primer cuartil (Q1)
df.quantile(0.5)                # Mediana (Q2)
df.quantile(0.75)               # Tercer cuartil (Q3)
df.quantile([0.25, 0.5, 0.75])  # Múltiples percentiles

# Rango Intercuartílico (IQR)
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3 - q1
```

### Resumen Estadístico
```python
df.describe()                   # Resumen completo
df.info()                       # Información general
df.shape                        # Dimensiones (filas, columnas)
df.dtypes                       # Tipos de datos
```

---

## 🔢 Conteos y Frecuencias

### Conteos Básicos
```python
df.count()                      # Valores no nulos por columna
df.nunique()                    # Valores únicos por columna
df['columna'].value_counts()    # Frecuencias de valores
df['columna'].value_counts(normalize=True)  # Frecuencias relativas
```

### Valores Nulos
```python
df.isnull().sum()               # Conteo de nulos por columna
df.notnull().sum()              # Conteo de no-nulos por columna
df.isnull().any()               # ¿Hay nulos en alguna columna?
df.isnull().all()               # ¿Todas son nulas en alguna columna?
```

---

## 🧮 Operaciones Aritméticas

### Entre Columnas
```python
df['A'] + df['B']               # Suma
df['A'] - df['B']               # Resta
df['A'] * df['B']               # Multiplicación
df['A'] / df['B']               # División
df['A'] ** df['B']              # Potencia
df['A'] % df['B']               # Módulo
```

### Con Escalares
```python
df['A'] + 10                    # Sumar constante
df['A'] * 2                     # Multiplicar por constante
df['A'] / 100                   # Dividir por constante
```

### Entre DataFrames
```python
df1 + df2                       # Suma elemento a elemento
df1 - df2                       # Resta elemento a elemento
df1 * df2                       # Multiplicación elemento a elemento
```

### Métodos Explícitos (con control de nulos)
```python
df['A'].add(df['B'], fill_value=0)      # Suma con valor de relleno
df['A'].sub(df['B'], fill_value=0)      # Resta con valor de relleno
df['A'].mul(df['B'], fill_value=1)      # Multiplicación con valor de relleno
df['A'].div(df['B'], fill_value=1)      # División con valor de relleno
```

---

## 🎯 Funciones de Agregación

### Función Lambda Personalizada
```python
# Aplicar función personalizada a columnas numéricas
df.select_dtypes(include=[np.number]).agg(lambda x: x.mean() * 2)
```

### Múltiples Funciones
```python
# Aplicar múltiples funciones a todas las columnas numéricas
df.select_dtypes(include=[np.number]).agg(['mean', 'std', 'min', 'max'])
```

### Funciones Específicas por Columna
```python
# Aplicar diferentes funciones a diferentes columnas
df.agg({
    'A': ['mean', 'std'],           # Para A: media y desviación estándar
    'B': ['min', 'max'],            # Para B: mínimo y máximo
    'C': ['sum', 'count']           # Para C: suma y conteo
})
```

---

## 🔄 Transform - Mantiene la Forma Original

### Transform Básico
```python
# Multiplicar todos los valores por 100
df.transform(lambda x: x * 100)

# Normalización z-score
df.transform(lambda x: (x - x.mean()) / x.std())
```

### Transform por Columna
```python
# Diferentes transformaciones por columna
df[['A', 'B']].transform({
    'A': lambda x: x * 2,           # A multiplicado por 2
    'B': lambda x: x ** 2           # B elevado al cuadrado
})
```

---

## 📊 Operaciones Acumulativas

```python
df.cumsum()                     # Suma acumulativa
df.cumprod()                    # Producto acumulativo
df.cummax()                     # Máximo acumulativo
df.cummin()                     # Mínimo acumulativo
df.cumcount()                   # Conteo acumulativo
```

---

## 🔧 Filtrado por Tipos de Datos

```python
# Seleccionar solo columnas numéricas
df.select_dtypes(include=[np.number])

# Seleccionar solo columnas de texto
df.select_dtypes(include=['object'])

# Seleccionar solo columnas de fecha
df.select_dtypes(include=['datetime'])

# Excluir tipos específicos
df.select_dtypes(exclude=['object'])
```

---

## 💡 Funciones Útiles de Pandas

### Funciones de String (`.str`)
```python
df['columna'].str.contains('texto')     # Contiene texto
df['columna'].str.startswith('inicio')  # Comienza con
df['columna'].str.endswith('final')     # Termina con
df['columna'].str.replace('old', 'new') # Reemplazar texto
df['columna'].str.split(',')            # Dividir por delimitador
df['columna'].str.len()                 # Longitud del string
df['columna'].str.upper()               # Mayúsculas
df['columna'].str.lower()               # Minúsculas
```

### Funciones de Fecha (`.dt`)
```python
df['fecha'].dt.year                     # Año
df['fecha'].dt.month                    # Mes
df['fecha'].dt.day                      # Día
df['fecha'].dt.dayofweek               # Día de la semana (0=lunes)
df['fecha'].dt.strftime('%Y-%m-%d')    # Formato personalizado
```

### Funciones de Ventana Móvil
```python
df.rolling(window=3).mean()             # Media móvil de 3 períodos
df.rolling(window=5).sum()              # Suma móvil de 5 períodos
df.expanding().mean()                   # Media expandida
df.ewm(span=10).mean()                  # Media exponencial
```

---

## 🎯 Consejos de Rendimiento

```python
# Para un solo valor, usar métodos rápidos
df.at[fila, columna]            # Más rápido que .loc[]
df.iat[i, j]                    # Más rápido que .iloc[]

# Para múltiples condiciones, usar query
df.query('A > 0 and B < 10')    # Más legible que filtros con &

# Para columnas numéricas, siempre usar numeric_only=True
df.mean(numeric_only=True)      # Evita errores con columnas no numéricas
```

---

## 🔍 Métodos de Exploración

```python
# Ver métodos disponibles
dir(df)                         # Todos los métodos de DataFrame
help(df.método)                 # Documentación de un método específico

# En Jupyter/IPython
df.método?                      # Documentación rápida
df.método??                     # Código fuente
```

---

## 📚 Recursos Adicionales

- **Documentación oficial**: https://pandas.pydata.org/docs/
- **API Reference**: https://pandas.pydata.org/docs/reference/index.html
- **User Guide**: https://pandas.pydata.org/docs/user_guide/index.html
- **Cheat Sheet**: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

---

*Esta guía cubre las operaciones más comunes en pandas. Para casos específicos o funciones avanzadas, consultar la documentación oficial.*
