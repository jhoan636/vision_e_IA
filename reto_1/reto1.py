import random
import time
import math

# INICIO MEDICIÓN TIEMPO
start_time = time.time()

# CONFIGURACIÓN
ROWS = 1000
COLS = 1000
OUTPUT_MATRIX_TXT = "matrix_1000x1000.txt"
OUTPUT_VECTOR_TXT = "vector_1000x1000.txt"

# CREAR MATRIZ 1000x1000
matrix = [
    [random.randint(0, 255) for _ in range(COLS)]
    for _ in range(ROWS)
]

# APLANAR MATRIZ
flat = [value for row in matrix for value in row]

# ESTADÍSTICAS BÁSICAS
n = len(flat)
min_val = min(flat)
max_val = max(flat)
mean = sum(flat) / n

variance = sum((x - mean) ** 2 for x in flat) / n
std_dev = math.sqrt(variance)

# FIN MEDICIÓN TIEMPO
end_time = time.time()

print("Minimo:", min_val)
print("Maximo:", max_val)
print("Media:", mean)
print("Desviacion estandar:", std_dev)
print("Tiempo total:", end_time - start_time, "Segundos")

# GUARDAR MATRIZ EN TXT
with open(OUTPUT_MATRIX_TXT, "w") as f:
    for row in matrix:
        f.write(" ".join(str(value) for value in row) + "\n")

# GUARDAR VECTOR APLASTADO EN TXT
with open(OUTPUT_VECTOR_TXT, "w") as f:
    f.write(" ".join(str(value) for value in flat))
