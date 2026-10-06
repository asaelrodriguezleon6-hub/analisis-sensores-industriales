# Análisis de sensores industriales

## Objetivo

Analizar las mediciones de sensores instalados en cuatro plantas industriales para obtener información sobre temperatura y detectar lecturas que superen el umbral de alerta establecido.

## Datos

El proyecto utiliza sensores_industriales.csv, que contiene 100,000 mediciones simuladas.

Columnas del archivo:

- id_registro: identificador de la medición.
- fecha_hora: fecha y hora de la lectura.
- id_sensor: identificador del sensor.
- planta: planta donde está instalado.
- temperatura_c: temperatura en grados Celsius.
- vibracion_mm_s: vibración en milímetros por segundo.

Los datos utilizados en este proyecto son simulados.

## Estructura

text
analisis-sensores-industriales/
├── data/
│   └── sensores_industriales.csv
├── resultados/
│   └── alertas.csv
├── evidencias/
├── analisis.py
├── informe.md
├── README.md
├── requirements.txt
└── .gitignore


## Instalación

Crear un entorno virtual:

bash
python3 -m venv .venv


Activar el entorno:

bash
source .venv/bin/activate


Instalar las dependencias:

bash
pip install -r requirements.txt


## Ejecución

Ejecutar el análisis:

bash
python analisis.py


El programa calcula los resultados directamente a partir del CSV.

También genera el archivo:

resultados/alertas.csv

Este archivo conserva las columnas originales y contiene las lecturas con temperatura mayor que 85 °C.
