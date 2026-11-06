#!/usr/bin/env python3
"""
Análisis y gráficas Búsqueda Binaria Iterativa
Equipo 2 – Bitácora 1
Ajustado según pautas de entrega.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    # Leer datos
    df = pd.read_csv('resultados.csv')

    # Estadísticas por n y tipo de caso (mediana y Q1/Q3 para boxplot)
    stats = df.groupby(['n', 'tipo_caso'])['tiempo_ns'].agg(['median', lambda x: x.quantile(0.25), lambda x: x.quantile(0.75)]).reset_index()
    stats.columns = ['n', 'tipo_caso', 'mediana_ns', 'q1_ns', 'q3_ns']

    # Guardar estadísticas en CSV
    stats.to_csv('estadisticas.csv', index=False)
    print("Estadísticas guardadas en 'estadisticas.csv'")

    # Gráfica 1: Mediana vs n (escala lineal)
    plt.figure(figsize=(10, 6))
    for caso in ['favorable', 'peor', 'negativo']:
        subset = stats[stats['tipo_caso'] == caso]
        plt.plot(subset['n'], subset['mediana_ns'], 'o-', label=f'Caso {caso}', linewidth=2, markersize=6)
    plt.xlabel('Tamaño del arreglo (n)')
    plt.ylabel('Tiempo mediano (ns)')
    plt.title('Búsqueda Binaria Iterativa: Mediana vs n')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_lineal.png', dpi=300)
    plt.close()
    print("Gráfica lineal guardada en 'grafica_lineal.png'")

    # Gráfica 2: Mediana vs log2(n) (escala logarítmica en X)
    plt.figure(figsize=(10, 6))
    for caso in ['favorable', 'peor', 'negativo']:
        subset = stats[stats['tipo_caso'] == caso]
        plt.plot(np.log2(subset['n']), subset['mediana_ns'], 'o-', label=f'Caso {caso}', linewidth=2, markersize=6)
    plt.xlabel('log₂(n)')
    plt.ylabel('Tiempo mediano (ns)')
    plt.title('Búsqueda Binaria Iterativa: Mediana vs log₂(n)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('grafica_log.png', dpi=300)
    plt.close()
    print("Gráfica logarítmica guardada en 'grafica_log.png'")

    # Gráfica 3: Boxplot por tipo de caso (n = 12800)
    plt.figure(figsize=(10, 6))
    subset = df[df['n'] == 12800]
    data_to_plot = [subset[subset['tipo_caso'] == c]['tiempo_ns'].values for c in ['favorable', 'peor', 'negativo']]
    plt.boxplot(data_to_plot, tick_labels=['Favorable', 'Peor', 'Negativo'])
    plt.ylabel('Tiempo (ns)')
    plt.title('Distribución de tiempos para n = 12,800 (100 repeticiones)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('boxplot.png', dpi=300)
    plt.close()
    print("Boxplot guardado en 'boxplot.png'")

    # Tabla de razones T(2n)/T(n) y análisis de cotas
    with open('analisis_cotas.txt', 'w') as f:
        f.write("=== ANÁLISIS DE COTAS Y RAZONES T(2n)/T(n) ===\n\n")
        f.write("Tamaños probados: 100, 200, 400, 800, 1600, 3200, 6400, 12800\n")
        f.write("Repeticiones: 100\n\n")

        for caso in ['favorable', 'peor', 'negativo']:
            f.write(f"--- Caso {caso.upper()} ---\n")
            subset = stats[stats['tipo_caso'] == caso].sort_values('n')
            f.write(f"{'n':>6} | {'Mediana (ns)':>12} | {'T(2n)/T(n)':>12}\n")
            f.write("-" * 38 + "\n")

            prev_median = None
            ratios = []
            for _, row in subset.iterrows():
                n = int(row['n'])
                med = row['mediana_ns']
                if prev_median is not None:
                    ratio = med / prev_median
                    ratios.append(ratio)
                    f.write(f"{n:>6} | {med:>12.1f} | {ratio:>12.3f}\n")
                else:
                    f.write(f"{n:>6} | {med:>12.1f} | {'(base)':>12}\n")
                prev_median = med

            avg_ratio = np.mean(ratios) if ratios else 0
            f.write(f"\nRazón promedio T(2n)/T(n): {avg_ratio:.3f} (esperado ~1.0 para log₂(n) + 1 iteración extra)\n")

            # Ajuste a modelo logarítmico: T(n) = a * log2(n) + b
            x = np.log2(subset['n'].values)
            y = subset['mediana_ns'].values
            coeff = np.polyfit(x, y, 1)
            r2 = np.corrcoef(x, y)[0, 1]**2

            f.write(f"Modelo: T(n) = {coeff[0]:.2f} * log₂(n) + {coeff[1]:.2f}\n")
            f.write(f"R² = {r2:.6f}\n\n")

            # Propuesta de cota asintótica con constantes c, n0
            # T(n) <= c * log2(n) + b
            f.write(f"Cota propuesta: T(n) <= {coeff[0]:.1f} * log₂(n) + {coeff[1]:.1f} para n >= 100\n\n")

    print("Análisis de cotas guardado en 'analisis_cotas.txt'")

    # Tabla LaTeX para el informe
    with open('tabla_latex.txt', 'w') as f:
        f.write("%% Tabla de estadísticas para el informe\n")
        f.write("\\begin{table}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\caption{Estadísticas de tiempo de ejecución (nanosegundos) por tamaño $n$ y tipo de caso.}\n")
        f.write("\\label{tab:estadisticas}\n")
        f.write("\\begin{tabular}{lrrrr}\n")
        f.write("\\toprule\n")
        f.write("$n$ & Caso & Mediana & Q1 & Q3 \\\\\n")
        f.write("\\midrule\n")
        for _, row in stats.iterrows():
            f.write(f"{int(row['n']):,} & {row['tipo_caso']} & {row['mediana_ns']:.1f} & {row['q1_ns']:.1f} & {row['q3_ns']:.1f} \\\\\n")
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")
    print("Tabla LaTeX guardada en 'tabla_latex.txt'")

if __name__ == "__main__":
    main()