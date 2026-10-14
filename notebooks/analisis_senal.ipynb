import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. PARÁMETROS DE MUESTREO (Teorema de Nyquist)
# ==========================================
fs = 8000  # Frecuencia de muestreo en Hz (8 kHz es estándar para voz/audio básico)
Ts = 1 / fs  # Período de muestreo en segundos
print(f"Frecuencia de muestreo (fs): {fs} Hz")
print(f"Período de muestreo (Ts): {Ts:.6f} segundos")

# ==========================================
# 2. SIMULACIÓN DE SEÑALES TEMPORALES (Transitorios)
# ==========================================
# Generamos un vector de tiempo de 0.2 segundos
t = np.linspace(0, 0.2, int(fs * 0.2))

# Simulación de un APLAUDO: Breve ráfaga de ruido de alta frecuencia con disipación rápida
aplauso = np.random.normal(0, 1, len(t)) * np.exp(-((t - 0.05)**2) / 0.0005)

# Simulación de un GOLPE: Impulso seco de menor frecuencia y mayor energía en bajas/medias
golpe = np.sin(2 * np.pi * 150 * t) * np.exp(-((t - 0.05)**2) / 0.001)

# ==========================================
# 3. REPRESENTACIÓN TEMPORAL (Gráficas)
# ==========================================
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, aplauso, color='tab:blue')
plt.title('Representación Temporal: Aplauso')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud Normalizada')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(t, golpe, color='tab:orange')
plt.title('Representación Temporal: Golpe')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud Normalizada')
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# 4. ANÁLISIS FRECUENCIAL (Transformada Rápida de Fourier - FFT)
# ==========================================
N = len(t)
# Aplicamos FFT y calculamos el espectro de magnitud
fft_aplauso = np.fft.rfft(aplauso)
fft_golpe = np.fft.rfft(golpe)
freqs = np.fft.rfftfreq(N, 1/fs)

mag_aplauso = np.abs(fft_aplauso) / N
mag_golpe = np.abs(fft_golpe) / N

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(freqs, mag_aplauso, color='tab:blue')
plt.title('Espectro en Frecuencia (FFT): Aplauso')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)
plt.xlim(0, 2000) # Enfocarnos en el rango audible relevante

plt.subplot(1, 2, 2)
plt.plot(freqs, mag_golpe, color='tab:orange')
plt.title('Espectro en Frecuencia (FFT): Golpe')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)
plt.xlim(0, 2000)

plt.tight_layout()
plt.show()
