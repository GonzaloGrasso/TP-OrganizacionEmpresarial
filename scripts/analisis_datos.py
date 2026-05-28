import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Carga del dataset oficial provisto por la UTN usando rutas relativas
ruta_csv = os.path.join("datos", "sales_sample_2024.csv")
df = pd.read_csv(ruta_csv)

# 2. Cálculos métricos sobre los 311 registros reales
ingresos_totales = df['sales_amount'].sum()
promedio_venta = df['sales_amount'].mean()
total_operaciones = df['id'].count()

print("====================================")
print("   REPORTE DE VENTAS OFICIAL 2024   ")
print("====================================")
print(f"Ingresos Totales Evaluados: ${ingresos_totales:,.2f}")
print(f"Promedio por Transacción: ${promedio_venta:,.2f}")
print(f"Cantidad de Operaciones Auditadas: {total_operaciones} registros")
print("====================================")

# 3. Generar el gráfico de la evolución temporal de las ventas
df['sales_date'] = pd.to_datetime(df['sales_date'])
df_agrupado = df.groupby('sales_date')['sales_amount'].sum()

plt.figure(figsize=(10, 5))
df_agrupado.plot(kind='line', color='royalblue', linewidth=1.5)
plt.title('Evolución Histórica de Ventas Comerciales')
plt.xlabel('Fecha de Registro')
plt.ylabel('Monto Facturado ($)')
plt.grid(True, linestyle='--')
plt.tight_layout()

# Guardado automático en la carpeta resultados usando ruta relativa
plt.savefig(os.path.join("resultados", "grafico_ventas.png"))
plt.close()
print("Análisis finalizado con éxito. Gráfico temporal exportado en /resultados.")
