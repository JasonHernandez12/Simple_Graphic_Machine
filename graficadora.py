import matplotlib.pyplot as plt
import pandas as pd

file = input("Ingrese el nombre del archivo:\n")
df = pd.read_csv(file+'.csv')
print(df.head())

tiempo = df["Tiempo (s) Serie Nº 1"]
aceleracion = df["Aceleración (m/s²) Serie Nº 1"]

plt.figure()
plt.plot(tiempo, aceleracion, marker='o')

plt.xlabel("Tiempo (s)")
plt.ylabel("Aceleración (m/s^2)")
plt.title(f"Aceleración vs Tiempo para {file}")
plt.grid()

plt.show()