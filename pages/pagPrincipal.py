from fasthtml.common import *
from pages.common import *

def contenido_principal():
    return Div(
        Div(
            H1(
                "Indicadores del Mercado Laboral 2022 - EPEN", 
                cls="text-3xl md:text-5xl font-bold text-white mb-4 z-10"
            ),
            P(
                "Proporcionar en el corto plazo indicadores de la dinámica del mercado laboral e información ",
                Br("de coyuntura, a nivel nacional y en las 26 principales ciudades."),
                cls="text-base md:text-lg text-gray-300 mb-6 z-10"
            ),
            Div(
                A("Objetivos", href="#section1", cls="bg-purple-600 text-white font-semibold py-2 px-4 rounded-lg z-10"),
                A("Gráficas", href="#section2", cls="bg-purple-600 text-white font-semibold py-2 px-4 rounded-lg z-10"),
                cls="flex space-x-4 z-10"
            ),
            cls="flex flex-col justify-start space-y-4 z-10"  # Contenido alineado a la izquierda
        ),
        Img(
            src="https://www.elespectador.com/resizer/v2/KY3RPLQJZNDILEAWPNSXAWA6AI.jpg?auth=0f899613ff69893e08a5145a2474af67c64c5ef234e953e77a47f393306d789c&width=920&height=613&smart=true&quality=60", 
            alt="Marketing Funnel", 
            cls="w-1/3 max-w-xs md:max-w-sm lg:max-w-md xl:max-w-lg z-0",  # Control de tamaño adaptable
            style="border-radius: 15px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); margin-left: auto; margin-right: 30px;"  # Alineación a la derecha y margen
        ),
        cls="relative flex flex-row items-center justify-between h-screen bg-gradient-to-r from-blue-900 to-purple-700 text-left p-6"
    )   

def seccion_cuadros():
    return Div(
        H2("OBJETIVO PRINCIPAL", cls="text-2xl md:text-3xl font-bold text-center mb-6 pt-6"),
        Div(
            P(
                "El objetivo principal de este estudio es analizar las tasas de desempleo juvenil en las diferentes regiones del Perú, utilizando el dataset disponible en el portal de Datos Abiertos del Perú, con el fin de identificar patrones de desigualdad en el acceso al empleo juvenil y comprender las causas estructurales que limitan las oportunidades laborales de los jóvenes.",
                cls="text-sm md:text-lg text-gray-600 text-center p-4 md:p-10"
            ),
            cls="bg-white rounded-lg shadow-lg p-6 m-4 transform transition duration-300 ease-in-out hover:scale-105 hover:shadow-3xl",
            style="margin: 0 auto; width: 80%;"
        ),
        Br(), Br(), Br(),
        H2("OBJETIVOS ESPECÍFICOS", cls="text-2xl md:text-3xl font-bold text-center mb-6"),
        Div(
            # Cuadro 1
            Div(
                H3("Análisis de las tasas de desempleo regionales", cls="font-semibold text-xl md:text-3xl text-purple-500 mb-4 text-center"),
                P("Estudiar las tasas de desempleo juvenil en las 26 ciudades más grandes del Perú, con un enfoque en identificar regiones con tasas más altas de desempleo juvenil.", cls="text-sm md:text-gray-600 text-center"),
                cls="bg-white rounded-lg border border-transparent shadow-2xl p-4 flex flex-col items-center objetivo-caja transform transition duration-300 ease-in-out hover:scale-105 hover:shadow-3xl",
                style="flex: 1; margin: 0 10px; height: auto;"
            ),
            # Cuadro 2
            Div(
                H3("Identificación de factores estructurales", cls="font-semibold text-xl md:text-3xl text-purple-500 mb-4 text-center"),
                P("Investigar cómo factores estructurales como la infraestructura económica, la educación y el acceso a servicios influyen en las tasas de desempleo juvenil en las diferentes regiones del país.", cls="text-sm md:text-gray-600 text-center"),
                cls="bg-white rounded-lg border border-transparent shadow-2xl p-4 flex flex-col items-center objetivo-caja transform transition duration-300 ease-in-out hover:scale-105 hover:shadow-3xl",
                style="flex: 1; margin: 0 10px; height: auto;"
            ),
            # Cuadro 3
            Div(
                H3("Comparación entre zonas urbanas y rurales", cls="font-semibold text-xl md:text-3xl text-purple-500 mb-4 text-center"),
                P("Comparar las diferencias en las tasas de desempleo juvenil entre zonas urbanas y rurales para entender mejor cómo las características regionales afectan el acceso a oportunidades laborales.", cls="text-sm md:text-gray-600 text-center"),
                cls="bg-white rounded-lg border border-transparent shadow-2xl p-4 flex flex-col items-center objetivo-caja transform transition duration-300 ease-in-out hover:scale-105 hover:shadow-3xl",
                style="flex: 1; margin: 0 10px; height: auto;"
            ),
            cls="flex flex-col md:flex-row md:justify-between p-10"
        ),
        cls="bg-white p-6 shadow-lg rounded-lg",
        id="section1"
    )


