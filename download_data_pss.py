#------------------------------------------------------------------------------
# Name:        APiArcgis.py
# Purpose:     1) Conectar con la plataforma de arcgis online
#              2) Buscar y extraer datos de Pss
#              3) Organizar los datos
#              4) Crear una copia de un dia para los datos
#
# Author:      Julian Herrera Torres ING.Proycetos ESP
# Created:     29/06/2022 
# Copyright:   (c) Veolia Colombia 2021
#-------------------------------------------------------------------------------

#Carga las librerias necesarias
import arcgis
from arcgis.gis import GIS
import os
from datetime import datetime
from zipfile import ZipFile
import pandas as pd
import shutil as sh

# establecer variables
now=datetime.now()
path='E:/01_analisis_datos/Datos_pss/data'# CAMBIAR DONDE SE PONGA
name_file= str(str(now.year) + str(now.month) + str(now.day)+str(now.hour) +str(now.minute)+str(now.second))


#Funcion Conexion_AGO, busqueda del archivo, exporta y borra los datos de AGOL
def conexion_ago (url,user,pw,item):
     
    gis = GIS (url,user,pw)
    resultado_item = gis.content.get(item)
    result = resultado_item.export(name_file,'CSV')
    result.download(path)
    result.delete()
    print('Finaliza descarga en ZIP')
    
print("Prepara entrada en AGOL")
conexion_ago('http://proactivaco.maps.arcgis.com', 'julian.herrera','julian1125A','9b73fc88d0204add99f9cb71d625bd26')
print("Entra con Exito!")
###
#extrae los archivos ZIP
print("Extrae archivo ZIP")
zip_file = ZipFile(path+'/'+name_file+'.zip')
zip_file.extractall(path=path)
print("Finaliza extraccion")
#crea carpeta LOGS
# Funcion para crear archivo de LOGS y para crear carpeta para guardar LOGS

def create_folder_logs():
    contenido=os.listdir(path)
    a=0
    for i in contenido:
        if(i!='logs'):
            a=a+1
            print("No crea capeta")
        if a == len(contenido):
            os.mkdir(path+'/logs')
            print("se crea capeta")
    del(a)

# crear archivo de logs
def create_files_logs():
    os.chdir(path+'/logs')
    contenido=os.listdir(path+'/logs')
    if(contenido == []):
        print("Crea Archivo porque no existe nada")
        logs_archivo_leido= pd.DataFrame({'nombre_Archivo': [], 'fecha': []})
        logs_archivo_leido.to_csv('archivo_log.txt', sep= '	', index_label=False)
    else:
        print("Valida si el archivo esta:")
        a=0
        for i in contenido:
            if(i=='archivo_log.txt'):
                a=a+1
                print("No crea Archivo")
                if a == len(contenido):
                    logs_archivo_leido= pd.DataFrame({'nombre_Archivo': [], 'fecha': []})
                    logs_archivo_leido.to_csv('archivo_log.txt', sep= '	', index_label=False)
        del(a)

create_folder_logs()
create_files_logs()
## leer el archivo log
now=datetime.now()
log=open('archivo_log.txt','a')
log.write('nombre_Archivo zip: {} fecha:{} \n'.format(name_file,now) )
log.close()
print("Se escribio el LOG")
#borrar el archivo ZIP
del(zip_file)
print("Borra restantes")
#Conversar copia
os.remove(path+'/'+name_file+'.zip')
print("Borra restantes")
