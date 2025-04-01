# Lulo Bank Technical Test 🏦

## 📚 Tabla de Contenido
- [🔍 Descripción del Proyecto](#descripción-del-proyecto)
    - [🎯 Objetivos](#objetivos)
    - [🚀 Beneficios](#beneficios)

- [🗂️ Estructura del Proyecto](#estructura-del-proyecto)
- [🎨 Patrones Aplicados](#patrones-aplicados)
- [🚀 Despliegue de la Aplicación](#despliegue-de-la-aplicación)
- [📖 Resumen de Endpoints y Cómo Usarlos](#resumen-de-endpoints-y-cómo-usarlos)
    - [Endpoints de Extract](#endpoints-de-extract)
    - [Endpoints de Transform](#endpoints-de-transform)
    - [Endpoint de Load](#endpoint-de-load)
- [✅ Ejecutar Tests Unitarios](#ejecutar-tests-unitarios)



## Descripción del Proyecto
El proyecto **Lulo Bank Tech Test** es una aplicación que demuestra cómo construir una solución técnica robusta usando Python y FastAPI. Su enfoque principal es implementar procesos ETL (Extracción, Transformación y Carga) y microservicios para resolver desafíos empresariales.

### Objetivos
- **Evaluación Técnica:** Mostrar buenas prácticas (SOLID, patrones de diseño).
- **Integración:** Combinar extracción de datos (API TVMaze), transformación y carga en bases de datos (Postgres/MySQL).
- **Microservicios:** Construir una arquitectura modular y escalable con FastAPI.
- **Calidad y Testeo:** Asegurar un código mantenible y bien probado.

### Beneficios
- **Mantenibilidad:** Código modular y fácil de actualizar.
- **Escalabilidad:** Arquitectura preparada para crecer según las necesidades.
- **Flexibilidad:** Soporte para múltiples formatos y motores de lectura/escritura (CSV, JSON, Parquet, YAML, HTML, PDF) tanto en local como en AWS S3.
¿Te parece bien este formato o deseas ajustar algún detalle?

## Estructura del Proyecto

El proyecto está organizado de manera modular para facilitar su mantenimiento y escalabilidad. A continuación, se muestra un resumen de la estructura principal:

- **pyproject.toml** 📦
  Configuración del proyecto y sus dependencias.

- **docker-compose.yml** 🐳
  Define los servicios y contenedores (Postgres, pgAdmin, migraciones y la aplicación).

- **app/** 💻
  Carpeta principal con el código fuente:
  - **main.py** 🚀
    Punto de entrada de la aplicación FastAPI.
  - **setup.py** ⚙️
    Inicialización y configuración de la aplicación.
  - **container.py** 🔗
    Configuración global e inyección de dependencias.
  - **file_io/** 📂
    Gestión de lectura y escritura de archivos en distintos formatos (CSV, JSON, Parquet, YAML, HTML, PDF) y en diferentes orígenes (local y AWS S3).
  - **db_connections/** 🔌
    Conexiones a bases de datos (Postgres y MySQL) usando SQLAlchemy y patrones de repositorio/Unit of Work.
  - **extract/** 🔍
    Funcionalidades para la extracción de datos (por ejemplo, desde el API TVMaze).
  - **transform/** 🔄
    Módulo para transformar y normalizar la información.
  - **load/** 📤
    Carga de datos en la base de datos siguiendo patrones ETL.

- **tests/** ✅
  Pruebas unitarias e integración que abarcan desde la gestión de archivos hasta conexiones y operaciones con bases de datos y servicios de extracción/carga.

Cada módulo se apoya en principios de inyección de dependencias y patrones de diseño, asegurando un código desacoplado, testable y fácil de extender.

## Patrones Aplicados

- **Inyección de Dependencias** 🔄
  Separa la creación y gestión de objetos mediante contenedores, lo que facilita el desacoplamiento y la testabilidad del sistema.

- **Domain-Driven Design (DDD)** 🏛️
  Enfoca la arquitectura en el dominio del negocio, creando un modelo claro que refleja la lógica y reglas empresariales.

- **Arquitectura Hexagonal** ⛏️
  Organiza la aplicación en capas (núcleo y adaptadores), permitiendo que la lógica central sea independiente de detalles técnicos y de infraestructura.

- **Principios SOLID** 📐
  Conjunto de prácticas (SRP, OCP, LSP, ISP, DIP) que promueven un código modular, mantenible y flexible.

- **Patrones de Diseño** 🔍
  Soluciones reutilizables a problemas comunes que ayudan a estructurar y organizar el código de forma clara y escalable.

## Despliegue de la Aplicación

Sigue estos pasos para desplegar la aplicación:

1. **Clonar el repositorio** 📥
Clona el proyecto desde GitHub:
```bash
git clone https://github.com/julian-icruz/tech_test_lulo_bank
cd tu_repositorio
```

2. **Configurar variables de entorno** 🔧
   Crea un archivo `.env` en la raíz del proyecto y define las variables de entorno necesarias (por ejemplo, para Postgres, pgAdmin, etc.):

> Copiar tal y como esta para facilidad de ejecucion.

```env
############################
# AWS credentials and configuration
############################
AWS_ACCESS_KEY_ID="ASIA2"
AWS_SECRET_ACCESS_KEY="ZFBr5mto7J"
AWS_DEFAULT_REGION="us-east-1"
AWS_SESSION_TOKEN="IQo="

############################
# PGADMIN CONFIG
############################
PGADMIN_DEFAULT_EMAIL=admin@lulo.com
PGADMIN_DEFAULT_PASSWORD=Temporal123*
PGADMIN_SERVER_JSON_FILE=/servers.json

############################
# POSTGRES CONFIG
############################
POSTGRES_USER=lulo_bank_user
POSTGRES_PASSWORD=lulo_bank_password
POSTGRES_DB=lulo_bank_db
POSTGRES_PORT=5432
POSTGRES_HOST=postgres_lulo_bank
POSTGRES_LOCAL_DATA_PATH=/postgres_data
```

3. **Activar el entorno virtual con Poetry** 🐍
   Asegúrate de tener instalado Poetry. Luego, instala las dependencias y activa el entorno:

> Asegurarse de tener una version de python correcta tal y como lo dice el .toml
```bash
poetry install
poetry .venv/bin/activate
```

4. **Ejecutar Docker Compose** 🐳
   Levanta los contenedores (Postgres, pgAdmin, migraciones y la aplicación) con:
```bash
docker-compose up --build
```

5. **Verificar el despliegue** 👀
   - Abre tu navegador en [http://localhost:8080](http://localhost:8080) para ver la aplicación FastAPI en acción.
   - Accede a [http://localhost](http://localhost) para abrir pgAdmin y administrar la base de datos.

   Las credenciales para acceder a la base de datos se enceuntrna en las vairables de entorno y serian estas:

```env

############################
# PGADMIN CONFIG / Para entrar al PGADMIN
############################
PGADMIN_DEFAULT_EMAIL=admin@lulo.com
PGADMIN_DEFAULT_PASSWORD=Temporal123*


############################
# POSTGRES CONFIG / Para entrar a la BD solo pedira la password
############################
POSTGRES_PASSWORD=lulo_bank_password

```
¡Listo! Con estos pasos tendrás la aplicación corriendo y podrás empezar a interactuar con ella.


## Resumen de Endpoints y Cómo Usarlos

A continuación se describen los principales endpoints de la API junto con ejemplos de comandos `curl` para probar cada uno.

## Endpoints de Extract

### 1. Obtener Horario de TV
**Endpoint:**
`GET /v1/extract/schedule?date=YYYY-MM-DD`

**Descripción:**
Este endpoint obtiene el horario de TV para la fecha especificada.

**Ejemplo:**
```bash
curl --location 'http://localhost:8080/v1/extract/schedule?date=2024-01-01'
```

### 2. Almacenar Horario de TV
**Endpoint:**
`POST /v1/extract/storage?date=YYYY-MM-DD`

**Descripción:**
Extrae el horario de TV para la fecha indicada y almacena cada entrada en un archivo.
La configuración del escritor (source, file_format y engine) se envía en el cuerpo de la solicitud.

**Ejemplo:**
```bash
curl --location 'http://localhost:8080/v1/extract/storage?date=2024-01-01' \
--header 'Content-Type: application/json' \
--data '{
  "source": "local",
  "file_format": "json",
  "engine": "json"
}'
```

---


## Endpoints de Transform

### 3. Generar Reporte de Perfilado
**Endpoint:**
`POST /v1/transform/profiling`

**Descripción:**
Procesa archivos de entrada para generar un reporte de perfilado en formato HTML.
El cuerpo de la solicitud debe incluir la configuración del lector, la configuración del escritor y la configuración de rutas de entrada y salida.

**Ejemplo:**
```bash
curl --location 'http://localhost:8080/v1/transform/profiling' \
--header 'Content-Type: application/json' \
--data '{
  "reader_config": {
    "source": "local",
    "file_format": "json",
    "engine": "pandas"
  },
  "writer_config": {
    "source": "local",
    "file_format": "html",
    "engine": "html"
  },
  "path_io": {
    "input_path": "json/date=2024-01-01/",
    "output_path": "profiling/date=2024-01-01/"
  }
}'
```

### 4. Limpieza de Datos
**Endpoint:**
`POST /v1/transform/cleaning`

**Descripción:**
Lee archivos de datos crudos, los limpia y procesa, y escribe los datos procesados en el formato indicado (por ejemplo, Parquet).
El cuerpo de la solicitud debe incluir la configuración del lector, la configuración del escritor y las rutas de entrada y salida.

**Ejemplo:**
```bash
curl --location 'http://localhost:8080/v1/transform/cleaning' \
--header 'Content-Type: application/json' \
--data '{
  "reader_config": {
    "source": "local",
    "file_format": "json",
    "engine": "pandas"
  },
  "writer_config": {
    "source": "local",
    "file_format": "parquet",
    "engine": "pandas"
  },
  "path_io": {
    "input_path": "json/date=2024-01-01/",
    "output_path": "data/date=2024-01-01/"
  }
}'
```

---

## Endpoint de Load

### 5. Cargar Datos a la Base de Datos
**Endpoint:**
`POST /v1/load/to_db?database=postgres`

**Descripción:**
Carga los datos procesados desde archivos en la base de datos especificada.
El cuerpo de la solicitud debe incluir la configuración del lector y la ruta de entrada de los archivos.

> Este solo se puede ejecutar una unica vez para cargar los datos luego tira error por lo que los datos yasse cargaron y se repetirian los IDs, si se quiere ejecutar nuevamete desde el PGADMIN se puede hacer

```sql
DELETE FROM <table_name>;
```

> recuerda la dependencia entre tablas para su eliminacion

**Ejemplo:**
```bash
curl --location 'http://localhost:8080/v1/load/to_db?database=postgres' \
--header 'Content-Type: application/json' \
--data '{
    "reader_config": {
        "source": "local",
        "file_format": "parquet",
        "engine": "pandas"
    },
    "path_io": {
        "input_path": "data/date=2024-01-01/"
    }
}'
```

---

Utiliza estos comandos para interactuar y probar los endpoints de la API. Ajusta las fechas y la configuración según sea necesario.

> Una vez se ejecutan los endpoints se generan los folders que se pedian en el challenge.

## Ejecutar Tests Unitarios

Para correr los tests unitarios, abre una terminal y ejecuta:

~~~bash
poetry run pytest
~~~
