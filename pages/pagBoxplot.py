from fasthtml.common import *
from grafico import *
from pages.common import *

columnasSelecBoxplot = [
    "C208", "OCUP300", "C377", "C203"
]

def seleccionBoxplot():
    return Div(
        Div(
            formulario(graficoSelect,"tipoGrafico","/graficas","BOXPLOT"),
            cls="flex-grow text-center p-2", 
            ),
        Div(
            formulario(columnasSelecBoxplot,"data","/graficaBoxplot","Seleccione una columna"),
            cls="flex-grow text-center p-2",
            ),
        cls="flex flex-row justify-center items-center p-4 bg-gradient-to-r from-blue-900 to-purple-700 pb-8"
    )

def graficaBoxplot(data: str, datos):
    return Div(
        Div(
            Div(
                datoGraficoBoxplot(data, datos), 
                cls="flex flex-col items-center space-y-2 justify-center p-2"
            ),
            cls="flex-grow text-center p-2",
            ),
        cls="flex flex-row justify-center items-center p-4 bg-gradient-to-r from-blue-900 to-purple-700 pb-8"
    )