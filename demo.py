import pandas as pd
import streamlit as st

# Reemplaza 'SalidaFinalVentas.xlsx' con la ruta correcta a tu archivo
df = pd.read_excel('SalidaFinalVentas.xlsx')

# Muestra el DataFrame usando Streamlit
st.dataframe(df) 
# Agrupar las ventas por región y sumarlas
ventas_por_region = df.groupby('Region')['Ventas'].sum()

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.bar(ventas_por_region.index, ventas_por_region.values)
plt.xlabel('Región')
plt.ylabel('Ventas Totales')
plt.title('Ventas por Región')
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mejor legibilidad
plt.tight_layout()  # Ajustar el diseño para evitar que las etiquetas se superpongan

# Mostrar la gráfica usando Streamlit
st.pyplot(plt)
