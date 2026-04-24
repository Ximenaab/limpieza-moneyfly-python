import pandas as pd

def cargar_datos(ruta="data/raw/gastos.csv"):
    df = pd.read_csv(ruta)
    return df

