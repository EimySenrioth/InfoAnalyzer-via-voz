# InfoAnalyzer-via-voz
Este proyecto es una herramienta diseñada para registrar, organizar y analizar datos.

El programa realiza un registro de 20 nombres, apellidos paternos y maternos a través de un sistema de reconocimiento de voz. Posteriormente, genera 10,000 tuplas de datos ficticios con información como ID, edad, peso y localidad. Además, se incluye una serie de funciones para analizar estos datos, tales como:

- Contar cuántos hermanos y homónimos hay en la base de datos.
- Generar histogramas de edades y pesos por localidad.
- Identificar la localidad con mayor porcentaje de menores, adultos o mayores, y más.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes librerías:

- `speech_recognition`
- `pyttsx3`
- `random`
- `matplotlib`

## Ejecución

Para ejecutar el programa, solo necesitas correr el script principal. Asegúrate de tener un micrófono conectado y configurado correctamente para que el sistema de reconocimiento de voz funcione.

python main.py

Durante la ejecución, el programa pedirá que registres nombres y apellidos. Luego, generará y mostrará los resultados de los análisis y los gráficos correspondientes.

## Resultados

1. Un listado de las tuplas generadas (ID, nombre, edad, peso, localidad).
2. El número total de hermanos y homónimos.
3. La localidad con mayor porcentaje de menores, adultos y mayores.
4. Los histogramas de edades y pesos, tanto a nivel general como por localidad.

## Gráficos
El programa genera histogramas de las edades y los pesos de las personas en la base de datos.

## Licencia
Este proyecto está bajo la Licencia MIT.
