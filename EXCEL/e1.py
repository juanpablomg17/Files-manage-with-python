
# Python no tiene una biblioteca estándar para tratar con ficheros Excel, por lo que presentaremos las bibliotecas xlrd y xlwt para lectura y escritura, respectivamente. Estas bibliotecas pueden ser consideradas estándares de facto, aunque presentaremos también brevemente la biblioteca pandas para lectura y escritura de dataframes desde/hacia ficheros Excel. Empezamos cargando las correspondientes bibliotecas:

from xlrd import open_workbook, colname
import xlwt
import pandas

def calSubvencionTotal():
    with open_workbook('../data/Cap1/subvenciones.xls',on_demand=True) as libro:
        asociaciones = {}
        for nombre in libro.sheet_names():
            hoja = libro.sheet_by_name(nombre)
            for i in range(1,hoja.nrows):
                fila = hoja.row(i)
                centro = fila[0].value
                subvencion = fila[2].value
                #print(fila[0].ctype)
                #print(fila[2].value)
                if centro in asociaciones:
                    asociaciones[centro] = asociaciones[centro] + subvencion
                else:
                    asociaciones[centro] = subvencion
        print(asociaciones)



# Ahora crearemos una nueva hoja, en la que tendremos una tabla con los centros, la subvención recibida, la subvención justificada, y la subvención que queda por justificar, que será una fórmula:

def nHojasYModificaciones():
    with open_workbook('../../data/Cap1/subvenciones.xls',on_demand=True) as libro_lect:
        asociaciones = {}
        libro_escr = xlwt.Workbook()
        for nombre in libro_lect.sheet_names():
            hoja_lect = libro_lect.sheet_by_name(nombre)
            hoja_escr = libro_escr.add_sheet(nombre)
            for i in range(hoja_lect.nrows):
                for j in range(hoja_lect.ncols):
                    hoja_escr.write(i, j, hoja_lect.row(i)[j].value)
                if i != 0:
                    fila = hoja_lect.row(i)
                    centro = fila[0].value
                    subvencion = float(fila[2].value)
                    if centro in asociaciones:
                        asociaciones[centro] = asociaciones[centro] + subvencion
                    else:
                        asociaciones[centro] = subvencion
        hoja_escr = libro_escr.add_sheet('Totales')
        hoja_escr.write(0, 0, "Asociación")
        hoja_escr.write(0, 1, "Importe total")
        hoja_escr.write(0, 2, "Importe justificado")
        hoja_escr.write(0, 3, "Restante")
        for i, clave in enumerate(asociaciones):
            fila = i + 1
            fila_form = i + 2
            hoja_escr.write(fila, 0, clave)
            hoja_escr.write(fila, 1, asociaciones[clave])
            hoja_escr.write(fila, 2, 0)
            hoja_escr.write(fila, 3, xlwt.Formula("C" + str(fila_form) + "-" + "B" + str(fila_form)))
        libro_escr.save('../../data/Cap1/subvenciones_totales.xls')


def mostrarColumnas():
    print(colname(2), colname(35))


def cargarYGuardarData():
    with pandas.ExcelFile('../../data/Cap1/subvenciones.xls') as xl:
        writer = pandas.ExcelWriter('../../data/Cap1/subvenciones_df.xls')
        for nombre in xl.sheet_names:
            df = xl.parse(nombre)
            df.to_excel(writer,nombre)
        writer.save()

