#codificacion camel case
# Float: 1.5 / Int: 35 / Str: Wendy
ventasTotales = 0.0

#Solicitar el numero de productos
numProductos = int(input('Ingrese el numero de productos a gestionar: '))


#Lista para almacenar la informacion
nombres = []
precios = []
cantidades = []

print('Ingreso inicial de productos a la tienda: ')
for i in range(numProductos):
    print(f'Producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('Digite el precio del producto: '))
    precios.append(precio)
    cantidad = int(input('Digite la cantidad del producto: '))
    cantidades.append(cantidad)

#Ciclo principal menu
while True:
    print('\n--- MENU DE GESTION DROGUERIA---')
    print('1. Vender Producto')
    print('2. Mostrar Inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')


    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        print('\nVender Producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVenta = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False

        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVenta <= cantidades[i]:
                    totalVenta = cantidadVenta * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVenta  #Actualizamos la lista, teniendo en cuenta la cantidad que vendimos
                    print(f'Venta realizada, total de esta venta ${totalVenta:.2f}')
                    print(f'Quedan {cantidades[i]} unidades de {nombres[i]} en el inventario')
                else:
                    print(f'Cantidad insuficiente en inventario, ya que en stock solo tenemos {cantidades[i]}')
                break
        if not productoEncontrado:
            print('Producto no encontrado')

    elif opcion == 2:
        print('\nInventario de productos')
        for i in range(len(nombres)):
            print(f'Producto {i+1}: {nombres[i].capitalize()}, Precio: ${precios[i]:.2f}, Cantidad: {cantidades[i]}')

    elif opcion == 3:
        print(f'\nVentas totales acumuladas: {ventasTotales:.2f}')
    
    elif opcion ==4:
        print('Gracias por usar el sistema de gestion de drogueria dev senior')
        break

    else:

        print('Opcion invalida. Ingresar entre (1-4)')
        
 
                             



