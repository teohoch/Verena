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


nVeces = 0
while True:
	# IMPRIME MENU OPCIONES PARA EL USUARIO
	lector_menus("menu.txt")

	# CONEXION A LA BASE DE DATOS ****** REVISAR
	conn = psycopg2.connect(host='icc.uandes.cl', database='grupo12', user='grupo12', password='lpqHGr')
	cur = conn.cursor()

	# PREGUNTA AL USUARIO QUE DESEA REALIZAR
	pregunta = raw_input("Escriba del 1 al 7 para procesar su solicitud:")
	if pregunta in ("1","2","3","4","5","6","7"):
		pregunta=int(pregunta)

		# ADMINISTRAR PRODUCTOS RAQUEL
		if pregunta == 1:

			# nVeces1=0
			while True:
				# IMPRIME LISTA PRODUCTOS
				cur = conn.cursor()

				cur.execute("SELECT id_producto, nombre, marca FROM producto ")
				rows = cur.fetchall()

				for row in rows:
					print '\n\tid_producto: {}'.format(row[0])
					print '\tnombre: {}'.format(row[1])
					print '\tmarca {}'.format(row[2])

				cur.close()

				lector_menus('ListaProductos.txt')

				# PREGUNTA AL USUARIO QUE DESEA REALIZAR
				pregunta = raw_input("Escriba del 1 al 4 para procesar su solicitud:")

				# numero de productos registrados iniciales
				ultimoId = rows[-1][0]

				# DISTINTAS OPCIONES SOBRE LOS PRODUCTOS
				if pregunta in ("1","2","3","4"):
					pregunta = int(pregunta)

					# OPCION 1: AGREGAR UN PRODUCTO
					if pregunta == 1:
						cur = conn.cursor()

						idProd = ultimoId + 1
						ultimoId += 1
						# Revisar, para cuadno el usuario entrega otro valor
						cur = conn.cursor()
						cur.execute("SELECT id_categoria, nombre FROM categoria ")
						rows = cur.fetchall()

						categorias = ""
						for row in rows:
							categorias += str(row[0]) + " " + str(row[1]) + ", "

						print " Categorias: Ingrese el numero que corresponde a la categoria: " + categorias
						numCateg = int(raw_input("Ingrese el numero de la Categoria:"))

						cur = conn.cursor()
						cur.execute("SELECT id_tamano, cantidad, unidad FROM tamano ")
						rows = cur.fetchall()

						tamanos = ""
						for row in rows:
							tamanos += str(row[1]) + " " + str(row[2]) + ": " + str(row[0]) + ", "

						print " Tamaños: Ingrese el numero que corresponde al tamaño: " + tamanos

						tam = int(raw_input("Ingrese el tamano del producto:"))

						nombre = raw_input("Ingrese el nombre del producto:")
						marca = raw_input("Ingrese la marca del producto:")

						# CONSULTAR CON RAIMUNDO  preguntar que pasa con el tamano
						cur.execute(
							"INSERT INTO producto (id_producto,id_categoria,id_tamano, nombre, marca) VALUES (%s,%s,%s,%s,%s);",
							(idProd, numCateg, tam, nombre, marca))
						conn.commit()

					# OPCION 2: ELIMINAR UN PRODUCTO
					elif pregunta == 2:
						cur = conn.cursor()

						print " Numero de Id registrados hasta el momento,", ultimoId
						idProd = int(raw_input("Ingrese el Id del producto que desea eliminar:"))

						# CONSULTAR CON RAIMUNDO
						cur.execute("DELETE FROM producto WHERE id_producto='%s'", [idProd])

						conn.commit()

					# OPCION 3: DETALLES DE UN PRODUCTO ******* FALTA ESTE
					elif pregunta == 3:
						pass

					# OPCION 4: SALIR DE LA APLICACION
					elif pregunta == 4:
						print "Usted salio de la aplicacion"
						break

						# ADMINISTRAR CATEGORIA RAQUEL
		elif pregunta == 2:

			# nVeces1=0
			while True:
				# IMPRIME LISTA DE CATEGORIAS
				cur = conn.cursor()

				cur.execute("SELECT id_categoria, nombre FROM categoria ")
				rows = cur.fetchall()

				for row in rows:
					print '\n\tid_categoria: {}'.format(row[0])
					print '\tnombre: {}'.format(row[1])

				cur.close()

				menu = open('ListaCategorias.txt')
				linea = menu.readline()
				print linea
				i = 0
				while i < len(linea):
					linea = menu.readline()
					print linea
					i += 1

				# PREGUNTA AL USUARIO QUE DESEA REALIZAR
				pregunta = int(raw_input("Escriba del 1 al 4 para procesar su solicitud:"))
				ultimaCateg = 5

				# DISTINTAS OPCIONES SOBRE LAS CATEGORIAS
				if pregunta == 1 or pregunta == 2 or pregunta == 3 or pregunta == 4:

					# OPCION 1: DETALLES DE LA CATEGORIA
					if pregunta == 1:
						pass

					# OPCION 2: AGREGAR UNA CATEGORIA
					elif pregunta == 2:
						cur = conn.cursor()

						numCateg = ultimaCateg + 1
						nombre = raw_input("Ingrese el nombre de la Categoria:")
						qCambios = 0

						cur.execute("INSERT INTO categoria (id_categoria,nombre,cantidad_cambios) VALUES (%s,%s,%s);",
						            (numCateg, nombre, qCambios))
						conn.commit()

					# OPCION 3: ELIMINAR UNA CATEGORIA
					elif pregunta == 3:
						cur = conn.cursor()

						numCateg = raw_input("Ingrese el Id de la Categoria que desea eliminar:")
						cur.execute("DELETE FROM categoria WHERE id_categoria='%s'", [numCateg])

						conn.commit()

					# OPCION 4: SALIR DE LA APLICACION
					elif pregunta == 4:
						print "Usted salio de la aplicacion"
						break

		# ADMINISTRAR LOCAL PEDRO
		elif pregunta == 3:

			# nVeces1=0
			while True:
				# IMPRIME LISTA DE LOCALES SEGUN SU CLASIFICACION
				cur = conn.cursor()

				cur.execute("SELECT id_local, clasificacion FROM local ")
				rows = cur.fetchall()

				for row in rows:
					print '\n\tid_local: {}'.format(row[0])
					print '\tclasificacion: {}'.format(row[1])

				cur.close()

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

				cur = conn.cursor()

				cur.execute("SELECT rut_cliente, nombre, apellido FROM cliente ")
				rows = cur.fetchall()

				for row in rows:
					print '\n\trut_cliente: {}'.format(row[0])
					print '\tnombre: {}'.format(row[1])
					print '\tapellido: {}'.format(row[2])

				cur.close()

				# PREGUNTA AL USUARIO QUE DESEA REALIZAR
				lector_menus("ListaClientes.txt")
				pregunta = raw_input("Escriba del 1 al 5 para procesar su solicitud:")
				# DISTINTAS OPCIONES SOBRE LOS CLIENTES
				if pregunta in ("1","2","3","4","5"):
					pregunta = int(pregunta)

					# OPCION 1: DETALLES DEL CLIENTE
					if pregunta == 1:
						rutCliente = raw_input("Ingrese el Rut del Cliente a mostrar:")
						clean_rut_cliente = int(rutCliente.split("-")[0])

						commando = "SELECT rut_cliente, nombre, apellido FROM cliente WHERE rut_cliente=" + str(clean_rut_cliente)
						commando_compras = "SELECT rut_cliente, cantidad, clasificacion FROM venta JOIN gondola_producto ON venta.id_gondola_producto = gondola_producto.id_gondola_producto JOIN gondola ON gondola_producto.id_gondola = gondola.id_gondola JOIN pasillo ON gondola.id_pasillo = pasillo.id_pasillo JOIN local ON pasillo.id_local = local.id_local WHERE rut_cliente={0}".format(
							str(clean_rut_cliente))

						cur = conn.cursor()
						cur.execute(commando)
						datos_personales=cur.fetchall()
						cur.execute(commando_compras)
						datos_compras=cur.fetchall()
						cur.close()

						print datos_personales
						print datos_compras


					# OPCION 2: AGREGAR UN CLIENTE
					elif pregunta == 2:
						cur = conn.cursor()

						rutCliente = raw_input("Ingrese el Rut del Cliente:")
						nombre = raw_input("Ingrese el Nombre del Cliente:")
						apellido = raw_input("Ingrese el Primer Apellido del Cliente:")
						fechaNacimiento = raw_input("Ingrese la fecha de nacimiento DD_MM_AA del Cliente:")
						comunaTrabajo = raw_input("Ingrese la Comuna donde Trabaja el Cliente:")
						comunaResidencia = raw_input("Ingrese la Comuna donde Reside el Cliente:")

						cur.execute(
							"INSERT INTO Cliente (rutCliente, nombre, apellido, fechaNacimiento, comunaTrabajo, comunaResidencia) VALUES (%s, %s,%s,%s,%s,%s);",
							(rutCliente, nombre, apellido, fechaNacimiento, comunaTrabajo, comunaResidencia))
						conn.commit()

					# OPCION 3: EDITAR UN CLIENTE
					elif pregunta == 3:
						pass

					# OPCION 4: ELIMINAR UN CLIENTE
					elif pregunta == 4:
						pass

					# OPCION 5: SALIR DE LA APLICACION
					elif pregunta == 5:
						print "Usted salio de la aplicacion"
						break



		# ADMINISTRAR VENTAS GRUPO
		elif pregunta == 6:

			# nVeces1=0
			while True:
				# IMPRIME EL MENU DE OPCIONES A SELECCIONAR
				menu = open('menuVentas.txt')
				linea = menu.readline()
				print linea
				i = 0
				while i < len(linea):
					linea = menu.readline()
					print linea
					i += 1

				# PREGUNTA AL USUARIO QUE DESEA REALIZAR
				pregunta = int(raw_input("Escriba del 1 al 4 para procesar su solicitud:"))
				# DISTINTAS OPCIONES SOBRE LAS VENTAS
				if pregunta == 1 or pregunta == 2 or pregunta == 3 or pregunta == 4:

					# OPCION 1: VER VENTAS
					if pregunta == 1:
						pass

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
		nVeces += 1
