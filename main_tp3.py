import secundario_tp3 as secundario

opciones = ('1) Crear arreglo de registros', '2) Cargar los datos de un ticket', '3) Mostrar todos los registros \
del arreglo', '4) ASDAASDASD', '5) ASDASDASDASD', '6) asdasdaasd', '7) ASDASDASD', '8) ASDASDASDSAD', '9) ASDADASDASD', '0) Salir')


def principal():
    opc = -1
    vector_registros = []

    for i in opciones:
        print(i)

    while opc != 0:
        print()
        opc = int(input("Escriba su opcion: "))
        print(f'Elegiste la opcion ({opciones[opc - 1]}:')

        if opc == 1:  # Falta comprobar si esta lo solicitado en el trabajo
            if len(vector_registros) == 0:
                with open("peajes-tp3.txt", "r") as archivo:
                    contador_lineas = 0
                    for linea in archivo:
                        if contador_lineas > 0:
                            objeto_nuevo = secundario.object_linea(linea)
                            vector_registros.append(objeto_nuevo)
                        contador_lineas += 1

            else:
                print(f'Cuidado! Estás por eliminar el arreglo anterior ¿Estás seguro que quieres continuar?')

                cancelar = int(input("Ingrese '0' para cancelar, o cualquier otro valor para continuar: "))
                if cancelar == 0:
                    print('El arreglo sigue igual')

                else:
                    print('El arreglo se modificó')
                    with open("peajes-tp3.txt", "r") as archivo:
                        contador_lineas = 0
                        for linea in archivo:
                            if contador_lineas > 0:
                                objeto_nuevo = secundario.object_linea(linea)
                                vector_registros.append(objeto_nuevo)
                            contador_lineas += 1

        elif opc == 2:
            pass

        elif opc == 3:
            print("----------USTED VERA LOS TIKCETS ORDENADOS POR CODIGO----------")
            for i in range(len(vector_registros)):
                print(vector_registros)
                tickets_ordenados = secundario.order_tickets_by_id(vector_registros)
                print(tickets_ordenados)
        elif opc == 4:
            pass

        elif opc == 5:
            pass

        elif opc == 6:
            pass

        elif opc == 7:
            pass

        elif opc == 8:
            pass

        elif opc == 9:
            pass


principal()
