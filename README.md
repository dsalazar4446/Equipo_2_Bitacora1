# Bitácora 1 — Búsqueda Binaria Iterativa
**Equipo 2 | Análisis y Diseño de Algoritmos | 2026-III**  
**Profa. MSc. Ana Sosa | UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA**

---

## 📋 Índice de Contenidos

1. [Contenido de la Entrega](#contenido-de-la-entrega)
2. [Reproducción del Experimento](#reproducción-del-experimento)
3. [Resultados Experimentales Clave](#resultados-experimentales-clave)
4. [Gráficas Generadas](#gráficas-generadas)

---

## 📦 Contenido de la Entrega

| Archivo | Descripción |
|---------|-------------|
| `informe_bitacora1.md` | Informe técnico completo (Markdown) |
| `informe_bitacora1.docx` | Informe en formato Word |
| `pruebas_busqueda.py` | Script de medición empírica |
| `analisis_graficas.py` | Script de análisis y generación de gráficas |
| `resultados.csv` | Datos crudos (2,400 mediciones) |
| `estadisticas.csv` | Mediana, Q1, Q3 por n y caso |
| `analisis_cotas.txt` | Razones T(2n)/T(n), modelos de regresión, cotas |
| `tabla_latex.txt` | Tabla LaTeX lista para compilar |
| `grafica_lineal.png` | Mediana vs n (escala lineal) |
| `grafica_log.png` | Mediana vs log₂(n) (escala logarítmica) |
| `boxplot.png` | Distribución n=12,800 (100 repeticiones) |
| `resumen_analisis.txt` | Resumen numérico del ajuste |

---

## 🔬 Reproducción del Experimento

### Requisitos
- Python 3.10+
- Paquetes: `pandas`, `matplotlib`, `numpy`

```bash
pip install pandas matplotlib numpy
```

### Ejecución paso a paso

```bash
# 1. Clonar repositorio
git clone https://github.com/dsalazar4446/Equipo_2_Bitacora1.git
cd Equipo_2_Bitacora1/

# 2. Generar datos empíricos (resultados.csv)
python3 pruebas_busqueda.py
# Salida esperada: "Script finalizado. Resultados en 'resultados.csv'"

# 3. Procesar datos y generar análisis + gráficas
python3 analisis_graficas.py
# Salida esperada: estadisticas.csv, grafica_lineal.png, grafica_log.png, boxplot.png, tabla_latex.txt, analisis_cotas.txt
```

### Parámetros del Experimento
| Parámetro | Valor |
|-----------|-------|
| **Tamaños (n)** | 100, 200, 400, 800, 1600, 3200, 6400, 12800 (potencias de 2 × 100) |
| **Repeticiones por caso** | 100 |
| **Casos evaluados** | Favorable, Peor, Negativo |
| **Semilla aleatoria** | Fija (`random.seed(42)`) |
| **Medición** | `time.perf_counter_ns()` (nanosegundos) |

---

## 📊 Resultados Experimentales Clave

### Análisis de Razones T(2n)/T(n)

| Caso | Razón Promedio T(2n)/T(n) | Interpretación |
|------|---------------------------|----------------|
| **Favorable** | **1.099** | ~1.0 confirma crecimiento logarítmico |
| **Peor** | **1.082** | ~1.0 confirma crecimiento logarítmico |
| **Negativo** | **1.105** | ~1.0 confirma crecimiento logarítmico |

> **Conclusión:** Las razones cercanas a 1.0 validan que $T(n) \in \Theta(\log_2 n)$.

---

## 📉 Gráficas Generadas

- **`grafica_lineal.png`**: Visualización del tiempo de ejecución en escala lineal.
- **`grafica_log.png`**: Visualización del tiempo de ejecución en escala logarítmica (ajuste a modelo $\log_2(n)$).
- **`boxplot.png`**: Distribución estadística del tiempo para el tamaño máximo de entrada.