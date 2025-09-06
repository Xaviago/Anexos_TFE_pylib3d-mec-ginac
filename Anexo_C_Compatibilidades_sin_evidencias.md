# Anexo C — Compatibilidades

| SO             |   Python | GCC   | VTK          | Probado   | Estado   | Módulo   | Framework   | Req. extra                         | Notas / Relación                               |
|:---------------|---------:|:------|:-------------|:----------|:---------|:---------|:------------|:-----------------------------------|:-----------------------------------------------|
| Ubuntu 18.04.2 |     3.7  | 8.4.0 | No instalado | Sí        | OK       | OK       | KO          | —                                  | nan                                            |
| Ubuntu 18.04.2 |     3.7  | 8.4.0 | 9.0.1        | Sí        | OK       | OK       | OK          | Requiere OpenSCAD; usar Tk/Tcl 8.6 | nan                                            |
| Ubuntu 18.04.2 |     3.12 | 8.4.0 | No instalado | Sí        | OK       | OK       | KO          | —                                  | nan                                            |
| Ubuntu 18.04.2 |     3.12 | 8.4.0 | 9.0.1        | Sí        | OK       | OK       | OK          | Requiere OpenSCAD; usar Tk/Tcl 8.6 | nan                                            |
| Ubuntu 18.04.2 |     3.7  | 7.4.0 | No instalado | Sí        | OK       | OK       | KO          | —                                  | Relacionado con generación de la .so (Anexo G) |
| Ubuntu 18.04.2 |     3.7  | 7.4.0 | 9.0.1        | Sí        | OK       | OK       | OK          | Requiere OpenSCAD; usar Tk/Tcl 8.6 | Relacionado con generación de la .so (Anexo G) |

---
**Notas:**
- Para **Framework OK** se requiere **OpenSCAD** y **Tk/Tcl 8.6** junto con **VTK 9.0.1**.
- Las filas con **GCC 7.4.0** están ligadas al entorno de **construcción de la `.so`** (ver **Anexo G**).
- Si en algún momento quieres añadir **evidencias gráficas**, solo aplicaría a ejecuciones de **Framework** (capturas de la GUI).
