## PCD_Equipo2026

> **SEMILLA: 6765**

Integrantes: Cruz González Erick Miguel y Escamilla Camarillo Ricardo.
Tema: Reservaciones


---

## Observaciones del profesor

### Práctica 1 — evaluación (8-oct-2026, 00:51 h)

**Calificación: 60 / 100**

Entregada el **6-oct-2026 a las 19:58**, dentro del plazo (la entrega cerraba el mar 6-oct), así que no lleva penalización por retraso.

**Criterios cubiertos al 100%:** Estructura del monorepo (6/6); Python puro (sin `csv` ni `pandas`, lectura con `open`); Encabezado: Archivo, Pareja, Seed; Primeras 5 filas (separadas con barra y espacios).

**Observaciones:**

1. Corrieron el script sobre el archivo de muestra `reservaciones-ruido_100.csv` en vez del dataset real `reservaciones-ruido_100000.csv`: reportan 103 filas y son 103000. **Esta es la causa de que casi todos los números del reporte no cuadren** (valores únicos, mínimos, máximos y celdas vacías). Vuelvan a correrlo apuntando al archivo `_100000` y el resto se corrige solo.
2. El script debe llamarse `resumen.py`; ustedes subieron `p1.py`.
3. La salida debe llamarse `resumen.txt`; ustedes subieron `resumen_ejemplo.txt`.
4. No cumplen el requisito de rama: se pedía crear una rama de trabajo (por ejemplo `feature/resumen`), trabajarla y mergearla a `main`. Su repositorio solo tiene `main`.
5. Faltan los encabezados de sección del formato pedido: `--- Dimensiones ---`. El contenido puede estar, pero las secciones deben ir delimitadas tal como las muestra el enunciado.
6. Los números de la columna categórica no cuadran: reportan 11 únicos y más frecuente `Puerto Vallarta` (17), y lo correcto es 20 únicos y `Merida` (13761).
7. El mínimo/máximo de `precio_noche` no coincide: reportan mín -2433.48 / máx 23353.4, y es mín -26954.3 / máx 325370.4.

**Desglose:**

| Criterio | Obtenido | Máximo |
|---|:---:|:---:|
| Estructura del monorepo (6/6) | 8 | 8 |
| Nombres exactos de los entregables | 0 | 10 |
| Requisitos de Git (3+ commits, rama mergeada) | 5 | 10 |
| Python puro (sin `csv` ni `pandas`, lectura con `open`) | 8 | 8 |
| Formato del `resumen.txt` (encabezado y secciones) | 7.6 | 9 |
| Encabezado: Archivo, Pareja, Seed | 10 | 10 |
| Dimensiones: filas, columnas, nombres | 6 | 10 |
| Primeras 5 filas (separadas con barra y espacios) | 5 | 5 |
| Columna categórica (nombre, únicos, más frecuente) | 5 | 12 |
| Columna numérica_1 (nombre, válidos, mín, máx) | 5 | 13 |
| Calidad de datos (celdas vacías) | 0 | 5 |
| **Total** | **60** | **100** |
### 22-sep-2026

**Estatus:** 5/6 de la estructura esperada.

Les falta agregar `requirements.txt` en la raíz del repo. También notamos varios archivos sueltos sin contenido claro (`aaa.txt`, `bbb.txt`, ... `fff.tx`) dentro de cada carpeta `practicaN/`, y una carpeta `src/` extra en la raíz que no forma parte de la estructura esperada — les recomendamos limpiarlos. Ya les dejamos su dataset (`reservaciones-ruido_100.csv` y `_100000.csv`) dentro de `datos/`.

### 23-sep-2026

**Estatus:** 5/6 de la estructura esperada.

Sigue pendiente agregar `requirements.txt` en la raíz. También siguen ahí los archivos sueltos (`aaa.txt`...`fff.tx`) y la carpeta `src/` extra en la raíz — les recordamos limpiarlos cuando puedan.

📖 **Práctica 1 ya está disponible.** La encontrarán en `labs/P1/P1_setup_reconocimiento.md`, dentro del repositorio del profesor: https://github.com/ESCOMLCD/pcd202701/blob/main/labs/P1/P1_setup_reconocimiento.md — léanla completa antes de empezar a programar, ahí está todo lo que deben hacer, el formato exacto de `resumen.txt` y la fecha de entrega (mar 6-oct).

### 26-sep-2026

**Estatus:** 6/6 de la estructura esperada.

¡Felicidades, ya cumplen toda la estructura! Agregaron `requirements.txt` y borraron la carpeta `src/` extra en la raíz. Todavía les quedan los archivos sueltos sin sentido dentro de cada `practicaN/` (`aaa.txt`…`fff.tx`) y `ggg.txt` en `proyecto/` — les recomendamos limpiarlos.
