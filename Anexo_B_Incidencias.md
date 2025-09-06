# Anexo B — Incidencias

## B-01
- **Fecha:** 2025-08-02
- **Severidad:** media
- **Estado:** Cerrada
- **Entorno:** Python 3.7, GCC 8.4.0, VTK 9.0.1
- **Resumen:** Error de carga/versión de VTK en GUI.
- **Comando:** `python
from vtk import vtkRenderWindow`
- **Mensaje / Contexto:**
```
Error principal: ModuleNotFoundError: No module named 'vtk'

Comando: python -c "from vtk import vtkRenderWindow"
python
```

- **Causa raíz:** Rutas o versión VTK incompatible.
- **Solución aplicada:** Fijar VTK 9.0.1 y Tk/Tcl 8.6; revisar PATHs.
- **Evidencia:** Captura de pantalla 2025-08-02 132234.png
---

## B-02
- **Fecha:** 2025-08-04
- **Severidad:** media
- **Estado:** Cerrada
- **Entorno:** Python 3.7, GCC 8.4.0, VTK 9.0.1
- **Resumen:** Error: FileNotFoundError: [Errno 2] No such file or directory: 'openscad': 'openscad'
- **Comando:** `python -m lib3d_mec_ginac examples/four_bar`
- **Mensaje / Contexto:**
```
Error: FileNotFoundError: [Errno 2] No such file or directory: 'openscad': 'openscad'

Comando: python -m lib3d_mec_ginac examples/four_bar
```

- **Causa raíz:** N/D
- **Solución aplicada:** N/D
- **Evidencia:** Captura de pantalla 2025-08-04 015953.png
---

## B-03
- **Fecha:** 2025-08-07
- **Severidad:** leve
- **Estado:** Cerrada
- **Entorno:** Python 3.7, GCC 7.4.0, VTK no instalada
- **Resumen:** Requisito de versión (CMake/VTK) no cumplido.
- **Comando:** `CMake 3.12...3.21 or higher is required`
- **Mensaje / Contexto:**
```
Error principal: CMake 3.12...3.21 or higher is required

Comando: sudo pip install .
```

- **Causa raíz:** Intento de usar VTK 9.5.0 → requería CMake superior; decisión: re-crear VM con VTK 9.0.1.
- **Solución aplicada:** Incidencia **leve**: rehacer VM con VTK 9.0.1; cerrar.
- **Evidencia:** Captura de pantalla 2025-08-07 140556.png
---

## B-04
- **Fecha:** 2025-08-30
- **Severidad:** media
- **Estado:** Cerrada
- **Entorno:** Python 3.12, GCC 8.4.0, VTK 9.0.1
- **Resumen:** Error principal: Did you forgot to import 'sys'?
- **Comando:** `python -m lib3d_mec_ginac examples/four_bar`
- **Mensaje / Contexto:**
```
Error principal: Did you forgot to import 'sys'?

Comando: python -m lib3d_mec_ginac examples/four_bar
```

- **Causa raíz:** N/D
- **Solución aplicada:** N/D
- **Evidencia:** Captura de pantalla 2025-08-30 010946.png
---
