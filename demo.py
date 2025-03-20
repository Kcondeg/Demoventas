import pandas as pd
import streamlit as st

# Reemplaza 'SalidaFinalVentas.xlsx' con la ruta correcta a tu archivo
df = pd.read_excel('SalidaFinalVentas.xlsx')

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Reemplaza 'SalidaFinalVentas.xlsx' con la ruta correcta a tu archivo
df = pd.read_excel('SalidaFinalVentas.xlsx')

# Muestra las primeras filas del DataFrame para verificar que se cargó correctamente
print(df.head()) 

# Reemplaza 'SalidaFinalVentas.xlsx' con la ruta correcta a tu archivo
df = pd.read_excel('SalidaFinalVentas.xlsx')

# Muestra el DataFrame usando Streamlit
st.dataframe(df) 

# Agrupar las ventas por región y sumarlas
ventas_por_region = df.groupby('Region')['Ventas'].sum()

# Crear la gráfica de barras
st.write("Ventas por Región")
fig, ax = plt.subplots()
ventas_por_region.plot(kind='bar', ax=ax)
ax.set_xlabel("Región")
ax.set_ylabel("Ventas")
st.pyplot(fig)
