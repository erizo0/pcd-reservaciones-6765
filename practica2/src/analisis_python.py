import json
import os

# Definir las rutas relativas al proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Usamos el dataset completo de 103,000 registros tal como exige la rúbrica
DATASET_PATH = os.path.normpath(os.path.join(BASE_DIR, '../../datos/reservaciones-ruido_100000.csv'))
OUTPUT_PATH = os.path.normpath(os.path.join(BASE_DIR, '../resultados/analisis_python.json'))

def leer_csv(ruta):
    """Lee el archivo CSV separado por '|' y retorna una lista de diccionarios."""
    datos = []
    if not os.path.exists(ruta):
        print(f"Error: No se encontró el archivo en {ruta}")
        return datos
    
    with open(ruta, mode='r', encoding='utf-8') as f:
        lineas = f.readlines()
        if not lineas:
            return datos
        
        # Obtener encabezados eliminando espacios y saltos de línea
        encabezados = [h.strip() for h in lineas[0].split('|')]
        
        for linea in lineas[1:]:
            valores = [v.strip() for v in linea.split('|')]
            if len(valores) == len(encabezados):
                fila_dict = dict(zip(encabezados, valores))
                datos.append(fila_dict)
    return datos

def valores_unicos(datos, columna):
    """Obtiene los valores únicos de una columna aplicando strip y descartando vacíos."""
    unicos = set()
    for fila in datos:
        val = fila.get(columna, '').strip()
        if val:
            unicos.add(val)
    return unicos

def conteo_por_categoria(datos, columna):
    """Construye un diccionario con el conteo por categoría (respetando variantes)."""
    conteo = {}
    for fila in datos:
        val = fila.get(columna, '').strip()
        if val:
            conteo[val] = conteo.get(val, 0) + 1
    return conteo

def calcular_mediana(lista_valores):
    """Calcula la mediana de una lista de floats ordenada."""
    if not lista_valores:
        return 0.0
    n = len(lista_valores)
    mitad = n // 2
    if n % 2 == 1:
        return lista_valores[mitad]
    else:
        return (lista_valores[mitad - 1] + lista_valores[mitad]) / 2.0

def estadisticas(datos, columna):
    """Calcula min, max, promedio y mediana usando filter y map."""
    # Filtrar valores no vacíos usando lambda y filter
    filas_validas = list(filter(lambda f: f.get(columna, '').strip() != '', datos))
    
    # Mapear a float los valores válidos
    valores = list(map(lambda f: float(f.get(columna)), filas_validas))
    
    n_validos = len(valores)
    if n_validos == 0:
        return {
            "columna": columna,
            "n_valores_validos": 0,
            "minimo": 0.0,
            "maximo": 0.0,
            "promedio": 0.0,
            "mediana": 0.0
        }
    
    valores_ordenados = sorted(valores)
    min_val = valores_ordenados[0]
    max_val = valores_ordenados[-1]
    promedio = sum(valores_ordenados) / n_validos
    mediana = calcular_mediana(valores_ordenados)
    
    return {
        "columna": columna,
        "n_valores_validos": n_validos,
        "minimo": round(min_val, 2),
        "maximo": round(max_val, 2),
        "promedio": round(promedio, 2),
        "mediana": round(mediana, 2)
    }

def promedio_por_categoria(datos, categorica, numerica):
    """Calcula el promedio de la columna numérica para cada categoría cruzando ambas columnas."""
    acumulador = {}
    for fila in datos:
        cat = fila.get(categorica, '').strip()
        num_str = fila.get(numerica, '').strip()
        if cat and num_str:
            try:
                num = float(num_str)
                if cat not in acumulador:
                    acumulador[cat] = {'suma': 0.0, 'count': 0}
                acumulador[cat]['suma'] += num
                acumulador[cat]['count'] += 1
            except ValueError:
                continue
                
    promedios = {}
    for cat, data in acumulador.items():
        promedio = data['suma'] / data['count'] if data['count'] > 0 else 0.0
        promedios[cat] = round(promedio, 2)
    return promedios

def analizar():
    print(f"Leyendo dataset desde: {DATASET_PATH}")
    datos = leer_csv(DATASET_PATH)
    print(f"Total de registros leídos: {len(datos)}")
    
    # Columnas específicas para el tema de reservaciones
    col_cat = "destino"
    col_num1 = "precio_noche"
    col_num2 = "dias_anticipacion"
    
    # 1. Valores únicos de la categórica
    set_unicos = valores_unicos(datos, col_cat)
    
    # 2. Conteo por categoría
    conteo = conteo_por_categoria(datos, col_cat)
    
    # 3. Categoría más frecuente
    cat_mas_freq = max(conteo.items(), key=lambda x: (x[1], x[0])) if conteo else ("", 0)
    
    # 4. Top 3 categorías (ordenadas por conteo descendente, desempate alfabético ascendente)
    top_3_sorted = sorted(conteo.items(), key=lambda x: (-x[1], x[0]))[:3]
    top_3_list = [{"valor": k, "conteo": v} for k, v in top_3_sorted]
    
    # 5. Estadísticas de columnas numéricas
    stats_num1 = estadisticas(datos, col_num1)
    stats_num2 = estadisticas(datos, col_num2)
    
    # 6. Promedio por categoría
    prom_por_cat = promedio_por_categoria(datos, col_cat, col_num1)
    
    # 7. Filtrado con percentil 90 en numerica_1
    filas_validas_num1 = list(filter(lambda f: f.get(col_num1, '').strip() != '', datos))
    valores_num1 = sorted(list(map(lambda f: float(f.get(col_num1)), filas_validas_num1)))
    
    n_val = len(valores_num1)
    umbral = 0.0
    if n_val > 0:
        idx_p90 = int(0.9 * n_val)
        if idx_p90 >= n_val:
            idx_p90 = n_val - 1
        umbral = valores_num1[idx_p90]
        
    # Filtrar registros que superan estrictamente el umbral usando filter + lambda
    cumplen = list(filter(lambda x: x > umbral, valores_num1))
    n_cumplen = len(cumplen)
    porcentaje = (n_cumplen / n_val * 100) if n_val > 0 else 0.0
    
    # Estructura de salida exacta solicitada
    resultado = {
        "archivo": "reservaciones-ruido.csv",
        "pareja": "Cruz González Erick Miguel y Escamilla Camarillo Ricardo",
        "seed": 6765,
        "valores_unicos_categorica": {
            "columna": col_cat,
            "n_valores_unicos": len(set_unicos),
            "valores": sorted(list(set_unicos))
        },
        "conteo_por_categoria": conteo,
        "categoria_mas_frecuente": {
            "valor": cat_mas_freq[0],
            "conteo": cat_mas_freq[1]
        },
        "top_3_categorias": top_3_list,
        "estadisticas_numerica_1": stats_num1,
        "estadisticas_numerica_2": stats_num2,
        "promedio_por_categoria": prom_por_cat,
        "filtrado": {
            "condicion": f"{col_num1} > {umbral}",
            "umbral_usado": round(umbral, 2),
            "n_registros_que_cumplen": n_cumplen,
            "porcentaje": round(porcentaje, 2)
        }
    }
    
    # Guardar resultados
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, mode='w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
        
    print(f"Análisis completado y guardado en: {OUTPUT_PATH}")

if __name__ == '__main__':
    analizar()