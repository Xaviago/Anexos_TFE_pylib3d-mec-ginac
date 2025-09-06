# Anexo H — Modos de uso (módulo y framework)

Este anexo describe **cómo ejecutar la herramienta** tanto como **módulo de Python** como en modo **framework** (GUI). Incluye
comandos, requisitos mínimos y notas sobre salidas y problemas comunes.

---

## H.1 — Resumen rápido
- **Módulo (CLI / scripting)**: pensado para ejecutar ficheros `.py` o bloques `-c`, producir resultados (archivos `.m`) y automatizar.
- **Framework (GUI)**: abre la interfaz gráfica, permite interactuar con ejemplos (p. ej. `four_bar`, `simple_pendulum`).

---

## H.2 — Uso como *módulo* de Python

### Requisitos mínimos
- Python (**3.7** ó **3.12**) con el paquete `lib3d_mec_ginac` correctamente instalado.  
- No requiere VTK/OpenSCAD para ejecutar cálculos y generar ficheros de salida.

### Comandos típicos
**Con fichero `.py`:**
```bash
# El script debe contener:  from lib3d_mec_ginac import *   (o import lib3d_mec_ginac)
python archivo.py
```

**Sin fichero `.py` (en línea):**
```bash
python -i -c "from lib3d_mec_ginac import *;  # …tus llamadas aquí…"
python -c   "from lib3d_mec_ginac import *;  # …tus llamadas aquí…"
```
> `-i` deja la sesión interactiva abierta tras ejecutar el bloque `-c` (útil para depurar).

### Salidas
- Se generan **ficheros `.m`** (Matlab/Octave) en el **directorio de trabajo actual** desde el que invocas `python`.
  - Ejemplo: si estás en `~/Escritorio` y el script está en otra carpeta, los `.m` quedarán en `~/Escritorio`.

---

## H.3 — Uso como *framework* (GUI)

### Requisitos
- **VTK 9.0.1** con **Tk/Tcl 8.6** y **OpenSCAD** instalados (ver Anexo C para la combinación exacta).
- Python (p. ej. **3.12**) con `lib3d_mec_ginac` instalado en el entorno validado.

### Comandos típicos
```bash
# Ejecutar un ejemplo incluido (ruta relativa al repo)
python -m lib3d_mec_ginac examples/four_bar
python -m lib3d_mec_ginac examples/simple_pendulum
```
> Nota: `-m` ejecuta el paquete como módulo; **no** se combina con `-c`.

### Salidas
- **No** se generan ficheros `.m`; la interacción es **gráfica** (botones y visualización).

---

## H.4 — Rutas y ejemplos
- Si el repositorio está en el Escritorio:
  - `pylib3d-mec-ginac/examples/four_bar`
  - `pylib3d-mec-ginac/examples/simple_pendulum`
- Para ejecutar un fichero propio (p. ej. `windturbine.py`) usa su **ruta completa** o sitúate en su carpeta antes de ejecutar.

---

## H.5 — Problemas comunes y pistas rápidas
- **Errores de VTK (carga/versión, símbolos no encontrados):** asegurar **VTK 9.0.1** y **Tk/Tcl 8.6** y que las rutas queden correctamente registradas (ver Anexo D/C).
- **OpenSCAD (parser/visualización):** instalar y tener en **PATH**. Si la GUI abre pero no renderiza, revisa la instalación de OpenSCAD.
- **Archivos `.m` en una carpeta “rara”:** recuerda que se guardan en el **cwd** (directorio actual); usa `cd` a la carpeta del script o lanza Python desde ahí.

---

## H.6 — Referencias cruzadas
- **Anexo C** — Compatibilidades por versión de SO/Python/GCC/VTK.
- **Anexo D** — Scripts de instalación y *makefile*.
- **Anexo E** — Especificación de la VM.
- **Anexo I** — Casos de prueba (I‑01, I‑02, I‑03) que validan tanto *framework* como *módulo*.
