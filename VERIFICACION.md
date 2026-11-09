# Comprobación de la Actividad 2

## Equipo y herramientas

Preparé el trabajo en macOS 26.3 con Apple Silicon. Anaconda Distribution ya estaba instalada y comprobé conda 26.7.3; no verifiqué la versión de la distribución completa. El entorno que creé se llama `ti2006b-workbench` y usa Python 3.12.16. En VS Code ya estaban Python y Pylance, e instalé la extensión oficial Jupyter.

## Pruebas realizadas

Seleccioné `ti2006b-workbench` como intérprete del script y como kernel del notebook en VS Code. Ejecuté el script con **Run Python File** y ejecuté el notebook con **Run All**. Ambos mostraron **14.00 unidades** como promedio diario. Guardé las salidas reales del notebook y revisé su formato.

Exporté `environment.yml` con `conda env export --from-history` y retiré la línea `prefix:` para evitar una ruta propia del equipo. `requirements.txt` conserva los mismos paquetes directos y los rangos de la plantilla del curso.

## Problema resuelto

Al comenzar, faltaban el entorno del proyecto y la extensión Jupyter. Además, el script tenía seleccionado el Python 3.9.6 del sistema. Creé el entorno con Python 3.12, instalé Jupyter y elegí el entorno correcto en los dos selectores de VS Code. Después, el script y el notebook dieron el resultado esperado desde el editor.

## Repositorio y entrega

Usé el repositorio indicado para esta actividad: https://github.com/Javier-Chicuate/ti2006b-2.6-A00842336. Comprobé que la cuenta de GitHub y la identidad local del commit fueran `Javier-Chicuate`.

El PDF pide continuar el Capstone de la Actividad 1 dentro de la organización del equipo. Al consultar `itd-messilovers/ti2006b-capstone` con mi cuenta, recibí una respuesta 404 y no pude comprobar ese repositorio. Integré los archivos en el repositorio personal indicado para este trabajo; todavía debo confirmar con el profesor si acepta ese destino.

La actividad se entrega en Experiencia21 con las URLs y un PDF de evidencias. Preparé el reporte con capturas reales del script, el kernel del notebook y la revisión de cambios. El archivo aún debe subirse a la plataforma; no registro la entrega como enviada.

## Revisión y sincronización

Revisé los cambios desde Source Control de VS Code, creé el commit de comprobación y usé Sync Changes. Después confirmé en GitHub que el commit estaba visible y atribuido a Javier-Chicuate.
