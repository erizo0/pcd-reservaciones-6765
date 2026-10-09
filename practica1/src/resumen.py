def estadisticas_columna(valores_str):
    numeros = []
    for v in valores_str:
        try:
            numeros.append(float(v))
        except (ValueError, TypeError):
            continue    
    
    if not numeros:
        return {"n_validos": 0, "minimo": None, "maximo": None, "promedio": None}
    
    return {
        "n_validos": len(numeros),
        "minimo": min(numeros),
        "maximo": max(numeros),
        "promedio": sum(numeros) / len(numeros)
    }

def mas_frecuente(conteo):
    valor = max(conteo, key=conteo.get)
    return valor, conteo[valor]

def contar_frecuencias(lista):
    conteo = {}
    for valor in lista:
        if valor.strip() == "":    
            continue
        conteo[valor] = conteo.get(valor, 0) + 1
    return conteo

def contar_vacios(filas, encabezados):
    """Cuenta celdas vacías por columna.
    filas: lista de listas (cada sublista es una fila)
    encabezados: lista con los nombres de las columnas
    Retorna un diccionario {columna: n_vacios}."""
    vacios = {col: 0 for col in encabezados}
    for fila in filas:
        for i, valor in enumerate(fila):
            if valor.strip() == "":
                vacios[encabezados[i]] += 1
    return vacios
#Separamos cada fila de datos para que sean filas "individuales"
with open("C:/Users/Laptop/Documents/ESCOM/Tercer semestre/PCD_2026/PCD_Asterix/datos/reservaciones-ruido_100000.csv", "r") as archivo:
    lineas = archivo.readlines()

#Indicamos que la primer fila individual es de encabezados.    
encabezados = lineas[0].strip().split("|")
#print(f"Encabezados: {encabezados}")
#print(f"Número de columnas: {len(encabezados)}")

#Las demás filas son los datos "importantes"
datos = []
for linea in lineas[1:]:
    fila = linea.strip().split("|")
    datos.append(fila)
#print(f"Número de filas de datos: {len(datos)}")
#print(f"Primera fila: {datos[0]}")

#Imprimimos las primeras cinco filas
#print(" | ".join(encabezados))
#print("-" * 60)
#for fila in datos[:5]:
    #print(" | ".join(fila))

#Accedemos a las dos columnas que nos importan: destino(categórica) y precio_noche(númerica 1).    
idx_destino = encabezados.index("destino")
idx_precioNoche = encabezados.index("precio_noche")
#Extraemos los destinos (para despues hacer el conteo).
destinos = [fila[idx_destino] for fila in datos]

#Contamos la frecuencia de cada destino del archivo.
conteo = contar_frecuencias(destinos)
#print("Conteo por destino:")
#for prod, n in conteo.items():
    #print(f"  {prod}: {n}")
nombre, veces = mas_frecuente(conteo)
#print(f"\nMás frecuente: {nombre} ({veces} veces)")

#Extraemos los datos de precio_noche como strings para posteriormente convertirlos en float
precioNoche_str = [fila[idx_precioNoche] for fila in datos]
#Los convertimos en flotantes y a la vez obtenemos sus "estadísticas principales"
stats = estadisticas_columna(precioNoche_str)

#Contamos las celdas vacías
vacios = contar_vacios(datos, encabezados)
total_vacios = sum(vacios.values())
#print(f"Celdas vacías totales: {total_vacios}")
#print(f"Celdas vacías por columna:")
#for col, n in vacios.items():
    #print(f"  {col}: {n}")

#Hacemos el resumen de resultado.
with open("resumen.txt", "w", encoding="utf-8") as f:
    f.write("=== RESUMEN DEL DATASET ===\n")
    f.write("Archivo: reservaciones_ruido.csv\n")
    f.write("Pareja: Cruz González Erick Miguel y Escamilla Camarillo Ricardo\n")
    f.write("Seed: 6765\n\n")

    f.write("--- Dimensiones ---\n")
    f.write(f"Filas: {len(datos)}\n")
    f.write(f"Columnas: {len(encabezados)}\n")
    f.write(f"Nombres de columnas: {', '.join(encabezados)}\n\n")

    f.write(f"\n--- Primeras 5 filas ---\n")
    f.write("       |      ".join(encabezados) + "\n")
    for fila in datos[:5]:
        f.write("|".join(fila) + "\n")

    f.write(f"\n--- Columna categórica: destino ---\n")
    f.write(f"Valores únicos: {len(conteo)}\n")
    nombre, veces = mas_frecuente(conteo)
    f.write(f"Valor más frecuente: {nombre} ({veces} apariciones)\n")

    f.write(f"\n--- Columna numérica: precio_noche ---\n")
    f.write(f"Valores válidos (no vacíos): {stats['n_validos']}\n")
    f.write(f"Mínimo: {stats['minimo']}\n")
    f.write(f"Máximo: {stats['maximo']}\n")

    f.write(f"\n--- Calidad de datos ---\n")
    f.write(f"Celdas vacías totales: {total_vacios}\n")
    f.write(f"Celdas vacías por columna:\n")
    for col, n in vacios.items():
        f.write(f"  {col}: {n}\n")

print("Archivo resumen.txt generado.")
with open("resumen.txt", "r", encoding="utf-8") as f:
    print(f.read())