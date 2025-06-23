import pandas as pd  # Paso 2
import plotly.express as px  # Paso 2
import streamlit as st  # Paso 2

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos  PASO 3

st.header('Analisis de venta de vehiculos')

hist_button = st.button(
    'Construir histograma de kilomettraje')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_lineplot = st.checkbox('Construir evolucion precio promedio por dia')

if build_lineplot:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Evolucion del precio promedio segun las condiciones del vehiculo')
    df = car_data.groupby(['date_posted', 'condition'])[
        'price'].mean().reset_index()

    # crear un grafico de barras
    fig = px.line(df, x='date_posted', y='price', color='condition',
                  title='Precio promedio de vehiculos segun dia de publicacion')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
