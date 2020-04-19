import xml.etree.ElementTree as ET



# Como en los ejemplos anteriores, vamos a empezar recorriendo el fichero y calculando un diccionario con la subvención total para cada centro:

def calDicMostrar():

    arbol = ET.parse('../data/Cap1/subvenciones.xml')
    raiz = arbol.getroot()
    asociaciones = {}
    for fila in raiz:
        centro = fila[0].text
        subvencion = float(fila[2].text)
        if centro in asociaciones:
            asociaciones[centro] = asociaciones[centro] + subvencion
        else:
            asociaciones[centro] = subvencion
    print(asociaciones)

# Igual que ocurría con JSON, el formato XML es más flexible que CVS y Excel y nos permite representar la información de manera más compacta. Vamos a crear un nuevo fichero XML a partir del que tenemos que contará con una raíz que tendrá como elementos las distintas asociaciones. Cada Asociacion tendrá como atributo su nombre y como elementos la subvención Total y la lista de Actividades. La lista de actividades tendrá elemenos Actividad con Nombre y Gasto.

def crearNuevoFichero():
    arbol = ET.parse('../data/Cap1/subvenciones.xml')
    raiz = arbol.getroot()
    nuevo = ET.ElementTree()
    raiz_nueva = ET.Element("Raiz")
    nuevo._setroot(raiz_nueva)
    elem_actual = ET.Element("Asociacion")
    asoc_actual = ""
    actividades = ET.SubElement(elem_actual, "Actividades")
    gasto = 0
    for fila in raiz.findall('Row'):
        asoc = fila.find('Asociaci_n').text
        act = fila.find('Actividad_Subvencionada').text
        imp = float(fila.find('Importe').text)
        if asoc_actual != asoc:
            gas_total = ET.SubElement(elem_actual, "Total")
            gas_total.text = str(gasto)
            elem_actual = ET.SubElement(raiz_nueva, "Asociacion")
            elem_actual.set('nombre', asoc)
            actividades = ET.SubElement(elem_actual, "Actividades")
            gasto = 0
        act_elem = ET.SubElement(actividades, "Actividad")
        nom_elem = ET.SubElement(act_elem, "Nombre")
        nom_elem.text = act
        imp_elem = ET.SubElement(act_elem, "Subvencion")
        imp_elem.text = str(imp)
        gasto = gasto + imp
        asoc_actual = asoc
    nuevo.write('../data/Cap1/subvenciones_lista_total.xml')

crearNuevoFichero()