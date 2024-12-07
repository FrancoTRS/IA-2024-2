from fasthtml.common import *
import seaborn as sns
import matplotlib
matplotlib.use("Agg")  # Usa el backend sin GUI
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd


def plot_to_base64(plot):
    buf = io.BytesIO()  # Crea un buffer en memoria
    plot.savefig(buf, format='png')  # Guarda la imagen del gráfico en el buffer en formato PNG
    plt.close(plot)  # Cierra el gráfico para liberar memoria
    buf.seek(0)  # Coloca el cursor del buffer al inicio
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')  # Codifica la imagen en base64
    return img_base64  # Devuelve la imagen codificada en base64


# GRAFICO HISPLOT
def datoGraficoHisplot(dg: str, dat):
    plot = sns.histplot(dat[dg], kde=True, bins=4)  # Crea un histograma con Seaborn
    img_base64 = plot_to_base64(plot.figure)  # Convierte el gráfico a base64
    return Img(src=f"data:image/png;base64,{img_base64}")  # Devuelve una etiqueta Img de FastHTML con la imagen en base64


# GRAFICO BOXPLOT
def datoGraficoBoxplot(dg: str, dat):
    # Limpieza de datos específica para OCUP300
    if dg == 'OCUP300' and dg in dat.columns:
        dat[dg] = dat[dg].replace(' ', None)  # Reemplaza valores vacíos
        dat[dg] = pd.to_numeric(dat[dg], errors='coerce')  # Convierte a numérico
        dat = dat.dropna(subset=[dg, 'ESTRATO'])  # Elimina filas con valores nulos en OCUP300 o ESTRATO

    # Filtrar los datos relevantes para la gráfica
    data_clean = dat[[dg, 'ESTRATO']].dropna()  # Limpia datos
    if data_clean.empty:
        return Div(H2(f"La columna {dg} no tiene datos válidos para graficar", cls="text-red-500"))

    if data_clean[dg].dtype in ['float64', 'int64']:
        data_clean[dg] = data_clean[dg].round(1)  # Redondea valores numéricos

    # Crear el gráfico
    plt.figure(figsize=(12, 8))
    plot = sns.boxplot(
        x=dg, y='ESTRATO', data=data_clean, palette="Set3", showfliers=False
    )
    plot.set_title(f"Boxplot de {dg} por ESTRATO", fontsize=16)
    plot.set_xlabel(dg, fontsize=12)
    plot.set_ylabel("Estrato", fontsize=12)

    # Ajustes visuales
    xticks = plot.get_xticks()
    if len(xticks) > 10:
        plot.set_xticks(xticks[::2])  # Reduce etiquetas del eje X
    plot.tick_params(axis='x', rotation=45)
    plot.figure.tight_layout()
    plot.grid(axis='y', linestyle='--', alpha=0.7)

    # Convertir gráfico a Base64
    img_base64 = plot_to_base64(plot.figure)
    return Img(src=f"data:image/png;base64,{img_base64}")  # Devuelve imagen Base64


# GRAFICO LINEPLOT
def datoGraficoLineplot(dg: str, dat):
    plot = sns.lineplot(x=dg, y='ANIO', hue=dg, style="ANIO", data=dat)  # Crea un histograma con Seaborn
    img_base64 = plot_to_base64(plot.figure)  # Convierte el gráfico a base64
    return Img(src=f"data:image/png;base64,{img_base64}")  # Devuelve una etiqueta Img de FastHTML con la imagen en base64


# GRAFICO DISPLOT
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



# def datoGraficoBoxplot(dg: str, dat):
#     plot = sns.boxplot(x=dg, y='ESTRATO', data=dat, hue=dg)  # Crea un histograma con Seaborn
#     img_base64 = plot_to_base64(plot.figure)  # Convierte el gráfico a base64
#     return Img(src=f"data:image/png;base64,{img_base64}")  # Devuelve una etiqueta Img de FastHTML con la imagen en base64