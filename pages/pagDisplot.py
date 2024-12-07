from fasthtml.common import *
from grafico import *
from pages.common import *

columnasSelecDisplot = [
    "ANIO", "C377", "CONGLOMERADO", "MUESTRA", "SELVIV", 
    "ESTRATO", "AREA_ENCUESTA", "CCDD", "C203", "OCUP300", "C208"
]

def seleccionDisplot():
    return Div(
        Div(
            formulario(graficoSelect,"tipoGrafico","/graficas","DISPLOT"),
            cls="flex-grow text-center p-2"
            ),
        Div(
            formulario(columnasSelecDisplot,"data","/graficaDisplot","Seleccione una columna"),
            cls="flex-grow text-center p-2"
            ),
        cls="flex flex-row justify-center items-center p-4 bg-gradient-to-r from-blue-900 to-purple-700 pb-8"
    )

def graficaDisplot(data: str, datos):
    return Div(
        Div(
            Div(
                datoGraficoDisplot(data, datos), 
                cls="flex flex-col items-center space-y-2 justify-center p-2"
            ),
            cls="flex-grow text-center p-2"
            ),
        cls="flex flex-row justify-center items-center p-4 bg-gradient-to-r from-blue-900 to-purple-700 pb-8"
    )


