# Prueba técnica Lulo Bank - Data engineers

**Prueba técnica Lulo Bank - Data engineers**  
**Versión:** 2024-01-01

**Objetivo:**  
Realizar esta prueba utilizando Python (Utilizar buenas prácticas de codificación).

- Debe generar un repositorio en GitHub (o similar) donde esté toda la información requerida para ejecutar el proyecto y los resultados obtenidos.  
  *(Se va a tener en cuenta el README y los commits realizados al repositorio)*

- Puntos extra por pruebas unitarias a las funciones/clases desarrolladas.

## Actividades

1. Obtener información del siguiente API Rest`http://api.tvmaze.com` trayendo todas las series que se emitieron en enero del 2024.  
   
> *Ayuda:* para obtener las series emitidas el 1 de enero del 2024 se utilizó el siguiente llamado: `http://api.tvmaze.com/schedule/web?date=2024-01-01`

2. Almacenar los datos crudos (json)

3. Con base a los JSON obtenidos del API, generar DataFrame(s) (con la librería de su elección, ej. pandas, dask, polars) que conserve la integridad de los datos del JSON.

4. Realizar profiling a los datos y análisis.

    -  Se espera el resultado del profiling (PDF o HTML) y el análisis de éste.

5. De acuerdo al profiling del punto anterior, realizar operaciones de limpieza a los datos de los DataFrames en caso de ser necesario.

6. Almacenar Guardar los DataFrames en archivos Parquet (con compresión snappy).

7. Leer los archivos Parquet y almacenar la información en una base de datos (Sugerimos sqlite), en un modelo de datos definido por ustedes que respete la integridad de los datos.

8. A partir de los archivos Parquet o de la base de datos, realizar operaciones de agregación para obtener para todos los shows del mes:

   - **Runtime promedio (averageRuntime).**
   - **Conteo de shows de TV por género.**
   - **Listar los dominios únicos (web)** del sitio oficial de los shows.

## Entregables

Link a un repositorio público de GitHub que contenga:

- **README.md:** (pasos de instalación/ejecución como mínimo)
- **Carpeta src/:** con el proyecto de Python que desarrolló el ejercicio (notebooks o scripts .py).
- **Carpeta json/:** con los JSON obtenidos de las consultas al API.
- **Carpeta profiling/:** con el archivo del profiling y un archivo adicional del análisis de éste.
- **Carpeta data/:** con los archivos Parquet generados.
- **Carpeta db/:** con el archivo o export de la base de datos generada.
- **Carpeta model/:** con imagen del modelo de datos creado para almacenar información.
