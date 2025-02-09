
Este archivo README es para explicar paso a paso el codigo de como , lo que facilita que los usuarios comprendan la funcionalidad y lautilicen  manera eficaz.

# Extractor de archivos 

Una herramienta de interfaz de línea de comandos (CLI) para extraer información de archivos PDF y XML. La herramienta puede identificar números de referencia en archivos PDF y extraer datos de facturas de archivos XML.

## Tabla de contenido
- [CLI de File Extractor](#file-extractor-cli)
- [Tabla de contenido](#table-of-contents)
- [Instalación](#installation)
- [Uso](#usage)
- [Opciones de CLI](#cli-options)
- [Comandos de ejemplo](#example-commands)
- [Cómo funciona](#how-it-works)
- [Clase FileExtractor](#fileextractor-class)
- [Requisitos](#requirements)
- [Dependencias](#dependencies)
- [Salida de ejemplo](#example-output)
- [Extracción de ID de PDF](#pdf-id-extraction)
- [Extracción de factura XML](#xml-invoice-extraction)
- [Licencia](#license)

## Instalación

1. **Crear un entorno virtual**:
```bash
python -m venv env
```

2. **Activar el entorno virtual**:
- En Windows:
```bash
.\env\Scripts\activate
```
- En macOS/Linux:
```bash
source env/bin/activate
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la CLI de File Extractor, use el siguiente comando:
```bash
python app.py -p "./data-storage/"
```
### Organizacion de datos
Para la ejecucion de este CLI, debe crear la siguientes extructura de carpetas:
- data-storage
 - pdf
  - xml

``data-storage``: Es la carpeta madre que contiene ``pdf`` y ``xml``
Para crear esta estructura de carpetas en **Windows** y **macOS**, puedes usar los siguientes comandos:

### **En Windows (en la Terminal o PowerShell):**
```bash
mkdir data-storage\data-storage\pdf data-storage\xml
```

### **En macOS (en la Terminal):**
```bash
mkdir -p data-storage/pdf data-storage/xml
```

Ambos comandos crearán la estructura de carpetas indicada en una sola línea.

### Nota
Deben de agregar los archivos correspondiente de a las facturas en formato ``pdf`` y ``xml`` en sus carpetas correspondientes.

Ademas debe crear dentro de la raiz de ``data-storage`` la carpeta ``csv`` que es la carpeta destino para la exportacion de las fracturas formato ``.csv``.

### Opciones de CLI

- `-p` o `--path`: especifica el directorio donde se almacenan los archivos PDF y XML. Este argumento es **obligatorio**.

### Comandos de ejemplo

1. **Extraer identificadores de PDF**:
- Ejecute la herramienta, seleccione la opción `1` y extraerá los números de referencia de los archivos PDF dentro del directorio especificado.

2. **Extraer facturas XML**:
- Ejecute la herramienta, seleccione la opción `2` y procesará los archivos XML, mostrando la información de la factura extraída en formato tabular.

3. **Exportar fractura a un archivo CSV**:
- Ejecute la herramieta, seleccion la opcion `3` y exportara el resultado en un archivo CSV.

4. **Salir del programa**:
- Seleccione la opción `4` para salir de la CLI.

## Cómo funciona

El programa tiene dos componentes principales:

1. **CLI principal (`app.py`)**:
- Proporciona un menú para que el usuario elija opciones para extraer datos de archivos PDF o XML.
- Utiliza la biblioteca `argparse` para manejar argumentos de línea de comandos.
- Utiliza la biblioteca `tabulate` para formatear y mostrar los datos extraídos.

2. **Clase FileExtractor (`extractor.py`)**:
- Maneja la lógica de extracción de archivos ``pdf`` y ``xml``.

3. **Metodo export_to_csv (`csv_exporter.py`)**:
- Maneja la lógica de expotar las facturas en formato ``.csv``.

### Clase FileExtractor

La clase `FileExtractor` contiene dos métodos:

1. **`extract_pdf_ids()`**:
- Busca patrones de "Número de referencia" en archivos PDF.
- Utiliza la biblioteca `PyPDF2` para leer archivos PDF y expresiones regulares para identificar números de referencia.
- Devuelve una lista de números de referencia extraídos.

2. **`extract_xml_invoices()`**:
- Analiza archivos XML para extraer información general y de proveedores de las facturas.
- Utiliza la biblioteca `xml.etree.ElementTree` para el análisis de XML.
- Devuelve una lista de datos de facturas extraídos, formateados como diccionarios.

### Requisitos

- Python 3.x
- Bibliotecas requeridas (instaladas mediante `requirements.txt`):
- `PyPDF2`: para lectura de PDF.
- `tabulate`: para salida formateada en la terminal.
- `xml.etree.ElementTree`: para análisis de XML (parte de la biblioteca estándar de Python).

## Dependencias

Las dependencias se administran en el archivo `requirements.txt`. Asegúrese de haber instalado todas las dependencias mediante:
```bash
pip install -r requirements.txt
```

## Ejemplo de salida

### Extracción de ID de PDF

```bash
--- CLI de File Extractor ---
1. Extraer ID de PDF
2. Extraer información de factura XML
3. Exportar facturas a CSV
4. Salir
Seleccione una opción (1-4): 1

ID de PDF extraídos (EJEMPLOS):
- 12345
- 67890
```

### Extracción de factura XML

```bash
--- CLI de File Extractor ---
1. Extraer ID de PDF
2. Extraer información de factura XML
3. Exportar facturas a CSV
3. Salir
Seleccione una opción (1-4): 2

Facturas procesadas:
+--------+--------------+
| Campo | Valor |
+--------+--------------+
| Ref | 0001 |
| Tipo | Venta |
| Fecha | 2024-01-01 |
| Moneda | USD |
| Proveedor | ABC Corp |
| CIF | B12345678 |
| Correo electrónico | abc@example.com |
+--------+--------------+
```
