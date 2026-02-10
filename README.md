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

###  Imagen Original
![alt text][(https://github.com/jhoan636/vision_e_IA/blob/main/reto_3/imagenOriginal.png)

###  Regiones de interes
https://github.com/jhoan636/vision_e_IA/blob/main/reto_3/regionesDeInteres.png
![alt text](https://github.com/jhoan636/vision_e_IA/blob/main/reto_3/regionesDeInteres.png)

## Estado del reto

✔ Reto 1 completado
✔ Punto 3 completado
