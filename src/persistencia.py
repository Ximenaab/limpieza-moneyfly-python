def guardar_datos(df, ruta="data/processed/gastos_limpios.csv"):
    df.to_csv(ruta, index=False, float_format="%.2f")
    print(f"✅ Archivo guardado en: {ruta}")

def guardar_resumen(df_resumen, ruta="data/processed/resumen_analitico_usuarios.csv"):
    # Redondear columnas numéricas a 2 decimales
    df_resumen["total_gastado"] = df_resumen["total_gastado"].round(2)
    df_resumen["promedio_gasto"] = df_resumen["promedio_gasto"].round(2)
    df_resumen.to_csv(ruta, index=False, float_format="%.2f")
    print(f"✅ Resumen guardado en: {ruta}")