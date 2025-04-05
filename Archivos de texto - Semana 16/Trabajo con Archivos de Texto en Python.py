#abrimos el archivo para poder escribir dentro de el
cosasP = open("my_notes.txt", "w")
#escribimos dentro del archivo
cosasP.write ("Hola mi Nombre es Danny.\n")
cosasP.write ("Tengo 18 Años de edad,\n")
cosasP.write ("Mi mascota se llama Sima.\n")
#cerramos el archivo
cosasP.close()

#abrimos el archivo para que se lea
cosasP = open("my_notes.txt", "r")
#Leemos cada linea
linea1= cosasP.readline()
linea2= cosasP.readline()
linea3= cosasP.readline()
#escribimos las lineas
print (linea1, linea2, linea3)
#cerramos el archivo
cosasP.close()
