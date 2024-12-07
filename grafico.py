from fasthtml.common import *
import seaborn as sns
import matplotlib
matplotlib.use("Agg")  # Usa el backend sin GUI
import matplotlib.pyplot as plt
import io
import base64

def plot_to_base64(plot):
    buf = io.BytesIO()  # Crea un buffer en memoria
    plot.savefig(buf, format='png')  # Guarda la imagen del gráfico en el buffer en formato PNG
    plt.close(plot)  # Cierra el gráfico para liberar memoria
    buf.seek(0)  # Coloca el cursor del buffer al inicio
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')  # Codifica la imagen en base64
    return img_base64  # Devuelve la imagen codificada en base64


def datoGraficoHisplot(dg: str, dat):
    plot = sns.histplot(dat[dg], kde=True, bins=4)  # Crea un histograma con Seaborn
    img_base64 = plot_to_base64(plot.figure)  # Convierte el gráfico a base64
    return Img(src=f"data:image/png;base64,{img_base64}")  # Devuelve una etiqueta Img de FastHTML con la imagen en base64

def datoGraficoBoxplot(dg: str, dat):
    plot = sns.boxplot(x=dg, y='ESTRATO', data=dat, hue=dg)  # Crea un histograma con Seaborn
    img_base64 = plot_to_base64(plot.figure)  # Convierte el gráfico a base64
    return Img(src=f"data:image/png;base64,{img_base64}")  # Devuelve una etiqueta Img de FastHTML con la imagen en base64

def datoGraficoLineplot(dg: str, dat):
    plot = sns.lineplot(x=dg, y='ANIO', hue=dg, style="ANIO", data=dat)  # Crea un histograma con Seaborn
    img_base64 = plot_to_base64(plot.figure)  # Convierte el gráfico a base64
    return Img(src=f"data:image/png;base64,{img_base64}")  # Devuelve una etiqueta Img de FastHTML con la imagen en base64

def datoGraficoDisplot(dg: str, dat):
    plot = sns.displot(data=dat,x=dg, hue=dg, kind="kde", height=6, multiple="fill", clip=(0, None), palette="ch:rot=-.25,hue=1,light=.75",)
    img_base64 = plot_to_base64(plot.figure)  # Convierte el gráfico a base64
    return Img(src=f"data:image/png;base64,{img_base64}")  # Devuelve una etiqueta Img de FastHTML con la imagen en base64

# -------------------------

# @app.route("/")
# def get():
#     return Div(H1("DATOSSSS"),
#                datoGrafico('ESTRATO',datos))
# datos = pd.read_csv("EPEN BD Anual 2022.csv")