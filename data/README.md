# Adquisición y Origen de los Datos

Las señales analizadas en esta etapa del proyecto corresponden a eventos acústicos transitorios de corta duración (específicamente **aplausos** y **golpes**).

## Procedencia y Parámetros
* **Origen de las muestras:** Para la presente entrega y validación inicial de los algoritmos de análisis, las señales han sido generadas de forma sintética mediante funciones matemáticas en Python (`NumPy`), modelando la envolvente exponencial y el comportamiento espectral característico de cada impacto.
* **Frecuencia de Muestreo ($f_s$):** $8000 \text{ Hz}$ (8 kHz), garantizando el cumplimiento del Teorema de Muestreo de Nyquist para el rango de audio relevante.
* **Período de Muestreo ($T_s$):** $T_s = \frac{1}{f_s} = 0.000125 \text{ s}$ ($125 \ \mu\text{s}$).
* **Unidades:** Amplitud normalizada en el rango $[-1, 1]$ en función del tiempo transcurrido en segundos ($s$).

*Nota: En las etapas posteriores, este repositorio albergará las grabaciones reales en formato `.wav` capturadas directamente mediante el sensor analógico conectado al ADC del microcontrolador ESP32.*
