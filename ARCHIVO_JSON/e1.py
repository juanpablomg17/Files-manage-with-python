import json

# Los objetos JSON se cargan en Python como diccionarios, mientras que los arrays JSON se traducen 
# como listas Python. Con esta información podemos usar load para cargar y visualizar el fichero:




def CargarYMostrarInfoFiltrada():
    with open('../data/Cap1/subvenciones.json', encoding='utf-8') as fich_lect, open('../data/Cap1/subvenciones_agrupadas.json', 'w', encoding='utf-8') as fich_escr:
        data = json.load(fich_lect)
        print(data[0:2])

def ModificarYGuardarNuevoJson():
    with open('../data/Cap1/subvenciones.json', encoding='utf-8') as fich_lect, open('../data/Cap1/subvenciones_agrupadas.json', 'w', encoding='utf-8') as fich_escr:
        data = json.load(fich_lect)
        asoc_str = "Asociación"
        act_str = "Actividad Subvencionada"
        imp_str = "Importe en euros"
        lista = []
        lista_act = []
        asoc_actual = ""
        dicc = {}
        for elem in data:
            asoc = elem[asoc_str]
            act = elem[act_str]
            imp = elem[imp_str]
            if asoc_actual != asoc:
                dicc["Actividades"] = lista_act
                dicc = {"Asociación": asoc}
                lista.append(dicc)
                lista_act = []
            lista_act.append({act_str : act, imp_str : imp})
            asoc_actual = asoc
        print(lista)
        json.dump(lista, fich_escr, ensure_ascii=False, indent=4) # , sort_keys=False
 


# Intentemos ahora calcular, como hicimos para CSV, el total de gasto para cada centro y almacenarlo como un nuevo campo de la estructura que hemos creado arriba. El código necesario para ello es:

def CalTotalGasto():
        with open('../data/Cap1/subvenciones.json', encoding='utf-8') as fich_lect, open('../data/Cap1/subvenciones_agrupadas_error.json', 'w', encoding='utf-8') as fich_escr:
            data = json.load(fich_lect)
            asoc_str = "Asociación"
            act_str = "Actividad Subvencionada"
            imp_str = "Importe en euros"
            lista = []
            lista_act = []
            asoc_actual = ""
            dicc = {}
            gasto = 0
            for elem in data:
                asoc = elem[asoc_str]
                act = elem[act_str]
                imp = float(elem[imp_str])
                if asoc_actual != asoc:
                    dicc["Actividades"] = lista_act
                    dicc["Gasto"] = gasto
                    dicc = {"Asociación": asoc}
                    lista.append(dicc)
                    lista_act = []
                    gasto = 0
                lista_act.append({act_str : act, imp_str : imp})
                gasto = gasto + imp
                asoc_actual = asoc
            print(lista)
            json.dump(lista, fich_escr, ensure_ascii=False, indent=4) # , sort_keys=False

    
def CalTotalGasto2():
    with open('../../data/Cap1/subvenciones.csv', encoding='latin1') as fich_lect, open('../../data/Cap1/subvenciones_agrupadas_con_gasto.json', 'w', encoding='utf-8') as fich_escr:
        dict_lector = csv.DictReader(fich_lect)
        asoc_str = "Asociación"
        act_str = "Actividad Subvencionada "
        imp_str = "Importe"
        lista = []
        lista_act = []
        asoc_actual = ""
        dicc = {}
        gasto = 0
        for linea in dict_lector:
            asoc = linea[asoc_str]
            act = linea[act_str]
            imp = float(linea[imp_str])
            if asoc_actual != asoc:
                dicc["Actividades"] = lista_act
                dicc["Gasto"] = gasto
                dicc = {"Asociación": asoc}
                lista.append(dicc)
                lista_act = []
                gasto = 0
            lista_act.append({act_str : act, imp_str : imp})
            gasto = gasto + imp
            asoc_actual = asoc
        json.dump(lista, fich_escr, ensure_ascii=False, indent=4) # , sort_keys=False