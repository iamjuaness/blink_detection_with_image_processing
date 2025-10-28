# Blink Detection with Image Processing

Este proyecto se centra en la detección de parpadeo utilizando procesamiento de imágenes y técnicas de visión por computador. Está pensado para ser usado principalmente en sistemas de monitoreo de fatiga y alerta en conductores mediante el análisis automático del estado de los ojos (abiertos/cerrados).

## Características principales

- Procesamiento de imágenes utilizando OpenCV y algoritmos clásicos.
- Extracción de características con métodos como SIFT y ORB.
- Análisis de líneas y círculos para evaluar la región ocular en imágenes.
- Estadísticas de resultados exportadas para evaluación y comparación.
- Carpeta organizada para imágenes de prueba, scripts de procesamiento y resultados.

## Estructura de carpetas
- images/ # Imágenes a procesar
- processing/ # Scripts y notebooks de procesamiento
- results/ # Resultados y estadísticas obtenidas

## Requisitos

- Python 3.8+
- OpenCV
- Numpy
- Matplotlib
- Scikit-image

Instalación recomendada:
```
pip install -r requirements.txt
```

## Ejecución

1. Coloca tus imágenes de prueba en la carpeta `images/`.
2. Ejecuta el notebook `processing/statistics_feature_extraction.ipynb` para extraer características y realizar la detección de parpadeo.
3. Los resultados se guardan automáticamente en la carpeta `results/`.

## Contribuir

¡Se aceptan contribuciones! Puedes crear issues o pull requests con sugerencias, correcciones o nuevas funcionalidades.

## Licencia

Este proyecto está bajo la licencia MIT.

---
