
#    REEMPLAZAR texto en cualquier archivo.-

Aeliminar = "Any Text"
Aconservar = "it will stay"
ArchModificar = "nombre de archivo"

# el archivo debe de localizarse en la misma carpeta o determinar la ubicación

cont = open(ArchModificar, "r").read()   
cont = cont.replace(Aeliminar, Aconservar)

with open(ArchModificar, "w") as archivo:
    archivo.write(cont)
    archivo.close()