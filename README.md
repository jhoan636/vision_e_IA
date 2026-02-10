# Reto 1 – Visión por Computador

## Resultados obtenidos

* Se obtuvieron valores consistentes de mínimo, máximo, media y desviación estándar tanto en el procesamiento manual como en NumPy.
* La matriz reconstruida pudo visualizarse correctamente como una imagen en escala de grises.
* La imagen mostró una distribución aleatoria de intensidades, coherente con los valores generados.

---

## Comparación de tiempos

* El cálculo manual permitió entender el proceso estadístico, pero resultó menos eficiente para grandes volúmenes de datos.
* NumPy mostró un mejor desempeño en el cálculo de estadísticas gracias a sus operaciones vectorizadas.
* El tiempo total en Google Colab se vio influenciado por la lectura de archivos desde Google Drive.

---

## Conclusiones

* Pudimos convertir números al azar en una representación matricial de valores numéricos.
* El uso de NumPy es altamente recomendable para el procesamiento de grandes cantidades de datos debido a su eficiencia.
* La lectura y escritura de archivos grandes puede impactar significativamente el tiempo total de ejecución.
* La visualización permitió validar visualmente la correcta reconstrucción de la matriz original.
* Este ejercicio refuerza la base conceptual de la visión por computador: los píxeles son datos numéricos organizados en matrices.

---

## Evidencias

### Local
![alt text](https://github.com/jhoan636/vision_e_IA/blob/main/reto_1/local.png)

### Remoto
![alt text](https://github.com/jhoan636/vision_e_IA/blob/main/reto_1/remoto.png)

## Matriz de grises
![alt text](https://github.com/jhoan636/vision_e_IA/blob/main/reto_1/matriz_grises.png)

---

# Punto 3 – Análisis de Imagen a Color

##  Resultados obtenidos

* Las regiones homogéneas presentaron **baja desviación estándar**, indicando uniformidad de color.
* La región no homogénea mostró **valores altos de desviación estándar**, reflejando variaciones significativas de color.
* Las medias de los canales permitieron identificar claramente el color dominante en cada ROI.
* Se confirmó que OpenCV maneja los canales en el orden **BGR**, lo cual es fundamental para interpretar correctamente los resultados.

---

##  Conclusiones

* Una imagen a color puede analizarse cuantitativamente mediante el estudio de sus canales B, G y R.
* La media de los canales permite identificar el color predominante en una región.
* La desviación estándar es un indicador clave para determinar la **homogeneidad cromática**.
* OpenCV es una herramienta eficiente para el análisis de imágenes y la manipulación de regiones de interés.
* Este ejercicio refuerza conceptos fundamentales de visión por computador relacionados con el análisis de color y segmentación básica.

---

##  Evidencias
### Media de los canales 
Rojo:         B=51.35, G=52.61, R=193.02
Verde:        B=50.57, G=128.18, R=89.10
Azul:         B=220.72, G=158.99, R=15.55
Amarillo:     B=28.58, G=147.04, R=191.50
Verde_agua:   B=183.20, G=175.33, R=112.32
No_homogeneo: B=159.03, G=145.78, R=144.61

### Desviacion estandar de los canales
Rojo:         B=37.26, G=26.21, R=15.72
Verde:        B=30.93, G=21.05, R=17.86
Azul:         B=66.34, G=46.05, R=32.31
Amarillo:     B=48.91, G=56.86, R=80.90
Verde_agua:   B=43.48, G=28.34, R=29.51
No_homogeneo: B=72.02, G=62.12, R=67.26

###  Imagen Original
![alt text](https://github.com/jhoan636/vision_e_IA/blob/main/reto_3/imagenOriginal.png)

###  Regiones de interes
![alt text](https://github.com/jhoan636/vision_e_IA/blob/main/reto_3/regionesDeInteres.png)

## Estado del reto

✔ Reto 1 completado
✔ Punto 3 completado
