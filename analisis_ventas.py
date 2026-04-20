# 1. Carga de Datos
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1200.0},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.0},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1200.0},
    {"fecha": "2024-01-02", "producto": "Monitor", "cantidad": 3, "precio": 300.0},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 2, "precio": 25.0}
]

# 2. Cálculo de Ingresos Totales
ingresos_totales_globales = 0
for venta in ventas:
    ingresos_totales_globales += venta["cantidad"] * venta["precio"]

# 3. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    cant = venta["cantidad"]
    if prod in ventas_por_producto:
        ventas_por_producto[prod] += cant
    else:
        ventas_por_producto[prod] = cant

# Identificar el más vendido
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# 4. Promedio de Precio por Producto (Usando Tuplas)
precios_por_producto = {}
for venta in ventas:
    prod = venta["producto"]
    ingreso_venta = venta["cantidad"] * venta["precio"]
    cant = venta["cantidad"]
    
    if prod in precios_por_producto:
        suma_ingreso, total_cant = precios_por_producto[prod]
        precios_por_producto[prod] = (suma_ingreso + ingreso_venta, total_cant + cant)
    else:
        precios_por_producto[prod] = (ingreso_venta, cant)

# 5. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

# 6. Representación de Datos (Resumen Final)
resumen_ventas = {}
for prod, datos in precios_por_producto.items():
    suma_ingreso, total_cant = datos
    resumen_ventas[prod] = {
        "cantidad_total": total_cant,
        "ingresos_totales": suma_ingreso,
        "precio_promedio": suma_ingreso / total_cant
    }

# --- IMPRESIÓN DE RESULTADOS ---
print(f"Ingresos Totales Globales: ${ingresos_totales_globales}")
print(f"Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")
print("\nIngresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: ${ingreso}")

print("\nResumen por Producto:")
for prod, info in resumen_ventas.items():
    print(f"{prod}: {info}")