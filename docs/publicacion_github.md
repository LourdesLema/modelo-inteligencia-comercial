# Preparación del repositorio en GitHub

El directorio de este paquete constituye la versión inicial del repositorio académico. Antes de cargarlo, la autora debe decidir si mantendrá la licencia pendiente o incorporará una licencia explícita. Sin licencia, se mantiene la reserva general de derechos de autor.

Se recomienda crear inicialmente el repositorio como privado mientras se confirma la versión de entrega y se verifica que la carpeta no contenga archivos locales con registros por cliente. La apertura pública puede realizarse posteriormente si corresponde a los requisitos institucionales.

## Carga mediante la interfaz de GitHub

1. Crear un repositorio vacío con un nombre descriptivo, por ejemplo `modelo-inteligencia-comercial-udla`.
2. Descargar y descomprimir `Repositorio_GitHub_UDLA_v01.zip`.
3. En GitHub, seleccionar la opción para cargar archivos existentes, arrastrar el contenido de la carpeta `repositorio_capstone` y confirmar la carga.
4. Verificar que se visualicen `README.md`, `CITATION.cff`, `docs/`, `notebooks/` y `evidencias/`.
5. Revisar el nivel de privacidad del repositorio y copiar su URL únicamente después de completar la carga.

## Carga mediante Git

Desde la carpeta descomprimida del repositorio, se pueden ejecutar estos comandos después de crear un repositorio vacío en GitHub y reemplazar la URL de ejemplo por la URL asignada:

```bash
git init
git add .
git status --short
git commit -m "Versión académica inicial"
git branch -M main
git remote add origin https://github.com/USUARIO/modelo-inteligencia-comercial-udla.git
git push -u origin main
```

Antes de ejecutar `git add .`, comprobar que los archivos de entrada locales estén fuera de la carpeta o excluidos por `.gitignore`. La salida de `git status --short` permite revisar el conjunto de archivos que se incorporaría al primer commit.
