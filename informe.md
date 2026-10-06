# Informe - Aplicación al caso de Big Data

## 5. Las 5 V aplicadas al proyecto

| V | Relación con el sistema | Ejemplo | Situación |
|---|---|---|---|
| Volumen | Se refiere a la cantidad de datos generados por los sensores. | El CSV contiene 100,000 mediciones. Si se agregan miles de sensores, la cantidad aumentará considerablemente. | Actual y futura ampliación |
| Velocidad | Se relaciona con la rapidez con la que se generan y reciben los datos. | Actualmente los sensores registran una medición por minuto. En la ampliación se recibirían mediciones cada segundo. | Actual y futura ampliación |
| Variedad | Se refiere a los diferentes tipos y formatos de información. | Actualmente el CSV contiene datos como temperatura y vibración. En el futuro también se agregarían fotografías y reportes de mantenimiento. | CSV actual y futura ampliación |
| Veracidad | Se relaciona con la calidad y confiabilidad de las mediciones. | Una lectura anormal podría deberse a un problema del sensor y tendría que validarse antes de tomar una decisión. | CSV actual |
| Valor | Consiste en obtener información útil de los datos. | Detectar temperaturas mayores que 85 °C permite identificar lecturas que requieren atención. | CSV actual |

## 6. Tipos de datos y procesamiento tradicional

El CSV de sensores es un dato estructurado porque tiene columnas y registros definidos.

Un mensaje JSON enviado por un sensor es semiestructurado porque utiliza claves y valores con una estructura flexible.

Una fotografía de una máquina es un dato no estructurado porque no se organiza en filas y columnas.

El texto libre de un reporte de mantenimiento es no estructurado porque su contenido no tiene una estructura fija.

Tener 100,000 registros no convierte automáticamente el archivo en Big Data. El archivo actual puede ser procesado en una computadora convencional utilizando Python y Pandas.

Al aumentar a miles de sensores y recibir datos cada segundo podrían aparecer problemas de almacenamiento, memoria, tiempo de procesamiento y velocidad de recepción. Además, fotografías y reportes aumentarían la variedad y el espacio necesario.

## 7. Batch y Streaming

El análisis realizado en este proyecto utiliza procesamiento batch, ya que trabaja sobre un archivo CSV que ya está almacenado y procesa un conjunto de datos existente.

Para emitir una alerta pocos segundos después de recibir una temperatura mayor que 85 °C utilizaría streaming. Esto permitiría procesar cada nueva lectura conforme llega y generar una alerta con baja demora.

Para generar un resumen al terminar el día utilizaría batch, porque no es necesario obtener el resultado inmediatamente. Se pueden reunir las mediciones del día y procesarlas juntas.

La elección depende del tiempo requerido: las alertas necesitan una respuesta rápida, mientras que un resumen diario puede esperar hasta que termine el periodo.

## 8. Lambda y Kappa

### Escenario A - Arquitectura Lambda

Utilizaría arquitectura Lambda porque se necesitan dos formas de procesamiento: una para analizar todo el historial por lotes y otra para atender rápidamente las mediciones nuevas.

Diagrama:

[ Sensores ]
     |
     +----> [ Procesamiento Batch ] ----> [ Resultados históricos ]
     |
     +----> [ Procesamiento en tiempo real ] ----> [ Resultados recientes ]
                                                        |
                                                        v
                                                [ Consulta final ]

### Escenario B - Arquitectura Kappa

Utilizaría arquitectura Kappa porque se busca mantener una sola lógica de procesamiento. Los eventos se almacenan y pueden volver a procesarse cuando sea necesario.

Diagrama:

[ Sensores ]
     |
     v
[ Flujo de eventos ]
     |
     v
[ Almacenamiento de eventos ]
     |
     v
[ Procesamiento ]
     |
     v
[ Resultados ]
     ^
     |
[ Reprocesamiento ]

Kappa evita mantener dos lógicas diferentes y permite volver a procesar los eventos almacenados.

## 9. Analítica descriptiva, predictiva y prescriptiva

### Descriptiva

El archivo contiene 100,000 registros correspondientes a 40 sensores.

La temperatura promedio obtenida para cada planta fue:

- Planta_1: 66.62 °C
- Planta_2: 66.53 °C
- Planta_3: 66.77 °C
- Planta_4: 66.67 °C

También se encontraron 6,954 lecturas con temperatura mayor que 85 °C. La Planta_3 presentó la mayor cantidad, con 1,777 alertas.

La temperatura máxima registrada fue de 104.99 °C, correspondiente al sensor S023 el 01/09/26 a las 22:23.

### Predictiva

Una pregunta predictiva sería:

¿Es posible anticipar qué máquinas presentan mayor probabilidad de tener temperaturas anormales en las siguientes horas?

Para investigarlo serían necesarios más datos, como historial de fallas, información de mantenimiento, carga de trabajo de las máquinas, condiciones ambientales, antigüedad del equipo y una relación entre cada sensor y la máquina que monitorea.

Una temperatura superior a 85 °C se considera una alerta para este ejercicio, pero por sí sola no demuestra que una máquina vaya a fallar.

### Prescriptiva

Si un modelo indicara un riesgo elevado, la empresa podría realizar una revisión preventiva de la máquina antes de que el problema aumente.

Antes de tomar una decisión revisaría las temperaturas recientes, vibración, historial de mantenimiento, fallas anteriores, condiciones de operación y confiabilidad del sensor.

Con esa información se podría decidir si continuar monitoreando, realizar mantenimiento preventivo o detener temporalmente el equipo para una inspección.
