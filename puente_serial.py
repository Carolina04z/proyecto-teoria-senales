from datetime import datetime
import os
import csv
import random
import matplotlib.pyplot as plt
import serial

# CONFIGURACIÓN: Cambia 'COM3' por el puerto serial de tu ESP32
PUERTO = "COM3"
BAUDIOS = 115200
ARCHIVO_CSV = "historial_eventos.csv"
CARPETA_RESULTADOS = "resultados"

os.makedirs(CARPETA_RESULTADOS, exist_ok=True)

# Crear cabecera incluyendo la columna de Frecuencia en Hz
if not os.path.exists(ARCHIVO_CSV) or os.path.getsize(ARCHIVO_CSV) == 0:
  with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Fecha_Hora", "Tipo_Evento", "Frecuencia_Hz", "Valor", "Ruta_Imagen"])

print("--- MODO SIMULACIÓN: Captura de Frecuencias en Hz activa ---")

while True:
  import time
  time.sleep(5)  # Simula un evento cada 5 segundos
  
  tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
  # Simulamos diferentes tipos de sonidos con sus respectivas frecuencias en Hz
  if random.choice([True, False]):
    tipo_evento = "Aplauso"
    frecuencia_hz = f"{random.randint(2000, 3800)} Hz"  # Frecuencia típica alta de aplausos
  else:
    tipo_evento = "Golpe / Impacto"
    frecuencia_hz = f"{random.randint(350, 950)} Hz"    # Frecuencia típica baja de golpes
    
  valor_prueba = f"Umbral Superado (Amplitud alta)"

  nombre_archivo_img = f"grafica_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
  ruta_imagen = os.path.join(CARPETA_RESULTADOS, nombre_archivo_img)

  # Generar la gráfica individual con su respectiva frecuencia en el título
  plt.figure(figsize=(8, 4))
  plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [200, 600, 1200, 3900, 1800, 800, 400, 200, 100, 50], marker="o", color="#ff4b4b", linewidth=2)
  plt.title(f"Análisis FFT - {tipo_evento} | Frecuencia: {frecuencia_hz}")
  plt.xlabel("Muestras de Tiempo (n)")
  plt.ylabel("Magnitud")
  plt.grid(True)
  
  plt.savefig(ruta_imagen)
  plt.close()

  # Guardar en el CSV con la frecuencia exacta
  with open(ARCHIVO_CSV, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([tiempo_actual, tipo_evento, frecuencia_hz, valor_prueba, ruta_imagen])
    
  print(f"[{tiempo_actual}] -> Evento: {tipo_evento} | Frecuencia registrada: {frecuencia_hz}")