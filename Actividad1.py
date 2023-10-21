 #!/bin/python3

import sys
import os
from modulos import comprobar_validez
import hashlib

if not (len(sys.argv) == 3):
    print("ERROR: Numero de parametros incorrecto.")
    print("python3 Actividad1.py <nombre_archivo_base> <nombre_carpeta_a_comprobar>")
    exit(-1)

p1_nombre_archivo_base = sys.argv[1]
p2_nombre_carpeta_a_comprobar = sys.argv[2]

def conseguir_mayor_num_ceros(relacion_fich_nceros):
    # Devuelve el numero mayor de 0 de la lista
    # No devuelve el elemento
    if len(relacion_fich_nceros) == 0:
        return 0

    key_max = max(relacion_fich_nceros, key=lambda x: relacion_fich_nceros[x]['longitud_0'])

    return relacion_fich_nceros[key_max]['longitud_0']

def conseguir_primero_ord_crono(relacion_fich_nceros):
    # Devuelve el primer elemento por orden
    # cronologico de creacion del fichero
    # secuencia_con_mayor_ceros = max(secuencias_hex, key=secuencias_hex.get)
    if len(relacion_fich_nceros) == 0:
        raise "La lista no puede estar vacia"

    return max(relacion_fich_nceros, key=lambda x: relacion_fich_nceros[x]['fecha_modif'])

def conseguir_ganador(relacion_fich_nceros):
    # 1. Llama a conseguir_mayor_num_nceros
    # 2. Filtra aquellos ficheros con ese num de ceros
    # 3. Llama a conseguir_primero_ord_crono con la lista 
    #    filtrada
    # 4. Devuelve el ganador

    lista_filtrada = {k: v for k, v in relacion_fich_nceros.items() if v['valido']}

    mayor_num_ceros = conseguir_mayor_num_ceros(relacion_fich_nceros)
    lista_filtrada = {k: v for k, v in relacion_fich_nceros.items() if v['longitud_0'] == mayor_num_ceros and v['valido']}
    
    if len(lista_filtrada) == 0:
        raise "No hay elementos validos en la carpeta"

    return conseguir_primero_ord_crono(lista_filtrada)
    

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