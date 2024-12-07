from fasthtml.common import *
from fasthtml import FastHTML
import pandas as pd
from pages.pagPrincipal import *
from pages.pagGraficas import *
from pages.pagHisplot import *
from pages.pagBoxplot import *
from pages.pagLineplot import *
from pages.pagDisplot import *

#prueba completoa a ver

# Incluir TailwindCSS
tailwindcss = Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css")
app = FastHTML(hdrs=(tailwindcss,))

# Cargar datos
datos = pd.read_csv("EPEN BD Anual 2022.csv")
columnas = datos.columns.values

# Pagina Principal
@app.get("/")
def home():
    return Div(
        paginaPrincipal(),
        cls="min-h-screen flex flex-col"
    ) 

# Pagina de Graficos
@app.get("/graficas")
def graficas():
    return Div(
        paginaGraficas(),
        cls="min-h-screen flex flex-col"
    )

# Post de la pagina de Graficos para seleccionar columnas
@app.post("/graficas")
def seleccionColumna(tipoGrafico: str):
    if tipoGrafico == "HISPLOT":
        return cabecera(), seleccionHisplot(), tablaEjemplos(), piePagina()
    elif tipoGrafico == "BOXPLOT":
        return cabecera(), seleccionBoxplot(), tablaEjemplos(), piePagina()
    elif tipoGrafico == "LINEPLOT":
        return cabecera(), seleccionLineplot(), tablaEjemplos(), piePagina()
    else:
        return cabecera(), seleccionDisplot(), tablaEjemplos(),piePagina()
    
# Post de cada grafica 
@app.post("/graficaHisplot")
def muestraGraficoHisplot(data: str):
    return cabecera(), seleccionHisplot(), graficaHisplot(data, datos), tablaEjemplos(), piePagina()

@app.post("/graficaBoxplot")
def muestraGraficoBoxplot(data: str):
    return cabecera(), seleccionBoxplot(), graficaBoxplot(data, datos), tablaEjemplos(), piePagina()

@app.post("/graficaLineplot")
def muestraGraficoLineplot(data: str):
    return cabecera(), seleccionLineplot(), graficaLineplot(data, datos), tablaEjemplos(), piePagina()

@app.post("/graficaDisplot")
def muestraGraficoDsiplot(data: str):
    return cabecera(), seleccionDisplot(), graficaDisplot(data, datos), tablaEjemplos(), piePagina()

serve()
