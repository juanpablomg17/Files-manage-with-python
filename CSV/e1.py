import csv

def MostrarTamano():
    with open('../data/Cap1/subvenciones.csv', encoding='latin1') as file:
        lector = csv.reader(file)
        
        next(lector, None)  # Se salta la cabecera
        importe_total = 0
        for linea in lector:
            importe_str = linea[2]
            importe = float(importe_str)
            importe_total = importe_total + importe
        print(importe_total)


# También podemos calcular las subvenciones por centro almacenando un diccionario que tenga como clave
# el nombre del centro y como valor las subvenciones recibidas:

def CalcularSubvenciones():
    with open('../data/Cap1/subvenciones.csv', encoding='latin1') as fichero_csv:
        lector = csv.reader(fichero_csv)
        next(lector, None)
        asociaciones = {}
        for linea in lector:
            centro = linea[0]
            subvencion = float(linea[2])
            if centro in asociaciones:
                asociaciones[centro] = asociaciones[centro] + subvencion
            else:
                asociaciones[centro] = subvencion
        print(asociaciones)

# Es también posible cargar el fichero como un diccionario. En este caso cada una de las filas
# será un diccionario en el que la clave será el nombre dado en la cabecera del fichero y el valor 
# el indicado en esa fila. De esta manera podemos acceder a los valores usando nombres y no la posición
# , lo que nos permite escribir un código más intuitivo. A continuación mostramos cómo sería el código
#  para calcular el diccionario de subvenciones mostrado anteriormente de esta manera:

def ComoDiccionario():
    with open('../data/Cap1/subvenciones.csv', encoding='latin1') as fichero_csv:
        dict_lector = csv.DictReader(fichero_csv)
        asociaciones = {}
        for linea in dict_lector:
            centro = linea['Asociación']
            subvencion = float(linea['Importe'])
            if centro in asociaciones:
                asociaciones[centro] = asociaciones[centro] + subvencion
            else:
                asociaciones[centro] = subvencion
        print(asociaciones)


def AsignarNombresCampos():
    with open('../../data/Cap1/subvenciones.csv', encoding='latin1') as fich_lect, open('../../data/Cap1/subvenciones_esc.csv', 'w', encoding='latin1') as fich_escr:
    dict_lector = csv.DictReader(fich_lect)
    campos = dict_lector.fieldnames + ['Justificación requerida', 'Justificación recibida']
    escritor = csv.DictWriter(fich_escr, fieldnames=campos)
    escritor.writeheader()
    for linea in dict_lector:
        if float(linea['Importe']) > 300:
            linea['Justificación requerida'] = "Sí"
        else:
            linea['Justificación requerida'] = "No"
        linea['Justificación recibida'] = "No"
        escritor.writerow(linea)