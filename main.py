#Leer informacion de un archivo Linea por Linea

#Paso 1 -> Abrir el archivo
Archivo = open("Letra_de_mi_cancion_favorita.txt", 'r')#Abre el archivo en modo de lectura
#Crea una lista, linea a linea con lo que tiene el archivo

#Paso 2 -> Procesar el archivo
for linea in Archivo:
    print(linea, end="")

#Paso 3 -> Cerrar el archivo
Archivo.close()
