# Comprobación de la Actividad 2

## Equipo y herramientas

El trabajo se preparó en macOS 26.3 con Apple Silicon. Anaconda Distribution ya estaba instalada y se comprobó conda 26.7.3; la versión de la distribución completa no se verificó. El entorno creado se llama `ti2006b-workbench` y usa Python 3.12.16. En VS Code ya estaban Python y Pylance, y se instaló la extensión oficial Jupyter.

## Pruebas realizadas

Se seleccionó `ti2006b-workbench` como intérprete del script y como kernel del notebook en VS Code. El script se ejecutó con **Run Python File** y el notebook con **Run All**. Ambos mostraron **14.00 unidades** como promedio diario. Se guardaron las salidas reales del notebook y se revisó su formato.

`environment.yml` se exportó con `conda env export --from-history` y se retiró la línea `prefix:` para evitar una ruta propia del equipo. `requirements.txt` conserva los mismos paquetes directos y los rangos de la plantilla del curso.

## Problema resuelto

Al comenzar, faltaban el entorno del proyecto y la extensión Jupyter. Además, el script tenía seleccionado el Python 3.9.6 del sistema. Se creó el entorno con Python 3.12, se instaló Jupyter y se eligió el entorno correcto en los dos selectores de VS Code. Después, el script y el notebook dieron el resultado esperado desde el editor.

## Repositorio y entrega

Se usa el repositorio confirmado para esta actividad: https://github.com/Javier-Chicuate/ti2006b-2.6-A00842336. La cuenta de GitHub verificada y la identidad local del nuevo commit son `Javier-Chicuate`.

El PDF pide continuar el Capstone de la Actividad 1 dentro de la organización del equipo. La consulta a `itd-messilovers/ti2006b-capstone` devolvió 404 con la cuenta actual, así que no se pudo comprobar ese repositorio. No se creó ni se cambió una organización. Los archivos se integraron en el repositorio personal que se indicó para este trabajo; queda por confirmar con el profesor si acepta ese destino.

La entrega en la plataforma del curso sigue pendiente: falta indicar cuál es la plataforma o el enlace de la actividad. Los enlaces del repositorio y del commit, junto con esta nota técnica y `REFLEXION.md`, son los elementos para entregar.
