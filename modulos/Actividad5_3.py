#!/bin/python3

import hashlib
import re
import os


def comprobar_ultima_linea(ultima_linea):
    patron = re.compile(r'^[0-9a-f]{8}(\t|\s+)[0-9a-f]{2}(\t|\s+)100')
    return bool(patron.match(ultima_linea))

def main(f1,f2):

    f_1 = open(f1, "rb")
    contenido_fichero_1 = f_1.read()

    f_2 = open(f2, "rb")
    contenido_fichero_2 = f_2.read()

        
    sha256 = hashlib.sha256()
    sha256.update(contenido_fichero_2)
    digest_2 = sha256.hexdigest()

    # num_filas_f1 = len(contenido_fichero_2.decode().splitlines())
    num_filas_f1 = sum(1 for _ in open(f1))
    num_filas_f2 = sum(1 for _ in open(f2))

    # Condiciones
    empiezan_igual = contenido_fichero_2.startswith(contenido_fichero_1)
    empieza_con_cero = digest_2.startswith("0")
    ultima_linea = comprobar_ultima_linea(contenido_fichero_2.decode().splitlines()[-1])
    ultima_linea_seguida = num_filas_f2 == (num_filas_f1 + 1) 

    # Resultados
    valido = empieza_con_cero and empiezan_igual and ultima_linea and ultima_linea_seguida
    num_0 = len(digest_2)-len(digest_2.lstrip('0'))
    fecha_modif = os.stat(f2).st_mtime

    return (valido,num_0,fecha_modif)
