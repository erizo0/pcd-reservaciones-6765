import json
import time
import numpy as np

def a_float(texto):
    try:
        return float(texto.strip())
    except (ValueError, AttributeError):
        return np.nan

def cargar_columna_numerica(ruta, nombre_columna):
    with open(ruta, "r") as f:
        lineas = f.read().strip().split("\n")
    
    cabecera = lineas[0].split("|")
    idx = cabecera.index(nombre_columna)
    
    filas = [linea.split("|") for linea in lineas[1:]]
    crudos = [fila[idx] for fila in filas]
    
    col = np.array([a_float(v) for v in crudos])
    return col[~np.isnan(col)]

def calcular_estadisticas(arr, nombre_columna):
    media = arr.mean()
    std = arr.std()
    p25, p75 = np.percentile(arr, [25, 75])
    
    return {
        "columna": nombre_columna,
        "n_valores_validos": int(arr.size),
        "media": round(float(media), 2),
        "desviacion_estandar": round(float(std), 2),
        "minimo": round(float(arr.min()), 2),
        "maximo": round(float(arr.max()), 2),
        "mediana": round(float(np.median(arr)), 2),
        "percentil_25": round(float(p25), 2),
        "percentil_75": round(float(p75), 2)
    }

def detectar_outliers(arr):
    media = arr.mean()
    std = arr.std()
    
    limite_inf = media - 3 * std
    limite_sup = media + 3 * std
    
    mascara = (arr < limite_inf) | (arr > limite_sup)
    outliers = arr[mascara]
    
    n_outliers = int(mascara.sum())
    porcentaje = round(float(100 * mascara.mean()), 2)
    
    outliers_min = round(float(outliers.min()), 2) if n_outliers > 0 else None
    outliers_max = round(float(outliers.max()), 2) if n_outliers > 0 else None
    
    return {
        "metodo": "desviacion_estandar_3",
        "limite_inferior": round(float(limite_inf), 2),
        "limite_superior": round(float(limite_sup), 2),
        "n_outliers": n_outliers,
        "porcentaje": porcentaje,
        "outliers_minimo": outliers_min,
        "outliers_maximo": outliers_max
    }

def benchmark_numpy_vs_bucle(arr_np):
    arr_py = arr_np.tolist()
    n = len(arr_py)
    
    inicio = time.perf_counter()
    suma = 0.0
    for v in arr_py:
        suma += v
    media_py = suma / n
    
    acum = 0.0
    for v in arr_py:
        acum += (v - media_py) ** 2
    std_py = (acum / n) ** 0.5
    t_py = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    media_np = arr_np.mean()
    std_np = arr_np.std()
    t_np = time.perf_counter() - inicio
    
    factor = round(t_py / t_np, 1) if t_np > 0.0 else None
    
    return {
        "n_filas": int(arr_np.size),
        "tiempo_bucle_python_seg": round(t_py, 6),
        "tiempo_numpy_seg": round(t_np, 6),
        "factor_velocidad": factor,
        "operacion_medida": "calcular media y desviacion estandar"
    }
tema = "Reservaciones"
pareja = "Cruz Gonzalez Erick Miguel y Escamilla Camarillo Ricardo"
seed = 3
columna_num_1 = "precio_noche"
columna_num_2 = "dias_anticipacion"

ruta_csv = f"C:/Users/Laptop/Documents/ESCOM/Tercer semestre/PCD_2026/P3/reservaciones-ruido_100000.csv"
ruta_json = "C:/Users/Laptop/Documents/ESCOM/Tercer semestre/PCD_2026/P3/resultados/analisis_numpy.json"

arr_num_1 = cargar_columna_numerica(ruta_csv, columna_num_1)
arr_num_2 = cargar_columna_numerica(ruta_csv, columna_num_2)

stats_1 = calcular_estadisticas(arr_num_1, columna_num_1)
stats_2 = calcular_estadisticas(arr_num_2, columna_num_2)

outliers_1 = detectar_outliers(arr_num_1)
outliers_2 = detectar_outliers(arr_num_2)

bench = benchmark_numpy_vs_bucle(arr_num_1)

resultado = {
    "archivo": "reservaciones-ruido_1000000.csv",
    "pareja": pareja,
    "seed": seed,
    "numerica_1": stats_1,
    "numerica_2": stats_2,
    "outliers_numerica_1": outliers_1,
    "outliers_numerica_2": outliers_2,
    "benchmark": bench
}

with open(ruta_json, "w") as f:
    json.dump(resultado, f, indent=2)