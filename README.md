## PCD_Equipo2026

> **SEMILLA: 6765**

Integrantes: Cruz González Erick Miguel y Escamilla Camarillo Ricardo.
Tema: Reservaciones


---

## Observaciones del profesor

### Práctica 2 — evaluación (27-oct-2026)

**Calificación: 100 / 100**

Entregada el **25-oct-2026 a las 18:48**, dentro del plazo (la entrega cerraba el lun 26-oct), así que no lleva penalización por retraso.

**Práctica correcta.** Los doce criterios salieron completos: el JSON coincide campo por campo con la solución de referencia de su tema y su semilla —conteos exactos y promedios dentro de tolerancia— y el código cumple todos los requisitos. Nada que corregir.

**Lo que destaca:** **La mejor recuperación del grupo:** venían de 60 en P1 y esta práctica salió completa. Además separaron la mediana en su propia función (`calcular_mediana`) y usaron 7 `lambda`. De paso limpiaron los archivos basura de `practica2/` (commit *Limpia archivos basura de la practica 2*). Queda pendiente, sin efecto en la calificación, hacer esa misma limpieza en `practica3/` a `practica6/` y en `proyecto/`, donde siguen 15 archivos de prueba (`cccc.txt`, `ddd.txt`, `eeee.txt`, `fff.tx`, `ggg.txt`, `kkdkjdsjsdlsdk.txt`, `rreange.txt` y los que están dentro de cada `src/` y `resultados/`). Es el pendiente más viejo del repo.

**Desglose:**

| Criterio | Obtenido | Máximo |
|---|:---:|:---:|
| Nombres exactos de los entregables | 10 | 10 |
| Requisitos de Git (3+ commits, rama integrada) | 8 | 8 |
| Requisitos de código (5 funciones, `lambda`, `map`/`filter`) | 12 | 12 |
| Encabezado del JSON: archivo, pareja, seed | 6 | 6 |
| `valores_unicos_categorica` | 10 | 10 |
| `conteo_por_categoria` | 10 | 10 |
| `categoria_mas_frecuente` | 6 | 6 |
| `top_3_categorias` | 8 | 8 |
| `estadisticas_numerica_1` (con mediana) | 12 | 12 |
| `estadisticas_numerica_2` (con mediana) | 8 | 8 |
| `promedio_por_categoria` | 6 | 6 |
| `filtrado` (percentil 90) | 4 | 4 |
| **Total** | **100** | **100** |

### 13-oct-2026 — Correcciones de la Práctica 1

**Calificación de P1: 60 → 90 / 100.**

**Atendieron 6 de sus 7 observaciones** (commits del 9-oct). Lo que corrigieron:

1. Corrieron el script sobre `reservaciones-ruido_100000.csv`: ya reportan 103000 filas, y
   con eso se acomodaron solos casi todos los números del reporte.
2. Renombraron `p1.py` a `resumen.py`.
3. Renombraron `resumen_ejemplo.txt` a `resumen.txt`.
4. Crearon la rama `feauture/resumen`, trabajaron ahí las correcciones y quedó integrada en
   `main`. Con eso ya cumplen el requisito de rama. Solo una nota: el nombre quedó con un
   typo (`feauture` en vez de `feature`); no afecta la calificación, pero vale cuidarlo.
5. Agregaron el encabezado de sección `--- Dimensiones ---`.
6. El mínimo y máximo de `precio_noche` ya cuadran: -26954.3 y 325370.4.

De la observación sobre la columna categórica queda una diferencia (ustedes reportan 27
valores únicos y `Merida` con 13482; la referencia tiene 20 y 13761), pero **no se les
descuenta**: es exactamente lo que sale al contar los valores sin aplicar `.strip()`, y esa
lectura se dio por válida para todo el grupo porque el enunciado de P1 no decía cómo
normalizar. Ténganlo presente para P4 y P5, donde van a limpiar justo ese tipo de ruido.

**Pendiente aparte, que no afecta la calificación de P1:** en `practica2/` a `practica6/` y
en `proyecto/` siguen los archivos de prueba (`bbb.txt`, `cccc.txt`, `ddd.txt`, `eeee.txt`,
`fff.tx`, `ggg.txt`, `nummm.txt`, `kkdkjdsjsdlsdk.txt`, `rreange.txt` y los que están dentro
de cada `src/` y `resultados/`). Ya limpiaron los de `practica1/`; hagan lo mismo con el
resto antes de entregar P2, porque un repositorio limpio es parte de lo que se evalúa.

**Cómo se aplicó el reconocimiento.** Nueve de los diez equipos que tenían observaciones las atendieron entre el 8 y el 12 de octubre. A quien corrigió y tenía 90 o más, su práctica queda en **99**; a quien tenía menos de 90, en **90**. El 100 se reserva para quien entregó bien desde la primera vez. En la tabla de calificaciones del curso su celda aparece como `anterior/vigente`: el primer número es la entrega original y **el segundo es el que cuenta**.

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

### 26-sep-2026

**Estatus:** 6/6 de la estructura esperada.

¡Felicidades, ya cumplen toda la estructura! Agregaron `requirements.txt` y borraron la carpeta `src/` extra en la raíz. Todavía les quedan los archivos sueltos sin sentido dentro de cada `practicaN/` (`aaa.txt`…`fff.tx`) y `ggg.txt` en `proyecto/` — les recomendamos limpiarlos.

### 23-sep-2026

**Estatus:** 5/6 de la estructura esperada.

Sigue pendiente agregar `requirements.txt` en la raíz. También siguen ahí los archivos sueltos (`aaa.txt`...`fff.tx`) y la carpeta `src/` extra en la raíz — les recordamos limpiarlos cuando puedan.

📖 **Práctica 1 ya está disponible.** La encontrarán en `labs/P1/P1_setup_reconocimiento.md`, dentro del repositorio del profesor: https://github.com/ESCOMLCD/pcd202701/blob/main/labs/P1/P1_setup_reconocimiento.md — léanla completa antes de empezar a programar, ahí está todo lo que deben hacer, el formato exacto de `resumen.txt` y la fecha de entrega (mar 6-oct).

### 22-sep-2026

**Estatus:** 5/6 de la estructura esperada.

Les falta agregar `requirements.txt` en la raíz del repo. También notamos varios archivos sueltos sin contenido claro (`aaa.txt`, `bbb.txt`, ... `fff.tx`) dentro de cada carpeta `practicaN/`, y una carpeta `src/` extra en la raíz que no forma parte de la estructura esperada — les recomendamos limpiarlos. Ya les dejamos su dataset (`reservaciones-ruido_100.csv` y `_100000.csv`) dentro de `datos/`.
