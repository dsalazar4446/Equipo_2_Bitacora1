# Bitácora 1 — Búsqueda Binaria Iterativa
**Equipo 2 | Análisis y Diseño de Algoritmos | 2026-III**  
**Profa. MSc. Ana Sosa | UNIVERSIDAD NACIONAL EXPERIMENTAL DE GUAYANA**

---

## Contenido de la Entrega

| Archivo | Descripción |
|---------|-------------|
| `informe_bitacora1.md` | Informe técnico completo (Markdown) |
| `informe_bitacora1.html` | Informe completo con estilos y gráficas embebidas |
| `informe_bitacora1.docx` | Informe en formato Word |
| `GUIA_DEFENSA_BITACORA1.md` | Guion de defensa oral (5 integrantes, 3 min c/u) |
| `GUIA_DEFENSA_BITACORA1.docx` | Guion en formato Word |
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

## Reproducción del Experimento

### Requisitos
- Python 3.10+
- Paquetes: `pandas`, `matplotlib`, `numpy`

```bash
pip install pandas matplotlib numpy
```

### Ejecución paso a paso

```bash
# 1. Clonar/ubicarse en la carpeta
cd bitacora/

# 2. Generar datos empíricos (resultados.csv)
python3 pruebas_busqueda.py
# Salida esperada: "Script finalizado. Resultados en 'resultados.csv'"

# 3. Procesar datos y generar análisis + gráficas
python3 analisis_graficas.py
# Salida esperada: estadisticas.csv, grafica_lineal.png, grafica_log.png, boxplot.png, tabla_latex.txt, analisis_cotas.txt
```

### Parámetros del experimento (fijos en el código)
| Parámetro | Valor |
|-----------|-------|
| Tamaños (n) | 100, 200, 400, 800, 1600, 3200, 6400, 12800 |
| Repeticiones por caso | 100 |
| Casos evaluados | Favorable (posición media), Peor (último), Negativo (−1) |
| Semilla aleatoria | Fija (`random.seed(42)` en el script) |
| Medición | `time.perf_counter_ns()` (nanosegundos) |

### Resultados esperados (resumen)
- **Razón T(2n)/T(n)** ≈ 1.08–1.11 para los tres casos (confirma log₂(n))
- **R² regresión log₂(n)** > 0.94 en todos los casos
- **Cotas propuestas** con constantes explícitas (c, n₀ = 100)

---

## Estructura del Informe (pautas cumplidas)

1. **Problema y Especificación** — Entradas, salidas, pre/postcondiciones formales
2. **Demostración de Corrección** — Pseudocódigo + Invariante de ciclo (3 momentos) + Terminación
3. **Análisis de Costo** — Operación dominante, recurrencia, Teorema Maestro, casos mejor/peor/promedio, cotas
4. **Pruebas Empíricas** — Metodología, tablas, gráficas (lineal, log-log, boxplot), contraste teoría vs. práctica
5. **Conclusiones** — 4 puntos: correctitud, complejidad, comportamiento casos, reproducibilidad

---

## Defensa Oral

Ver `GUIA_DEFENSA_BITACORA1.md` o `GUIA_DEFENSA_BITACORA1.docx`:
- 5 integrantes × 3 minutos = 15 min total
- Cada uno con texto base (~2:30) + tabla preguntas/respuestas
- Distribución: Especificación → Correctitud → Teoría → Empírico → Cierre

---

## Contacto

**Equipo 2** — Análisis y Diseño de Algoritmos — 2026-III  
Universidad Nacional Experimental de Guayana