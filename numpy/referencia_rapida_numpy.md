# 📋 Referencia Rápida de NumPy

Guía de consulta rápida para las operaciones más comunes en NumPy.

---

## 🔧 Importación y Configuración

```python
import numpy as np

# Configuración básica
np.set_printoptions(precision=4)        # Precisión decimal
np.set_printoptions(suppress=True)      # Suprimir notación científica
np.random.seed(42)                      # Semilla para reproducibilidad
```

---

## 📊 Creación de Arrays

### Arrays Básicos

```python
# Desde listas
arr = np.array([1, 2, 3, 4])            # Array 1D
arr = np.array([[1, 2], [3, 4]])        # Array 2D

# Arrays especiales
np.zeros(5)                             # Array de ceros
np.ones((3, 4))                         # Array de unos
np.full((2, 3), 7)                      # Array lleno de un valor
np.eye(4)                               # Matriz identidad
np.empty((2, 3))                        # Array vacío (valores aleatorios)
```

### Rangos y Secuencias

```python
np.arange(0, 10, 2)                     # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)                    # [0, 0.25, 0.5, 0.75, 1]
np.logspace(0, 2, 3)                    # [1, 10, 100]
```

### Arrays Aleatorios

```python
np.random.random(5)                     # Números aleatorios [0, 1)
np.random.randint(0, 10, 5)            # Enteros aleatorios
np.random.randn(3, 4)                  # Distribución normal estándar
np.random.normal(0, 1, 5)              # Distribución normal personalizada
np.random.choice([1, 2, 3], 5)         # Selección aleatoria con reemplazo
```

---

## 📏 Propiedades de Arrays

```python
arr.shape                               # Forma del array (filas, columnas)
arr.size                                # Número total de elementos
arr.ndim                                # Número de dimensiones
arr.dtype                               # Tipo de datos
arr.itemsize                            # Tamaño en bytes de cada elemento
arr.nbytes                              # Tamaño total en bytes
```

---

## 🎯 Indexado y Slicing

### Indexado Básico

```python
# Array 1D
arr[0]                                  # Primer elemento
arr[-1]                                 # Último elemento
arr[1:4]                                # Elementos del 1 al 3

# Array 2D
arr[0, 1]                               # Fila 0, columna 1
arr[0, :]                               # Toda la fila 0
arr[:, 1]                               # Toda la columna 1
arr[1:3, 0:2]                          # Submatriz
```

### Indexado Avanzado

```python
# Indexado booleano
arr[arr > 5]                            # Elementos mayores que 5
arr[(arr > 2) & (arr < 8)]             # Múltiples condiciones

# Indexado fancy
arr[[0, 2, 4]]                          # Elementos en posiciones específicas
arr[[0, 1], [1, 2]]                     # Elementos (0,1) y (1,2)
```

---

## 🔧 Manipulación de Forma

### Cambio de Forma

```python
arr.reshape(3, 4)                       # Cambiar forma (debe mantener tamaño)
arr.resize(2, 6)                        # Cambiar forma in-place
arr.flatten()                           # Aplanar a 1D (copia)
arr.ravel()                             # Aplanar a 1D (vista si es posible)
```

### Transposición y Rotación

```python
arr.T                                   # Transponer
np.transpose(arr)                       # Transponer
np.rot90(arr)                           # Rotar 90 grados
np.flip(arr)                            # Voltear array
np.fliplr(arr)                          # Voltear izquierda-derecha
np.flipud(arr)                          # Voltear arriba-abajo
```

### Concatenación y División

```python
# Concatenar
np.concatenate([arr1, arr2])            # Concatenar arrays
np.vstack([arr1, arr2])                 # Apilar verticalmente
np.hstack([arr1, arr2])                 # Apilar horizontalmente
np.column_stack([arr1, arr2])           # Crear columnas

# Dividir
np.split(arr, 3)                        # Dividir en 3 partes
np.vsplit(arr, 2)                       # Dividir verticalmente
np.hsplit(arr, 2)                       # Dividir horizontalmente
```

---

## 🧮 Operaciones Aritméticas

### Operaciones Elemento a Elemento

