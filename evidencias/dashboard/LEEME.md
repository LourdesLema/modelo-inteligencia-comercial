# Dashboard de inteligencia comercial — versión gerencial v02

## Abrir
Descomprime el ZIP y abre Dashboard_inteligencia_comercial_v02.html en Chrome o Safari. No requiere conexión, servidor ni instalación. El HTML contiene unos 16 MB de datos y cartografía; puede tardar unos segundos en abrir. Verificado en Chrome de escritorio; pendiente Safari y móvil.

## Lectura para gerencia
Comienza en Visión gerencial. Elige corte, criterio y capacidad. Las tarjetas distinguen clientes, porcentaje efectivo, suma estimada y valor observado posteriormente. Los tres mensajes describen concentración, comparación frente a H y composición geográfica. El control de estimación informa la diferencia monetaria observada menos estimada: no es MAE ni efecto de contacto.
La tabla de bandas muestra toda la cohorte. El mapa y los productos muestran únicamente la selección actual. La ficha consulta cualquier cliente elegible, sin alterar la selección. Desempeño predictivo conserva métricas y criterio de selección; Priorización comercial conserva comparación y exportación CSV del grupo completo.

## Decisiones ejecutadas en esta versión
A = posiciones 1 a floor(0,10 n); B = siguientes hasta floor(0,20 n); C = siguientes hasta floor(0,30 n); resto = posiciones posteriores. Son bandas excluyentes de un ranking existente, no clustering ni ABC por porcentaje de ventas. La usuaria aprobó esta ampliación; no supone aprobación expresa del profesor. No se modificaron modelos ni selección RF09.
País = único valor registrado en toda la historia de 180 días previa al corte; más de uno se presenta como Múltiples países. Los clientes no se duplican. No se utiliza la ubicación futura. No hay ciudad ni sector económico disponible. Mapa Natural Earth 1:110m: países pequeños pueden no estar representados; se enumeran los casos en la tabla. La tabla incluye todos. Correspondencias geográficas: EIRE→Ireland, USA→United States of America, RSA→South Africa, Czech Republic→Czechia. País no se añade como predictor.
Productos = compras válidas de mercancía en los 180 días previos, factura sin C, cantidad y precio positivos. La tabla muestra unidades e importes positivos y compradores distintos. Descuentos D no son productos. En la ficha, el neto por producto suma mercancía de ambos signos; no asigna descuentos D a productos. Las descripciones se toman del último registro histórico disponible por código en el corte. No se predice demanda por producto ni se recomiendan ventas cruzadas como hallazgo demostrado.
La ficha utiliza los cinco predictores de la matriz validada. La cifra futura observada se identifica como evaluación posterior; no estaba disponible al decidir. No se calcula rentabilidad, efecto causal ni capacidad óptima.

## Verificaciones
27 escenarios: tamaños, sumas, bandas excluyentes y distribución geográfica sin duplicar clientes. 8.764 perfiles: importes históricos contra matriz original, M/F y diversidad contra productos válidos. Se conservan las nueve métricas y las predicciones de v01. Chrome: navegación, 27 combinaciones de filtros, mapa ampliado, ficha válida y ficha inexistente. No se probó Safari ni móvil.

## Código y evidencia
- dashboard_v02/enriquecer.py: genera datos históricos adicionales a partir de la base v04 y la matriz v06; no entrena modelos.
- dashboard_v02/data.json: datos incrustados listos para reconstruir el HTML.
- dashboard_v02/template_v02.html: interfaz y lógica.
- dashboard_v02/build.py: combina plantilla y datos (biblioteca estándar de Python).
- dashboard_v02/verificar.py: verifica escenarios y perfiles.
- auditoria_enriquecimiento.json y bitacora_verificacion.json: evidencia de controles y reglas.
- world.geojson: cartografía Natural Earth, dominio público, fuente registrada en auditoría.
Para reconstruir: python3 dashboard_v02/build.py. Para verificar: python3 dashboard_v02/verificar.py.
Para recalcular el enriquecimiento se requieren pandas y los archivos originales ya entregados: upload/base_preprocesada_v04.csv.gz, upload/Evidencias_cortes_v06(1).zip y CSVs de base_dashboard. Los originales no se duplican en este paquete.

## Incorporación al documento
Actualizar menciones de Power BI por dashboard HTML/CSS/JavaScript. Describir las bandas y enriquecimientos como capa descriptiva de la propuesta, posterior al cierre de selección; no como nuevos predictores. Reservar la evaluación posterior para comparar desempeño y no usarla para redefinir RF09. El mapa no prueba viabilidad logística. La clasificación A/B/C no identifica la capacidad empresarial óptima. Antes de uso operativo se requiere capacidad real y evaluación prospectiva.
