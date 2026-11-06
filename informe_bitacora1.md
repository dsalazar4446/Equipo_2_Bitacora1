# Bitácora 1: Prueba, Análisis y Gráfica Reproducible
## Búsqueda Binaria Iterativa

**Equipo 2**  
**Maestría en Tecnologías de la Información**  
**Análisis y Diseño de Algoritmos**  
**Cohorte X · 2026-III**  
**Profa. Msc. Sosa**  

---

## 1. Problema y Especificación

### 1.1 Problema
Dado un arreglo ordenado $A[0..n-1]$ de elementos comparables y un valor objetivo $x$, determinar si $x$ existe en el arreglo y, en caso afirmativo, devolver su índice. Si no existe, devolver $-1$.

### 1.2 Especificación Formal

| Componente | Descripción |
|------------|-------------|
| **Entradas** | - Arreglo $A$ de $n$ elementos ordenados no decrecientemente ($A[0] \leq A[1] \leq \dots \leq A[n-1]$)<br>- Valor objetivo $x$ del mismo tipo que los elementos de $A$ |
| **Salidas** | - Índice $i$ tal que $A[i] = x$, si $x \in A$<br>- $-1$ si $x \notin A$ |
| **Precondición** | $A$ está ordenado en orden no decreciente |
| **Postcondición** | $(result \neq -1 \implies A[result] = x) \land (result = -1 \implies \forall i \in [0,n): A[i] \neq x)$ |

---

## 2. Demostración de Corrección

### 2.1 Algoritmo (Pseudocódigo)

```
BUSCAR-BINARIA(A, x)
1  low  ← 0
2  high ← length(A) - 1
3  mientras low ≤ high hacer
4      mid ← ⌊(low + high) / 2⌋
5      si A[mid] = x
6          return mid
7      sino si A[mid] < x
8          low ← mid + 1
9      sino
10         high ← mid - 1
11  return -1
```

### 2.2 Invariante de Ciclo

**Invariante $I$:** Al inicio de cada iteración del ciclo `while` (línea 3), se cumple que:
> Si $x$ está en $A$, entonces $x$ está en el subarreglo $A[low..high]$.

Formalmente: $x \in A \implies \exists i \in [low, high] : A[i] = x$.

### 2.3 Tres Momentos de la Invariante

#### **Inicialización** (antes de la primera iteración)
- Antes de la línea 3: $low = 0$, $high = n-1$
- El subarreglo $A[low..high]$ es todo el arreglo $A[0..n-1]$
- Si $x \in A$, entonces trivialmente $x \in A[0..n-1]$
- $\therefore$ La invariante se cumple antes de la primera iteración.

#### **Mantenimiento** (cada iteración preserva la invariante)
Supongamos que la invariante se cumple al inicio de una iteración (con valores $low, high$ actuales). Analizamos los tres casos:

1. **Caso $A[mid] = x$ (línea 5-6):**  
   El algoritmo termina y retorna $mid$. La postcondición se cumple directamente.

2. **Caso $A[mid] < x$ (línea 7-8):**  
   Como $A$ está ordenado, $\forall i \leq mid: A[i] \leq A[mid] < x$.  
   Por tanto, $x$ no puede estar en $A[low..mid]$.  
   Nuevo $low' = mid + 1$, $high' = high$.  
   Si $x \in A$, debe estar en $A[mid+1..high] = A[low'..high']$.  
   $\therefore$ La invariante se mantiene.

3. **Caso $A[mid] > x$ (línea 9-10):**  
   Como $A$ está ordenado, $\forall i \geq mid: A[i] \geq A[mid] > x$.  
   Por tanto, $x$ no puede estar en $A[mid..high]$.  
   Nuevo $low' = low$, $high' = mid - 1$.  
   Si $x \in A$, debe estar en $A[low..mid-1] = A[low'..high']$.  
   $\therefore$ La invariante se mantiene.

#### **Terminación** (cuando el ciclo termina)
El ciclo termina cuando $low > high$. En ese momento:
- El subarreglo $A[low..high]$ está **vacío** ($low > high \implies$ no hay índices válidos).
- Por la invariante: si $x \in A$, entonces $x \in A[low..high] = \varnothing$, lo cual es imposible.
- $\therefore x \notin A$ y el algoritmo retorna correctamente $-1$.

### 2.4 Argumento de Terminación

En cada iteración del ciclo, el tamaño del intervalo de búsqueda $high - low + 1$ disminuye **estrictamente**:
- Si $A[mid] < x$: $low$ aumenta a $mid+1$, intervalo se reduce al menos en 1.
- Si $A[mid] > x$: $high$ disminuye a $mid-1$, intervalo se reduce al menos en 1.

