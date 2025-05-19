ventas = [
    {"fecha": "2025-05-10", "producto": "Laptop", "cantidad": 3, "precio": 1200000},
    {"fecha": "2025-05-10", "producto": "Mouse", "cantidad": 12, "precio": 1500},
    {"fecha": "2025-05-20", "producto": "Laptop", "cantidad": 2, "precio": 115000},
    {"fecha": "2025-05-20", "producto": "Teclado", "cantidad": 8, "precio": 29000},
    {"fecha": "2025-05-30", "producto": "Mouse", "cantidad": 10, "precio": 8950},
    {"fecha": "2025-05-30", "producto": "Laptop", "cantidad": 5, "precio": 110000},
]

# 1. Cálculo de Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]
print(f"Ingresos totales: $ {ingresos_totales}")
print()

# 2. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]
print(f"Producto más vendido: {producto_mas_vendido} (Cantidad: {cantidad_mas_vendida})")
print()
# 3. Promedio de Precio por Producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso = venta["cantidad"] * venta["precio"]
    cantidad = venta["cantidad"]
    if producto in precios_por_producto:
        suma_ingresos, suma_cantidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_ingresos + ingreso, suma_cantidades + cantidad)
    else:
        precios_por_producto[producto] = (ingreso, cantidad)

precios_promedios = {}
for producto, (total_ingresos, total_cantidad) in precios_por_producto.items():
    promedio = total_ingresos / total_cantidad
    precios_promedios[producto] = promedio
    print(f"Precio promedio de {producto}: ${promedio:.2f}")
print()

# 4. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

print("Ingresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f" - {fecha}: ${ingreso:.2f}")
print()

# 5. Resumen de Ventas por Producto
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto, _ = precios_por_producto[producto]
    precio_promedio = precios_promedios[producto]
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio,
    }

print("Resumen de ventas por producto:")
for producto, resumen in resumen_ventas.items():
    print(f"\nProducto: {producto}")
    print(f" - Cantidad total: {resumen['cantidad_total']}")
    print(f" - Ingresos totales: ${resumen['ingresos_totales']:.2f}")
    print(f" - Precio promedio: ${resumen['precio_promedio']:.2f}")