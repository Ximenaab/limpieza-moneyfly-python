from src.carga import cargar_datos
from src.limpieza import limpiar_datos
from src.analisis import analizar_datos
from src.persistencia import guardar_datos, guardar_resumen

#CARGA
df = cargar_datos()

print("=== PRIMERAS FILAS DEL DATASET ORIGINAL ===")
print(df.head())
print("\n=== INFORMACIÓN GENERAL ===")
df.info()
print("\n=== ESTADÍSTICAS DESCRIPTIVAS ===")
print(df.describe(include="all"))
print("\n=== NOMBRES DE COLUMNAS ===")
print(df.columns)
print("\n=== VALORES ÚNICOS EN CATEGORÍA (ANTES DE LIMPIAR) ===")
print(df["categoria"].value_counts(dropna=False))
print("\n=== VALORES ÚNICOS EN MÉTODO DE PAGO (ANTES DE LIMPIAR) ===")
print(df["metodo_pago"].value_counts(dropna=False))
print("\n=== CANTIDAD DE VALORES NULOS POR COLUMNA ===")
print(df.isnull().sum())

#LIMPIEZA
df_limpio = limpiar_datos(df)

print("\n=== DATASET LIMPIO ===")
print(df_limpio)
print("\n=== INFORMACIÓN DEL DATASET LIMPIO ===")
df_limpio.info()
print("\n=== VALORES ÚNICOS EN CATEGORÍA (DESPUÉS DE LIMPIAR) ===")
print(df_limpio["categoria"].value_counts(dropna=False))
print("\n=== VALORES ÚNICOS EN MÉTODO DE PAGO (DESPUÉS DE LIMPIAR) ===")
print(df_limpio["metodo_pago"].value_counts(dropna=False))

#ANALISIS
df_resumen = analizar_datos(df_limpio)

print("\n=== RESUMEN ANALÍTICO POR USUARIO ===")
print(df_resumen)

#GUARDADO
guardar_datos(df_limpio)
guardar_resumen(df_resumen)

#ANÁLISIS POR CATEGORÍA
from src.analisis import analizar_categorias

resumen_cat, cat_max, cat_min = analizar_categorias(df_limpio)

print("\n=== GASTO TOTAL POR CATEGORÍA ===")
print(resumen_cat.to_string(index=False))

print(f"\n💸 Categoría donde MÁS se gasta: {cat_max['categoria']}")
print(f"   Total: ${cat_max['total_gastado']:,.0f} | Transacciones: {int(cat_max['cantidad_transacciones'])}")

print(f"\n💰 Categoría donde MENOS se gasta: {cat_min['categoria']}")
print(f"   Total: ${cat_min['total_gastado']:,.0f} | Transacciones: {int(cat_min['cantidad_transacciones'])}")