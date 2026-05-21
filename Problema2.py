# ----------------------------------------------------
# PROBLEMA 3 - AUDITORÍA DE INVENTARIO
# Curso: Fundamentos de Programación
# ----------------------------------------------------

# Matriz del inventario
inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 15, 10],
    ["A103", "Monitor", 3, 8],
    ["A104", "Impresora", 12, 12],
    ["A105", "USB", 2, 6]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Título del reporte
print("========================================")
print("   REPORTE DE REABASTECIMIENTO")
print("========================================")


# Recorrido de la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamado de la función
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultados
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)
    print("----------------------------------------")