```python
arr1 + arr2                             # Suma
arr1 - arr2                             # Resta
arr1 * arr2                             # Multiplicación
arr1 / arr2                             # División
arr1 ** arr2                            # Potencia
arr1 % arr2                             # Módulo
```

### Operaciones con Escalares

```python
arr + 5                                 # Sumar escalar
arr * 2                                 # Multiplicar por escalar
arr / 10                                # Dividir por escalar
arr ** 2                                # Elevar al cuadrado
```

### Funciones Matemáticas Universales

```python
np.abs(arr)                             # Valor absoluto
np.sqrt(arr)                            # Raíz cuadrada
np.exp(arr)                             # Exponencial
np.log(arr)                             # Logaritmo natural
np.log10(arr)                           # Logaritmo base 10
np.sin(arr)                             # Seno
np.cos(arr)                             # Coseno
np.tan(arr)                             # Tangente
```

---

## 📊 Estadísticas y Agregación

### Estadísticas Básicas

```python
# Sin especificar eje (todo el array)
np.mean(arr)                            # Media
np.median(arr)                          # Mediana
np.std(arr)                             # Desviación estándar
np.var(arr)                             # Varianza
np.min(arr)                             # Mínimo
np.max(arr)                             # Máximo
np.sum(arr)                             # Suma
np.prod(arr)                            # Producto
```

### Estadísticas por Eje

```python
# axis=0: opera sobre filas (resultado por columna)
# axis=1: opera sobre columnas (resultado por fila)
np.mean(arr, axis=0)                    # Media por columna
np.mean(arr, axis=1)                    # Media por fila
np.sum(arr, axis=0)                     # Suma por columna
np.sum(arr, axis=1)                     # Suma por fila
```

### Funciones de Orden

```python
np.sort(arr)                            # Ordenar elementos
np.argsort(arr)                         # Índices de ordenamiento
np.argmin(arr)                          # Índice del mínimo
np.argmax(arr)                          # Índice del máximo
np.percentile(arr, 50)                  # Percentil 50 (mediana)
np.quantile(arr, 0.75)                  # Cuantil 75
```

---

## 🔍 Operaciones Lógicas y Comparación

### Comparaciones

```python
arr == 5                                # Igualdad
arr != 5                                # Desigualdad
arr > 5                                 # Mayor que
arr < 5                                 # Menor que
arr >= 5                                # Mayor o igual
arr <= 5                                # Menor o igual
```

### Operaciones Lógicas

```python
np.logical_and(arr1, arr2)              # Y lógico
np.logical_or(arr1, arr2)               # O lógico
np.logical_not(arr)                     # NO lógico
np.logical_xor(arr1, arr2)              # XOR lógico

# Con arrays booleanos
(arr > 2) & (arr < 8)                   # Y lógico con paréntesis
(arr < 2) | (arr > 8)                   # O lógico con paréntesis
~(arr > 5)                              # NO lógico
```

### Funciones de Validación

```python
np.any(arr > 5)                         # ¿Algún elemento cumple?
np.all(arr > 0)                         # ¿Todos los elementos cumplen?
np.isnan(arr)                           # ¿Es NaN?
np.isinf(arr)                           # ¿Es infinito?
np.isfinite(arr)                        # ¿Es finito?
```

---

## 🔢 Álgebra Lineal

### Operaciones Básicas

```python
np.dot(arr1, arr2)                      # Producto punto
arr1 @ arr2                             # Producto matricial (Python 3.5+)
np.matmul(arr1, arr2)                   # Producto matricial
np.cross(arr1, arr2)                    # Producto cruz
```

### Operaciones Matriciales

```python
np.linalg.det(arr)                      # Determinante
np.linalg.inv(arr)                      # Inversa
np.linalg.eig(arr)                      # Valores y vectores propios
np.linalg.svd(arr)                      # Descomposición SVD
np.linalg.qr(arr)                       # Descomposición QR
np.linalg.solve(A, b)                   # Resolver sistema Ax = b
```

### Normas

