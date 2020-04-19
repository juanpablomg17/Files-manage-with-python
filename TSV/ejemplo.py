import csv


# El formato TSV es similar al CSV, pero en el caso de TSV las columnas se separan con tabuladores.
#  Para crear y manipular estos ficheros seguiremos usando la biblioteca csv, usando la opción delimiter=
#  '\t'. Por ejemplo, podemos crear un fichero TSV a partir del CSV anterior simplemente usando esta opción
#   al crear el objeto escritor:

def tsv():    
    with open('../data/Cap1/subvenciones.csv', encoding='latin1') as fich_lect, open('../ data/Cap1/subvenciones.tsv', 'w', encoding='latin1') as fich_escr:
        dict_lector = csv.DictReader(fich_lect)
        campos = dict_lector.fieldnames
        escritor = csv.DictWriter(fich_escr, delimiter='\t', fieldnames=campos)
        escritor.writeheader()
        for linea in dict_lector:
            escritor.writerow(linea)


# Una vez creado el fichero, podemos recorrerlo como hacíamos arriba, eligiendo como separador el tabulador. 
# La función siguiente calcula las subvenciones por centro como hicimos con CSV:

def Mostrar():
    with open('../data/Cap1/subvenciones.tsv', encoding='latin1') as fichero:
        dict_lector = csv.DictReader(fichero, delimiter='\t')
        asociaciones = {}
        for linea in dict_lector:
            centro = linea['Asociación']
            subvencion = float(linea['Importe'])
            if centro in asociaciones:
                asociaciones[centro] = asociaciones[centro] + subvencion
            else:
                asociaciones[centro] = subvencion
        print(asociaciones)

Mostrar()





