from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import numpy as np
import datetime
import os
import pandas as pd

# Cargar modelo
modelo = joblib.load(os.path.join(os.path.dirname(__file__), '..', 'models', 'modelo_lightgbm.pkl'))

# Iniciar aplicación
app = Flask(__name__)
app.secret_key = 'sitycleta'

@app.route('/', methods=['GET', 'POST'])
def home():
    # Cargar lista de estaciones
    df_preds = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'data', 'predicted', 'predicciones_lightgbm.csv'))
    estaciones = sorted(df_preds['Place number'].unique())

    if request.method == 'POST':
        fecha_str = request.form['fecha']
        place_number = int(request.form['estacion'])
        fecha = datetime.datetime.fromisoformat(fecha_str)

        # Limitar fechas válidas: solo futuras a partir del 1 de mayo 2025
        fecha_minima = datetime.datetime(2025, 5, 1, 0, 0)
        if fecha < fecha_minima:
            session['error'] = "Solo puedes predecir fechas a partir del 1 de mayo de 2025."
            return redirect(url_for('home'))

        # Derivar variables
        hora = fecha.hour
        mes = fecha.month
        day_of_week = fecha.weekday()
        is_weekend = 1 if day_of_week >= 5 else 0
        week_of_year = int(fecha.strftime('%U'))
        is_holiday = 0

        # Valores promedio
        temp_c = 0.41
        precip_mm = 0.005
        wind_speed_kmh = 0.42
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

        # Guardar resultados en sesión
        session['pred'] = prediccion
        session['fecha_mostrada'] = fecha.strftime('%A %d de %B de %Y a las %H:%M')
        session['estacion'] = place_number
        return redirect(url_for('home'))

    # Mostrar resultados
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