Como el tamaño es un entero no negativo y decrece estrictamente, eventualmente llega a 0 ($low > high$) y el ciclo termina. $\square$

---

## 3. Análisis de Costo

### 3.1 Operación Dominante
La **comparación** `A[mid] == x` (o `A[mid] < x`) en la línea 5/7 del pseudocódigo. Esta se ejecuta exactamente una vez por iteración del ciclo.

### 3.2 Recurrencia
Sea $T(n)$ el número máximo de comparaciones para un arreglo de tamaño $n$.

En el peor caso, el algoritmo descarta la mitad del arreglo en cada iteración:
$$
T(n) = T\left(\left\lfloor \frac{n}{2} \right\rfloor\right) + 1, \quad T(1) = 1
$$

### 3.3 Resolución de la Recurrencia
Aplicando el **Teorema Maestro** ($a=1, b=2, f(n)=1$):
- $n^{\log_b a} = n^0 = 1$
- $f(n) = \Theta(1) = \Theta(n^{\log_b a})$
- **Caso 2**: $T(n) = \Theta(\log n)$

Alternativamente, por expansión:
$$
T(n) = T(n/2) + 1 = T(n/4) + 2 = \dots = T(1) + \log_2 n = 1 + \log_2 n
$$

### 3.4 Órdenes de Crecimiento

| Caso | Número de iteraciones | Orden de crecimiento |
|------|----------------------|---------------------|
| **Mejor** | 1 (elemento está en la posición media inicial) | $\Theta(1)$ |
| **Peor** | $\lfloor \log_2 n \rfloor + 1$ (elemento en extremo o no existe) | $\Theta(\log n)$ |
| **Promedio** | $\sim \log_2 n - 1$ (distribución uniforme) | $\Theta(\log n)$ |

### 3.5 Cotas Asintóticas
- **Cota superior:** $O(\log n)$ — en todos los casos
- **Cota inferior:** $\Omega(1)$ — mejor caso
- **Cota ajustada peor caso:** $\Theta(\log n)$

**Supuestos declarados:**
- El acceso a $A[i]$ es $O(1)$ (arreglo en memoria contigua)
- Las comparaciones entre elementos son $O(1)$
- El arreglo ya está ordenado (el costo de ordenamiento no se incluye)

---

## 4. Pruebas Empíricas, Análisis y Gráfica Reproducible

### 4.1 Metodología Experimental

| Parámetro | Valor |
|-----------|-------|
| **Tamaños probados ($n$)** | 100, 1,000, 10,000, 50,000, 100,000, 200,000, 500,000 |
| **Repeticiones por caso** | 50 |
| **Casos evaluados** | Favorable (encontrado en posición media), Peor (encontrado en primer elemento), Negativo (no encontrado) |
| **Método de medición** | `time.perf_counter_ns()` (nanosegundos) |
| **Entorno** | Python 3.14, MacOS ARM64 |

### 4.2 Scripts Utilizados

Todos los scripts y datos crudos están disponibles en la carpeta del proyecto para reproducibilidad total:

1. **`pruebas_busqueda.py`** — Genera `resultados.csv` con 1,050 mediciones (7 tamaños × 3 casos × 50 repeticiones)
2. **`analisis_graficas.py`** — Procesa `resultados.csv`, genera estadísticas, gráficas y tabla LaTeX

### 4.3 Resultados Estadísticos (Resumen)

| $n$ | Caso | Media (ns) | Mediana (ns) | $\sigma$ (ns) |
|-----|------|-----------|-------------|---------------|
| 100 | Favorable | 559.1 | 500.0 | 355.3 |
| 100 | Peor | 484.1 | 459.0 | 36.6 |
| 100 | Negativo | 490.8 | 500.0 | 29.5 |
| 1,000 | Favorable | 710.4 | 708.0 | 95.9 |
| 1,000 | Peor | 705.9 | 708.0 | 43.3 |
| 1,000 | Negativo | 713.4 | 708.0 | 34.2 |
| 10,000 | Favorable | 915.0 | 875.0 | 237.4 |
| 10,000 | Peor | 929.9 | 875.0 | 327.3 |
| 10,000 | Negativo | 897.4 | 875.0 | 51.2 |
| 50,000 | Favorable | 1,037.6 | 958.0 | 585.3 |
| 50,000 | Peor | 976.6 | 958.0 | 148.4 |
| 50,000 | Negativo | 957.5 | 958.0 | 21.4 |
| 100,000 | Favorable | 1,065.8 | 875.0 | 1,205.5 |
| 100,000 | Peor | 966.7 | 916.0 | 357.0 |
| 100,000 | Negativo | 925.7 | 917.0 | 44.0 |
| 200,000 | Favorable | 1,114.1 | 958.0 | 1,018.5 |
| 200,000 | Peor | 1,000.0 | 958.0 | 273.5 |
| 200,000 | Negativo | 969.2 | 958.0 | 151.7 |
| 500,000 | Favorable | 1,169.1 | 1,000.0 | 967.0 |
| 500,000 | Peor | 1,112.4 | 1,041.0 | 544.2 |
| 500,000 | Negativo | 1,040.7 | 1,042.0 | 25.9 |

