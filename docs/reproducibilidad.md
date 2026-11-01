# Reproducibilidad y secuencia de trabajo

## Secuencia de cuadernos

| Orden | Archivo | Propósito | Entrada local principal | Alcance de ejecución |
|---|---|---|---|---|
| 1 | `01_preparacion_y_limpieza_v03.ipynb` | Integrar las hojas originales, identificar solapamiento y aplicar exclusiones v03 | Libro `online_retail_II 2.xlsx` descargado desde UCI | Puede iniciarse desde el libro original; genera archivos comprimidos de datos y auditoría que no deben publicarse en el repositorio |
| 2 | `02_preprocesamiento_v04.ipynb` | Asignar tipos y comprobar conservación de registros | `base_limpia_v03.csv.gz` | Requiere la salida local del paso 1 o el ZIP de evidencia de limpieza |
| 3 | `03_analisis_exploratorio_v09.ipynb` | Complementar análisis exploratorio de la cohorte inicial | ZIP local `Evidencias_cortes_v06.zip` | Requiere el archivo de cortes v06; sus resultados guardados se retiraron en la copia pública |
| 4 | `04_regresion_lineal_validacion_marzo.ipynb` | Ajustar y evaluar regresión lineal en marzo | ZIP local de cortes v06 | Produce predicciones y métricas cliente-corte; no publicar sus salidas individuales |
| 5 | `05_regresion_lineal_validacion_junio.ipynb` | Ampliar el entrenamiento y validar junio | Cortes v06 y ZIP local de resultados de marzo | Produce resultados individuales que deben mantenerse fuera del repositorio público |
| 6 | `06_random_forest_validacion.ipynb` | Comparar 16 configuraciones de Random Forest y seleccionar con validación | Cortes v06 y evidencia previa de regresión lineal | Requiere insumos locales; la selección documentada es RF09 |
| 7 | `07_prueba_final_colab.ipynb` | Reajustar con los cinco primeros cortes y evaluar septiembre reservado | Cortes v06 y ZIP local de validación RF | La ejecución auditada se realizó en Google Colab; sus predicciones por cliente no se publican |

## Entradas que se mantienen fuera del repositorio

Los notebooks de modelado esperan archivos ZIP creados durante los bloques previos, incluidos los cortes v06, los resultados de validación lineal y RF, y la base preprocesada v04 para el enriquecimiento del dashboard. Esos archivos contienen filas cliente-corte, identificadores o predicciones individuales. No se incluyen en el repositorio para limitar la redistribución de datos a nivel de registro y evitar que el usuario confunda los CSV con evidencia agregada.

El dashboard también requiere un archivo `data.json` derivado de perfiles y escenarios. El JSON no se incorpora porque contiene información por cliente y aumenta sustancialmente el tamaño del paquete. En consecuencia, el código y la plantilla están presentes, pero la reconstrucción completa exige obtener localmente los insumos documentados en `evidencias/dashboard/LEEME.md`.

## Entorno de la prueba final

La bitácora final registra Python 3.13.18, pandas 2.2.3, NumPy 2.1.3 y scikit-learn 1.6.1. La prueba final recibió 14.935 observaciones cliente-corte para entrenamiento y 2.768 para prueba. El archivo de controles agregado documenta 33 verificaciones aprobadas. Los hashes de las entradas v06 coinciden con las evidencias cotejadas.

Las copias de notebooks en este repositorio tienen eliminadas sus salidas guardadas y contadores de ejecución. Por ello, al abrirlas en GitHub no se mostrarán resultados calculados previamente. Las cifras comunicadas en el documento se respaldan con los CSV agregados de `evidencias/` y la bitácora original de Colab, no con salidas incrustadas en los notebooks.

## Scripts

Los scripts de priorización y elaboración de figuras requieren los archivos intermedios señalados en su código y en la bitácora original. Los CSV agregados incluidos permiten consultar los valores reportados, pero no reemplazan los archivos individuales que requieren algunos procedimientos. No se debe atribuir una ejecución reproducible desde un clon limpio a los scripts que dependen de esos insumos ausentes.

El script `scripts/figuras/generar.py` puede generar dos figuras descriptivas a partir de los CSV agregados incluidos en el repositorio; guarda los archivos resultantes en `salidas_figuras/`, directorio excluido de Git. En cambio, `scripts/priorizacion/calcular.py` requiere predicciones individuales de validación que no se publican y no puede ejecutarse desde un clon limpio.
