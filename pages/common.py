from fasthtml.common import *

graficoSelect = [
    "HISPLOT", "BOXPLOT", "LINEPLOT", "DISPLOT"
]

def cabecera():
    return Header(
        Div(
            # Logo a la izquierda
            Img(
                src="https://www.urp.edu.pe/img/thumbnails/wm/220/hm/68/we/220/he/68/x/0/y/0/s/0/q/100/zc/3/f/0/rgb/000000/src/4162/n/logo-urp.jpg", 
                alt="Logo", 
                cls="h-8 w-auto"
            ),
            # Tres palabras al lado derecho
            Div(
                A(
                    "Inicio", 
                    href="#", 
                    cls="text-gray-900 font-semibold hover:text-blue-500"
                ),  # Cambia el color al pasar el mouse
                A(
                    "Dataset", 
                    href="https://www.datosabiertos.gob.pe/dataset/per%C3%BA-indicadores-del-mercado-laboral-nivel-departamental-y-de-principales-ciudades-2022-epen", 
                    cls="text-gray-900 font-semibold hover:text-blue-500", 
                    target="_blank"
                ),  # Cambia el color al pasar el mouse
                cls="flex flex-col space-y-2 sm:flex-row sm:space-x-8 sm:space-y-0 justify-end flex-grow"
            ),
            cls="flex flex-col items-center space-y-4 sm:flex-row sm:justify-between sm:space-y-0 p-6"
        ),
        cls="bg-white shadow"
    )

def piePagina():
    return Footer(
        Div(
            P(
                "© 2024 Mi Sitio Web. Todos los derechos reservados.", 
                cls="text-white"
            ),
            P(
                "Creado por alumnos del curso de Inteligencia Artificial 2024-2", 
                cls="text-white"
            ),
            cls="flex flex-col items-center space-y-2 p-4 bg-gray-800"
        )
    )

def tablaEjemplos():
    datos_fijos = {
        "ANIO": "Año de ejecución de la encuesta",
        "C377": "Por sus costumbres y sus antepasados, se siente o se considera",
        "CONGLOMERADO": "Conglomerado Nro",
        "MUESTRA": "Muestra",
        "SELVIV": "Número de selección de la vivienda",
        "ESTRATO": "Estrato Poblacional",
        "AREA_ENCUESTA": "Área de residencia",
        "CCDD": "Código del departamento",
        "C203": "Cuál es la relación de parentesco con el jefe del hogar",
        "OCUP300": "Nivel de Ocupación",
        "C208": "Qué edad tiene en años cumplidos"
    }
    
    filas = [Tr(
                Td(dato1, cls="border-2 border-emerald-700 px-4 bg-white text-black"),
                Td(dato2, cls="border-2 border-emerald-700 px-4 bg-white text-black")
            ) for dato1, dato2 in datos_fijos.items()]
    
    return Div(
        H2(
            "COLUMNAS EN EL DATASET", 
            cls="text-3xl font-bold text-white m-4"
        ),
        P(
            "Ejemplos de columnas existentes en el DataSet:", 
            cls="text-center text-white pb-3"
        ),
        Table(
            Tr(
                Th("Columna", cls="border-2 border-emerald-700 px-4 bg-gray-200 text-black"),
                Th("Información", cls="border-2 border-emerald-700 px-4 bg-gray-200 text-black")
            ),
            *filas,
            cls="table-auto border-separate"
        ),
        cls="flex flex-col items-center space-y-4 justify-center p-4 bg-gradient-to-r from-blue-900 to-purple-700",
        id="section2"
    )


def formulario(colum,tipoID,accion,columOrGraf):
    return Div(
            Form(
                Select(
                    Option(columOrGraf, value="", disabled=True, selected=True),  # Placeholder
                    *[Option(col, value=col) for col in colum],  # Opciones de columnas
                    id=tipoID, # Tipo o nombre del dato que va a llevar
                    name=tipoID, 
                    cls="border rounded p-2 w-full md:w-96"
                ),
                Button(
                    "Buscar", 
                    type="submit", 
                    cls="bg-blue-500 text-white p-2 rounded ml-2 text-center"
                    ), 
                action=accion, method="post", # Que accion del post va a realizar
                cls="flex flex-col space-y-4 mt-6 md:flex-row md:space-x-4 md:space-y-0 items-center justify-center"
            )
    )