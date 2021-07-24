import os
import re
path = input("Ingresa la ruta del directorio a renombrar: ")
Destination = input("Ingresa la ruta del directorio de Destino: ")
name = input("Ingresa el nombre del TV show: ")
season = input("Ingresa la temporada: ")
format = input("Ingresa el formato de los archivos(sin puntos): ")
try:   
    files = os.listdir(path)
    files.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    count=1
except:
    print("Error en los directorios.")
def main():
    try:
        for count,filename in enumerate(files):
            dst = name+"S"+season+"E"+str(count+1) +"."+format
          
            # rename() function will
            # rename all the files
            os.rename(os.path.join(path, filename),  os.path.join(Destination, dst))  
    except:
        print("HA OCURRIDO UN ERROR.")

# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()