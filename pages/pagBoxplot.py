from fasthtml.common import *
from grafico import *
from pages.common import *

columnasSelecBoxplot = [
    "C208", "C201", "C377", "C317A"
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
            Div(
                P(f"{data}", cls="text-gray-100 text-xl font-bold text-center w-full"),  # Texto de "data" en negrita y encima del texto descriptivo
                P(textoGrafico(data), cls="text-gray-100 text-lg text-left p-4 max-w-full", style="text-align: justify;"),
                P(ConclusionGrafica(data), cls="text-gray-100 text-lg text-left p-4 max-w-full", style="text-align: justify;"),
                cls="flex flex-col items-center space-y-2 justify-center p-2 max-w-lg"
            ),
            cls="flex flex-row items-center justify-center p-2",
        ),
        cls="flex flex-row justify-center items-center p-4 bg-gradient-to-r from-blue-900 to-purple-700 pb-8"
    )

def textoGrafico(data: str):
    if data == "C208":
        return "Este gráfico muestra la distribución de las edades de los encuestados. A través del boxplot, podemos observar la mediana, los cuartiles y la presencia de valores atípicos en las edades. Esto es útil para identificar la diversidad etaria de la muestra y detectar grupos de edad más representados o extremos que podrían influir en los resultados."
    elif data == "C201":
        return "El boxplot para esta variable analiza diferencias en una característica cuantitativa (como edad o ingresos) según el sexo (1: Masculino, 2: Femenino). Sirve para detectar desigualdades o variaciones entre los géneros, ayudando a analizar el impacto del sexo en los datos recolectados."
    elif data == "C377":
        return "El boxplot para la identidad étnica explora cómo se distribuyen características numéricas relacionadas con cada categoría de identidad. Permite identificar diferencias entre los grupos y detectar valores extremos, proporcionando un panorama de la diversidad cultural dentro de la muestra."
    else:
        return "Este gráfico analiza cómo se distribuyen variables cuantitativas según el nivel de instrucción alcanzado por los encuestados. Ayuda a visualizar diferencias entre niveles educativos y la existencia de valores extremos, aportando información clave sobre las oportunidades educativas en la población."

def ConclusionGrafica(variable):
    if variable == "C208":
        return "El boxplot titulado Boxplot de C208 por ESTRATO muestra la distribución de la variable C208 (edades de los encuestados) a través de diferentes estratos socioeconómicos. Los valores de **C208** están agrupados en diferentes edades y cada caja del boxplot representa los cuartiles y la mediana de las edades dentro de cada estrato. Por ejemplo, en el estrato 4.00, la mediana de las edades es de aproximadamente 35 años, con un rango intercuartílico de 25 a 45 años. En contraste, el estrato 6.00 muestra una mediana más baja, alrededor de 25 años, con un rango intercuartílico de 20 a 30 años. Los puntos fuera de los bigotes representan edades atípicas, lo que destaca la presencia de encuestados mucho más jóvenes o mayores que el rango medio. Este gráfico ayuda a visualizar la diversidad etaria de la muestra y detectar grupos de edad más representados o extremos que podrían influir en los resultados del estudio."
    elif variable == "C201":
        return "El boxplot titulado Boxplot de C201 por ESTRATO muestra la distribución de la variable C201, que representa el sexo de los encuestados, clasificado por diferentes estratos socioeconómicos. Los valores de **C201** son 1 (Masculino) y 2 (Femenino). Cada caja en el gráfico muestra la mediana y los cuartiles de la variable C201 para cada estrato, permitiendo comparar las diferencias en la distribución del sexo en diversos estratos. Por ejemplo, en el estrato 5000, la mediana es 1,5, indicando una distribución relativamente equilibrada entre hombres y mujeres. Los límites superior e inferior de las cajas representan el rango intercuartílico, y los puntos fuera de los bigotes son valores atípicos que destacan diferencias significativas en la distribución del sexo. Este gráfico es útil para detectar desigualdades o variaciones entre los géneros en diferentes contextos socioeconómicos, proporcionando información valiosa sobre cómo el sexo se distribuye a través de los estratos y ayudando a analizar el impacto del sexo en los datos recolectados."
    elif variable == "C377":
        return "El boxplot muestra la distribución de la variable C377, que representa la identidad étnica de los encuestados, a través de diferentes estratos socioeconómicos. Los valores de C377 incluyen identidades como Quechua, Aymara, Blanco, Mestizo, entre otros. Cada caja representa la mediana y los cuartiles de estos valores por estrato. Por ejemplo, en el estrato 5000, la mediana es 7, indicando que la mayoría se identifica como mestizos, mientras que en el estrato 9998, la mediana es 6, indicando una mayor identificación como blancos. Los valores atípicos muestran identidades menos comunes en cada estrato. Este gráfico permite visualizar la diversidad étnica y comparar cómo varía entre diferentes contextos socioeconómicos."
    else:
        return "El boxplot muestra la distribución del número de personas que trabajan en el negocio (C317A) en diferentes estratos socioeconómicos. Cada caja en el gráfico representa los cuartiles y la mediana del número de empleados en cada estrato. Por ejemplo, en el estrato 2, la mediana es de 3 empleados, con el 50% central de los datos concentrado entre 1 y 5 empleados. En el estrato 10, la mediana es de 4 empleados, con un rango intercuartílico de 2 a 6 empleados. Los valores atípicos, que son puntos fuera de los bigotes del boxplot, indican negocios significativamente más grandes o más pequeños. Este gráfico permite visualizar y comparar el tamaño de los negocios en diferentes contextos socioeconómicos, revelando patrones y diferencias clave entre los estratos y proporcionando una mejor comprensión del mercado laboral en la población estudiada."