# Detector de Aplausos, Golpes y Eventos Acústicos

* **Integrantes:** Natalia Aguirre, Carolina Zuluaga
* **Asignatura:** Teoría de Señales (6to Semestre, Ingeniería en Sistemas y Telecomunicaciones)
* **Universidad:** Universidad de Manizales

## 1. Descripción Breve
Este proyecto estudia y procesa señales acústicas transitorias de corta duración (específicamente aplausos y golpes). El objetivo del sistema es adquirir, representar y analizar estas señales en los dominios del tiempo y de la frecuencia para lograr diferenciarlas entre sí y separarlas del ruido ambiental.

## 2. Estado Actual del Proyecto
* **Fase completada:** Planteamiento teórico, definición de la arquitectura de hardware (basada en microcontrolador ESP32 y sensor de audio analógico) y estructuración inicial del repositorio.
* **En desarrollo (Segunda Entrega):** Preparación de scripts en Python para la carga de audios de prueba, representación temporal, cálculo de la frecuencia de muestreo ($f_s$), y análisis espectral inicial mediante la Transformada Rápida de Fourier (FFT).
* **Pendiente:** Integración final del algoritmo en el hardware físico del ESP32 y calibración contra ruido ambiental.

## 3. Datos y Recursos
* **Dataset:** Se utilizará un conjunto de muestras de audio digital en formato `.wav` correspondientes a aplausos y golpes almacenadas en la carpeta `datos/`.
* **Hardware:** Microcontrolador ESP32 con sensor de micrófono analógico (módulo tipo MAX9814 con salida analógica).

## 4. Cómo Ejecutar
1. Clonar el repositorio localmente.
2. Instalar las dependencias necesarias de Python ejecutando en la terminal:
   ```bash
   pip install numpy scipy matplotlib
