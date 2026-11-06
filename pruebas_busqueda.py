#!/usr/bin/env python3
"""
Pruebas empíricas Búsqueda Binaria Iterativa
Equipo 2 – Bitácora 1
Ajustado para cumplir pautas de entrega.
"""

import time
import random
import csv

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def generar_datos(n):
    return sorted(random.sample(range(n * 10), n))

def medir_tiempo(arr, target):
    start_time = time.perf_counter_ns()
    binary_search(arr, target)
    end_time = time.perf_counter_ns()
    return end_time - start_time

def main():
    # Tamaños de entrada ajustados según pautas
    sizes = [100, 200, 400, 800, 1600, 3200, 6400, 12800]
    repeticiones = 100 # Aumentado para mayor estabilidad

    with open('resultados.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'tipo_caso', 'tiempo_ns'])

        for n in sizes:
            arr = generar_datos(n)

            # Caso Favorable (elemento en la mitad)
            target_favorable = arr[n // 2]
            for _ in range(repeticiones):
                writer.writerow([n, 'favorable', medir_tiempo(arr, target_favorable)])

            # Caso Peor (elemento al final o al principio)
            target_peor = arr[-1]
            for _ in range(repeticiones):
                writer.writerow([n, 'peor', medir_tiempo(arr, target_peor)])

            # Caso Negativo (no encontrado)
            target_negativo = -1
            for _ in range(repeticiones):
                writer.writerow([n, 'negativo', medir_tiempo(arr, target_negativo)])

    print("Script finalizado. Resultados en 'resultados.csv'.")

if __name__ == "__main__":
    main()
