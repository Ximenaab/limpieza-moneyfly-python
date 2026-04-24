def guardar_datos(df, ruta="data/processed/gastos_limpios.csv"):
    df.to_csv(ruta, index=False)
    print(f"✅ Archivo guardado en: {ruta}")

def guardar_resumen(df_resumen, ruta="data/processed/resumen_analitico_usuarios.csv"):
    df_resumen.to_csv(ruta, index=False)
    print(f"✅ Resumen guardado en: {ruta}")