 #!/bin/python3

import sys
import os
from modulos import comprobar_validez
import random

if not (len(sys.argv) == 3):
    print("ERROR: Numero de parametros incorrecto.")
    print("python3 Actividad1.py <nombre_archivo_base> <nombre_carpeta_a_comprobar>")
    exit(-1)

p1_nombre_archivo_base = sys.argv[1]
p2_nombre_carpeta_a_comprobar = sys.argv[2]

def conseguir_ganador(relacion_fich_nceros):
    # 1. Filtrar los candidatos validos
    # 2. Sortear el ganador entre los candidatos validos
    # 3. Devuelve el ganador

    lista_filtrada = {k: v for k, v in relacion_fich_nceros.items() if v['valido']}

    return random.choice(list(lista_filtrada.keys()))
    

def conseguir_relacion_nceros(nombre_archivo_base, nombre_carpeta):
    # Devuelve una lista con los archivos asociados a
    # su longitud de 0, validez y fecha de modificacion
    
    relacion_fich_nceros = {}
    
    for v in os.walk(nombre_carpeta, topdown=True):
        (_,_,files) = v 
        for file_name in files:
            (valido,longitud_0,fecha_modif) = comprobar_validez(nombre_archivo_base,os.path.join(nombre_carpeta,file_name))
            relacion_fich_nceros[file_name] = {"valido": valido, "longitud_0": longitud_0, "fecha_modif":fecha_modif}
        return relacion_fich_nceros

def imprimir_relacion_fich(relacion_fich_nceros):
    lista_ordenada = {k: v for k, v in sorted(relacion_fich_nceros.items(), key=lambda x: (x[1]['valido'],x[1]['longitud_0'],x[1]['fecha_modif']),reverse=True)}
    for (nombre_archivo,datos) in lista_ordenada.items():
        str_longitud_0 = str(datos['longitud_0']) if datos['valido'] else 'No valido'
        print(nombre_archivo + " : " + str_longitud_0)

def main():
    relacion_fich_nceros = conseguir_relacion_nceros(p1_nombre_archivo_base,p2_nombre_carpeta_a_comprobar)
    ganador = conseguir_ganador(relacion_fich_nceros)

    imprimir_relacion_fich(relacion_fich_nceros)
    
    print("Ganador: " + ganador)


if __name__ == "__main__":
    main()