def seccion_graficos_referenciales():
    return Div(
        H2("Importancia de los Gráficos", cls="text-2xl md:text-3xl font-bold text-center mb-6 text-white"),
        Div(
            # Tarjeta para Histplot
            Div(
                Div(
                    Img(src="https://python-charts.com/es/distribucion/histograma-seaborn_files/figure-html/histplot-seaborn.png", alt="Ejemplo de Histplot", cls="w-1/2 rounded-lg shadow-md"),
                    Div(
                        H3("Histplot", cls="text-xl font-semibold text-blue-500 mb-2 text-center"),
                        P("Importancia: Permite visualizar la distribución de una variable cuantitativa. Uso: Ideal para identificar la forma de la distribución y detectar anomalías. Aplicación: Utilizado en análisis exploratorio de datos.", cls="text-gray-600 text-center mt-2"),
                        cls="w-1/2 flex flex-col justify-center"
                    ),
                    cls="flex flex-row"
                ),
                cls="bg-white p-4 rounded-lg shadow-lg m-4"
            ),
            # Tarjeta para Boxplot
            Div(
                Div(
                    Img(src="https://interactivechaos.com/sites/default/files/inline-images/tutorial_sns_catplot_09.JPG", alt="Ejemplo de Boxplot", cls="w-1/2 rounded-lg shadow-md"),
                    Div(
                        H3("Boxplot", cls="text-xl font-semibold text-blue-500 mb-2 text-center"),
                        P("Importancia: Muestra la distribución de datos a través de sus cuartiles. Uso: Ayuda a identificar outliers y la simetría de los datos. Aplicación: Comúnmente usado en comparaciones entre grupos.", cls="text-gray-600 text-center mt-2"),
                        cls="w-1/2 flex flex-col justify-center"
                    ),
                    cls="flex flex-row"
                ),
                cls="bg-white p-4 rounded-lg shadow-lg m-4"
            ),
            # Tarjeta para Lineplot
            Div(
                Div(
                    Img(src="https://interactivechaos.com/sites/default/files/inline-images/tutorial_sns_relplot_line_01.JPG", alt="Ejemplo de Lineplot", cls="w-1/2 rounded-lg shadow-md"),
                    Div(
                        H3("Lineplot", cls="text-xl font-semibold text-blue-500 mb-2 text-center"),
                        P("Importancia: Visualiza la relación entre dos variables continuas a lo largo del tiempo. Uso: Ideal para observar tendencias y patrones en los datos temporales. Aplicación: Utilizado en series temporales y análisis de tendencia.", cls="text-gray-600 text-center mt-2"),
                        cls="w-1/2 flex flex-col justify-center"
                    ),
                    cls="flex flex-row"
                ),
                cls="bg-white p-4 rounded-lg shadow-lg m-4"
            ),
            # Tarjeta para Displot
            Div(
                Div(
                    Img(src="https://plantsandpython.github.io/PlantsAndPython/_images/4.6_Seaborn_16_21.png", alt="Ejemplo de Displot", cls="w-1/2 rounded-lg shadow-md"),
                    Div(
                        H3("Displot", cls="text-xl font-semibold text-blue-500 mb-2 text-center"),
                        P("Importancia: Combina histogramas y gráficos de densidad. Uso: Proporciona una vista detallada de la distribución de datos. Aplicación: Utilizado para análisis profundo de distribuciones.", cls="text-gray-600 text-center mt-2"),
                        cls="w-1/2 flex flex-col justify-center"
                    ),
                    cls="flex flex-row"
                ),
                cls="bg-white p-4 rounded-lg shadow-lg m-4"
            ),
            cls="grid grid-cols-1 md:grid-cols-2 gap-8 mt-8"
        ),
        cls="w-full bg-gradient-to-r from-blue-900 to-purple-700 py-10",
        id="section_graficos_referenciales"  # Identificador para que el botón "Gráfica" pueda enlazar aquí
    )


def btnGrafica():
    return Div(
        P(
            "Explora los gráficos estadísticos de los Indicadores del Mercado Laboral y descubre las tendencias importantes.",
            cls="text-lg text-gray-100 mb-4 text-center"
        ),
        A(
            "GRAFICAS",
            href="/graficas",
            cls="bg-purple-600 text-white font-semibold py-3 px-6 rounded-lg shadow-md hover:bg-purple-700 hover:shadow-lg transition-all duration-300"
        ),
        cls="flex flex-col items-center space-y-4 justify-center p-4 pt-10 bg-gradient-to-r from-blue-900 to-purple-700",
    )


def paginaPrincipal():
    return Div(
        cabecera(), 
        contenido_principal(), 
        seccion_cuadros(), 
        btnGrafica(), 
        seccion_graficos_referenciales(),
        piePagina()
    )