# Autor: Alan Baez
# Proyecto de pre-entrega

# Lista para almacenar los productos
products = []

# Bucle principal del programa
while True:
    # Muestro el menú de opciones
    print("\nMenú principal de opciones:")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")  

    # Solicito la opción al usuario
    option = input("\nSeleccione una opción: ").strip()
    # Verifico que la opción sea válida 
    option_valid = option.isdigit() and int(option) >= 1 and int(option) <= 5
    # Si la opción es válida, procedo a ejecutar la acción correspondiente
    if option_valid:
        match int(option):

            # Agregar producto
            case 1:
                # Solicito los datos de entrada y los convierto a minúsculas
                name = input("Ingrese el nombre del producto: ").lower()
                category = input("Ingrese la categoría del producto: ").lower()
                price = input("Ingrese un número entero para el precio del producto ($): ")

                # Limpieza de espacios al inicio y al final
                name = name.strip()
                category = category.strip()
                price = price.strip()

                # Verificación de que todos los datos son correctos
                name_valid = name.isalpha()
                category_valid = category.isalpha()
                price_valid = price.isdigit() and int(price) >= 0

                # Si todo es correcto procedo a registrar el producto
                if name_valid and category_valid and price_valid:
                    price = int(price)
                    product = [name, category, price]
                    print("Producto registrado exitosamente")
                    products.append(product)
                # Si hay algún error, informo y vuelvo a pedir los datos
                else:
                    print("\nError en los datos ingresados. Por favor tenga en cuenta las reglas:")
                    print("- El nombre y la categoría deben contener solo letras (sin números nicaracteres especiales).")
                    print("- El precio debe ser un número entero positivo.\n")
            
            # Mostrar productos
            case 2:
                if products:
                    # Visualización de productos registrados
                    print("Productos registrados")
                    for index in range(len(products)):
                        print(f"{index+1}. Nombre: {products[index][0]} | Categoría: {products[index][1]} | Precio: ${products[index][2]}")
                else:
                    print("No hay productos registrados.")

            # Buscar producto
            case 3:
                # Pido el nombre del producto a buscar
                search_name = input("Ingrese el nombre del producto que desea buscar: ").lower().strip()
                # Valido el nombre ingresado
                name_valid = search_name.isalpha()
                # Si el nombre es válido procedo a buscarlo
                if name_valid:
                    found_products = []
                    for i_product in range(len(products)):
                        if products[i_product][0] == search_name:
                            found_products.append([products[i_product], i_product+1])
                    # Muestro los productos encontrados o informo si no hubo coincidencias
                    if found_products:
                        print("Productos encontrados:")
                        for index in range(len(found_products)):
                            print(f"{found_products[index][1]}. Nombre: {found_products[index][0][0]} | Categoría: {found_products[index][0][1]} | Precio: ${found_products[index][0][2]}")
                    else:
                        print("No se encontraron resultados para el producto buscado.")
                # Si el nombre no es válido informo el error
                else:
                    print("Error en el nombre ingresado. Debe contener solo letras (sin números ni caracteres especiales).")

            # Eliminar producto
            case 4:
                # Pido el número del producto a eliminar
                delete_product = input("Ingrese el número del producto que desea eliminar: ").strip()
                # Valido el número ingresado
                index_valid = delete_product.isdigit() and int(delete_product) >= 1 and int(delete_product) <= len(products)
                # Si el número es válido procedo a eliminar el producto
                if index_valid:
                    delete_index = int(delete_product) - 1
                    deleted_product = products.pop(delete_index)
                    print("El producto eliminado es:")
                    print(f"Nombre: {deleted_product[0]} | Categoría: {deleted_product[1]} | Precio: ${deleted_product[2]}")
                # Si el número no es válido informo el error
                else:
                    print("Error en el número ingresado. Debe ser un número entero válido correspondiente a un producto en la lista.")

            # Salir
            case 5:
                print("Saliendo del programa. ¡Hasta luego!")
                break
    
    # Si no fue una opción adecuada, aviso al usuario
    else:
        print("Opción no válida. Por favor seleccione una opción del 1 al 5.")