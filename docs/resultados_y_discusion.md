# Resultados y discusión

## Validación temporal y selección del modelo

La selección se realizó mediante el promedio simple del error absoluto medio (MAE) obtenido en dos cortes de validación temporal. La referencia histórica H alcanzó un MAE de 343,26 GBP en marzo y 443,62 GBP en junio, con un promedio de 393,44 GBP. La regresión lineal registró 372,11 GBP y 406,35 GBP, respectivamente, con un promedio de 389,23 GBP. Random Forest RF09 obtuvo 369,98 GBP en marzo y 396,29 GBP en junio, con un promedio de 383,13 GBP. En consecuencia, RF09 presentó el menor MAE promedio y fue seleccionado para el reajuste final.

El desempeño no fue uniforme entre períodos: H obtuvo el menor MAE en marzo y RF09 lo obtuvo en junio. La selección refleja el criterio previamente establecido de igual ponderación de ambos cortes; no implica que RF09 haya sido superior en cada período.

## Desempeño en la prueba final

Después de cerrar la selección, los modelos se reajustaron con las observaciones de los cinco primeros cortes temporales. La evaluación reservada de septiembre de 2011 incluyó 2.768 clientes elegibles y las ventas netas de los 90 días posteriores. RF09 registró un MAE de 581,69 GBP, un RMSE de 2.462,48 GBP y un R² de 0,6413. La referencia H obtuvo 621,56 GBP, 2.568,61 GBP y 0,6097, respectivamente. La regresión lineal alcanzó 587,02 GBP, 2.719,69 GBP y 0,5625.

El MAE de RF09 fue 6,42 % menor que el de H en la prueba final. RF09 también presentó el menor RMSE y el mayor R² de las tres alternativas en ese corte. La regresión lineal, sin embargo, alcanzó un RMSE mayor que H pese a presentar un MAE menor. Esta combinación muestra que las métricas describen aspectos distintos del error y deben interpretarse conjuntamente. La diferencia observada en un único período reservado no demuestra estabilidad temporal ni transferencia a otras poblaciones.

## Priorización bajo escenarios hipotéticos de capacidad

La evaluación comercial ordenó los mismos 2.768 clientes por cada criterio y comparó las ventas netas futuras observadas en los grupos seleccionados. Con una capacidad hipotética del 10 %, se seleccionaron 276 clientes: H concentró 1.233.971,29 GBP, la regresión lineal 1.271.749,74 GBP y RF09 1.276.779,83 GBP. La concentración fue de 52,76 %, 54,38 % y 54,59 %, respectivamente. RF09 superó a H en 42.808,54 GBP.

Con una capacidad hipotética del 20 %, se seleccionaron 553 clientes. H concentró 1.503.317,74 GBP, la regresión lineal 1.556.300,76 GBP y RF09 1.557.419,58 GBP. Las proporciones respectivas fueron 64,28 %, 66,54 % y 66,59 %. La diferencia entre RF09 y H fue 54.101,84 GBP; la ventaja de RF09 respecto de la regresión lineal fue de 1.118,82 GBP.

Con una capacidad hipotética del 30 %, se seleccionaron 830 clientes. H concentró 1.699.441,03 GBP, la regresión lineal 1.754.139,31 GBP y RF09 1.751.042,26 GBP. La regresión lineal alcanzó una concentración de 75,00 %, frente a 74,87 % de RF09. Ambos criterios predictivos superaron a H en ventas netas observadas, aunque la mayor suma entre las alternativas predictivas dependió del tamaño del grupo seleccionado.

Estos resultados distinguen la precisión predictiva de la utilidad descriptiva para ordenar clientes. Un menor MAE no garantiza que un modelo seleccione el grupo con la mayor suma futura para toda capacidad. Las sumas y proporciones describen observaciones retrospectivas; no cuantifican ventas incrementales causadas por contactar a los clientes.

## Implicaciones y límites

Los resultados respaldan el uso del historial transaccional como insumo para estimar ventas netas y construir una priorización dentro de las condiciones evaluadas. La evidencia no establece una capacidad operativa óptima, no mide margen ni rentabilidad y no permite atribuir causalmente las ventas observadas a una acción comercial. La decisión de uso requeriría definir capacidad real, evaluar prospectivamente el desempeño y establecer indicadores de resultado compatibles con los objetivos de la organización.

La investigación incluye dos cortes de validación y un corte de prueba; las personas clientes pueden repetirse y las ventanas históricas pueden solaparse. Esta estructura genera dependencia entre observaciones y limita el alcance inferencial. No se calcularon intervalos de confianza, pruebas de significancia ni análisis de sensibilidad a las repeticiones. Las ventanas de 180 y 90 días son decisiones operativas justificadas, no parámetros óptimos demostrados.

Como referencia metodológica, Gadgil et al. (2023) estudian una alternativa de regresión apilada basada en metaaprendizaje para el valor de vida del cliente. Su objetivo y diseño no son idénticos a la estimación monetaria de ventas netas futuras de este proyecto; por ello, no corresponde comparar directamente los errores numéricos entre estudios. En este trabajo no se implementó un tercer modelo derivado de esa investigación.
