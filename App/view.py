"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from time import process_time 
from App import controller
assert config
from DISClib.ADT import orderedmap as om
import datetime

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

large = 'US_Accidents_Dec19.csv'
large_2016 = 'us_accidents_dis_2016.csv'
large_2017 = 'us_accidents_dis_2017.csv'
large_2018 = 'us_accidents_dis_2018.csv'
large_2019 = 'us_accidents_dis_2019.csv'
small = 'us_accidents_small.csv'
smaller = 'us_accidents_smaller.csv'
accidentsfile = small

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Conocer los accidentes en una fecha (REQ 1)")
    print("4- Conocer los accidentes anteriores a una fecha (REQ 2)")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de accidentes....")
        t1_start = process_time()
        controller.loadData(cont, accidentsfile)
        t1_stop= process_time()
        print('\nAccidentes cargados: ' + str(controller.accidentsSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
        time = t1_stop - t1_start
        print("\nTiempo de ejecución: " + str(time))

    elif int(inputs[0]) == 3:
        initialDate = input("\nIngrese la fecha (YYYY-MM-DD): ")
        t1_start = process_time()
        severityTuple = controller.getAccidentsBySeverity(cont,initialDate)
        t1_stop= process_time()
        if severityTuple == "fecha":
            print('\nPor favor ingrese una fecha que se encuentre en el archivo.')
        elif severityTuple == "formato":
            print("\nPor favor ingrese un formato de fecha válido.")
        else:
            print("\nEn " + initialDate + " ocurrieron " + str(severityTuple[0]) + " accidentes." + 
                " Sus severidades fueron: \n\nSeveridad 1: " + str(severityTuple[1]) + "\nSeveridad 2: " + str(severityTuple[2]) +
                "\nSeveridad 3: " + str(severityTuple[3]) + "\nSeveridad 4: " + str(severityTuple[4]))        
        time = t1_stop - t1_start
        print("\nTiempo de ejecución: " + str(time))

    elif int(inputs[0]) == 4:
        finalDate = input("\nIngrese la fecha (YYYY-MM-DD): ")
        t1_start = process_time()
        beforeTuple = controller.getAccidentsBeforeDate(cont,finalDate)
        t1_stop = process_time()
        if beforeTuple == "fecha":
            print('\nPor favor ingrese una fecha que se encuentre en el archivo.')
        elif beforeTuple == "formato":
            print("\nPor favor ingrese un formato de fecha válido.")
        else:
            print("\nLa cantidad de accidentes ocurridos antes de " + finalDate + " fue: " + str(beforeTuple[0]) + 
                    " y la fecha en la que más ocurrieron accidentes fue: " + str(beforeTuple[1]) + ".")
        time = t1_stop - t1_start
        print("\nTiempo de ejecución: " + str(time))

    else:
        sys.exit(0)
sys.exit(0)
