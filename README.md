## Modelo de inteligencia comercial para la estimación de ventas futuras y priorización de clientes mediante analítica predictiva

Repositorio académico del proyecto de titulación de la Maestría en Inteligencia de Negocios y Ciencia de Datos de la Universidad de Las Américas (UDLA).

**Autora:** Lourdes Lorena Lema Zambrano  
**Diseño:** estudio retrospectivo con datos públicos  
**Moneda de análisis:** libra esterlina (GBP)

## Propósito y alcance

Este repositorio documenta las decisiones metodológicas, los cuadernos de análisis, la evidencia agregada y los límites de interpretación del estudio. Se evalúa si el comportamiento histórico de clientes permite estimar sus ventas netas en un horizonte posterior y ordenar clientes para escenarios hipotéticos de atención comercial.

El análisis no estima el efecto causal de contactar clientes ni la rentabilidad de una intervención. No incorpora crédito, morosidad, visitas, margen ni sector económico. Los escenarios de capacidad son ilustrativos y no representan una capacidad empresarial verificada.

## Fuente de datos

Se utiliza *Online Retail II*, publicado por Chen (2012) en UCI Machine Learning Repository, DOI: [10.24432/C5CG6D](https://doi.org/10.24432/C5CG6D). La base contiene transacciones minoristas del Reino Unido expresadas en GBP. El archivo original y las matrices transaccionales o cliente-corte no se redistribuyen en este repositorio. La preparación requiere obtener el libro original desde UCI y los pasos posteriores requieren generar localmente los insumos descritos en `docs/reproducibilidad.md`.

## Diseño analítico

La unidad de análisis es un cliente en una fecha de corte. La elegibilidad se establece exclusivamente con información anterior al corte. Se emplean una ventana histórica de 180 días y un objetivo de ventas netas para los 90 días siguientes. Se consideran seis cortes entre junio de 2010 y septiembre de 2011; marzo y junio de 2011 se utilizan para validación y septiembre de 2011 se reserva para la evaluación final.

Los cinco predictores son recencia desde la última compra válida, frecuencia de compras válidas, diversidad de productos, importe histórico neto y valor promedio neto por compra. La referencia histórica H corresponde a las ventas netas de los 90 días previos y se utiliza como criterio comparativo, no como predictor.

Se comparan regresión lineal y Random Forest Regressor. La selección de configuración se basa en el promedio simple del MAE de los dos cortes de validación; se seleccionó RF09. La prueba final no se utilizó para elegir modelos ni ajustar hiperparámetros. MAE es la métrica principal; RMSE y R² son complementarias.

## Resultados finales documentados

En la prueba final, con 2.768 clientes elegibles, RF09 obtuvo MAE de 581,69 GBP, RMSE de 2.462,48 GBP y R² de 0,6413. La referencia H obtuvo MAE de 621,56 GBP, RMSE de 2.568,61 GBP y R² de 0,6097. La regresión lineal obtuvo MAE de 587,02 GBP, RMSE de 2.719,69 GBP y R² de 0,5625. Los datos sin redondear se conservan en `evidencias/metricas_prueba_colab.csv`.

La evaluación descriptiva de priorización compara grupos de igual tamaño. RF09 alcanzó mayor concentración de ventas futuras netas observadas que H en los escenarios del 10 % y 20 %; regresión lineal lo hizo en el 30 %. Las diferencias observadas no representan ventas adicionales causadas por una intervención. Véanse los valores y las reglas de cálculo en `evidencias/priorizacion_prueba_agregada.csv` y la discusión en `docs/resultados_y_discusion.md`.

## Contenido

- `notebooks/`: siete cuadernos secuenciales de preparación, análisis, validación y prueba final. Las copias para el repositorio no contienen resultados guardados en celdas.
- `docs/`: metodología, trazabilidad, límites, resultados y guía de reproducción.
- `evidencias/`: métricas, resultados agregados y controles de la prueba final, sin filas de clientes.
- `scripts/`: código de figuras y cálculo de priorización, cuya ejecución requiere los archivos intermedios locales especificados en la guía.
- `evidencias/dashboard/`: plantilla y código de construcción del prototipo HTML. No se incluye el archivo de datos de perfiles; por tanto, el dashboard completo no puede reconstruirse desde un clon limpio sin los insumos locales correspondientes.

## Reproducción y entorno

Los notebooks se prepararon para Google Colab y requieren entradas externas que no se distribuyen aquí. El procedimiento, el orden de ejecución, las entradas esperadas y los límites de reproducción se detallan en `docs/reproducibilidad.md`. La ejecución final auditada en Colab registró Python 3.13.18, pandas 2.2.3, NumPy 2.1.3 y scikit-learn 1.6.1. Las versiones principales se encuentran en `requirements.txt`.

La bitácora de la prueba final registra 33 controles aprobados y huellas coincidentes para los archivos v06 de cortes y validación utilizados. La matriz cliente-corte reconstruida independientemente conserva 65 controles aprobados, pero aún no se ha cotejado celda por celda con la matriz v06; no debe tratarse como sustituto de la matriz utilizada por los modelos.

## Protección de datos y alcance de publicación

El repositorio omite libros de datos y archivos de filas cliente-corte, predicciones individuales, exportaciones de selección y el JSON del dashboard. El archivo `.gitignore` excluye formatos y nombres asociados con estos insumos. Antes de publicar, debe comprobarse que no se agreguen por accidente archivos locales con registros individuales.

La licencia de reutilización permanece pendiente de decisión de la autora. La ausencia de una licencia no concede permisos adicionales de reutilización. La cita bibliográfica del proyecto puede consultarse en `CITATION.cff`.

## Referencias

Chen, D. (2012). *Online Retail II* [Conjunto de datos]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CG6D

Gadgil, K., Gill, S. S., & Abdelmoniem, A. M. (2023). A meta-learning based stacked regression approach for customer lifetime value prediction. *Journal of Economy and Technology, 1*, 197–207. https://doi.org/10.1016/j.ject.2023.09.001
