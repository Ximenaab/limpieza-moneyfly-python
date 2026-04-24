import pandas as pd

def limpiar_datos(df):
    # Eliminar duplicados exactos
    df = df.drop_duplicates()

    # Limpiar texto: quitar espacios y homogenizar formato
    df["nombre_usuario"] = df["nombre_usuario"].fillna("").str.strip().str.title()
    df["categoria"] = df["categoria"].fillna("").str.strip().str.title()
    df["comercio"] = df["comercio"].fillna("").str.strip().str.title()
    df["metodo_pago"] = df["metodo_pago"].fillna("").str.strip().str.title()

    # Reemplazar textos incorrectos o inconsistentes
    df["categoria"] = df["categoria"].replace({
        "Comidda": "Comida",
        "": "Sin Categoria"
    })
    df["nombre_usuario"] = df["nombre_usuario"].replace({"": "Anonimo"})
    df["comercio"] = df["comercio"].replace({"": "No Registrado"})
    df["metodo_pago"] = df["metodo_pago"].replace({"": "No Registrado"})

    # Convertir valor a numérico
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df["valor"] = df["valor"].fillna(0)
    df.loc[df["valor"] < 0, "valor"] = 0

    # Convertir fecha a datetime
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=True)
    df["fecha"] = df["fecha"].fillna(pd.Timestamp("2026-01-01"))

    return df