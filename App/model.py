import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------

def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los accidentes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'accidents': None,
                'dateIndex': None
                }

    analyzer['accidents'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['dateIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    return analyzer

# Funciones para agregar informacion al catalogo

def addAccident(analyzer, accident):
    """
    """
    lt.addLast(analyzer['accidents'], accident)
    updateDateIndex(analyzer['dateIndex'], accident)
    return analyzer

def updateDateIndex(map, accident):
    """
    Se toma la fecha del accidente y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de accidentes
    y se actualiza el indice de tipos de accidentes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de accidentes
    """
    start_time = accident['Start_Time']
    accidentdate = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, accidentdate.date())
    if entry is None:
        datentry = newDataEntry(accident)
        om.put(map, accidentdate.date(), datentry)
    else:
        datentry = me.getKey(entry)
    addDateIndex(datentry, accident)
    return map

def addDateIndex(datentry, accident):
    """
    Actualiza un indice de tipo de accidentes.  Este indice tiene una lista
    de accidentes y una tabla de hash cuya llave es el tipo de accidentes y
    el valor es una lista con los accidentes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstaccidents']
    lt.addLast(lst, accident)
    stateIndex = datentry['stateIndex']
    offentry = m.get(stateIndex,accident['State'])
    if (offentry is None):
        entry = newStateEntry(accident['State'], accident)
        lt.addLast(entry['lststate'], accident)
        m.put(stateIndex,accident['State'],entry)
    else:
        entry = me.getKey(offentry)
        lt.addLast(entry['lststate'],accident)
    return datentry

def newDataEntry(accident):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'stateIndex': None, 'lstaccidents': None}
    entry['stateIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareSeverities)
    entry['lstaccidents'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def newStateEntry(stategrp, accident):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'state': None, 'lststate': None}
    ofentry['state'] = stategrp
    ofentry['lststate'] = lt.newList('SINGLE_LINKED', compareSeverities)
    return ofentry

# ==============================
# Funciones de consulta
# ==============================

def accidentSize(analyzer):
    """
    Número de libros en el catago
    """
    return lt.size(analyzer['accidents'])

def indexHeight(analyzer):
    """Numero de autores leido
    """
    return om.height(analyzer['dateIndex'])

def indexSize(analyzer):
    """Numero de autores leido
    """
    return om.size(analyzer['dateIndex'])

def minKey(analyzer):
    """Numero de autores leido
    """
    return om.minKey(analyzer['dateIndex'])

def maxKey(analyzer):
    """Numero de autores leido
    """
    return om.maxKey(analyzer['dateIndex'])

def getAccidentsByState(analyzer, initialDate, finalDate):
    accidentdate = om.get(analyzer['dateIndex'], initialDate)
    if accidentdate['key'] is not None:
        statemap = me.getKey(accidentdate)['stateIndex']
        estado = m.get(statemap, finalDate)
        if estado is not None:
            return me.getKey(num['lststate']))
        return estado

# ==============================
# Funciones de Comparacion
# ==============================

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareSeverities(severity1, severity2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    severity = me.getKey(severity2)
    if (severity1 == severity):
        return 0
    elif (severity1 > severity):
        return 1
    else:
        return -1
