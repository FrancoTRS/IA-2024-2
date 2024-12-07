from fasthtml.common import *
from grafico import *
from pages.common import *

columnasSelecLineplot = [
    "C330", "C339_1", "C317A", "C377", "OCUP300"
]

def seleccionLineplot():
    return Div(
        Div(
            formulario(graficoSelect,"tipoGrafico","/graficas","LINEPLOT"),
            cls="flex-grow text-center p-2", 
            ),
        Div(
            formulario(columnasSelecLineplot,"data","/graficaLineplot","Seleccione una columna"),
            cls="flex-grow text-center p-2",
            ),
        cls="flex flex-row justify-center items-center p-4 bg-gradient-to-r from-blue-900 to-purple-700 pb-8"
    )

def graficaLineplot(data: str, datos):
    return Div(
        Div(
            Div(
                datoGraficoLineplot(data, datos),
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
    if data == "C330":
        return "Este gráfico muestra la evolución del total de hijos nacidos vivos en relación con otra variable (por ejemplo, edad o año). Sirve para analizar patrones reproductivos y cómo factores como la edad, la región o el estrato socioeconómico pueden influir en el número de hijos reportados."
    elif data == "C339_1":
        return "Este gráfico analiza cómo varían los ingresos personales según una segunda variable (como edad, nivel de instrucción o región). Es útil para identificar tendencias económicas, desigualdades salariales y grupos poblacionales con mayores o menores ingresos."
    elif data == "C317A":
        return "El gráfico refleja cómo el nivel de instrucción alcanzado varía en función de otra variable (por ejemplo, edad o región). Permite observar tendencias educativas, identificar mejoras en la formación a lo largo de generaciones o analizar brechas en función de factores sociodemográficos."
    elif data == "C377":
        return "Este gráfico muestra cómo las percepciones de identidad étnica varían según otra dimensión (como edad, región o nivel de instrucción). Ayuda a comprender la diversidad cultural y las diferencias generacionales o regionales en la percepción étnica."
    else:
        return "Este gráfico ilustra cómo el nivel de ocupación laboral varía en función de otra variable (como edad, nivel educativo o ingresos). Es útil para analizar patrones de empleo, identificar grupos etarios con mayor participación laboral o estudiar relaciones entre educación y empleo."

def ConclusionGrafica(variable):
    if variable == "C330":
        return "El gráfico de líneas titulado Lineplot de C330 contra C208 muestra la relación entre el número total de hijos nacidos vivos (C330) y la edad en años cumplidos (C208) de los encuestados. En el eje X se encuentran los valores de C330, que representan el número total de hijos nacidos vivos, mientras que en el eje Y se muestra la edad de los encuestados. La línea azul del gráfico indica que a medida que aumenta el número de hijos, la edad promedio de los encuestados también tiende a aumentar. Por ejemplo, los encuestados con 1 a 3 hijos tienen una edad promedio de alrededor de 25 a 30 años, mientras que aquellos con más de 6 hijos tienen una edad promedio de aproximadamente 45 años. Las áreas sombreadas alrededor de la línea representan intervalos de confianza, mostrando la variabilidad en los datos. Este gráfico es útil para analizar patrones reproductivos y entender cómo la edad influye en el número de hijos nacidos vivos reportados, proporcionando una visión de las tendencias demográficas y socioeconómicas en la población estudiada."
    elif variable == "C339_1":
        return "El gráfico de líneas muestra la relación entre el ingreso total mensual (C339_1), que incluye horas extras, bonificaciones, pago por refrigerio, movilidad, comisiones, etc., y la edad de los encuestados en años cumplidos (C208). En el eje X se encuentran los diferentes valores de ingreso total en soles peruanos (S/), mientras que en el eje Y se muestra la edad de los encuestados. La línea azul del gráfico indica que a medida que aumentan los ingresos, la edad promedio de los encuestados también tiende a aumentar. Por ejemplo, los encuestados con ingresos de alrededor de S/ 1000 tienen una edad promedio cercana a los 25 años, mientras que aquellos con ingresos mayores, como S/ 4000, tienen una edad promedio de aproximadamente 45 años. Las áreas sombreadas alrededor de la línea representan intervalos de confianza, mostrando la variabilidad en los datos. Este gráfico es útil para entender cómo varían los ingresos personales según la edad, proporcionando una visión de las tendencias económicas y las desigualdades salariales entre diferentes grupos etarios en la población estudiada."
    elif variable == "C317A":
        return "El gráfico de líneas titulado Lineplot de C317A contra C208 muestra la relación entre el número de personas que trabajan en el negocio del encuestado (C317A) y la edad de los encuestados en años cumplidos (C208). En el eje X se encuentran los valores de C317A, que varían de 1 a 10 personas, mientras que en el eje Y se muestra la edad de los encuestados. La línea azul del gráfico indica que a medida que aumenta el número de empleados (C317A), la edad promedio de los encuestados también tiende a aumentar ligeramente. Por ejemplo, los negocios con 1 a 3 empleados tienen una edad promedio de alrededor de 25 a 35 años, mientras que aquellos con más empleados, como 8 a 10 personas, tienen una edad promedio de aproximadamente 40 años. Las áreas sombreadas alrededor de la línea representan intervalos de confianza, mostrando la variabilidad en los datos. Este gráfico es útil para entender cómo el tamaño del negocio, en términos de número de empleados, se relaciona con la edad de los encuestados, proporcionando una visión de la dinámica laboral y las características demográficas en diferentes tamaños de negocios."
    elif variable == "C377":
        return "El gráfico de líneas muestra la relación entre la edad (C208) y la identidad étnica (C377) según las costumbres y los antepasados de los encuestados. En el eje X se encuentran las categorías de identidad étnica: 1 (Quechua), 2 (Aymara), 3 (Nativo o Indígena de la Amazonía), 4 (Perteneciente a otro pueblo indígena originario), 5 (Negro/Moreno/Zambo/Mulato/Pueblo Afro peruano o Afrodescendiente), 6 (Blanco), 7 (Mestizo), 8 (Otro) y 9 (No sabe/No responde). En el eje Y se muestra la edad en años cumplidos. Los datos indican que las personas que se consideran Blancos (categoría 6) tienen una edad promedio de alrededor de 45 años, mientras que aquellos que se identifican como Quechuas (categoría 1) tienen una edad promedio de 35 años. La categoría de Mestizos (categoría 7) presenta una edad promedio de 40 años. Las bandas sombreadas alrededor de las líneas representan intervalos de confianza, mostrando la variabilidad en los datos. Este gráfico es útil para analizar cómo varían las percepciones de identidad étnica según la edad, proporcionando una visión de la diversidad cultural y generacional en la muestra estudiada."
    else:
        return "El gráfico de líneas muestra la relación entre el nivel de ocupación (OCUP300) y la edad en años cumplidos (C208). En el eje X se encuentran los niveles de ocupación: 1 (Ocupado), 2 (Desempleado Abierto), 3 (Desempleado Oculto) y 4 (Inactivos). En el eje Y se muestra la edad. Los datos indican que las personas ocupadas (nivel 1) tienen una edad promedio de alrededor de 40 años. Los desempleados abiertos (nivel 2) tienen una edad promedio más baja, cercana a los 10 años, lo cual podría ser un error o una anomalía en los datos. Los desempleados ocultos (nivel 3) tienen una edad promedio de alrededor de 35 años, y los inactivos (nivel 4) tienen una edad promedio de aproximadamente 40 años. La banda azul alrededor de la línea representa el intervalo de confianza, mostrando la variabilidad de los datos. Este gráfico es relevante para analizar cómo la edad influye en el nivel de ocupación laboral."