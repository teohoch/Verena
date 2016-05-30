# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:37:24 2016

@author: Raquel Cutillas
"""

# ***************** TAREA 2  *************************************************
# from numpy import random
# from matplotlib import *
import psycopg2


# **************** INICIO CODIGO PROGRAMA *************************************
def lector_menus(archivo_menu):
    print ""
    with open(archivo_menu) as archivo:
        archivo.readline()
        print archivo.read()

def table_printer(data, headers):

    if len(data)>0:
        col_width = max([max(len(str(word)) for row in data for word in row), max(len(str(word)) for word in headers )]) + 2

        print "\n\t| " + "|".join(str(word).ljust(col_width) for word in headers) +"|"
        print "\t"+ ("-"*((col_width*len(headers))+5))
        for row in data:
            print "\t| " + "|".join(str(word).ljust(col_width) for word in row)+"|"
    else:
        col_width = max(len(str(word)) for word in headers) + 2
        print "\n\t| " + "|".join(str(word).ljust(col_width) for word in headers) + "|"
        print "\t" + ("-" * ((col_width * len(headers)) + 3))


conn = psycopg2.connect(host='icc.uandes.cl', database='grupo12', user='grupo12', password='lpqHGr')


def fetch(command):
    cursor = conn.cursor()
    cursor.execute(command)
    if cursor.rowcount>0:
        data = cursor.fetchall()
    else:
        data = []
    cursor.close()
    return data


def execute(command):
    cur = conn.cursor()
    cur.execute(command)
    conn.commit()
    cur.close()


while True:
    primera = True
    # IMPRIME MENU OPCIONES PARA EL USUARIO
    lector_menus("menu.txt")

    # CONEXION A LA BASE DE DATOS ****** REVISAR
    conn = psycopg2.connect(host='icc.uandes.cl', database='grupo12', user='grupo12', password='lpqHGr')
    cur = conn.cursor()

    # PREGUNTA AL USUARIO QUE DESEA REALIZAR
    pregunta = raw_input("Escriba del 1 al 7 para procesar su solicitud:")
    if pregunta in ("1", "2", "3", "4", "5", "6", "7"):
        pregunta = int(pregunta)

        # ADMINISTRAR PRODUCTOS
        if pregunta == 1:

            # nVeces1=0
            while True:
                # IMPRIME LISTA PRODUCTOS
                comando = "SELECT producto.id, producto.nombre, marca, categoria.nombre FROM producto " \
                          "JOIN categoria ON producto.id_categoria = categoria.id"
                rows = fetch(comando)

                if primera:
                    table_printer(rows, ["ID Producto", "Nombre", "Marca","Categoria"])
                    primera = False

                lector_menus('ListaProductos.txt')

                # PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta = raw_input("Escriba del 1 al 4 para procesar su solicitud:")


                # DISTINTAS OPCIONES SOBRE LOS PRODUCTOS
                if pregunta in ("1", "2", "3", "4"):
                    pregunta = int(pregunta)

                    # OPCION 1: AGREGAR UN PRODUCTO
                    if pregunta == 1:
                        categorias = fetch("SELECT id, nombre FROM categoria")
                        nombre = raw_input("\nIngrese el nombre del producto: ")
                        marca = raw_input("Ingrese la Marca del Producto: ")
                        precio = int(raw_input("Ingrese el precio unitario del producto: "))

                        table_printer(categorias,["ID","Categorias"])
                        categoria = int(raw_input("De las categorias listadas, ingrese el ID de la categoria al cual corresponde este Producto: "))

                        comando_crear = "INSERT INTO producto (id_categoria, nombre, marca, precio) VALUES" \
                                        " ({},'{}','{}',{})".format(categoria, nombre, marca, precio)

                        execute(comando_crear)
                        print "\n¡Producto creado con exito!"
                        primera = True

                    # OPCION 2: ELIMINAR UN PRODUCTO
                    elif pregunta == 2:
                        id_producto = int(raw_input("Seleccione el ID del producto a eliminar: "))
                        comando = "SELECT producto.id, producto.nombre FROM producto " \
                                  "WHERE producto.id={}".format(id_producto)
                        data = fetch(comando)
                        if len(data)>0:
                            confirmacion = raw_input("\n\tSeguro que desea eliminar {} (ID = {}) (Si/No)? ".format(data[0][1], data[0][0]))
                            confirmacion = confirmacion.lower()
                            if confirmacion=="si":
                                delete_command="DELETE FROM producto WHERE id={}".format(id_producto)
                                execute(delete_command)
                                print "\nProducto eliminado correctamente"
                        else:
                            "\nProducto no encontrado en la base de datos"

                    # OPCION 3: DETALLES DE UN PRODUCTO Incluyendo lista de locales en los cuales esta disponible y si estan en gondola especial
                    elif pregunta == 3:
                        pass

                    # OPCION 4: SALIR DE LA APLICACION
                    elif pregunta == 4:
                        print "\nVolviendo al menu anterior"
                        break

                    # ADMINISTRAR CATEGORIA RAQUEL
        elif pregunta == 2:
            while True:
                # IMPRIME LISTA DE CATEGORIAS
                if primera:
                    data = fetch("SELECT id, nombre FROM categoria ")
                    table_printer(data,["ID Categoria", "Nombre"])
                    primera=False

                lector_menus('ListaCategorias.txt')

                # PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta = raw_input("Escriba del 1 al 4 para procesar su solicitud:")

                # DISTINTAS OPCIONES SOBRE LAS CATEGORIAS
                if pregunta in ("1","2","3","4"):

                    # OPCION 1: DETALLES DE LA CATEGORIA
                    if pregunta == "1":
                        pass

                    # OPCION 2: AGREGAR UNA CATEGORIA
                    elif pregunta == "2":
                        nombre = raw_input("Ingrese el nombre de la nueva Categoria:")
                        comando_crear = "INSERT INTO categoria (nombre) VALUES ('{}')".format(nombre)
                        execute(comando_crear)
                        print "\nCategoria creada"
                        primera=True


                    # OPCION 3: ELIMINAR UNA CATEGORIA
                    elif pregunta == "3":
                       pass

                    # OPCION 4: SALIR DE LA APLICACION
                    elif pregunta == "4":
                        print "\nVolviendo al menu anterior"
                        break
                else:
                    print "\nOpcion Invalida pruebe nuevamente"

        # ADMINISTRAR LOCAL PEDRO
        elif pregunta == 3:

            # nVeces1=0
            while True:
                # IMPRIME LISTA DE LOCALES SEGUN SU CLASIFICACION
                cur = conn.cursor()

                cur.execute("SELECT id_local, clasificacion FROM local ")
                rows = cur.fetchall()

                cur.close()

                table_printer(rows, "ID Local", "Clasificacion")

                menu = open('ListaLocales.txt')
                linea = menu.readline()
                print linea
                i = 0
                while i < len(linea):
                    linea = menu.readline()
                    print linea
                    i += 1

                # PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta = int(raw_input("Escriba del 1 al 4 para procesar su solicitud:"))
                # DISTINTAS OPCIONES SOBRE LOS LOCALES
                if pregunta == 1 or pregunta == 2 or pregunta == 3 or pregunta == 4:

                    # OPCION 1: DETALLES DEL LOCAL
                    if pregunta == 1:
                        pass

                    # OPCION 2: AGREGAR UN LOCAL
                    elif pregunta == 2:
                        cur = conn.cursor()

                        clasificacion = raw_input("Ingrese la clasificacion del local:")
                        direccion = raw_input("Ingrese la direccion del local:")
                        comuna = raw_input("Ingrese la comuna del local:")

                        cur.execute("INSERT INTO Local (nclasificacion, direccion, comuna) VALUES (%s, %s,%s);",
                                    (clasificacion, direccion, comuna))
                        conn.commit()

                    # OPCION 3: ELIMINAR UN LOCAL
                    elif pregunta == 3:
                        cur = conn.cursor()

                        nombre = raw_input("Ingrese la clasificacion del Local que desea eliminar:")
                        cur.execute("DELETE FROM producto WHERE clasificacion='%s'", [clasificacion])

                        conn.commit()

                    # OPCION 4: SALIR DE LA APLICACION
                    elif pregunta == 4:
                        print "Usted salio de la aplicacion"
                        break


        # ADMINISTRAR PASILLOS Y GONDOLAS GRUPO
        elif pregunta == 4:
            # TODO REVISAR OPCION ENTERA

            # nVeces1=0
            while True:
                # IMPRIME LISTA DE LOCALES SEGUN SU CLASIFICACION
                cur = conn.cursor()

                cur.execute("SELECT id_local, clasificacion FROM local ")
                rows = cur.fetchall()

                for row in rows:
                    print '\n\tid_local: {}'.format(row[0])
                    print '\tclasificacion: {}'.format(row[1])

                variable = raw_input("Ingrese la clasificacion que desea:")

                cur.execute(
                    "SELECT pa.id_pasillo, pa.numero FROM local L, pasillo pa WHERE pa.id_local=l.id_local AND l.clasificacion='{}'".format(
                        variable))

                rows = cur.fetchall()

                for row in rows:
                    print '\n\tpa.id_pasillo: {}'.format(row[0])
                    print '\tpa.numero: {}'.format(row[1])

                cur.close()

                ##### me quedo aqui





                # IMPRIME MENU OPCIONES PARA EL USUARIO
                menu = open('menuPasilloGondola.txt')
                linea = menu.readline()
                print linea
                i = 0
                while i < len(linea):
                    linea = menu.readline()
                    print linea
                    i += 1

                # PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta = int(raw_input("Escriba del 1 al 8 para procesar su solicitud:"))
                ultimoIdPas = 30
                numPasLocal = 5
                ultimoIdGon = 120

                # DISTINTAS OPCIONES SOBRE LOS LOCALES
                if pregunta == 1 or pregunta == 2 or pregunta == 3 or pregunta == 4 or pregunta == 5 or pregunta == 6 or pregunta == 7 or pregunta == 8:

                    # OPCION 1: AGREGAR PASILLO
                    if pregunta == 1:
                        cur = conn.cursor()

                        idPasillo = ultimoIdPas + 1

                        # Revisar, para cuando el usuario entrega otro valor
                        print " Categorias: Ingrese el numero que corresponde a la categoria: Dulces 1, Congelados 2, Bebidas 3, Limpieza 4 y Despensa 5"
                        numCateg = int(raw_input("Ingrese el numero de la Categoria:"))

                        print "Locales: Ingrese el numero que corresponde al local: Hipermercado Vitacura 1, Hipermercado Las Condes 2, Supermercado Lo Curro 3, Almacen Maria 4, Supermercado Estoril 5, Almacen Alba 6:"
                        idLocal = raw_input("Ingrese el Id del local:")

                        numero = numPasLocal + 1

                        cur.execute(
                            "INSERT INTO pasillo (id_pasillo, id_categoria, id_local,numero) VALUES (%s, %s,%s, %s);",
                            (idPasillo, numCateg, idLocal, numero))
                        conn.commit()

                    # OPCION 2: EDITAR CATEGORIA
                    elif pregunta == 2:
                        pass

                    # OPCION 3: AGREGAR GONDOLA
                    elif pregunta == 3:

                        cur = conn.cursor()

                        idGondola = ultimoIdGon + 1

                        print " Recuerde que cada local tiene inicialmente 5 pasillos"
                        id_pasillo = int(raw_input("Ingrese el numero del pasillo:"))

                        nivel = 0
                        print " Recuerde tipo Normal o Preferecial"
                        tipo = raw_input("Ingrese la comuna del local:")

                        if tipo == "Normal":
                            nivel += 2
                        else:
                            nivel += 1

                        cur.execute("INSERT INTO gondola (id_gondola, id_pasillo, nivel, tipo) VALUES (%s,%s,%s,%s);",
                                    (clasificacion, direccion, comuna))
                        conn.commit()

                    # OPCION 4: ASIGNAR GONDOLA
                    elif pregunta == 4:
                        pass

                    # OPCION 5:ADMINISTRAR GONDOLAS PREFERENCIALES
                    elif pregunta == 5:
                        pass

                    # OPCION 6: VER UBICACIONES
                    elif pregunta == 6:
                        pass

                    # OPCION 7: ELIMINAR GONDOLA
                    elif pregunta == 7:

                        cur = conn.cursor()

                        idGon = int(raw_input("Ingrese el Id de la gondola que desea eliminar:"))
                        cur.execute("DELETE FROM gondola WHERE id_gondola='%s'", [idGon])

                        conn.commit()

                    # OPCION 8: SALIR DE LA APLICACION
                    elif pregunta == 8:
                        print "Usted salio de la aplicacion"
                        break


        # ADMINISTRAR CLIENTES VICENTE
        elif pregunta == 5:

            while True:

                if primera:
                    cur = conn.cursor()
                    cur.execute("SELECT rut_cliente, nombre, apellido FROM cliente ")
                    rows = cur.fetchall()
                    cur.close()

                    table_printer(rows,["Rut Cliente", "Nombre","Apellido"])
                    primera = False

                # PREGUNTA AL USUARIO QUE DESEA REALIZAR
                lector_menus("ListaClientes.txt")
                pregunta = raw_input("Escriba del 1 al 5 para procesar su solicitud:")
                # DISTINTAS OPCIONES SOBRE LOS CLIENTES
                if pregunta in ("1", "2", "3", "4", "5"):
                    pregunta = int(pregunta)

                    # OPCION 1: DETALLES DEL CLIENTE
                    if pregunta == 1:
                        rutCliente = raw_input("Ingrese el Rut del Cliente a mostrar:")
                        clean_rut_cliente = int(rutCliente.split("-")[0])

                        commando = "SELECT rut_cliente, nombre, apellido, fecha_nacimiento, comuna_residencia, " \
                                   "comuna_trabajo FROM cliente WHERE rut_cliente=" + str(clean_rut_cliente)
                        cur = conn.cursor()
                        cur.execute(commando)
                        datos_personales = cur.fetchall()
                        if len(datos_personales)>0:
                            commando_compras = "SELECT clasificacion, producto.nombre, cantidad FROM venta " \
                                               "JOIN gondola_producto ON venta.id_gondola_producto = gondola_producto.id_gondola_producto " \
                                               "JOIN gondola ON gondola_producto.id_gondola = gondola.id_gondola " \
                                               "JOIN pasillo ON gondola.id_pasillo = pasillo.id_pasillo " \
                                               "JOIN local ON pasillo.id_local = local.id_local " \
                                               "JOIN producto ON gondola_producto.id_producto = producto.id_producto " \
                                               "WHERE rut_cliente={0}".format(str(clean_rut_cliente))
                            cur.execute(commando_compras)
                            datos_compras = cur.fetchall()
                            cur.close()
                            n_compras = len(datos_compras)
                            if n_compras>0:
                                total = 0
                                locales = []
                                for compra in datos_compras:
                                    total += compra[2]
                                    locales.append(compra[0])

                                max_local = max(set(locales), key=locales.count)
                                promedio = total/n_compras

                                print "\nDatos del Cliente:"
                                print "\tNombre completo: " + datos_personales[0][1] + " " + datos_personales[0][2]
                                print "\tRUT: " + str(datos_personales[0][0])
                                print "\tFecha Nacimiento: " + str(datos_personales[0][3].strftime('%d-%m-%Y'))
                                print "\tComuna de Residencia: " + str(datos_personales[0][4])
                                print "\tComuna de Trabajo: " + str(datos_personales[0][4])
                                table_printer(datos_compras,["Local","Producto","Cantidad"])
                                print "\tLocal mas frecuente: " + max_local
                                print "\tPromedio de productos adquiridos por compra: "+str(promedio)
                            else:
                                print "El cliente no registra ninguna compra"
                        else:
                            print "\nCliente no encontrado en la base de datos"


                    # OPCION 2: AGREGAR UN CLIENTE
                    elif pregunta == 2:


                        rutCliente = raw_input("Ingrese el Rut del Cliente:")
                        clean_rut_cliente = int(rutCliente.split("-")[0])
                        nombre = raw_input("Ingrese el Nombre del Cliente:")
                        apellido = raw_input("Ingrese el Primer Apellido del Cliente:")
                        fechaNacimiento = raw_input("Ingrese la fecha de nacimiento DD-MM-AAAA del Cliente:")
                        comunaTrabajo = raw_input("Ingrese la Comuna donde Trabaja el Cliente:")
                        comunaResidencia = raw_input("Ingrese la Comuna donde Reside el Cliente:")

                        comando = "INSERT INTO Cliente (rut_cliente, nombre, apellido, fecha_nacimiento, " \
                                  "comuna_trabajo, comuna_residencia) VALUES ({}, '{}', '{}', '{}', '{}', '{}');"\
                            .format(clean_rut_cliente,nombre,apellido,fechaNacimiento,comunaResidencia,comunaTrabajo)

                        cur = conn.cursor()
                        cur.execute("SET DATESTYLE = DMY")
                        cur.execute(comando)
                        conn.commit()
                        cur.close()

                        print " ".join("\nCliente", nombre,apellido,"creado con exito")

                    # OPCION 3: EDITAR UN CLIENTE
                    elif pregunta == 3:
                        rutCliente = raw_input("Ingrese el Rut del Cliente a editar:")
                        clean_rut_cliente = int(rutCliente.split("-")[0])

                        commando = "SELECT rut_cliente, nombre, apellido, fecha_nacimiento, comuna_residencia, " \
                                   "comuna_trabajo FROM cliente WHERE rut_cliente=" + str(clean_rut_cliente)
                        cur = conn.cursor()
                        cur.execute(commando)
                        datos_personales = cur.fetchall()
                        if len(datos_personales)>0:
                            print "\nDatos del Cliente:"
                            print "\tNombre completo: " + datos_personales[0][1] + " " + datos_personales[0][2]
                            print "\tRUT: " + str(datos_personales[0][0])
                            print "\tFecha Nacimiento: " + str(datos_personales[0][3].strftime('%d-%m-%Y'))
                            print "\tComuna de Residencia: " + str(datos_personales[0][4])
                            print "\tComuna de Trabajo: " + str(datos_personales[0][5])

                            nombre = raw_input("Ingrese el Nombre del Cliente (Actualmente es '"+datos_personales[0][1]+"'):")
                            apellido = raw_input("Ingrese el Primer Apellido del Cliente (Actualmente es '"+datos_personales[0][2]+"'):")
                            fechaNacimiento = raw_input("Ingrese la fecha de nacimiento DD-MM-AAAA del Cliente (Actualmente es '"+str(datos_personales[0][3].strftime('%d-%m-%Y'))+"'):")
                            comunaTrabajo = raw_input("Ingrese la Comuna donde Trabaja el Cliente (Actualmente es '"+datos_personales[0][4]+"'):")
                            comunaResidencia = raw_input("Ingrese la Comuna donde Reside el Cliente (Actualmente es '"+datos_personales[0][5]+"'):")

                            update_command = "UPDATE cliente SET nombre='{}', apellido='{}'," \
                                             " fecha_nacimiento= to_date('{}','DD-MM-YYYY'), comuna_trabajo='{}'" \
                                             ",comuna_residencia='{}' WHERE rut_cliente = {};"\
                                .format(nombre,apellido,fechaNacimiento,comunaTrabajo,comunaResidencia,clean_rut_cliente)
                            cur = conn.cursor()
                            cur.execute(update_command)
                            conn.commit()
                            cur.close()
                            print "\nCliente modificado correctamente"
                        else:
                            print "\nCliente no encontrado en la base de datos"


                    # OPCION 4: ELIMINAR UN CLIENTE
                    elif pregunta == 4:
                        rutCliente = raw_input("Ingrese el Rut del Cliente a eliminar:")
                        clean_rut_cliente = int(rutCliente.split("-")[0])

                        commando = "SELECT rut_cliente, nombre, apellido FROM cliente WHERE rut_cliente=" + str(clean_rut_cliente)
                        cur = conn.cursor()
                        cur.execute(commando)
                        datos_personales = cur.fetchall()
                        confirmacion = raw_input("\n\tSeguro que desea eliminar a " + datos_personales[0][1] + " "
                                                 +datos_personales[0][2]+" (Rut "+str(datos_personales[0][0])
                                                 +") (Si/No)?")
                        confirmacion = confirmacion.lower()
                        if confirmacion == "si":
                            delete_command = "DELETE FROM cliente WHERE rut_cliente={}".format(clean_rut_cliente)
                            cur.execute(delete_command)
                            conn.commit()
                        else:
                            print "\nVolviendo al menu anterior"
                        cur.close()

                    # OPCION 5: SALIR DE LA APLICACION
                    elif pregunta == 5:
                        print "\nVolviendo al menu anterior"
                        break



        # ADMINISTRAR VENTAS GRUPO
        elif pregunta == 6:

            # nVeces1=0
            while True:
                # IMPRIME EL MENU DE OPCIONES A SELECCIONAR
                lector_menus('menuVentas.txt')

                # PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta = int(raw_input("Escriba del 1 al 4 para procesar su solicitud:"))
                # DISTINTAS OPCIONES SOBRE LAS VENTAS
                if pregunta == 1 or pregunta == 2 or pregunta == 3 or pregunta == 4:

                    # OPCION 1: VER VENTAS DE ESTE MES
                    if pregunta == 1:
                        commando_compras = "SELECT clasificacion, producto.nombre, cantidad FROM venta " \
                                           "JOIN gondola_producto ON venta.id_gondola_producto = gondola_producto.id_gondola_producto " \
                                           "JOIN gondola ON gondola_producto.id_gondola = gondola.id_gondola " \
                                           "JOIN pasillo ON gondola.id_pasillo = pasillo.id_pasillo " \
                                           "JOIN local ON pasillo.id_local = local.id_local " \
                                           "JOIN producto ON gondola_producto.id_producto = producto.id_producto " \
                                           "WHERE date_trunc('month', venta.fecha) = date_trunc('month', current_date)"

                    # OPCION 2: VER TODAS LAS VENTAS
                    elif pregunta == 2:
                        pass

                    # OPCION 3: AGREGAR VENTAS
                    elif pregunta == 3:
                        pass

                    # OPCION 4: PARA SALIR DE LA APLICACION
                    elif pregunta == 4:
                        print "Usted salio de la aplicacion"
                        break

        # SALIR DE LA APLICACION
        elif pregunta == 7:
            print "Usted salio de la aplicacion"
            break

    else:
        print "La opcion ingresada es incorrecta"
