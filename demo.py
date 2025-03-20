import streamlit as st
import pandas as pd

# Reemplaza 'SalidaFinal.xlsx' con la ruta correcta a tu archivo
df = pd.read_excel('SalidaFinal.xlsx')

# Imprime las primeras filas del DataFrame para verificar que se haya leído correctamente
# print(df.head()) 

st.dataframe(df)
