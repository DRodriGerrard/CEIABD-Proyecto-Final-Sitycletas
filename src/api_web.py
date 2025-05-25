from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np
import datetime
import os
import pandas as pd
import requests

# Cargar modelo
modelo = joblib.load(os.path.join(os.path.dirname(__file__), '..', 'models', 'modelo_lightgbm.pkl'))

# Iniciar aplicación
app = Flask(__name__)
app.secret_key = 'sitycleta'

@app.route('/', methods=['GET', 'POST'])
def home():
    # Leer estaciones disponibles
    df_preds = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'predicted', 'predicciones_lightgbm.csv'))
    estaciones = sorted(df_preds['Place number'].unique())

    if request.method == 'POST':
        fecha_str = request.form['fecha']
        place_number = int(request.form['estacion'])
        is_holiday = int(request.form['is_holiday'])
        clima = request.form['clima']

        fecha = datetime.datetime.fromisoformat(fecha_str)

        if fecha < datetime.datetime(2025, 5, 1):
            session['error'] = "Solo puedes predecir a partir del 1 de mayo de 2025."
            return redirect(url_for('home'))

        # Variables temporales
        hora = fecha.hour
        mes = fecha.month
        day_of_week = fecha.weekday()
        is_weekend = 1 if day_of_week >= 5 else 0
        week_of_year = int(fecha.strftime('%U'))

        # Simulación meteorológica según clima elegido
        if clima == 'soleado':
            temp_c = 0.42
            precip_mm = 0.0
            wind_speed_kmh = 0.35
        elif clima == 'nublado':
            temp_c = 0.40
            precip_mm = 0.01
            wind_speed_kmh = 0.4
        elif clima == 'lluvioso':
            temp_c = 0.38
            precip_mm = 0.05
            wind_speed_kmh = 0.45
        elif clima == 'viento fuerte':
            temp_c = 0.39
            precip_mm = 0.0
            wind_speed_kmh = 0.7
        else:
            temp_c = 0.41
            precip_mm = 0.005
            wind_speed_kmh = 0.42

        # Simulación de valores históricos
        free_bikes_lag1 = 5.0
        free_bikes_roll3 = 5.2

        # Input al modelo
        feature_names = [
            'hour_of_day', 'day_of_week', 'is_weekend', 'month', 'week_of_year', 'is_holiday',
            'temp_c', 'precip_mm', 'wind_speed_kmh', 'free_bikes_lag1', 'free_bikes_roll3'
        ]
        features = [
            hora, day_of_week, is_weekend, mes, week_of_year, is_holiday,
            temp_c, precip_mm, wind_speed_kmh, free_bikes_lag1, free_bikes_roll3
        ]

        df_input = pd.DataFrame([features], columns=feature_names)
        prediccion = int(round(modelo.predict(df_input)[0]))

        # Guardar resultados
        session['pred'] = prediccion
        session['fecha_mostrada'] = fecha.strftime('%A %d de %B de %Y a las %H:%M')
        session['estacion'] = place_number
        return redirect(url_for('home'))

    # GET
    pred = session.pop('pred', None)
    fecha_mostrada = session.pop('fecha_mostrada', None)
    estacion = session.pop('estacion', None)
    error = session.pop('error', None)

    return render_template('formulario.html',
                           prediccion=pred,
                           fecha_mostrada=fecha_mostrada,
                           estacion=estacion,
                           error=error,
                           estaciones=estaciones)

if __name__ == '__main__':
    app.run(debug=True)