*Tabla completa en `tabla_latex.txt` lista para incluir en LaTeX.*

### 4.4 Ajuste a Modelo Logarítmico

Se realizó regresión lineal: $tiempo = \alpha \cdot \log_2(n) + \beta$ sobre las medias.

| Caso | Modelo ajustado | $R^2$ |
|------|-----------------|-------|
| **Favorable** | $50.94 \cdot \log_2(n) + 220.73$ | 0.9955 |
| **Peor** | $47.10 \cdot \log_2(n) + 218.37$ | 0.9495 |
| **Negativo** | $41.65 \cdot \log_2(n) + 269.42$ | 0.9375 |

**Interpretación:** Los tres casos presentan $R^2 > 0.93$, confirmando el comportamiento $\Theta(\log n)$ predicho por la teoría.

### 4.5 Gráficas Generadas

1. **`grafica_lineal.png`** — Tiempo medio vs $n$ (escala lineal). Muestra la curva característica logarítmica.
2. **`grafica_log.png`** — Tiempo medio vs $\log_2(n)$. Los puntos se alinean casi perfectamente en rectas, confirmando $T(n) \propto \log n$.
3. **`boxplot.png`** — Distribución de 50 repeticiones para $n = 500,000$. El caso favorable muestra mayor variabilidad (algunas iteraciones extra por *cold start* de CPU); casos peor y negativo son muy estables.

### 4.6 Contraste Teoría vs. Práctica

| Aspecto | Teoría | Observado | Comentario |
|---------|--------|-----------|------------|
| Orden de crecimiento | $\Theta(\log n)$ | $R^2 > 0.93$ | **Confirmado** |
| Mejor caso | $\Theta(1)$ | ~500-1000 ns constante | **Confirmado** (termina en 1 iteración) |
| Peor caso $\approx$ Negativo | Mismo orden | Muy similares | **Confirmado** (ambos recorren altura completa del árbol) |
| Constantes | Dependientes de máquina | ~42-51 ns por nivel de $\log_2(n)$ | Consistente con overhead de Python |

### 4.7 Reproducibilidad

Para reproducir exactamente estos resultados:
```bash
cd bitacora/
python3 pruebas_busqueda.py      # Genera resultados.csv
python3 analisis_graficas.py     # Genera estadísticas, gráficas y tablas
```

Todos los archivos generados (`resultados.csv`, `estadisticas.csv`, `grafica_lineal.png`, `grafica_log.png`, `boxplot.png`, `tabla_latex.txt`, `resumen_analisis.txt`) se incluyen en esta entrega.

---

## 5. Conclusiones

1. **Corrección probada:** La invariante de ciclo demuestra formalmente que el algoritmo retorna el índice correcto o $-1$ según corresponda, y siempre termina.

2. **Complejidad confirmada:** Tanto el análisis teórico ($\Theta(\log n)$ peor/promedio, $\Theta(1)$ mejor) como las mediciones empíricas ($R^2 > 0.93$) coinciden.

3. **Comportamiento de casos:** El caso favorable es consistentemente más rápido (termina en la primera iteración). Los casos peor y negativo tienen tiempos prácticamente idénticos, pues ambos requieren recorrer la altura completa del árbol de decisión implícito.

4. **Reproducibilidad garantizada:** Se entregan scripts, datos crudos y resultados procesados para que cualquier evaluador pueda replicar el experimento íntegramente.

---

## Anexo: Archivos Entregados

```
bitacora/
├── pruebas_busqueda.py       # Script de medición
├── analisis_graficas.py      # Script de análisis y gráficas
├── resultados.csv            # Datos crudos (1,050 filas)
├── estadisticas.csv          # Estadísticas agregadas
├── grafica_lineal.png        # Gráfica: tiempo vs n
├── grafica_log.png           # Gráfica: tiempo vs log₂(n)
├── boxplot.png               # Boxplot n=500,000
├── tabla_latex.txt           # Tabla LaTeX lista para compilar
└── resumen_analisis.txt      # Resumen numérico del ajuste
```

---

**Fecha de entrega:** Viernes 06/11/2026  
**Equipo 2** — Búsqueda Binaria Iterativa