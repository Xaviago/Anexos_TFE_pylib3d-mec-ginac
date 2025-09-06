# Anexo A — Diario de trabajo

 **Nota sobre horas:** las horas registradas **no incluyen** tiempos de espera pasivos de comandos largos; solo contabilizan trabajo efectivo.

### 2025-07-16
- **Actividad:** Definir imagen base de VM (Ubuntu 18.04.2) y patrón de instalación replicable (carpeta compartida + Guest Additions).
- **Horas (~):** 4
- **Resultado:** Patrón de VM estable y rápido, sin utilidades innecesarias ni actualización de librerías críticas.
- **Evidencia/Refs:** —; ver Anexo E (VMs).

### 2025-08-04
- **Actividad:** Alcanzar entorno funcional donde la herramienta corre como módulo y como framework en su forma básica (según README).
- **Horas (~):** 100
- **Resultado:** Ejecución mínima por ambas vías.
- **Evidencia/Refs:** Ver Anexo H (Modos de uso).

### 2025-08-14
- **Actividad:** Preparar entorno de construcción para iniciar la generación de la biblioteca compartida.
- **Horas (~):** 50
- **Resultado:** Entorno listo para compilar y enlazar la .so.
- **Evidencia/Refs:** —

### 2025-08-14
- **Actividad:** Diseñar makefile para descargar proyecto, compilar *.cc a *.o y generar lib_3d_mec_ginac.so.
- **Horas (~):** 5
- **Resultado:** Makefile funcional con objetivos de build y limpieza.
- **Evidencia/Refs:** Ver Anexo D (Scripts) → makefile.

### 2025-08-26
- **Actividad:** Diagnosticar diferencia de tamaño entre la .so original y la generada con símbolos equivalentes (nm -D).
- **Horas (~):** 60
- **Resultado:** Hipótesis sobre flags/depuración y enlace estático/dinámico; evidencias recopiladas.
- **Evidencia/Refs:** Ver Anexo G (§G.5–G.8: readelf, nm, comparar.py).

### 2025-08-29
- **Actividad:** Crear entorno moderno con Python 3.12 (módulo OK, framework KO inicialmente) y automatizar instalación.
- **Horas (~):** 25
- **Resultado:** Script setup_entorno.sh con Python 3.12; base del entorno moderno.
- **Evidencia/Refs:** Ver Anexo D (Scripts) → setup_entorno.sh.

### 2025-09-02
- **Actividad:** Completar soporte de framework en el entorno moderno y actualizar el instalador.
- **Horas (~):** 25
- **Resultado:** Framework OK en Py 3.12; instalador actualizado.
- **Evidencia/Refs:** Ver Anexo D → setup_entorno.sh; ver Anexo H.
- **Notas:** Commits a900e63 (ajuste menor en makefile) y 4d461dc (añade scripts de QoL y el makefile en `scripts/` en la raíz del repo).

### 2025-09-03
- **Actividad:** Generar con éxito la biblioteca compartida con tamaño muy cercano al original y automatizar el proceso.
- **Horas (~):** 15
- **Resultado:** .so funcional y reproducible (equivalente según evidencias).
- **Evidencia/Refs:** Ver Anexo G (equivalencia y evidencias) y Anexo D (setup_so.sh + makefile).
- **Notas:** Commit e21e85c — sustitución de archivo en el repositorio (identificador SHA del cambio).

