from fasthtml.common import *
from grafico import *
from pages.common import *

def sectorSeleccionGrafica():
    return Div(
        Div(
            formulario(graficoSelect,"tipoGrafico","/graficas","Seleccione un grafico"),
            cls="flex-grow text-center p-2", 
            ),
        cls="flex flex-row justify-center items-center p-4 bg-gradient-to-r from-blue-900 to-purple-700 pb-8"
    )

def seccionGraficosReferencia():
    return Div(
        H2("Gráficos Referenciales", cls="text-2xl md:text-3xl font-bold text-center mb-6 text-white"),
        Div(
            # Tarjeta para Histplot
            Div(
                H3("Histplot", cls="text-xl font-semibold text-blue-500 mb-2 text-center"),
                Img(src="https://python-charts.com/es/distribucion/histograma-seaborn_files/figure-html/histplot-seaborn.png", alt="Ejemplo de Histplot", cls="w-full rounded-lg shadow-md"),
                P("Ejemplo de un gráfico de distribución (Histplot)", cls="text-gray-600 text-center mt-2"),
                cls="bg-white p-4 rounded-lg shadow-lg m-4"  # Fondo blanco completo para el cuadro
            ),
            # Tarjeta para Boxplot
            Div(
                H3("Boxplot", cls="text-xl font-semibold text-blue-500 mb-2 text-center"),
                Br(),
                Img(src="https://interactivechaos.com/sites/default/files/inline-images/tutorial_sns_catplot_09.JPG", alt="Ejemplo de Boxplot", cls="w-full rounded-lg shadow-md"),
                P("Ejemplo de un gráfico de caja (Boxplot)", cls="text-gray-600 text-center mt-2"),
                cls="bg-white p-4 rounded-lg shadow-lg m-4"
            ),
            # Tarjeta para Lineplot
            Div(
                H3("Lineplot", cls="text-xl font-semibold text-blue-500 mb-2 text-center"),
                Img(src="https://interactivechaos.com/sites/default/files/inline-images/tutorial_sns_relplot_line_01.JPG", alt="Ejemplo de Lineplot", cls="w-full rounded-lg shadow-md"),
                Br(),
                P("Ejemplo de un gráfico de línea (Lineplot)", cls="text-gray-600 text-center mt-2"),
                cls="bg-white p-4 rounded-lg shadow-lg m-4"
            ),
            # Tarjeta para Displot
            Div(
                H3("Displot", cls="text-xl font-semibold text-blue-500 mb-2 text-center"),
                Br(),
                Img(src="https://plantsandpython.github.io/PlantsAndPython/_images/4.6_Seaborn_16_21.png", alt="Ejemplo de Displot", cls="w-full rounded-lg shadow-md"),
                Br(),
                P("Ejemplo de un gráfico de distribución (Displot)", cls="text-gray-600 text-center mt-2"),
                cls="bg-white p-4 rounded-lg shadow-lg m-4"
            ),
            cls="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mt-8"
        ),
        cls="w-full bg-gradient-to-r from-blue-900 to-purple-700 py-10",
        id="section_graficos_referenciales"  # Identificador para que el botón "Gráfica" pueda enlazar aquí
    )

def paginaGraficas():
    return Div(
        cabecera(),
        sectorSeleccionGrafica(),
        seccionGraficosReferencia(),
        tablaEjemplos(),
        piePagina()
        )
