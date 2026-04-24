import numpy as np

def analizar_datos(df):
    df_resumen = df.groupby(["id_usuario", "nombre_usuario"]).agg(
        total_gastado=("valor", "sum"),
        promedio_gasto=("valor", "mean"),
        cantidad_gastos=("id_gasto", "count")
    ).reset_index()

    # Columna derivada de segmento
    df_resumen["segmento"] = np.where(
        df_resumen["promedio_gasto"] > 15000,
        "Alto Gasto",
        "Gasto Regular"
    )

    # Ordenar de mayor a menor
    df_resumen = df_resumen.sort_values(by="total_gastado", ascending=False)

    return df_resumen
def analizar_categorias(df):
    resumen_categorias = df.groupby("categoria").agg(
        total_gastado=("valor", "sum"),
        cantidad_transacciones=("id_gasto", "count"),
        promedio_por_transaccion=("valor", "mean")
    ).reset_index()

    resumen_categorias = resumen_categorias.sort_values(
        by="total_gastado", ascending=False
    )

    categoria_max = resumen_categorias.iloc[0]
    categoria_min = resumen_categorias.iloc[-1]

    return resumen_categorias, categoria_max, categoria_min