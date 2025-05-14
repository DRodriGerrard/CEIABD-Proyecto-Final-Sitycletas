
# Predicción de disponibilidad de bicicletas Sitycleta (Las Palmas de Gran Canaria)

Proyecto de Trabajo Fin de CEIABD (Curso Especializado en Inteligencia Artificial y Big Data).  
Alumno: David Rodríguez Gerrard
Año académico: 2024-2025  

---

## 🎯 Descripción

Este proyecto desarrolla un modelo predictivo para estimar la disponibilidad de bicicletas públicas en las estaciones de la red **Sitycleta (SAGULPA)** de Las Palmas de Gran Canaria.

La solución se basa en técnicas de análisis de series temporales y aprendizaje automático, utilizando como variable objetivo el número de bicicletas disponibles (`Free bikes`) y enriqueciendo el dataset con información adicional:

- Variables de calendario (hora, día de la semana, mes...)
- Festivos oficiales de Canarias
- Variables meteorológicas (temperatura, lluvia, viento)

El objetivo principal es aportar una herramienta que ayude a mejorar la gestión y experiencia de los usuarios del sistema de movilidad urbana sostenible.

---

## 📂 Estructura del proyecto

```
/project_name/
│
├── data/
│   ├── raw/                   # Dataset original de SAGULPA
│   ├── external/              # Datasets externos (clima, eventos, festivos...)
│   ├── processed/             # Dataset final ya limpio y enriquecido
│
├── notebooks/
│   ├── 01_data_exploration.ipynb     # Análisis exploratorio inicial
│   ├── 02_data_cleaning.ipynb        # Limpieza y transformación de datos
│   ├── 03_model_training.ipynb       # Entrenamiento de modelos
│   ├── 04_evaluation_results.ipynb   # Comparativa y resultados
│
├── models/
│   ├── prophet_model.pkl
│   ├── xgboost_model.pkl
│   ├── lightgbm_model.pkl
│
├── src/
│   ├── data_loader.py          # Código para cargar datasets
│   ├── feature_engineering.py  # Enriquecimiento y creación de variables
│   ├── model_utils.py          # Funciones de entrenamiento y evaluación
│
├── docs/
│   ├── memoria_proyecto.pdf    # Documento final
│   ├── presentacion.pptx       # Presentación para la defensa
│   ├── images/                 # Gráficas, capturas de resultados
│
├── requirements.txt            # Librerías necesarias
├── README.md                   # Descripción del proyecto
---

## 📋 Dataset utilizado

- Datos reales de disponibilidad de bicicletas (SAGULPA) desde diciembre 2023 hasta abril 2025 obtenidos en Datos Abiertos: https://www.sagulpa.com/datos-abiertos.
- Datos meteorológicos descargados desde la librería de Meteostat: https://meteostat.net/es/
- Festivos oficiales obtenidos con la librería python-holidays para Canarias: https://pypi.org/project/holidays/

*Nota: El dataset completo no se publica por licencia y tamaño, pero se incluye una muestra para fines educativos.*

                       +----------------+
                       | Dataset SAGULPA|
                       | (datos base)   |
                       +--------+-------+
                                |
                                |
       +------------------------+-----------------------+
       |                        |                       |
       |                        |                       |
+--------------+        +----------------+      +------------------+
| Datos clima  |        | Datos calendario |     | Datos eventos (opcional) |
| (Meteostat)  |        | (festivos, fines |     | (maratones, ferias...)   |
|              |        | de semana...)    |     |  *No aplicado            |
+--------------+        +----------------+      +------------------+
       |                        |                       |
       +------------------------+-----------------------+
                                |
                                V
                    +----------------------------+
                    |  Dataset enriquecido final |
                    |  (para entrenamiento)      |
                    +----------------------------+
---

## 🛠️ Tecnologías utilizadas (actualizándose)

- Python 3.11
- Pandas, Numpy
- Scikit-learn
- Prophet
- LightGBM / XGBoost
- Meteostat API
- Python-holidays
- Matplotlib, Seaborn

---

## 🚀 Estructura del pipeline (puede variar)

1. Carga y exploración del dataset
2. Enriquecimiento con calendario y clima
3. Preprocesamiento de datos
4. Entrenamiento y evaluación de modelos
5. Comparación de resultados y visualización

---

## 🎨 Resultados esperados

- Gráficas de predicción vs valores reales
- Métricas de error (MAE, RMSE) para distintos modelos
- Análisis de comportamiento estacional y patrones de uso

---

## 📄 Informe del proyecto

El informe académico completo se encuentra en `/docs/memoria_proyecto.pdf` (pendiente).

---

## 📜 Licencia

Este proyecto se entrega exclusivamente como Trabajo Fin de Curso y no tiene fines comerciales.

---

## 🙏 Agradecimientos

- SAGULPA (Sitycleta Las Palmas)
- Meteostat API
- Comunidad open-source
