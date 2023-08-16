# Maximum-Index-Product
# Maximum Index Product

Este es un programa en Python que resuelve el problema de encontrar el máximo Index Product para una lista dada.

## Descripción

Dado un conjunto de números representados como una lista, para cada elemento `arr[i]`, se definen dos valores `Left(i)` y `Right(i)` de la siguiente manera:

- `Left(i)` es el índice más cercano `j` tal que `j < i` y `arr[j] > arr[i]`. Si no existe un `j` que cumpla esta condición, entonces `Left(i)` es igual a 0.

- `Right(i)` es el índice más cercano `k` tal que `k > i` y `arr[k] > arr[i]`. Si no existe un `k` que cumpla esta condición, entonces `Right(i)` es igual a 0.

El programa calcula el producto de `Left(i)` y `Right(i)` para cada elemento `arr[i]` y luego encuentra el máximo de estos productos, conocido como `Index Product`.

## Cómo Usar

El programa está implementado en Python y se proporciona en el archivo `max_index_product.py`. Para usarlo, simplemente reemplaza la lista `arr` con tu propia lista de números. A continuación, ejecuta el programa y mostrará el resultado del máximo Index Product.

```python
arr = [4, 7, 2, 8, 5, 1, 6]

def solve(arr):
    # ... (resto del código)
    # ...
    maximumIndexProduct = max(indexProduct)
    return maximumIndexProduct

print(solve(arr))
```

## Ejemplo

Supongamos que usamos la lista `arr = [4, 7, 2, 8, 5, 1, 6]`, luego de ejecutar el programa, obtendríamos el siguiente resultado:
```
Left: [0, 1, 1, 3, 2, 0, 4]
Right: [2, 0, 4, 0, 4, 6, 0]
Index-Product: [0, 0, 4, 0, 8, 0, 0]
Maximum Index Podroduct = 8
````
## Contribuciones

Siéntete libre de realizar contribuciones o mejoras a este programa. ¡Disfruta resolviendo problemas y aprendiendo juntos!

## Licencia

Este programa se distribuye bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.


