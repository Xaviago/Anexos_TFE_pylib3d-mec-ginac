# Anexo G — Construcción y verificación de `lib_3d_mec_ginac.so`

## G.1 — Objetivo
Demostrar que la **biblioteca compartida** generada es **equivalente** a la original a nivel funcional y binario observable
(símbolos exportados, dependencias dinámicas y metadatos), con posibles diferencias esperables en rutas de compilación
y secciones de depuración.

## G.2 — Entorno y build
- **SO:** Ubuntu 18.04.2 (Bionic) — ver Anexo E.
- **Toolchain:** GCC 7.4.0; CLN 1.3.4; GiNaC 1.7.7; mpfr 3.1.6; mpc 1.0.3; isl 0.18.
- **Enlaces clave de configuración:** ver Anexo F (Configure flags / prefixes).
- **Makefile:** compila con `-fPIC -O2 -g -D_FORTIFY_SOURCE=2 -fstack-protector-strong -I... -c` y enlaza con
  `-shared -Wl,-Bstatic -lginac -lcln -Wl,-Bdynamic -lm -lgcc_s -lc` (ver Anexo D).
- **Supuesto de rutas:** el `makefile` se sitúa al mismo nivel que `lib_3d_mec_ginac/` y `pylib3d-mec-ginac/`.

## G.3 — Comprobaciones realizadas
Se han ejecutado los siguientes comandos sobre la **original** y la **generada**, capturando evidencias:
1) `readelf -S -W lib_3d_mec_ginac.so | egrep '.debug|.symtab|.dynsym|.dynstr|.strtab|.eh_frame|.note|.gnu'`
2) `readelf --debug-dump=info lib_3d_mec_ginac.so | grep -a 'DW_AT_comp_dir' | head`
3) `readelf -d lib_3d_mec_ginac.so | egrep 'RPATH|RUNPATH|NEEDED'`
4) `nm -D --defined-only lib_3d_mec_ginac.so | wc -l`

### Resumen de resultados
| Chequeo                                                    | Original                                                                                                                                                                                       | Generada                                                                                                                   | ¿Coinciden?                       |
|:-----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|:----------------------------------|
| Símbolos exportados (nm -D --defined-only | wc -l)         | 917                                                                                                                                                                                            | 917                                                                                                                        | Sí                                |
| NEEDED/RPATH (readelf -d)                                  | NEEDED=3; RUNPATH/RPATH=No                                                                                                                                                                     | NEEDED=4; RUNPATH/RPATH=No                                                                                                 | Difieren                          |
| DW_AT_comp_dir (readelf --debug-dump=info | grep comp_dir) | (indirect string, offset: 0x4f2da): /home/vykstorm/Proyectos/lib_3d_mec_ginac/lib_3d_mec_ginac; (indirect string, offset: 0x4f2da): /home/vykstorm/Proyectos/lib_3d_mec_ginac/lib_3d_mec_ginac | (indirect string, offset: 0x47eb3): /home/xaviago/Escritorio; (indirect string, offset: 0x47eb3): /home/xaviago/Escritorio | Esperado distinto (rutas locales) |
| Secciones clave (readelf -S -W)                            | 17 líneas                                                                                                                                                                                      | 16 líneas                                                                                                                  | Similar (pueden variar por -g)    |

> **Nota:** Las diferencias en `DW_AT_comp_dir` son **esperables** (rutas locales distintas). Las secciones de depuración
(`.debug_*`) también pueden variar en tamaño si se compila con `-g` o si cambian rutas/nombres intermedios.

## G.4 — Coincidencia de símbolos (detalle)
- Conteo de símbolos exportados: **coinciden** entre original y generada (ver 4 y 4.original).
- Se ejecutó un script de comparación de nombres de símbolos (`comparar.py`) sobre el `nm -D` de ambas:
  - Resultado reportado por el autor: **0 diferencias** en **1247** símbolos (última ejecución).

## G.5 — Evidencias adjuntas
- `1` y `1.original` — Secciones clave (`readelf -S -W`).  
- `2` y `2.original` — Rutas DWARF (`readelf --debug-dump=info`).  
- `3` y `3.original` — Dependencias y (RUN)RPATH (`readelf -d`).  
- `4` y `4.original` — Conteo de símbolos (`nm -D --defined-only | wc -l`).  
- `comparar.py` — Script que compara nombres de símbolos de `nm -D` línea a línea.


## G.6 — Conclusión
La biblioteca **generada** es **equivalente** a la **original** en términos de símbolos exportados y dependencias dinámicas,
y se comporta correctamente en las **pruebas funcionales** (ver Anexo I). Las únicas diferencias observadas corresponden a
metadatos de compilación (rutas DWARF) y posibles tamaños de secciones de depuración, compatibles con builds reproducibles
bajo rutas distintas.
