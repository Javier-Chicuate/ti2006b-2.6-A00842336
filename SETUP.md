# Actividad 2: preparar y usar el entorno

En esta actividad uso una tabla inventada de ventas de cinco días para comprobar que Python y pandas funcionan. El promedio esperado es de **14 unidades por día**.

## Herramientas y entorno

El proyecto usa Anaconda Distribution, Git y Visual Studio Code, con las extensiones oficiales Python, Pylance y Jupyter. El entorno se llama `ti2006b-workbench` y usa Python 3.12. Para prepararlo desde la raíz del repositorio:

```bash
conda env create -f environment.yml
conda activate ti2006b-workbench
python --version
conda env list
python -c "import pandas, matplotlib, jupyter; print('El entorno está listo')"
```

Si falta Anaconda, se descarga desde https://www.anaconda.com/download según el sistema y procesador. VS Code y Git se instalan por separado. Después de instalar, hay que abrir una terminal nueva. Los paquetes se instalan en el entorno del proyecto, sin agregarlos a `base`.

`environment.yml` documenta las dependencias de conda; `requirements.txt` mantiene las mismas dependencias para la alternativa con pip en Python 3.12. Se conservan los rangos de pandas, JupyterLab, nbconvert y Plotly de la plantilla del curso. No hace falta instalar ambos archivos en el mismo entorno. Las dependencias directas permiten reconstruirlo, pero no fijan todas las versiones internas.

Para registrar las dependencias solicitadas después de instalar:

```bash
conda env export --from-history > environment.yml
```

Antes de guardar ese archivo en Git, se elimina cualquier línea `prefix:` con una ruta local y se revisa que ambos manifiestos sigan alineados.

## Ejecutar el script y el notebook

```bash
conda activate ti2006b-workbench
python src/hello_ds.py
```

El resultado debe ser: `Promedio diario de ventas (datos sintéticos): 14.00 unidades`.

En VS Code se abre la raíz del repositorio, se elige **Python: Select Interpreter** y se selecciona `ti2006b-workbench`. Después se abre `notebooks/02_workbench_check.ipynb` y se selecciona el mismo entorno desde **Select Kernel**. Hay que reiniciar el kernel, usar **Run All** y guardar las salidas. La selección del intérprete y del kernel son pasos distintos; la metadata del archivo no demuestra por sí sola que ambos estén seleccionados.

Si el entorno no aparece, se reinicia VS Code. También se puede registrar con:

```bash
python -m ipykernel install --user --name ti2006b-workbench --display-name "Python (ti2006b-workbench)"
```

## Revisar y sincronizar

En **Source Control** se revisan los cambios, se preparan los archivos de la actividad y se crea un commit con un mensaje claro. Después se usa **Sync Changes** y se comprueba el commit en GitHub. La rama y el pull request son opcionales. Antes del commit se revisa que la identidad de Git sea la personal y que la cuenta de GitHub sea `Javier-Chicuate`. No se incluyen claves, tokens, archivos `.env`, datos privados ni cachés.

Repositorio de esta entrega: https://github.com/Javier-Chicuate/ti2006b-2.6-A00842336.

La reflexión de cinco oraciones está en `REFLEXION.md`. Las comprobaciones reales y lo que queda pendiente están en `VERIFICACION.md`.

## Fuentes

- PDF de la Actividad 2, versión 1.1, páginas 1–3.
- [Plantilla del curso](https://github.com/tec-research/ti2006b/tree/main/templates/init-example-repository).
- [Entornos conda](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html).
- [Notebooks en VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