```python
np.linalg.norm(arr)                     # Norma euclidiana
np.linalg.norm(arr, ord=1)              # Norma L1
np.linalg.norm(arr, ord=np.inf)         # Norma infinito
```

---

## 🎯 Funciones de Búsqueda y Selección

```python
np.where(condition, x, y)               # x si condición, y si no
np.select([cond1, cond2], [choice1, choice2])  # Múltiples condiciones
np.choose(indices, choices)             # Elegir por índices
np.nonzero(arr)                         # Índices de elementos no-cero
np.argwhere(arr > 5)                    # Índices donde condición es True
```

---

## 🔄 Operaciones de Conjunto

```python
np.unique(arr)                          # Elementos únicos
np.intersect1d(arr1, arr2)             # Intersección
np.union1d(arr1, arr2)                 # Unión
np.setdiff1d(arr1, arr2)               # Diferencia
np.in1d(arr1, arr2)                    # ¿Elementos de arr1 están en arr2?
```

---

## 📈 Operaciones Acumulativas

```python
np.cumsum(arr)                          # Suma acumulativa
np.cumprod(arr)                         # Producto acumulativo
np.maximum.accumulate(arr)              # Máximo acumulativo
np.minimum.accumulate(arr)              # Mínimo acumulativo
```

---

## 🔧 Manipulación de Tipos de Datos

```python
arr.astype(np.int32)                    # Cambiar tipo de datos
arr.astype('float64')                   # Cambiar a float64
arr.astype(str)                         # Convertir a string

# Tipos comunes
np.int8, np.int16, np.int32, np.int64   # Enteros
np.float16, np.float32, np.float64      # Punto flotante
np.bool_                                # Booleano
np.complex64, np.complex128             # Números complejos
```

---

## 🎭 Enmascaramiento (Masked Arrays)

```python
# Crear array enmascarado
masked_arr = np.ma.masked_where(arr > 5, arr)

# Operaciones con máscaras
masked_arr.mean()                       # Media ignorando valores enmascarados
masked_arr.compressed()                 # Array sin valores enmascarados
```

---

## 📊 Broadcasting

```python
# Broadcasting automático
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_1d = np.array([10, 20, 30])
result = arr_2d + arr_1d                # Se suma a cada fila

# Broadcasting manual
arr_1d[:, np.newaxis]                   # Convertir a columna
arr_1d[np.newaxis, :]                   # Convertir a fila
```

---

## 🔍 Funciones de E/S (Entrada/Salida)

```python
# Guardar y cargar arrays
np.save('array.npy', arr)               # Guardar array
arr = np.load('array.npy')              # Cargar array
np.savez('arrays.npz', arr1=arr1, arr2=arr2)  # Múltiples arrays
np.savetxt('array.txt', arr)            # Guardar como texto
arr = np.loadtxt('array.txt')           # Cargar desde texto
```

---

## 💡 Consejos de Rendimiento

```python
# Usar funciones vectorizadas en lugar de loops
np.sum(arr)                             # Más rápido que sum(arr)

# Especificar dtype al crear arrays
np.zeros(1000, dtype=np.float32)       # Más eficiente en memoria

# Usar vistas en lugar de copias cuando sea posible
arr_view = arr[::2]                     # Vista (comparte memoria)
arr_copy = arr[::2].copy()              # Copia (nueva memoria)

# Operaciones in-place para ahorrar memoria
arr += 5                                # Modifica arr directamente
np.add(arr, 5, out=arr)                # Equivalente in-place
```

---

## 🔍 Depuración y Exploración

```python
# Información del array
np.info(arr)                            # Información detallada
arr.flags                               # Flags del array
arr.strides                             # Información de memoria

# En IPython/Jupyter
arr?                                    # Información rápida
np.función?                             # Documentación de función
```

---

## 📚 Recursos Adicionales

- **Documentación oficial**: https://numpy.org/doc/
- **User Guide**: https://numpy.org/doc/stable/user/index.html
- **API Reference**: https://numpy.org/doc/stable/reference/index.html
- **Cheat Sheet**: https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf

---

*Esta guía cubre las operaciones más comunes en NumPy. Para funciones específicas o casos avanzados, consultar la documentación oficial.*
