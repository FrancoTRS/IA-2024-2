from fasthtml.common import *
from grafico import *
from pages.common import *

columnasSelectHisplot = [
    "ANIO", "C377", "CONGLOMERADO", "MUESTRA", "SELVIV", 
    "ESTRATO", "AREA_ENCUESTA", "C203", "OCUP300", "C208"
]

def seleccionHisplot():
    return Div(
        Div(
            formulario(graficoSelect,"tipoGrafico","/graficas","HISPLOT"),
            cls="flex-grow text-center p-2", 
            ),
        Div(
            formulario(columnasSelectHisplot,"data","/graficaHisplot","Seleccione una columna"),
            cls="flex-grow text-center p-2",
            ),
        cls="flex flex-row justify-center items-center p-4 bg-gradient-to-r from-blue-900 to-purple-700 pb-8"
    )

def graficaHisplot(data: str, datos):
    return Div(
        Div(
            Div(
                datoGraficoHisplot(data, datos),
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
    if data == "ANIO":
        return "Representa el año de ejecución de la encuesta. Este gráfico puede ayudar a identificar la distribución de datos recolectados por año, útil para detectar tendencias temporales o cambios en las características estudiadas."
    elif data == "C377":
        return "Indica la percepción de la persona sobre su identidad étnica basada en costumbres y antepasados. El histograma puede revelar la diversidad cultural de la población encuestada."
    elif data == "CONGLOMERADO":
        return "Código del conglomerado asignado en el diseño muestral. Los gráficos de esta variable pueden reflejar el tamaño relativo o la distribución de los conglomerados incluidos en el estudio."
    elif data == "MUESTRA":
        return "Tamaño de la muestra seleccionada para cada conglomerado. El histograma puede mostrar la variabilidad en el tamaño de las muestras utilizadas en el estudio."
    elif data == "SELVIV":
        return "Número de selección de la vivienda dentro del conglomerado. Un histograma de esta variable puede ayudar a analizar la distribución de viviendas encuestadas, asegurando una selección adecuada."
    elif data == "ESTRATO":
        return "Clasificación del estrato poblacional, generalmente en función de características socioeconómicas. Los gráficos pueden destacar cómo se distribuyen los datos según los diferentes estratos."
    elif data == "AREA_ENCUESTA":
        return "Diferencia entre áreas urbanas (1) y rurales (2). Este gráfico es útil para visualizar la proporción de datos recolectados en áreas geográficas distintas."
    elif data == "C203":
        return "Relación de parentesco con el jefe del hogar. Un gráfico de esta variable puede resaltar las composiciones familiares predominantes en la población encuestada."
    elif data == "OCUP300":
        return "Nivel de ocupación laboral de las personas de 14 años o más. Este gráfico puede proporcionar una visión general sobre la situación laboral de la población encuestada."
    else:
        return "Edad de las personas encuestadas en años cumplidos. El histograma puede ilustrar la distribución etaria, permitiendo observar si la muestra está balanceada en términos de edad."

def ConclusionGrafica(variable):
    if variable == "ANIO":
        return "Solo se muestra en el año 2022"
    elif variable == "C377":
        return "El histograma con una curva de densidad superpuesta muestra que la mayoría de los encuestados se identifican como mestizos (valor 7), lo que refleja una mezcla predominante de ascendencia indígena y europea en la población estudiada. La curva de densidad tiene su pico en el valor 7 y disminuye rápidamente hacia otros valores, respaldando la observación de que la identificación mestiza es la más común. Valores como Quechua (1), Aymara (2), Negro/Moreno/Zambo/Mulato/Pueblo Afro peruano o Afrodescendiente (5), Blanco (6), Nativo o Indígena de la Amazonía (3) y Otro (8) tienen una representación menor, indicando que estas identidades culturales y étnicas son menos frecuentes en la población encuestada. Esto sugiere una diversidad cultural, pero con una predominancia mestiza, y puede ser útil para diseñar políticas públicas que consideren estas distribuciones demográficas y culturales."
    elif variable == "CONGLOMERADO":
        return "El histograma con la curva de densidad superpuesta muestra la distribución de la variabl CONGLOMERADO. Se observa que la mayoría de los conglomerados tienen valores concentrados entre 0 y 200,000, con una frecuencia máxima cerca de 175, lo que sugiere una alta representatividad de estos conglomerados en el estudio. También hay una menor concentración de conglomerados alrededor de 600,000 a 700,000, con una frecuencia más baja, indicando menos representatividad. Este gráfico nos permite visualizar cómo están distribuidos los conglomerados en el diseño muestral, ayudando a entender la estructura y la representatividad de la muestra en el estudio."
    elif variable == "MUESTRA":
        return "El histograma con la curva de densidad superpuesta muestra la distribución del tamaño de las muestras seleccionadas para cada conglomerado. En el eje horizontal se encuentran los valores de la variable MUESTRA, que representan diferentes tamaños de muestra, mientras que en el eje vertical se muestra la frecuencia de estos tamaños. La mayoría de las muestras se concentran entre 0 y 5, con una frecuencia alta en este rango, indicando que la mayoría de los conglomerados tienen muestras de tamaño pequeño. También hay una barra más pequeña alrededor del valor 20, lo que sugiere que hay unos pocos conglomerados con tamaños de muestra mayores. Este gráfico permite visualizar la variabilidad en el tamaño de las muestras utilizadas en el estudio, proporcionando información sobre cómo se distribuyen las muestras entre los conglomerados y ayudando a asegurar que la selección de muestras sea representativa del diseño muestral."
    elif variable == "SELVIV":
        return "El histograma con la curva de densidad superpuesta muestra la distribución de la variable que representa el número de selección de la vivienda dentro del conglomerado. En el eje horizontal se encuentran los valores de SELVIV, y en el eje vertical, la frecuencia de estos valores. La mayor concentración de datos se encuentra en el rango de 0 a 50, lo que indica que la mayoría de las viviendas seleccionadas están dentro de este rango. La curva de densidad proporciona una visualización más clara de esta distribución, destacando la alta frecuencia en los valores más bajos. Esto sugiere que la selección de viviendas dentro de los conglomerados sigue una distribución donde la mayoría de los números de selección son bajos, lo cual puede ser útil para analizar la representatividad y asegurarse de que la selección de viviendas sea adecuada y equilibrada en el estudio."
    elif variable == "ESTRATO":
        return "En el grafico, la mayor concentración de datos se encuentra en el rango correspondiente al estrato poblacional de 20,000 a 49,999 habitantes (estrato 4.00 a 4.50), lo que indica que la mayoría de los encuestados provienen de UPMs con estas características poblacionales. La curva de densidad sigue la misma tendencia, destacando la alta representatividad de este estrato. Menor frecuencia de datos se observa en los estratos con más y menos población (estrato 1 y estrato 6), lo que sugiere que hay menos encuestados provenientes de UPMs muy grandes o muy pequeñas. Este gráfico es útil para analizar patrones y tendencias dentro de los diferentes estratos de la población y proporciona información valiosa sobre la distribución socioeconómica de los encuestados en el estudio."
    elif variable == "AREA_ENCUESTA":
        return "El histograma con la curva de densidad superpuesta muestra la distribución de las respuestas de la encuesta según el área geográfica, diferenciando entre áreas urbanas (valor 1) y rurales (valor 2). En el eje horizontal se encuentran los valores de AREA_ENCUESTA, mientras que en el eje vertical se muestra la frecuencia de las respuestas. La mayor concentración de respuestas se encuentra en el área urbana (valor 1), lo que indica que un mayor número de encuestas se realizaron en zonas urbanas en comparación con las rurales. La curva de densidad refuerza esta observación, mostrando un pico más alto en el valor 1. Este gráfico es útil para visualizar la proporción de datos recolectados en diferentes áreas geográficas, ayudando a entender mejor la representatividad de la encuesta en términos de distribución urbana y rural."
    elif variable == "C203":
        return "La mayor concentración de respuestas se encuentra en el valor 2 (Esposo/a o compañero/a), indicando que una proporción significativa de los encuestados son esposos/as o compañeros/as del jefe del hogar. A medida que los valores aumentan, la frecuencia de las respuestas disminuye, con excepciones como el valor 3 (Hijo/a o hijastro/a), que también tiene una alta frecuencia. Esta distribución resalta las composiciones familiares predominantes en la población encuestada, proporcionando una visión de cómo están estructuradas las relaciones dentro de los hogares. La curva de densidad suaviza esta distribución, facilitando la identificación de patrones y tendencias en los datos. En resumen, el gráfico revela que la mayoría de los encuestados son esposos/as o compañeros/as y hijos/as o hijastros/as del jefe del hogar, reflejando la estructura familiar típica de la población encuestada."
    elif variable == "OCUP300":
        return "La mayor concentración de datos se encuentra en el valor 1 (Ocupado), indicando que una gran proporción de la población encuestada está empleada. Esto sugiere que la mayoría de las personas de 14 años o más tienen algún tipo de ocupación laboral. A medida que los valores aumentan, la frecuencia de las respuestas disminuye significativamente, con menos encuestados en las categorías de Desempleado Abierto (2), Desempleado Oculto (3) e Inactivos (4). La curva de densidad sigue la forma del histograma, alcanzando su pico en la misma categoría de Ocupado, y disminuyendo hacia los otros valores. Esta distribución proporciona una visión general sobre la situación laboral de la población encuestada, resaltando que la mayoría está ocupada, y ofreciendo información valiosa para comprender la estructura del empleo en la muestra estudiada."
    else:
        return "Los grupos de edad están divididos en cuatro categorías: 0-20, 20-40, 40-60 y 60-80. La mayor concentración de datos se encuentra en el grupo de 20-40 años, seguido por el grupo de 0-20 años, el grupo de 40-60 años y, finalmente, el grupo de 60-80 años con la menor frecuencia. La curva de densidad refuerza esta observación, mostrando un pico en el grupo de 20-40 años. Este gráfico ilustra cómo se distribuye la edad de los encuestados, permitiendo observar si la muestra está balanceada en términos de edad. La información proporcionada al lado del gráfico explica que C208 representa la edad de los encuestados en años cumplidos y destaca la utilidad del histograma para visualizar la distribución etaria. Esta visualización es clave para entender la composición por edad de la muestra y para asegurar que se cubran adecuadamente todas las edades relevantes en el estudio."