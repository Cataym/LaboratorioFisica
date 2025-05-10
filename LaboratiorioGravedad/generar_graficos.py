import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo, usando la primera fila como nombres de columnas y la primera columna como índice
df = pd.read_excel("gravedadExcel.xlsx", header=0, index_col=0)

# Mostrar para verificar
print("DataFrame cargado correctamente:")
print(df.head())

# Limpiar nombres de columnas quitando 'cm' y manteniendo las longitudes como strings para mantener el formato original
df.columns = [col.strip() for col in df.columns]

# Transponer: ahora longitudes serán el índice
df_transposed = df.transpose()

# Calcular tiempo promedio por longitud
tiempos_promedio = df_transposed.mean(axis=1)
tiempos_cuadrado = tiempos_promedio ** 2

# Cálculos estadísticos: media, moda y mediana
media = tiempos_promedio.mean()
moda = tiempos_promedio.mode()[0]  # Moda puede ser múltiple, tomamos la primera
mediana = tiempos_promedio.median()

# Función para hacer el ajuste de mínimos cuadrados
def ajuste_lineal(x, y):
    # Calcula la pendiente (m) y la intersección (b) de la recta
    m, b = np.polyfit(x, y, 1)
    return m, b

# Obtener los valores de la regresión lineal para tiempo promedio
x_vals = np.array([int(i.replace("cm", "")) for i in df_transposed.index])  # Convertir longitudes a enteros
y_vals = tiempos_promedio.values

# Calcular la línea de regresión
m, b = ajuste_lineal(x_vals, y_vals)
linea_regresion = m * x_vals + b

# Gráfico 1: Tiempo promedio vs Longitud con ajuste de mínimos cuadrados
plt.figure(figsize=(12, 5))
plt.plot(df_transposed.index, tiempos_promedio, marker='o', color='b', label='Tiempo Promedio')
plt.plot(df_transposed.index, linea_regresion, color='r', linestyle='--', label=f'Ajuste Lineal: y = {m:.2f}x + {b:.2f}')
plt.title('Tiempo Promedio vs Longitud (Con Ajuste de Mínimos Cuadrados)', fontsize=16)
plt.xlabel('Longitud (cm)', fontsize=12)
plt.ylabel('Tiempo (ms)', fontsize=12)
plt.grid(True)
plt.legend(loc='upper left')


# Guardar y mostrar el gráfico
plt.subplots_adjust(right=0.75)  # Ajustar el espacio para el recuadro
plt.savefig('tiempo_vs_longitud_con_ajuste.png')
plt.show()

# Gráfico 2: Tiempo² promedio vs Longitud con ajuste de mínimos cuadrados
y_vals_cuadrado = tiempos_cuadrado.values
m2, b2 = ajuste_lineal(x_vals, y_vals_cuadrado)
linea_regresion_cuadrado = m2 * x_vals + b2

plt.figure(figsize=(12, 5))
plt.plot(df_transposed.index, tiempos_cuadrado, marker='o', color='orange', label='Tiempo² Promedio')
plt.plot(df_transposed.index, linea_regresion_cuadrado, color='r', linestyle='--', label=f'Ajuste Lineal: y = {m2:.2f}x + {b2:.2f}')
plt.title('Tiempo² Promedio vs Longitud (Con Ajuste de Mínimos Cuadrados)', fontsize=16)
plt.xlabel('Longitud (cm)', fontsize=12)
plt.ylabel('Tiempo² (ms²)', fontsize=12)
plt.grid(True)
plt.legend(loc='upper left')


# Guardar y mostrar el gráfico
plt.subplots_adjust(right=0.75)  # Ajustar el espacio para el recuadro
plt.savefig('tiempo_cuadrado_vs_longitud_con_ajuste.png')
plt.show()
