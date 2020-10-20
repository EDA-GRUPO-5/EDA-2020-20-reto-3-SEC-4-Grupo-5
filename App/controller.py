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

import config as cf
from App import model
import datetime
import csv
from DISClib.ADT import orderedmap as om

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    accidentsfile = cf.data_dir + accidentsfile
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),
                                delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    return analyzer

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def accidentsSize(analyzer):
    """
    Numero de accidentes leidos
    """
    return model.accidentSize(analyzer)


def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)


def getAccidentsBySeverity(analyzer, initialDate):
    try:
        initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
        if om.contains(analyzer['dateIndex'], initialDate.date()) == False:
            return "fecha"
        else:
            severity1 = int(model.getAccidentsBySeverity(analyzer, initialDate.date(), '1'))
            severity2 = int(model.getAccidentsBySeverity(analyzer, initialDate.date(), '2'))
            severity3 = int(model.getAccidentsBySeverity(analyzer, initialDate.date(), '3'))
            severity4 = int(model.getAccidentsBySeverity(analyzer, initialDate.date(), '4'))
            total = severity1 + severity2 + severity3 +severity4
            return (total, severity1, severity2, severity3, severity4)
    except:
        return "formato"


def getAccidentsBeforeDate(analyzer, finalDate):
    try:
        finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
        if om.contains(analyzer['dateIndex'], finalDate.date()) == False:
            return "fecha"
        else:    
            return model.getAccidentsBeforeDate(analyzer,finalDate.date())
    except:
        return "formato"
     
     
def getAccidentsByDates(analyzer, initialDate, finalDate):
    """
    Retorna el total de accidentes en un rango de fechas
    """
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    return model.getAccidentsByRange(analyzer, initialDate.date(), finalDate.date())
   

def getAccidentsByHours(analyzer, initialHour, finalHour):
    """
    Retorna el total de accidentes en un rango de horas
    """
    initialHour = datetime.datetime.strptime(initialHour, '%H:%M')
    finalHour = datetime.datetime.strptime(finalHour, '%H:%M')
    return model.getAccidentsByHours(analyzer, initialHour, finalHour)


def getAccidentsByDate(analyzer, accidentDate):
    accidentDate = datetime.datetime.strptime(accidentDate, '%Y-%m-%d')
    return model.getAccidentsByDate(analyzer, accidentDate.date())     


