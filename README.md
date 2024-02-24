# Propuesta de un Sistema de Mapeo para una Superficie Subacuática

Este repositorio contiene el código desarrollado como parte de la tesis "Propuesta de un sistema de mapeo para una superficie subacuática". El objetivo principal del sistema es realizar un mapeo tridimensional de la superficie subacuática utilizando un enfoque basado en triangulación láser.

## Descripción del Código

El código está implementado en Python y se divide en varias etapas que abarcan desde la captura de imágenes hasta la generación de una nube de puntos 3D representativa de la superficie subacuática. A continuación, se presenta un resumen de las principales funcionalidades:

1. **Generación de Línea de Referencia:**
   - Se implementó un código para generar una línea en la mitad de la pantalla, visible para la cámara. Este paso es crucial para alinear un láser en la posición correcta, utilizando el método de triangulación láser.

2. **Captura de Imágenes en Movimiento:**
   - Cuando una estructura con cámara y láser se movía, el sistema enviaba un mensaje de texto para capturar una imagen en el instante en que se detenía.
   - Se realizaba un recorte de la zona de interés para optimizar el uso computacional.

3. **Procesamiento de Imágenes:**
   - Se seleccionaron los canales de color R y G, ya que contenían la información más relevante.
   - Se aplicó un proceso de segmentación utilizando el método de Otsu.
   - Se adelgazó la imagen para simplificar la representación de la superficie.

4. **Triangulación Láser:**
   - Se detectaron las coordenadas (x, y) donde la imagen era blanca, aplicando el algoritmo de triangulación láser.

5. **Generación de Nube de Puntos 3D:**
   - Con las coordenadas (x, y) obtenidas de todas las imágenes capturadas, se generó un archivo que representa una nube de puntos en 3D.
   - Esta nube de puntos proporciona una visualización tridimensional del objeto subacuático mapeado.

## Instrucciones de Uso

1. Clona el repositorio: `git clone https://github.com/tu_usuario/tu-repositorio.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el código principal: `python main.py`

## Contribuciones y Problemas

Si deseas contribuir al proyecto o encuentras algún problema, por favor, abre un problema o envía una solicitud de extracción. Tu colaboración es bienvenida.

## Autor

Jorge Luis Leiton

## Licencia

Impetus Indomitus, Universidad del Valle.
