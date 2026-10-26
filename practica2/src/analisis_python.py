import csv
import json
import os

# Definir las rutas de los archivos relativas al proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.normpath(os.path.join(BASE_DIR, '../../datos/reservaciones-ruido_100000.csv'))
OUTPUT_PATH = os.path.normpath(os.path.join(BASE_DIR, '../resultados/analisis_python.json'))

def analizar_reservaciones():
    print(f"Leyendo dataset desde: {DATASET_PATH}")
    
    if not os.path.exists(DATASET_PATH):
        print("Error: No se encontró el archivo CSV en la ruta especificada.")
        return

    total_registros = 0
    destinos_stats = {}
    
    with open(DATASET_PATH, mode='r', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        
        for fila in lector:
            total_registros += 1
            
            # Extraer y limpiar datos de las columnas
            destino = fila.get('destino', '').strip()
            
            try:
                precio = float(fila.get('precio_noche', 0))
            except ValueError:
                precio = 0.0
                
            try:
                dias_ant = int(fila.get('dias_anticipacion', 0))
            except ValueError:
                dias_ant = 0
                
            # Acumular valores por cada destino (agrupación nativa con diccionarios)
            if destino not in destinos_stats:
                destinos_stats[destino] = {
                    'cantidad_reservaciones': 0,
                    'suma_precio': 0.0,
                    'suma_dias_anticipacion': 0
                }
            
            destinos_stats[destino]['cantidad_reservaciones'] += 1
            destinos_stats[destino]['suma_precio'] += precio
            destinos_stats[destino]['suma_dias_anticipacion'] += dias_ant

    # Calcular promedios y estructurar los resultados finales
    resultado_final = {
        'total_registros': total_registros,
        'destinos': {}
    }

    for destino, datos in destinos_stats.items():
        cantidad = datos['cantidad_reservaciones']
        promedio_precio = datos['suma_precio'] / cantidad if cantidad > 0 else 0
        promedio_dias = datos['suma_dias_anticipacion'] / cantidad if cantidad > 0 else 0
        
        resultado_final['destinos'][destino] = {
            'total_reservaciones': cantidad,
            'precio_promedio_noche': round(promedio_precio, 2),
            'dias_anticipacion_promedio': round(promedio_dias, 2)
        }

    # Asegurarnos de que el directorio de resultados exista
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # Escribir los resultados en formato JSON
    with open(OUTPUT_PATH, mode='w', encoding='utf-8') as archivo_json:
        json.dump(resultado_final, archivo_json, indent=4, ensure_ascii=False)

    print(f"Análisis completado con éxito. Resultados guardados en: {OUTPUT_PATH}")

if __name__ == '__main__':
    analizar_reservaciones()