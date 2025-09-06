# Anexo J — Estructura del repositorio y guía de contribución

Este anexo documenta la estructura del repositorio y define un flujo mínimo de contribución para mantener
la reproducibilidad del entorno y la calidad del código.

## J.1 — Estructura (vista general)

- `.github/` — CI y plantillas de issues/PR.  
- `docker/` — recetas para entornos reproducibles.  
- `docs/` — documentación del proyecto.  
- `examples/` — ejemplos (`four_bar`, `simple_pendulum`, ...).  
- `include/` — cabeceras C/C++ (`include/`, `include/cln/`, `include/ginac/`).  
- `lib/linux/x86_64/` — artefactos y la `.so` resultante.  
- `scripts/` — `setup_entorno.sh`, `setup_so.sh`, `makefile` (Anexo D).  
- `src/` — código fuente C++/Cython.  
- `tests/` — pruebas.  
- `.gitignore`, `LICENSE.txt`, `README.md`, `install.sh`, `requirements.txt`, `setup.py`.

## J.1.1 — Árbol del repositorio (vista rápida)

```text
pylib3d-mec-ginac/  (rama: feature/qol-scripts-and-lib-update)
├─ .github/
├─ docker/
├─ docs/
├─ examples/
│  ├─ four_bar/
│  ├─ simple_pendulum/
│  └─ …
├─ include/
│  ├─ cln/
│  ├─ ginac/
│  └─ *.h (headers del proyecto)
├─ lib/
│  └─ linux/
│     └─ x86_64/
│        └─ lib_3d_mec_ginac.so
├─ scripts/
│  ├─ setup_entorno.sh
│  ├─ setup_so.sh
│  └─ makefile
├─ src/
├─ tests/
├─ .gitignore
├─ LICENSE.txt
├─ README.md
├─ install.sh
├─ requirements.txt
└─ setup.py
```

## J.2 — Convenciones y ramas
- **Ramas activas**: trabajar en `feature/*` y abrir PR hacia la rama de integración acordada.  
- **Commits de referencia del TFG**: `a900e63` (ajuste makefile), `4d461dc` (nuevos scripts `setup_*` y makefile), `e21e85c` (sustitución de archivo clave).  
- **Mensajes de commit**: formato _imperativo corto_ + contexto (p. ej., `build: añade flags --with-* a GCC`).

## J.3 — Flujo de contribución (mínimo)
1. **Fork** + `git checkout -b feature/<breve-descripción>`  
2. **Entorno**: reproducir VM (Anexo E) o Docker.  
3. **Desarrollo**:  
   - Scripts: actualizar `scripts/` y documentar APT/CMake en Anexo D.  
   - C++/Cython: mantener flags (-fPIC, -O2, -g) y dependencias.  
4. **Build**: generar `.so` con `setup_so.sh` + `makefile`.  
5. **Pruebas**: ejecutar **I-01**, **I-02**, **I-03** (Anexo I).  
6. **Evidencias**: adjuntar salidas de `readelf`/`nm` si afecta a la `.so` (Anexo G).  
7. **PR**: enlazar anexos modificados y describir impacto.

## J.4 — Estilo y calidad
- **Python**: seguir PEP8; tipado donde sea razonable.  
- **C/C++**: clases y headers en `include/`; compilar con `-D_FORTIFY_SOURCE=2` y `-fstack-protector-strong`.  
- **CMake**: opciones de VTK documentadas en **F**; no cambiar versiones sin actualizar compatibilidades (**C**).

## J.5 — Versionado y etiquetas
- **Tags** de terceros usados en el TFG: `VTK v9.0.1`, `GiNaC 1.7.7`, `CLN 1.3.4`.  
- **Python**: `3.7` (legacy) y `3.12` (moderno), ver **C**/**D**.  
- **Biblioteca resultante**: `lib_3d_mec_ginac.so` (verificación en **G**).

## J.6 — Checklist de PR
- [ ] Scripts actualizados y ejecutables (`bash -x` limpia).  
- [ ] `.so` generada y verificada (Anexo G).  
- [ ] Pruebas **I-0x** en **OK** (Anexo I).  
- [ ] README actualizado si cambia el uso.  
- [ ] Licencias de terceros intactas (GPLv2).
