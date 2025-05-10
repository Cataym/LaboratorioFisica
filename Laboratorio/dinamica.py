import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
fuerza = np.array([196, 294, 343, 441, 490, 588])  # Fuerza externa (N)
aceleracion = np.array([37.25, 82.14, 104.87, 155.122, 205.84, 273.82])  # Aceleración (m/s^2)

# Ajuste lineal usando mínimos cuadrados
coeficientes = np.polyfit(fuerza, aceleracion, 1)
pendiente, intercepto = coeficientes
ajuste = np.poly1d(coeficientes)

# Datos para línea ajustada
fuerza_fit = np.linspace(min(fuerza), max(fuerza), 100)
aceleracion_fit = ajuste(fuerza_fit)

# Mostrar ecuación ajustada
print(f"Ajuste lineal: aceleración = {pendiente:.4f} * fuerza + {intercepto:.4f}")

# Graficar
plt.figure(figsize=(8, 5))
plt.scatter(fuerza, aceleracion, color='blue', label='Datos experimentales')
plt.plot(fuerza_fit, aceleracion_fit, color='red', label='Ajuste lineal')

plt.title('Fuerza externa vs Aceleración')
plt.xlabel('Fuerza externa (N)')
plt.ylabel('Aceleración (m/s²)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar ticks exactos en los ejes X e Y
plt.xticks(fuerza)
plt.yticks(aceleracion)

# Guardar imagen
plt.savefig("grafico_fuerza_vs_aceleracion.png", dpi=300)

plt.show()
