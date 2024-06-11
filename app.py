import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Crear gráfico")    
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Histograma') # crear un botón
dis_button = st.button("Dispersión") # crear un boton

if hist_button: # al hacer clic en el botón 
    # escribir un mensaje
    st.write('Creación de histograma con {car_data} para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dis_button: 
    # crear gráfico de dispersión
    st.write('Creación de gráfico de dispersión con {car_data} para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig1 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)