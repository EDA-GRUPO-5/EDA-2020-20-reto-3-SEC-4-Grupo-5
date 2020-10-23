import sys
import config
from DISClib.ADT import list as lt
from time import process_time 
from App import controller
assert config
from DISClib.ADT import orderedmap as om
import datetime

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
    print("6- Estado")
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

    elif int(inputs[0]) == 6:
        initialDate = input("\nIngrese la fecha inicial (YYYY-MM-DD): ")
        finalDate = input("\nIngrese la fecha final (YYYY-MM-DD): ")
        t1_start = process_time()
        estado = controller.getAccidentsByState(cont,initialDate, finalDate)
        t1_stop= process_time()
        print("\nEstado: " + estado)        
        time = t1_stop - t1_start
        print("\nTiempo de ejecución: " + str(time))
        
    else:
        sys.exit(0)
sys.exit(0)
