import pandas as pd
import streamlit as st

# Reemplaza 'SalidaFinalVentas.xlsx' con la ruta correcta a tu archivo
df = pd.read_excel('SalidaFinalVentas.xlsx')

# Muestra el DataFrame usando Streamlit
st.dataframe(df) 
