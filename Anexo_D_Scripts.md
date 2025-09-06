# Anexo D — Scripts

## D.1 — Resumen
| Archivo          | Propósito                                                                                                 | Paquetes APT (explícitos)                                                                                                                                                                                                                                                                                                                                                              | CMake/Config (resumen -D...)                                                                                                                                                                                                                                                                                                                                                                                      | Salida/Artefactos                                       | Ejecución             | Logs                                          |
|:-----------------|:----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------|:----------------------|:----------------------------------------------|
| setup_entorno.sh | Entorno moderno (Ubuntu 18.04.2): Python 3.12, VTK 9.0.1, Tk/Tcl 8.6 para módulo/framework.               | git, build-essential, zlib1g-dev, libncurses5-dev, libgdbm-dev, true, libnsl-dev                                                                                                                                                                                                                                                                                                       | -DCMAKE_INSTALL_PREFIX=/usr/lib -DCMAKE_INSTALL_LIBDIR=. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DVTK_WRAP_PYTHON=ON -DVTK_PYTHON_VERSION=3 -DPython3_EXECUTABLE="${PY_EXE}" -DPython3_INCLUDE_DIR="${PY_INC}" -DPython3_LIBRARY="${PY_LIB}" -DVTK_GROUP_ENABLE_Qt=NO -DVTK_GROUP_ENABLE_StandAlone=YES -DVTK_GROUP_ENABLE_Rendering=YES -DVTK_USE_TK=ON -DVTK_PYTHON_SITE_PACKAGES_SUFFIX="${VTK_PY_… | Python 3.12; VTK con wrappers; paquete usable.          | bash setup_entorno.sh | bash setup_entorno.sh | tee setup_entorno.log |
| setup_so.sh      | Toolchain de build (GCC 7.4.0, CLN 1.3.4, GiNaC 1.7.7, mpfr/mpc/isl) y generación de lib_3d_mec_ginac.so. | git, python3.7, make, python3-pip, build-essential, python3.7-dev, make-guile, autoconf, automake, libtool, libfreetype6-dev, libexpat1-dev, gperf, pkg-config, libgl1-mesa-dev, texinfo, bison, flex, libreadline-dev, transfig, doxygen, texlive-latex-base, texlive-latex-extra, texlive-fonts-recommended, texlive-fonts-extra, dvipng, libgmp-dev, libc6-dev-i386, lib32gcc-7-dev | N/D                                                                                                                                                                                                                                                                                                                                                                                                               | lib_3d_mec_ginac.so; instalación (Py 3.7 si aplica).    | bash setup_so.sh      | bash setup_so.sh | tee setup_so.log           |
| makefile         | Compilar *.cc → *.o con -fPIC y enlazar .so (-shared); mover artefacto al árbol Python.                   | N/A                                                                                                                                                                                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                                                                                                                                                                                               | lib_3d_mec_ginac.so en lib/linux/x86_64/ (target move). | make [target]         | make 2>&1 | tee build.log                     |

## D.2 — Detalle por archivo

### D.2.1 — setup_entorno.sh
- **Paquetes APT (explícitos).** git, build-essential, zlib1g-dev, libncurses5-dev, libgdbm-dev, true, libnsl-dev
- **CMake/Config (resumen -D...).** -DCMAKE_INSTALL_PREFIX=/usr/lib -DCMAKE_INSTALL_LIBDIR=. -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DVTK_WRAP_PYTHON=ON -DVTK_PYTHON_VERSION=3 -DPython3_EXECUTABLE="${PY_EXE}" -DPython3_INCLUDE_DIR="${PY_INC}" -DPython3_LIBRARY="${PY_LIB}" -DVTK_GROUP_ENABLE_Qt=NO -DVTK_GROUP_ENABLE_StandAlone=YES -DVTK_GROUP_ENABLE_Rendering=YES -DVTK_USE_TK=ON -DVTK_PYTHON_SITE_PACKAGES_SUFFIX="${VTK_PY_…
- **CMake VTK (bloque detectado):**
```bash
cmake ..
  -DCMAKE_INSTALL_PREFIX=/usr/lib
  -DCMAKE_INSTALL_LIBDIR=.
  -DCMAKE_BUILD_TYPE=Release
  -DBUILD_SHARED_LIBS=ON
  -DVTK_WRAP_PYTHON=ON
  -DVTK_PYTHON_VERSION=3
  -DPython3_EXECUTABLE="${PY_EXE}"
  -DPython3_INCLUDE_DIR="${PY_INC}"
  -DPython3_LIBRARY="${PY_LIB}"
  -DVTK_GROUP_ENABLE_Qt=NO
  -DVTK_GROUP_ENABLE_StandAlone=YES
  -DVTK_GROUP_ENABLE_Rendering=YES
  -DVTK_USE_TK=ON
  -DVTK_PYTHON_SITE_PACKAGES_SUFFIX="${VTK_PY_SPKG_SUFFIX}"
```

### D.2.2 — setup_so.sh
- **Paquetes APT (explícitos).** git, python3.7, make, python3-pip, build-essential, python3.7-dev, make-guile, autoconf, automake, libtool, libfreetype6-dev, libexpat1-dev, gperf, pkg-config, libgl1-mesa-dev, texinfo, bison, flex, libreadline-dev, transfig, doxygen, texlive-latex-base, texlive-latex-extra, texlive-fonts-recommended, texlive-fonts-extra, dvipng, libgmp-dev, libc6-dev-i386, lib32gcc-7-dev
- **CMake/Config (resumen -D...).** N/D

### D.2.3 — makefile
- **Targets:** .SILENT, all, clone, enter, doOFile, doSoFile, move, erase
