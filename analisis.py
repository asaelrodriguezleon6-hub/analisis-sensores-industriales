import pandas as pd
from pathlib import Path

# Rutas relativas del proyecto
archivo = Path("data/sensores_industriales.csv")
carpeta_resultados = Path("resultados")
carpeta_resultados.mkdir(exist_ok=True)

# Leer el CSV
df = pd.read_csv(archivo)

print("=== ANALISIS DE SENSORES INDUSTRIALES ===")

# 1. Cantidad de registros y sensores distintos
print(f"\nCantidad de registros: {len(df)}")
print(f"Sensores distintos: {df['id_sensor'].nunique()}")

# 2. Temperatura promedio de cada planta
promedios = df.groupby("planta")["temperatura_c"].mean()

print("\nTemperatura promedio por planta:")
print(promedios.round(2))

# 3. Temperatura maxima
indice_max = df["temperatura_c"].idxmax()
registro_max = df.loc[indice_max]

print("\nTemperatura maxima:")
print(f"Temperatura: {registro_max['temperatura_c']} °C")
print(f"Sensor: {registro_max['id_sensor']}")
print(f"Fecha: {registro_max['fecha_hora']}")

# 4. Lecturas mayores que 85 °C
alertas = df[df["temperatura_c"] > 85].copy()

print(f"\nLecturas mayores que 85 °C: {len(alertas)}")

# 5. Planta o plantas con mas alertas
conteo_alertas = alertas.groupby("planta").size()

if len(conteo_alertas) > 0:
    max_alertas = conteo_alertas.max()
    plantas_max = conteo_alertas[conteo_alertas == max_alertas]

    print("\nPlanta(s) con mas alertas:")
    for planta, cantidad in plantas_max.items():
        print(f"{planta}: {cantidad} alertas")
else:
    print("\nNo se encontraron alertas.")

# 6. Exportar las lecturas con alerta
salida = carpeta_resultados / "alertas.csv"
alertas.to_csv(salida, index=False)

print(f"\nArchivo generado: {salida}")
