# Compara el contenido de los archivos simbolos.
## No se tiene en cuenta ni el orden ni el inicio de las líneas, sólo a partir de la segunda columna, es decir, si es "B"/"U"/"T"/"W" y el contenido es el mismo (a partir del 18 carácter).

# Ficheros
fichero1 = "simbolos_mios5.txt"
fichero2 = "simbolos_original.txt"

# Se genera un fichero intermedio sin los 18 primeros caracteres para cada fichero
with open(fichero1, "r") as f1, open("simbolos_intermedios_mios5.txt", "w") as fout1, open(fichero2, "r") as f2, open("simbolos_intermedios_original.txt", "w") as fout2:
    # Para cada línea en ambos ficheros
    for line1, line2 in zip(f1, f2):
        fout1.write(line1[17:])
        fout2.write(line2[17:])

    # Se cierran los ficheros intermedios
    fout1.close()
    fout2.close()

# Se comparan los ficheros intermedios y se ponen las diferencias en un fichero. Se cuenta como una diferencia por cada línea que no esté en el otro fichero independientemente del orden.
with open("simbolos_intermedios_mios5.txt", "r") as f1, open("simbolos_intermedios_original.txt", "r") as f2, open("diferencias5.txt", "w") as fout:
    # Se leen las líneas de ambos ficheros
    lines1 = set(f1.readlines())
    lines2 = set(f2.readlines())

    # Se encuentran las diferencias
    diferencias = lines1.symmetric_difference(lines2)

    # Se escriben las diferencias en el fichero de salida
    for diff in diferencias:
        fout.write("Diferencia encontrada:\n")
        fout.write("Mios: " + diff if diff in lines1 else "Original: " + diff)