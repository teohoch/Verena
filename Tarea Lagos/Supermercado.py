# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:37:24 2016

@author: Raquel Cutillas
"""

#***************** TAREA 2  *************************************************
#from numpy import random
#from matplotlib import *
import psycopg2

#**************** INICIO CODIGO PROGRAMA *************************************
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




nVeces=0
while True:
    #IMPRIME MENU OPCIONES PARA EL USUARIO
    menu=open('menu.txt')
    linea = menu.readline()
    print linea
    i=0
    while i<len (linea):
        linea = menu.readline()
        print linea
        i+=1
    
   
    #CONEXION A LA BASE DE DATOS ****** REVISAR
    conn= psycopg2.connect (host= 'icc.uandes.cl', database= 'grupo12', user ='grupo12', password='lpqHGr')
    cur=conn.cursor()
    
    #PREGUNTA AL USUARIO QUE DESEA REALIZAR
    pregunta= int(raw_input("Escriba del 1 al 7 para procesar su solicitud:"))
    if pregunta ==1 or pregunta ==2 or pregunta ==3 or pregunta ==4 or pregunta ==5 or pregunta==6 or pregunta ==7:
    
                
       #ADMINISTRAR PRODUCTOS RAQUEL
        if pregunta==1:
            
            #nVeces1=0
            while True:
                #IMPRIME LISTA PRODUCTOS
                cur=conn.cursor()

                cur.execute ("SELECT id_producto, nombre, marca FROM producto ")
                rows=cur.fetchall()
                
                for row in rows:
                    
                    print '\n\tid_producto: {}' .format (row[0])
                    print '\tnombre: {}' .format (row[1])
                    print '\tmarca {}' .format (row[2]) 
                    
                cur.close()
                
                menu=open('ListaProductos.txt')
                linea = menu.readline()
                print linea
                i=0
                while i<len (linea):
                    linea = menu.readline()
                    print linea
                    i+=1
                    
                #PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta= int(raw_input("Escriba del 1 al 4 para procesar su solicitud:"))
                
                #numero de productos registrados iniciales
                ultimoId=40           
                
                #DISTINTAS OPCIONES SOBRE LOS PRODUCTOS
                if pregunta ==1 or pregunta ==2 or pregunta ==3 or pregunta ==4:
                         
                    #OPCION 1: AGREGAR UN PRODUCTO
                    if pregunta==1:
                        cur=conn.cursor()
                        
                        idProd=ultimoId +1
                        ultimoId+=1
                        #Revisar, para cuadno el usuario entrega otro valor
                        cur=conn.cursor()
                        cur.execute ("SELECT id_categoria, nombre FROM categoria ")
                        rows=cur.fetchall()
                        
                        categorias = ""
                        for row in rows:
                            categorias += str(row[0]) + " " + str(row[1]) + ", " 
                            
                        print " Categorias: Ingrese el numero que corresponde a la categoria: " + categorias
                        numCateg=int(raw_input("Ingrese el numero de la Categoria:"))
                        
                        cur=conn.cursor()
                        cur.execute ("SELECT id_tamano, cantidad, unidad FROM tamano ")
                        rows=cur.fetchall()
                        
                        tamanos = ""
                        for row in rows:
                            tamanos += str(row[1]) + " " + str(row[2]) + ": " + str(row[0]) + ", " 
                            
                        print " Tamaños: Ingrese el numero que corresponde al tamaño: " + tamanos 
                        
                        tam=int(raw_input("Ingrese el tamano del producto:"))
                        
                        nombre=raw_input("Ingrese el nombre del producto:")
                        marca=raw_input("Ingrese la marca del producto:")
                        
                        #CONSULTAR CON RAIMUNDO  preguntar que pasa con el tamano                    
                        cur.execute ("INSERT INTO producto (id_producto,id_categoria,id_tamano, nombre, marca) VALUES (%s,%s,%s,%s,%s);", (idProd,numCateg, tam, nombre, marca))
                        conn.commit()
                        
                    #OPCION 2: ELIMINAR UN PRODUCTO    
                    elif pregunta==2:
                        cur=conn.cursor ()
                        
                        print " Numero de Id registrados hasta el momento,",ultimoId                                            
                        idProd=int(raw_input("Ingrese el Id del producto que desea eliminar:"))
                        
                        #CONSULTAR CON RAIMUNDO     
                        cur.execute("DELETE FROM producto WHERE id_producto='%s'",[idProd])
                        
                        conn.commit()
                                                  
                    #OPCION 3: DETALLES DE UN PRODUCTO ******* FALTA ESTE 
                    elif pregunta==3:
                        pass
   
                    #OPCION 4: SALIR DE LA APLICACION
                    elif pregunta==4:
                        print "Usted salio de la aplicacion"
                        break
             
       #ADMINISTRAR CATEGORIA RAQUEL
        elif pregunta==2:
            
            #nVeces1=0
            while True:
                #IMPRIME LISTA DE CATEGORIAS
                cur=conn.cursor()

                cur.execute ("SELECT id_categoria, nombre FROM categoria ")
                rows=cur.fetchall()
                
                for row in rows:
                    
                    print '\n\tid_categoria: {}' .format (row[0])
                    print '\tnombre: {}' .format (row[1])
                                        
                cur.close()
                
                menu=open('ListaCategorias.txt')
                linea = menu.readline()
                print linea
                i=0
                while i<len (linea):
                    linea = menu.readline()
                    print linea
                    i+=1
                    
                #PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta= int(raw_input("Escriba del 1 al 4 para procesar su solicitud:"))
                ultimaCateg=5
                
                #DISTINTAS OPCIONES SOBRE LAS CATEGORIAS
                if pregunta ==1 or pregunta ==2 or pregunta ==3 or pregunta ==4:
                         
                    #OPCION 1: DETALLES DE LA CATEGORIA
                    if pregunta==1:
                        pass
                        
                    #OPCION 2: AGREGAR UNA CATEGORIA  
                    elif pregunta==2:
                        cur=conn.cursor()
                        
                        numCateg= ultimaCateg + 1
                        nombre=raw_input("Ingrese el nombre de la Categoria:")
                        qCambios=0
                                                                        
                        cur.execute ("INSERT INTO categoria (id_categoria,nombre,cantidad_cambios) VALUES (%s,%s,%s);", (numCateg,nombre,qCambios))
                        conn.commit()
                                                  
                    #OPCION 3: ELIMINAR UNA CATEGORIA
                    elif pregunta==3:
                        cur=conn.cursor ()
                        
                        numCateg=raw_input("Ingrese el Id de la Categoria que desea eliminar:")
                        cur.execute("DELETE FROM categoria WHERE id_categoria='%s'",[numCateg])
                        
                        conn.commit()
 
                    #OPCION 4: SALIR DE LA APLICACION
                    elif pregunta==4:
                        print "Usted salio de la aplicacion"
                        break
          
        #ADMINISTRAR LOCAL PEDRO
        elif pregunta==3:
            
            #nVeces1=0
            while True:
                #IMPRIME LISTA DE LOCALES SEGUN SU CLASIFICACION
                cur=conn.cursor()

                cur.execute ("SELECT id_local, clasificacion FROM local ")
                rows=cur.fetchall()
                
                for row in rows:
                    
                    print '\n\tid_local: {}' .format (row[0])
                    print '\tclasificacion: {}' .format (row[1])
                                        
                cur.close()
                
                menu=open('ListaLocales.txt')
                linea = menu.readline()
                print linea
                i=0
                while i<len (linea):
                    linea = menu.readline()
                    print linea
                    i+=1
                    
                #PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta= int(raw_input("Escriba del 1 al 4 para procesar su solicitud:"))
                #DISTINTAS OPCIONES SOBRE LOS LOCALES
                if pregunta ==1 or pregunta ==2 or pregunta ==3 or pregunta ==4:
                         
                    #OPCION 1: DETALLES DEL LOCAL
                    if pregunta==1:
                        pass
                        
                    #OPCION 2: AGREGAR UN LOCAL
                    elif pregunta==2:
                        cur=conn.cursor()
                        
                        clasificacion=raw_input("Ingrese la clasificacion del local:")
                        direccion=raw_input("Ingrese la direccion del local:")
                        comuna=raw_input("Ingrese la comuna del local:")
                                               
                        cur.execute ("INSERT INTO Local (nclasificacion, direccion, comuna) VALUES (%s, %s,%s);", (clasificacion, direccion, comuna))
                        conn.commit()
                                                  
                    #OPCION 3: ELIMINAR UN LOCAL
                    elif pregunta==3:
                        cur=conn.cursor ()
                        
                        nombre=raw_input("Ingrese la clasificacion del Local que desea eliminar:")
                        cur.execute("DELETE FROM producto WHERE clasificacion='%s'",[clasificacion])
                        
                        conn.commit()
 
                    #OPCION 4: SALIR DE LA APLICACION
                    elif pregunta==4:
                        print "Usted salio de la aplicacion"
                        break
                      
         
        #ADMINISTRAR PASILLOS Y GONDOLAS GRUPO
        elif pregunta==4:
            
            
            #nVeces1=0
            while True:
                #IMPRIME LISTA DE LOCALES SEGUN SU CLASIFICACION
                cur=conn.cursor()

                cur.execute ("SELECT id_local, clasificacion FROM local ")
                rows=cur.fetchall()
                
                for row in rows:
                    
                    print '\n\tid_local: {}' .format (row[0])
                    print '\tclasificacion: {}' .format (row[1])
                                        
                variable= raw_input("Ingrese la clasificacion que desea:")
                            
                cur.execute ("SELECT pa.id_pasillo, pa.numero FROM local L, pasillo pa WHERE pa.id_local=l.id_local AND l.clasificacion='{}'".format (variable))
                
                rows=cur.fetchall()
                
                for row in rows:
                    
                    print '\n\tpa.id_pasillo: {}' .format (row[0])
                    print '\tpa.numero: {}' .format (row[1])
                                        
                cur.close()        
                
                ##### me quedo aqui
                
                
                
                
                
                #IMPRIME MENU OPCIONES PARA EL USUARIO
                menu=open('menuPasilloGondola.txt')
                linea = menu.readline()
                print linea
                i=0
                while i<len (linea):
                    linea = menu.readline()
                    print linea
                    i+=1
               
               #PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta= int(raw_input("Escriba del 1 al 8 para procesar su solicitud:"))
                ultimoIdPas=30
                numPasLocal=5
                ultimoIdGon=120
                
                #DISTINTAS OPCIONES SOBRE LOS LOCALES
                if pregunta ==1 or pregunta ==2 or pregunta ==3 or pregunta ==4 or pregunta==5 or pregunta ==6 or pregunta==7 or pregunta==8:
                         
                    #OPCION 1: AGREGAR PASILLO
                    if pregunta==1:
                        cur=conn.cursor()
                        
                        idPasillo=ultimoIdPas + 1
                        
                        #Revisar, para cuando el usuario entrega otro valor
                        print " Categorias: Ingrese el numero que corresponde a la categoria: Dulces 1, Congelados 2, Bebidas 3, Limpieza 4 y Despensa 5"
                        numCateg=int(raw_input("Ingrese el numero de la Categoria:"))
                        
                        print "Locales: Ingrese el numero que corresponde al local: Hipermercado Vitacura 1, Hipermercado Las Condes 2, Supermercado Lo Curro 3, Almacen Maria 4, Supermercado Estoril 5, Almacen Alba 6:"
                        idLocal=raw_input("Ingrese el Id del local:")
                        
                        numero=numPasLocal+1
                                               
                        cur.execute ("INSERT INTO pasillo (id_pasillo, id_categoria, id_local,numero) VALUES (%s, %s,%s, %s);", (idPasillo, numCateg, idLocal, numero))
                        conn.commit()
                        
                    #OPCION 2: EDITAR CATEGORIA
                    elif pregunta==2:
                        pass
                                                  
                    #OPCION 3: AGREGAR GONDOLA
                    elif pregunta==3:
                        
                        cur=conn.cursor()
                        
                        idGondola=ultimoIdGon +1
                        
                        print " Recuerde que cada local tiene inicialmente 5 pasillos"
                        id_pasillo=int(raw_input("Ingrese el numero del pasillo:"))
                        
                        nivel=0
                        print " Recuerde tipo Normal o Preferecial"
                        tipo=raw_input("Ingrese la comuna del local:")
                        
                        if tipo== "Normal":
                            nivel+=2
                        else:
                            nivel+=1
                                               
                        cur.execute ("INSERT INTO gondola (id_gondola, id_pasillo, nivel, tipo) VALUES (%s,%s,%s,%s);", (clasificacion, direccion, comuna))
                        conn.commit()
                        
                    #OPCION 4: ASIGNAR GONDOLA
                    elif pregunta==4:    
                        pass
                    
                    #OPCION 5:ADMINISTRAR GONDOLAS PREFERENCIALES    
                    elif pregunta==5:
                        pass     
                    
                    #OPCION 6: VER UBICACIONES        
                    elif pregunta==6:
                        pass
                    
                    #OPCION 7: ELIMINAR GONDOLA    
                    elif pregunta==7:
                        
                        cur=conn.cursor ()
                        
                        idGon=int(raw_input("Ingrese el Id de la gondola que desea eliminar:"))
                        cur.execute("DELETE FROM gondola WHERE id_gondola='%s'",[idGon])
                        
                        conn.commit()
 
                    #OPCION 8: SALIR DE LA APLICACION
                    elif pregunta==8:
                        print "Usted salio de la aplicacion"
                        break
                       
                    
        #ADMINISTRAR CLIENTES VICENTE
        elif pregunta==5:

            while True:

                cur = conn.cursor()
                cur.execute("SELECT rut_cliente, nombre, apellido FROM cliente ")
                rows = cur.fetchall()
                cur.close()

                table_printer(rows, ["Rut Cliente", "Nombre", "Apellido"])

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

                        print "\nDatos del Cliente:"
                        print "\tNombre completo: " + datos_personales[0][1] + " " + datos_personales[0][2]
                        print "\tRUT: " + str(datos_personales[0][0])
                        print "\tFecha Nacimiento: " + str(datos_personales[0][3].strftime('%d-%m-%Y'))
                        print "\tComuna de Residencia: " + str(datos_personales[0][4])
                        print "\tComuna de Trabajo: " + str(datos_personales[0][4])

                        if len(datos_personales) > 0:
                            commando_compras = "SELECT venta.fecha, local.clasificacion, venta.cantidad FROM venta " \
                                               "JOIN local ON venta.id_local = local.id_local " \
                                               "WHERE rut_cliente={0}".format(str(clean_rut_cliente))
                            cur.execute(commando_compras)
                            datos_compras = cur.fetchall()
                            cur.close()
                            n_compras = len(datos_compras)
                            if n_compras > 0:
                                total = 0
                                locales = []
                                for compra in datos_compras:
                                    total += compra[2]
                                    locales.append(compra[1])

                                max_local = max(set(locales), key=locales.count)
                                promedio = total / n_compras

                                print "\n\tCompras realizadas por el Cliente:"
                                table_printer(datos_compras, ["Fecha", "Local", "Cantidad"])
                                print "\tLocal mas frecuente: " + max_local
                                print "\tPromedio de productos adquiridos por compra: " + str(promedio)
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
                                  "comuna_trabajo, comuna_residencia) VALUES ({}, '{}', '{}', '{}', '{}', '{}');" \
                            .format(clean_rut_cliente, nombre, apellido, fechaNacimiento, comunaResidencia,
                                    comunaTrabajo)

                        cur = conn.cursor()
                        cur.execute("SET DATESTYLE = DMY")
                        cur.execute(comando)
                        conn.commit()
                        cur.close()

                        print " ".join("\nCliente", nombre, apellido, "creado con exito")

                    # OPCION 3: EDITAR UN CLIENTE
                    elif pregunta == 3:
                        rutCliente = raw_input("Ingrese el Rut del Cliente a editar:")
                        clean_rut_cliente = int(rutCliente.split("-")[0])

                        commando = "SELECT rut_cliente, nombre, apellido, fecha_nacimiento, comuna_residencia, " \
                                   "comuna_trabajo FROM cliente WHERE rut_cliente=" + str(clean_rut_cliente)
                        cur = conn.cursor()
                        cur.execute(commando)
                        datos_personales = cur.fetchall()
                        if len(datos_personales) > 0:
                            print "\nDatos del Cliente:"
                            print "\tNombre completo: " + datos_personales[0][1] + " " + datos_personales[0][2]
                            print "\tRUT: " + str(datos_personales[0][0])
                            print "\tFecha Nacimiento: " + str(datos_personales[0][3].strftime('%d-%m-%Y'))
                            print "\tComuna de Residencia: " + str(datos_personales[0][4])
                            print "\tComuna de Trabajo: " + str(datos_personales[0][5])

                            nombre = raw_input(
                                "Ingrese el Nombre del Cliente (Actualmente es '" + datos_personales[0][1] + "'):")
                            apellido = raw_input(
                                "Ingrese el Primer Apellido del Cliente (Actualmente es '" + datos_personales[0][
                                    2] + "'):")
                            fechaNacimiento = raw_input(
                                "Ingrese la fecha de nacimiento DD-MM-AAAA del Cliente (Actualmente es '" + str(
                                    datos_personales[0][3].strftime('%d-%m-%Y')) + "'):")
                            comunaTrabajo = raw_input(
                                "Ingrese la Comuna donde Trabaja el Cliente (Actualmente es '" + datos_personales[0][
                                    4] + "'):")
                            comunaResidencia = raw_input(
                                "Ingrese la Comuna donde Reside el Cliente (Actualmente es '" + datos_personales[0][
                                    5] + "'):")

                            update_command = "UPDATE cliente SET nombre='{}', apellido='{}'," \
                                             " fecha_nacimiento= to_date('{}','DD-MM-YYYY'), comuna_trabajo='{}'" \
                                             ",comuna_residencia='{}' WHERE rut_cliente = {};" \
                                .format(nombre, apellido, fechaNacimiento, comunaTrabajo, comunaResidencia,
                                        clean_rut_cliente)
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

                        commando = "SELECT rut_cliente, nombre, apellido FROM cliente WHERE rut_cliente=" + str(
                            clean_rut_cliente)
                        cur = conn.cursor()
                        cur.execute(commando)
                        datos_personales = cur.fetchall()
                        confirmacion = raw_input("\n\tSeguro que desea eliminar a " + datos_personales[0][1] + " "
                                                 + datos_personales[0][2] + " (Rut " + str(datos_personales[0][0])
                                                 + ") (Si/No)?")
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
            
            
        #ADMINISTRAR VENTAS GRUPO
        elif pregunta== 6:
           
           #nVeces1=0
            while True:
                #IMPRIME EL MENU DE OPCIONES A SELECCIONAR
                lector_menus('menuVentas.txt')

                #PREGUNTA AL USUARIO QUE DESEA REALIZAR
                pregunta= raw_input("Escriba del 1 al 4 para procesar su solicitud:")
                #DISTINTAS OPCIONES SOBRE LAS VENTAS
                if pregunta in ("1", "2", "3", "4"):
                    pregunta = int(pregunta)
                         
                    #OPCION 1: VER VENTAS
                    if pregunta==1:
                        comando_ventas = "SELECT * FROM venta WHERE date_trunc('month', venta.fecha) = date_trunc('month', current_date)"
                        cur = conn.cursor()
                        cur.execute(comando_locales)
                        ventas_mes = cur.fetchall()
                        cur.close()

                        

                        
                    #OPCION 2: VER TODAS LAS VENTAS
                    elif pregunta==2:
                        pass
                    
                    #OPCION 3: AGREGAR VENTAS
                    elif pregunta==3:
                        comando_locales = "SELECT id_local, clasificacion FROM local"
                        comando_productos = "SELECT id_producto, nombre FROM producto"
                        cur = conn.cursor()
                        cur.execute(comando_locales)
                        locales = cur.fetchall()
                        cur.execute(comando_productos)
                        productos = cur.fetchall()
                        cur.close()

                        rut_cajero = raw_input("Ingrese el Rut del Cajero: ")
                        rut_client = raw_input("Ingrese el Rut del Cliente: ")
                        clean_rut_cliente = int(rut_client.split("-")[0])
                        clean_rut_cajero = int(rut_cajero.split("-")[0])

                        print "\tLocales disponibles:"
                        table_printer(locales,["ID Local","Local"])
                        id_local = raw_input("\nIngrese ID del local: ")

                        print "\tProductos:"
                        table_printer(productos,["ID Producto", "Producto"])
                        productos = []
                        cantidad_total = 0
                        while True:
                            id_producto = int(raw_input("Ingrese ID del producto a Vender: "))
                            cantidad = int(raw_input("Ingrese la cantidad de este producto a vender: "))
                            cantidad_total+=cantidad
                            productos.append([id_producto,cantidad])
                            if (raw_input("¿Desea agregar otro  producto a la venta? (Si/No")).lower()=="no":
                                break
                        comando_crear_venta = "INSERT INTO venta (fecha, cantidad, id_local,rut_cliente,rut_cajero) " \
                                              "VALUES (CURRENT_TIMESTAMP ,{},{},{},{}) RETURNING id"\
                            .format(cantidad_total,id_local,clean_rut_cliente,clean_rut_cajero)
                        cur = conn.cursor()
                        cur.execute(comando_crear_venta)
                        id_venta = cur.fetchone()[0]
                        conn.commit()
                        cur.close()


                        str_productos = []
                        for producto in productos:
                            str_productos.append("({},{},{})".format(id_venta,str(producto[0]),str(producto[1])))
                        comando_crear_venta_producto = "INSERT INTO venta_producto (id_venta, id_producto, cantidad) " \
                                                       "VALUES " + ", ".join(str_productos)
                        cur = conn.cursor()
                        cur.execute(comando_crear_venta_producto)
                        conn.commit()
                        cur.close()

                        print "Venta Creada con Exito"


                    
                    #OPCION 4: PARA SALIR DE LA APLICACION
                    elif pregunta==4:
                        print "Usted salio de la aplicacion"
                        break
          
        #SALIR DE LA APLICACION 
        elif pregunta==7:
            print "Usted salio de la aplicacion"
            break
    
    else:
        print "El numero ingresado es incorrecto"
        nVeces+=1 

    
















            
            
            
           
   