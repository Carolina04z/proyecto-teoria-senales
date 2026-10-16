# Interpretación de Resultados y Gráficas

A continuación se detalla la caracterización e interpretación técnica de los resultados obtenidos tras el procesamiento de las señales en el dominio del tiempo y de la frecuencia.

## 1. Representación en el Dominio del Tiempo
* **Comportamiento Transitorio:** Tanto el aplauso como el golpe presentan un pico de amplitud drástico y repentino en el instante $t = 0.05 \text{ s}$, seguido de una disipación exponencial rápida de la energía en pocos milisegundos.
* **Diferencia de Forma de Onda:** 
  * El **aplauso** muestra variaciones de amplitud de alta frecuencia debido a la fricción y turbulencia del aire entre las manos.
  * El **golpe** presenta una oscilación más suave y sostenida producida por la resonancia mecánica de la superficie impactada.

## 2. Análisis en el Dominio de la Frecuencia (FFT)
* **Aislación Espectral del Aplauso:** Muestra una distribución energética de banda ancha (*broadband*), extendiéndose con presencia significativa en frecuencias medias y altas (por encima de $1000 \text{ Hz}$).
* **Aislación Espectral del Golpe:** La energía se concentra principalmente en un espectro de baja frecuencia ($< 500 \text{ Hz}$), correspondiente a la frecuencia fundamental de resonancia del objeto golpeado.

## Conclusión del Análisis
Esta diferencia en la distribución espectral obtenida mediante la Transformada Rápida de Fourier (FFT) confirma que el criterio de clasificación basado en la frecuencia permitirá discriminar con alta precisión entre un aplauso y un golpe en el software final.
