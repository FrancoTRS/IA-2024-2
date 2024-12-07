from fasthtml.common import *
from grafico import *
from pages.common import *

columnasSelecDisplot = [
    "C208", "C339_1", "C330", "C377"
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
        return "Este gráfico muestra la distribución de las edades de los encuestados. Permite identificar la concentración de edades predominantes, rangos de edad más comunes y posibles extremos. Es útil para analizar la composición etaria de la población y cómo esta puede influir en otros aspectos, como ingresos, nivel educativo o tamaño de la familia."
    elif data == "C339_1":
        return "El gráfico refleja la distribución de los ingresos personales reportados por los encuestados. Ayuda a observar cómo se agrupan los ingresos en la población, destacando los valores más comunes, la dispersión de los ingresos y la presencia de outliers. Esto es clave para analizar desigualdades económicas y definir perfiles de ingresos en diferentes sectores."
    elif data == "C330":
        return "Este gráfico representa la distribución del número total de hijos nacidos vivos entre los encuestados. Permite identificar el número de hijos más frecuente, variaciones en los patrones reproductivos y valores extremos. Este análisis es útil para estudiar dinámicas demográficas y su relación con factores como edad, región o nivel socioeconómico."
    else:
        return "El gráfico analiza la distribución de las percepciones de identidad étnica basada en costumbres y antepasados. Permite observar cuáles son las categorías de identidad más comunes entre los encuestados y su dispersión. Esto es útil para comprender la diversidad cultural y cómo se perciben las identidades dentro de la población."

def ConclusionGrafica(variable):
    if variable == "C208":
        return "El gráfico muestra la distribución de las edades (C208) de los encuestados en relación con su parentesco con el jefe del hogar (C203). La mayor concentración de encuestados se encuentra en edades jóvenes, especialmente en el rango de 0 a 20 años, lo que sugiere que muchos de ellos son hijos/as (valor 3) o nietos/as (valor 5) del jefe del hogar. A medida que la edad aumenta, la densidad de encuestados disminuye, indicando menos personas en edades avanzadas. Por ejemplo, las categorías de mayor edad tienen menos frecuencia en los valores de parentesco como padre/madre/suegro/a (valor 6) y pensionista (valor 10). Este análisis es útil para entender la composición etaria de los hogares y cómo las diferentes relaciones de parentesco se distribuyen en función de la edad, lo cual puede influir en aspectos como ingresos, nivel educativo o tamaño de la familia."
    elif variable == "C339_1":
        return "El gráfico de dispersión muestra la distribución del ingreso total mensual (C339_1), que incluye horas extras, bonificaciones, pago por refrigerio, movilidad, comisiones, etc., entre los encuestados. En el eje horizontal se encuentran los ingresos expresados en soles (S/), mientras que en el eje vertical se observa la relación de parentesco con el jefe del hogar (C203). El gráfico resalta que la mayoría de los encuestados reportan ingresos en un rango común, con una alta densidad de puntos en valores más bajos de ingreso. También se pueden identificar valores atípicos o outliers, que representan ingresos significativamente más altos. Este gráfico es clave para analizar las desigualdades económicas y definir perfiles de ingreso en diferentes relaciones de parentesco dentro del hogar, proporcionando una visión de la distribución económica en la población encuestada."
    elif variable == "C330":
        return "El gráfico de densidad muestra la distribución del número total de hijos nacidos vivos (C330) en relación con la relación de parentesco con el jefe del hogar (C203). En el eje horizontal se encuentra el número total de hijos nacidos vivos, mientras que en el eje vertical se muestra la relación de parentesco. Las áreas sombreadas en tonos de azul indican diferentes niveles de densidad, con las áreas más oscuras representando una mayor concentración de datos. Por ejemplo, se observa una mayor densidad de datos para los hijos/as (valor 3) del jefe del hogar, indicando que estos suelen tener un número de hijos que oscila entre 1 y 4. Este gráfico es útil para identificar patrones reproductivos y variaciones en las dinámicas familiares, proporcionando información valiosa sobre las características demográficas en función del parentesco dentro del hogar."
    else:
        return "El gráfico de densidad muestra la distribución de las percepciones de identidad étnica (C377) basadas en costumbres y antepasados en relación con la relación de parentesco con el jefe del hogar (C203). En el eje horizontal se encuentran las categorías de identidad étnica, mientras que en el eje vertical se observa la relación de parentesco. Las áreas sombreadas en tonos de azul indican la densidad de las respuestas, siendo las áreas más oscuras las de mayor concentración de datos. Por ejemplo, se observa una alta densidad de datos en la categoría 7 (Mestizo) y la categoría 1 (Quechua). Este gráfico es útil para comprender la diversidad cultural y cómo se perciben las identidades dentro de la población, permitiendo observar las categorías de identidad más comunes entre los encuestados y su dispersión, lo que proporciona una visión clara de la diversidad étnica en relación con las dinámicas familiares dentro de los hogares."


