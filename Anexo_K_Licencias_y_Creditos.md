# Anexo K — Licencias y créditos

Este anexo consolida las **licencias de terceros** empleadas por el TFG y la **licencia del propio proyecto**.
Se indican usos (build/runtime), enlaces de origen y obligaciones principales de redistribución.

## K.1 — Tabla resumen
| Componente                         | Versión/Tag   | Licencia (tipo)             | Enlace de origen                                             | Uso                               | ¿Redistribuido en repo?   | Obligaciones clave                                                        |
|:-----------------------------------|:--------------|:----------------------------|:-------------------------------------------------------------|:----------------------------------|:--------------------------|:--------------------------------------------------------------------------|
| Proyecto (pylib3d-mec-ginac, fork) | —             | GPL-2.0                     | repo del TFG                                                 | Código propio                     | Sí                        | Mantener GPL-2.0; incluir LICENSE; publicar cambios.                      |
| GCC                                | 7.4.0         | GPL-3.0 + Runtime Exception | (sistema)                                                    | Build                             | No                        | No redistribuir binarios; respetar excepción de runtime.                  |
| CMake                              | 3.10.2        | BSD-3-Clause                | (sistema)                                                    | Build                             | No                        | Mantener notices si se redistribuyera.                                    |
| CLN                                | 1.3.4         | GPL-2.0+                    | git://www.ginac.de/cln.git                                   | Runtime/Link                      | No (se instala en VM)     | El enlace con CLN exige compatibilidad GPL para la .so resultante.        |
| GiNaC                              | 1.7.7         | GPL-2.0+                    | git://www.ginac.de/ginac.git                                 | Runtime/Link                      | No (se instala en VM)     | El enlace con GiNaC exige compatibilidad GPL para la .so resultante.      |
| mpfr                               | 3.1.6         | LGPL-3.0+                   | (tar oficial)                                                | Build/Runtime (dep. de toolchain) | No                        | Si se redistribuye: incluir licencia y ofrecer objeto para relink (LGPL). |
| mpc                                | 1.0.3         | LGPL-3.0+                   | (tar oficial)                                                | Build/Runtime (dep. de toolchain) | No                        | Como mpfr.                                                                |
| isl                                | 0.18          | MIT                         | (tar oficial)                                                | Build (dep. de toolchain)         | No                        | Mantener notice si se redistribuye.                                       |
| VTK                                | v9.0.1        | BSD-3-Clause                | https://github.com/Kitware/VTK.git                           | Framework GUI                     | No (se instala en VM)     | Mantener notices si se redistribuye.                                      |
| Tcl/Tk                             | 8.6           | Tcl/Tk (BSD-like)           | (sistema)                                                    | Requisito VTK                     | No                        | Mantener avisos si se redistribuye.                                       |
| OpenSCAD                           | —             | GPL-3.0                     | (sistema)                                                    | Framework GUI (render)            | No                        | Si se redistribuye: GPL-3.0.                                              |
| fontconfig                         | 2.12.6        | MIT                         | (sistema)                                                    | Runtime                           | No                        | Mantener notice si se redistribuye.                                       |
| libSM                              | 1.2.2-1       | MIT                         | (sistema)                                                    | Runtime                           | No                        | Mantener notice si se redistribuye.                                       |
| libXrender                         | 0.9.10-1      | MIT                         | (sistema)                                                    | Runtime                           | No                        | Mantener notice si se redistribuye.                                       |
| mesa-utils                         | 8.4.0-1       | MIT                         | (sistema)                                                    | Runtime (diag)                    | No                        | Mantener notice si se redistribuye.                                       |
| Python                             | 3.12.10       | PSF-2.0                     | https://www.python.org/ftp/python/3.12.10/Python-3.12.10.tgz | Runtime                           | No                        | Mantener licencia PSF si se redistribuye.                                 |

## K.2 — Notas de cumplimiento y distribución

- **No se redistribuyen binarios de terceros** en el repositorio; todo se **instala en la VM** (Anexo E) o mediante scripts (Anexo D).
- Al compilar `lib_3d_mec_ginac.so` y **enlazar** con **GiNaC/CLN (GPL‑2.0+)**, la biblioteca resultante debe mantenerse **GPL‑compatible**.
- **BSD/MIT/PSF/Tcl**: si en algún momento se redistribuyeran binarios o código de estos proyectos, **incluir los notices** y archivos de licencia correspondientes.
- **LGPL (mpfr/mpc)**: si se redistribuyeran, proporcionar **medio de relink** (o enlaces dinámicos) y texto de licencia.
- **GCC**: herramienta de compilación (GPL‑3.0 con excepciones para runtime); **no** se redistribuye.

## K.3 — Créditos
- Agradecimientos a proyectos: **GiNaC**, **CLN**, **VTK/Kitware**, **Python**, **Fontconfig**, **X.Org**, **Mesa**, **Tcl/Tk**, **OpenSCAD** y la comunidad FLOSS.
- El repositorio del TFG referencia de forma explícita orígenes/commits en **Anexo F**.
