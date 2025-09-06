# Anexo E — Entornos / VMs

## E.1 — Ficha del entorno (resumen)

| Ítem               | Valor                                               | Notas                                           |
|:-------------------|:----------------------------------------------------|:------------------------------------------------|
| Sistema operativo  | Ubuntu 18.04.2 LTS (Bionic Beaver)                  | Validado en Anexo C                             |
| Kernel             | 5.4.0-150-generic #167~18.04.1-Ubuntu (x86_64)      | nan                                             |
| CPUs               | 4                                                   | nan                                             |
| Memoria RAM        | 8192 MB                                             | nan                                             |
| Disco              | 25 GB                                               | nan                                             |
| Carpeta compartida | Escritorio\TFG\Documentos apoyo TFG\carpeta pruebas | Opción: Automontar                              |
| Guest Additions    | Instaladas                                          | VirtualBox (para carpeta compartida y gráficos) |
| Hostname           | xaviago-VirtualBox                                  | nan                                             |
| Red                | Intel PRO/1000 MT Desktop (NAT)                     |                                                 |

---

## E.2 — Evidencias del sistema (salidas de comandos)

```text
lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.2 LTS
Release:	18.04
Codename:	bionic
```
```text
uname -a
Linux xaviago-VirtualBox 5.4.0-150-generic #167~18.04.1-Ubuntu SMP Wed May 24 00:51:42 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```
```text
cat /etc/os-release 
NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.2 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
```

```text
Recursos de la VM
- RAM: 8192 MB
- CPUs: 4
- Disco: 25 GB
- Carpeta compartida:
	Ruta (host): Escritorio\TFG\Documentos apoyo TFG\carpeta pruebas
	Opciones: Automontar
- Red: Intel PRO/1000 MT Desktop (NAT)
```

---

## E.3 — Plantilla de VM (reproducibilidad)

1. **Crear VM** (VirtualBox) con:
   - SO: Ubuntu **18.04.2** (Bionic), **4 CPUs**, **8 GB RAM**, **25 GB** de disco.
   - **Guest Additions** instaladas.
   - **Red**: Intel PRO/1000 MT Desktop (**NAT**).
   - **Carpeta compartida**: ruta del host `Escritorio\TFG\Documentos apoyo TFG\carpeta pruebas`, **Automontar**.
2. **Instalar Ubuntu 18.04.2** evitando actualizar librerías base que rompan compatibilidad (ver Anexo C).
3. **Configurar entorno** según el objetivo:
   - **Uso moderno (Py 3.12 + VTK 9.0.1)** → ejecutar `setup_entorno.sh` (ver Anexo D).
   - **Construcción de `.so` (GCC 7.4.0 + CLN/GiNaC)** → ejecutar `setup_so.sh` y `makefile` (ver Anexos D y G).
4. **Comprobaciones rápidas**:
   - `python -c "import vtk; print(vtk.vtkVersion().GetVTKVersion())"`
   - `python -m lib3d_mec_ginac examples/four_bar`
5. **Snapshots recomendados** (nomenclatura):
   - `E0-base-18.04.2`, `E1-entorno-Py312-VTK901`, `E2-build-so-gcc74`.
   - (Opcional) **Exportar OVA** tras cada hito.
6. **Notas**:
   - Si se requiere **Framework OK**, asegurarse de **OpenSCAD** y **Tk/Tcl 8.6** (ver Anexo C/H).
   - Evitar `apt upgrade` indiscriminado en esta serie de VMs para no cambiar versiones clave.

---

## E.4 — Relación con otros anexos
- **C**: Matriz de combinaciones probadas.
- **D**: Scripts de instalación y build (APT explícitos y CMake).
- **G**: Evidencias de equivalencia de la `.so`.
- **H**: Cómo ejecutar (módulo/framework).
- **I**: Casos de prueba y resultados.
