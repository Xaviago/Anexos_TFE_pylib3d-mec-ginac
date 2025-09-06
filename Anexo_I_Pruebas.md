# Anexo I — Casos de prueba

Este anexo recopila las **pruebas funcionales** ejecutadas para validar el uso como **framework** y como **módulo**.
Cada caso incluye precondiciones, pasos, datos de entrada y resultados.

## I-01 — Ejecutar four_bar en framework y verificar la GUI (botones y funciones).
- **Modo:** Framework (GUI)
- **Precondiciones:** Python 3.12; VTK 9.0.1; Tk 8.6; Tcl 8.6; GCC 8.4.0; CLN 1.3.4; GiNaC 1.7.7; Fontconfig 2.12.6; mpfr 3.1.6; mpc 1.0.3; isl 0.18; CMake 3.10.2; mesa-utils 8.4.0-1; libsm6 2:1.2.2-1; libxrender1 1:0.9.10-1; libfontconfig1 2.12.6-0ubuntu2.
- **Pasos:**  
```
1) Ejecutar: python -m lib3d_mec_ginac examples/four_bar
2) Verificar que la ventana aparece y que todos los botones existen y responden.
```
- **Datos de entrada:** Ruta al ejemplo: pylib3d-mec-ginac/examples/four_bar
- **Resultado esperado:** Carga correcta de la GUI; todos los controles visibles y funcionales.
- **Resultado obtenido:** OK (sin errores).
- **Estado:** OK
- **Evidencia:** Vídeo 2
---

## I-02 — Ejecutar simple_pendulum en framework y verificar la GUI.
- **Modo:** Framework (GUI)
- **Precondiciones:** Python 3.12; VTK 9.0.1; Tk 8.6; Tcl 8.6; GCC 8.4.0; CLN 1.3.4; GiNaC 1.7.7; Fontconfig 2.12.6; mpfr 3.1.6; mpc 1.0.3; isl 0.18; CMake 3.10.2; mesa-utils 8.4.0-1; libsm6 2:1.2.2-1; libxrender1 1:0.9.10-1; libfontconfig1 2.12.6-0ubuntu2.
- **Pasos:**  
```
1) Ejecutar: python -m lib3d_mec_ginac examples/simple_pendulum
2) Verificar que la ventana aparece y que todos los botones existen y responden.
```
- **Datos de entrada:** Ruta al ejemplo: pylib3d-mec-ginac/examples/simple_pendulum
- **Resultado esperado:** Carga correcta de la GUI; todos los controles visibles y funcionales.
- **Resultado obtenido:** OK (sin errores).
- **Estado:** OK
- **Evidencia:** Vídeo 2
---

## I-03 — Ejecutar windturbine como módulo y verificar generación de salidas .m.
- **Modo:** Módulo (CLI)
- **Precondiciones:** Python 3.12; GCC 8.4.0; CLN 1.3.4; GiNaC 1.7.7; Fontconfig 2.12.6; mpfr 3.1.6; mpc 1.0.3; isl 0.18; CMake 3.10.2; mesa-utils 8.4.0-1; libsm6 2:1.2.2-1; libxrender1 1:0.9.10-1; libfontconfig1 2.12.6-0ubuntu2.
- **Pasos:**  
```
1) Ejecutar: python windturbine  (o python windturbine.py)
2) Comprobar que se generan los ficheros de salida en el directorio actual.
```
- **Datos de entrada:** Ruta completa al fichero windturbine(.py).
- **Resultado esperado:** Generación de 5 ficheros con extensión .m con contenido correcto.
- **Resultado obtenido:** OK: 5 ficheros .m generados y validados visualmente.
- **Estado:** OK
- **Evidencia:** Vídeo 2
---
