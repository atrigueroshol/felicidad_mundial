# ETL PYTHON

Este proyecto consiste en un analisis, limpieza, transformación y carga de datos. Se ha utilizado el siguiente dataset de la plataforma de kaggle https://www.kaggle.com/datasets/yadiraespinoza/world-happiness-2015-2024/data. Este conjunto de datos contiene información sobre la felicidad mundial recopilada anualmente entre 2015 y 2024. Los datos provienen del Informe Mundial de la Felicidad y proporcionan una visión integral de los factores que influyen en el bienestar de las naciones. Cada archivo representa un año específico y contiene métricas clave relacionadas con la felicidad y el desarrollo socioeconómico de diferentes países.

## Objetivo
Este proyecto automatiza el proceso completo de extracción, análisis, limpieza, transformación y unificación de múltiples archivos **CSV** en un único archivo **CSV** final. El objetivo es generar un conjunto de datos limpio y estructurado que sirva como base para dashboards, análisis exploratorio y modelos de machine learning.

## Ficheros
Los ficheros que se han utilizado como **input** son los siguientes:
 - world_happiness_2015.csv
 - world_happiness_2016.csv
 - world_happiness_2017.csv
 - world_happiness_2018.csv
 - world_happiness_2019.csv
 - world_happiness_2020.csv
 - world_happiness_2021.csv
 - world_happiness_2022.csv
 - world_happiness_2023.csv
 - world_happiness_2024.csv
 
El fichero resultante como **output** de todo el proceso de limpieza y transformación es el siguiente:
 - world_happiness_clean.csv

## Estructura del proyecto

 - **data**
	 - **raw**: Carpeta en la que se encuentran los ficheros csv raw.
	 - **clean**: Carpeta en la que se encuentra el fichero resultante de todo el proceso de limpieza y transformación.
 - **src**
	 - **exploration.ipynb**: Cuaderno de jupyter para explorar las variables del dataset e identificar cuales necesitan transformaciones.
	 - **extract.py**: Script de python que contiene las funciones de extracción de los datos.
	 - **load.py**: Script de python que contiene las funciones de carga de los datos.
	 - **transform.py**: Script de python que contiene las funciones de transformación de los datos.
	 - **main.py**: Progama principal que se encarga de ejecutar la extracción, limpieza, transformación y carga de los datos.
 - **requirements.txt**: Fichero que contiene las librerías necesarías para la ejecución del proyecto.


