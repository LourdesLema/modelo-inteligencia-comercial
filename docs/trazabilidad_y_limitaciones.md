# Trazabilidad, decisiones y limitaciones

## Delimitación analítica

El proyecto utiliza Online Retail II y mantiene como unidad de análisis al cliente observado en una fecha de corte. Una compra válida requiere una factura distinta sin prefijo C que contenga mercancía con cantidad y precio positivos. Los descuentos D no cuentan como compras ni productos. El importe neto conserva los signos definidos en el procesamiento y las etiquetas se calculan dentro de ventanas temporales explícitas.

La elegibilidad utiliza exclusivamente información anterior al corte. Las historias abarcan 180 días y los objetivos 90 días. La referencia H corresponde a ventas netas de los 90 días previos. No se incorporan como predictores país, sector, margen, crédito ni indicadores de contacto.

## Entrenamiento y selección

Los cortes de marzo y junio de 2011 se usaron para validación temporal acumulativa. La selección de RF09 minimizó el promedio simple del MAE en esos dos cortes. La prueba de septiembre se reservó hasta cerrar la configuración. El protocolo final registra cinco predictores y los parámetros RF09: 400 árboles, profundidad máxima 8, una observación mínima por hoja y tres variables candidatas por división.

## Evidencia de prueba final

La ejecución de Colab registró Python 3.13.18, pandas 2.2.3, NumPy 2.1.3 y scikit-learn 1.6.1. Se reportaron 14.935 filas de entrenamiento, 2.768 de prueba y 33 controles aprobados. Las huellas registradas para los cortes v06 y validación RF coinciden con los insumos entregados; las huellas de las salidas registradas coinciden con los miembros del ZIP revisado.

Métricas de prueba (GBP salvo R²):

| Criterio | MAE | RMSE | R² |
|---|---:|---:|---:|
| Referencia H | 621,56 | 2.568,61 | 0,6097 |
| Regresión lineal | 587,02 | 2.719,69 | 0,5625 |
| Random Forest RF09 | 581,69 | 2.462,48 | 0,6413 |

Los resultados de priorización son sumas retrospectivas de ventas netas observadas para grupos de igual tamaño. No estiman ventas incrementales causadas por el contacto.

## Límites de interpretación

La matriz cliente-corte reconstruida independientemente reporta 65 controles aprobados, pero no ha sido cotejada celda por celda con la matriz v06 usada por los modelos. Por ello no se presenta como sustituto de la matriz original.

El estudio incluye dos validaciones y un corte de prueba. Los clientes pueden repetirse y sus historias pueden solaparse; la dependencia limita interpretaciones inferenciales. No se calcularon intervalos de confianza, pruebas de significancia ni sensibilidad a las repeticiones. La búsqueda RF cubrió 16 configuraciones y una semilla. Las ventanas de 180 y 90 días son decisiones operativas justificadas, no óptimos demostrados.

La evaluación comercial es retrospectiva; no demuestra causalidad, margen, rentabilidad ni capacidad empresarial óptima. Las capacidades de 10 %, 20 % y 30 % son escenarios hipotéticos.

## Nota de consistencia documental

El ZIP descargado de Colab contiene una `nota_interpretacion.txt` con una frase provisional que indica que el cotejo está pendiente. Esa frase no refleja la bitácora final: esta registra ejecución en Colab (`ejecucion_local: false`), versión scikit-learn 1.6.1 y huellas verificadas. Al citar la evidencia, prevalecen la bitácora y la coincidencia de huellas; en una futura versión del ZIP conviene reemplazar la nota obsoleta y regenerar su manifiesto.
