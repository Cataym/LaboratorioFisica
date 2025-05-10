# Importamos las librerías necesarias
import pandas as pd               # pandas se usa para manejar y analizar datos en forma de tablas (como Excel)
import matplotlib.pyplot as plt   # matplotlib se usa para crear gráficos
import statistics                 # statistics tiene funciones como media, mediana y moda

# Ruta del archivo Excel que contiene nuestros datos
archivo_excel = './Informe_Piano.xlsx'  # Asegurate de tener el archivo en la misma carpeta o poné la ruta completa

# Leemos el archivo Excel desde la fila 3 (índice 2), porque las primeras dos filas no tienen los datos importantes
df = pd.read_excel(archivo_excel, header=2)

# Renombramos algunas columnas para que los nombres sean más fáciles de usar en el código
df.rename(columns={
    'Tiempo (s)': 'Tiempo',               # Cambiamos "Tiempo (s)" a "Tiempo"
    'Instrumento?': 'Instrumento',        # Cambiamos "Instrumento?" a "Instrumento"
    'Edad (años)': 'Edad'                # Cambiamos "Edad (años)" a "Edad"
}, inplace=True)

# Mostramos las primeras filas de los datos para verificar que todo esté bien
print(df.head())

# ===============================
# CALCULAMOS MEDIA, MEDIANA Y MODA
# ===============================

# Filtramos los valores no nulos para evitar errores en los cálculos
tiempos = df['Tiempo'].dropna()

# Calculamos los valores estadísticos
media = round(tiempos.mean(), 2)                         # Media: promedio
mediana = round(tiempos.median(), 2)                     # Mediana: valor del medio
moda = round(tiempos.mode().iloc[0], 2) if not tiempos.mode().empty else None  # Moda: el valor que más se repite

# Mostramos los valores en consola
print(f"Media: {media} segundos")
print(f"Mediana: {mediana} segundos")
print(f"Moda: {moda} segundos")

# ===============================
# 1. HISTOGRAMA DEL TIEMPO + LÍNEAS DE MEDIA, MEDIANA Y MODA
# ===============================

plt.figure(figsize=(10, 6))

# Histograma con los tiempos
plt.hist(tiempos, bins=20, color='purple', edgecolor='black', alpha=0.7)

# Título y etiquetas
plt.title('Histograma del Tiempo Total')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia')
plt.grid(True)

# Dibujamos líneas verticales para media, mediana y moda
plt.axvline(media, color='blue', linestyle='dashed', linewidth=2, label=f'Media: {media}s')
plt.axvline(mediana, color='green', linestyle='dashed', linewidth=2, label=f'Mediana: {mediana}s')
plt.axvline(moda, color='red', linestyle='dashed', linewidth=2, label=f'Moda: {moda}s')

# Mostramos la leyenda (cuadro con etiquetas)
plt.legend()

# Ajustamos todo y mostramos
plt.tight_layout()
plt.show()
