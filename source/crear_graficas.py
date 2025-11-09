import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

carpeta_graficos = "dataset/graficos";
archivo_csv = "dataset/productos.csv"

# Cargamos los datos para generar las gráficas
df = pd.read_csv(archivo_csv, sep=';')
# quitamos del precio el símbolo del euro y guardamos la valoración sobre 5 como número
df["Precio (€)"] = df["Precio"].str.replace("€", "").str.replace(",", ".").astype(float)
df["Val_num (sobre 5)"] = df["Valoración"].str.replace("/5", "").str.replace(",", ".").astype(float)

# Valoración media por marca
sns.barplot(data=df, x="Marca", y="Valoración", estimator="mean")
plt.title("Valoración media por marca")
plt.xticks(rotation=45)
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficos, "valoracion_media_por_marca.png"))
plt.close()

# Relación: valoración y precio
sns.scatterplot(data=df, x="Precio (€)", y="Valoración", hue="Marca")
plt.title("Relación: valoración y precio")
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficos, "precio_vs_valoracion.png"))
plt.close()

# Valoraciones globales
valoraciones = df[[
    "Valoraciones 5 estrellas",
    "Valoraciones 4 estrellas",
    "Valoraciones 3 estrellas",
    "Valoraciones 2 estrellas",
    "Valoraciones 1 estrellas"
]].sum()

valoraciones.plot(kind="bar", color=["green","lightgreen","orange","salmon","red"])
plt.title("Valoraciones globales")
plt.ylabel("Número total de reseñas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficos, "valoraciones_globales.png"))
plt.close()

# Precios por marca
sns.boxplot(data=df, x="Marca", y="Precio (€)")
plt.title("Precios por marca")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(carpeta_graficos, "precios_por_marca.png"))
plt.close()