# Comprobación de la actividad

- Equipo: macOS 26.3, Apple Silicon.
- Anaconda Distribution ya estaba instalada; conda 26.7.3. La versión de la distribución completa no se verificó.
- Entorno creado: `ti2006b-workbench`, Python 3.12.16.
- VS Code: Python y Pylance ya estaban instaladas; se instaló Jupyter con sus componentes oficiales.
- Script ejecutado con el Python del entorno: resultado **14.00 unidades**.
- Notebook ejecutado completo mediante nbconvert con el kernel local `ti2006b-workbench`: sin errores y con las salidas guardadas.
- Formato del notebook y espacios del diff comprobados.
- Cuenta autenticada comprobada: `Javier-Chicuate`. Identidad de Git conservada: `Chicuatin`.

## Problema y solución

El entorno del proyecto todavía no existía y VS Code no tenía la extensión Jupyter. Se creó el entorno con Python 3.12, se instaló la extensión y se registró su kernel; después el script y el notebook funcionaron con el resultado esperado.

## Evidencia que todavía falta en VS Code

El proyecto y el notebook se abrieron en VS Code, pero no se logró comprobar la selección final del intérprete y del kernel desde sus menús. La ejecución registrada se hizo mediante nbconvert, no con el botón Run All del editor. Tampoco se completó la revisión y sincronización desde Source Control: el guardado y envío se realizan mediante Git. Para demostrar esos puntos exactos de la rúbrica, falta elegir `ti2006b-workbench` en Python: Select Interpreter y Select Kernel, ejecutar Run All, guardar y revisar los cambios desde Source Control.

Repositorio: https://github.com/Javier-Chicuate/ti2006b-2.6-A00842336. El enlace al commit de esta entrega se proporciona al terminar la sincronización.
