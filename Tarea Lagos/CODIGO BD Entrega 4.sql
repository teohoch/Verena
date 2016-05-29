DROP TABLE IF EXISTS Local
CASCADE;
DROP TABLE IF EXISTS Pasillo
CASCADE;
DROP TABLE IF EXISTS Gondola
CASCADE;
DROP TABLE IF EXISTS Categoria
CASCADE;
DROP TABLE IF EXISTS Tamano
CASCADE;
DROP TABLE IF EXISTS Producto
CASCADE;
DROP TABLE IF EXISTS Cliente
CASCADE;
DROP TABLE IF EXISTS Venta
CASCADE;
DROP TABLE IF EXISTS Cajero
CASCADE;
DROP TABLE IF EXISTS Gondola_Producto
CASCADE;
DROP TABLE IF EXISTS Promocion
CASCADE;
DROP TABLE IF EXISTS Movimiento
CASCADE;


CREATE TABLE Local (
    Id_local INTEGER PRIMARY KEY,
    Clasificacion VARCHAR(255),
    Direccion VARCHAR (255),
    Comuna VARCHAR (255)
);

CREATE TABLE Pasillo (
   Id_pasillo INTEGER PRIMARY KEY,
   Id_categoria INTEGER,
   Id_local  INTEGER,
   Numero INTEGER
);

CREATE TABLE Gondola (
   Id_gondola INTEGER PRIMARY KEY,
   Id_pasillo INTEGER,
   Nivel  INTEGER,
   Tipo VARCHAR(255)
);

CREATE TABLE Categoria (
   Id_categoria INTEGER PRIMARY KEY,
   Nombre VARCHAR(255),
   Cantidad_cambios  INTEGER
);

CREATE TABLE Tamano (
   Id_tamano INTEGER PRIMARY KEY,
   Cantidad INTEGER,
   Unidad VARCHAR(255)
 );

CREATE TABLE Producto (
   Id_producto INTEGER PRIMARY KEY,
   Id_categoria INTEGER,
   Id_tamano  INTEGER,
   Nombre VARCHAR(255),
   Marca VARCHAR(255)
);


CREATE TABLE Cliente (
   Rut_cliente INTEGER PRIMARY KEY,
   Nombre VARCHAR(255),
   Apellido VARCHAR(255),
   Fecha_nacimiento DATE,
   Comuna_trabajo VARCHAR(255),
   Comuna_residencia VARCHAR(255)
 );

CREATE TABLE Venta (
   Rut_cliente INTEGER,
   Id_gondola_producto INTEGER,
   Rut_cajero INTEGER,
   Fecha TIMESTAMP,
   Cantidad INTEGER,
   PRIMARY KEY (Rut_cliente, Id_gondola_producto)
);

CREATE TABLE Cajero (
   Rut_cajero INTEGER PRIMARY KEY,
   Id_local INTEGER,
   Nombre VARCHAR(255),
   Apellido VARCHAR(255),
   Hora_inicio TIME,
   Hora_fin TIME,
   Sueldo INTEGER
 );

CREATE TABLE Gondola_Producto (
    Id_gondola_producto INTEGER PRIMARY KEY,   
    Id_gondola INTEGER,
    Id_producto INTEGER,   
    Nivel INTEGER
);

CREATE TABLE Promocion (
   Id_promocion INTEGER PRIMARY KEY,
   Id_gondola INTEGER,
   Descuento VARCHAR(255),
   Fecha_inicio TIMESTAMP,
   Fecha_fin TIMESTAMP
 );

CREATE TABLE Movimiento(
   Id_gondola_original INTEGER, 
   Id_gondola_destino INTEGER, 
   Nivel_original INTEGER, 
   Nivel_destino INTEGER, 
   Id_producto INTEGER,
   Fecha TIMESTAMP,
   PRIMARY KEY (Id_gondola_original, Id_gondola_destino,Nivel_original, Nivel_destino, Id_producto)
);


ALTER TABLE Pasillo
ADD CONSTRAINT Id_categoria_fk 
FOREIGN KEY (Id_categoria) 
REFERENCES Categoria (Id_categoria)
ON DELETE CASCADE;

ALTER TABLE Pasillo
ADD CONSTRAINT Id_local_fk 
FOREIGN KEY (Id_local) 
REFERENCES Local (Id_local)
ON DELETE CASCADE;

ALTER TABLE Producto 
ADD CONSTRAINT Id_categoria_fk 
FOREIGN KEY (Id_categoria) 
REFERENCES Categoria (Id_categoria)
ON DELETE CASCADE;

ALTER TABLE Producto  
ADD CONSTRAINT Id_tamano_fk 
FOREIGN KEY (Id_tamano) 
REFERENCES Tamano (Id_tamano)
ON DELETE CASCADE;

ALTER TABLE Venta
ADD CONSTRAINT Id_gondola_producto_fk 
FOREIGN KEY (Id_gondola_producto) 
REFERENCES Gondola_Producto (Id_gondola_producto)
ON DELETE CASCADE;

ALTER TABLE Venta
ADD CONSTRAINT Rut_cliente_fk 
FOREIGN KEY (Rut_cliente) 
REFERENCES Cliente (Rut_cliente)
ON DELETE CASCADE; 
  
ALTER TABLE Venta
ADD CONSTRAINT Rut_cajero_fk 
FOREIGN KEY (Rut_cajero) 
REFERENCES Cajero (Rut_cajero)
ON DELETE CASCADE;  

ALTER TABLE Gondola_Producto
ADD CONSTRAINT Id_gondola_fk 
FOREIGN KEY (Id_gondola) 
REFERENCES Gondola (Id_gondola)
ON DELETE CASCADE;  

ALTER TABLE Gondola_Producto
ADD CONSTRAINT Id_producto_fk 
FOREIGN KEY (Id_producto) 
REFERENCES Producto (Id_producto)
ON DELETE CASCADE;  

ALTER TABLE Gondola
ADD CONSTRAINT Id_pasillo_fk 
FOREIGN KEY (Id_pasillo) 
REFERENCES Pasillo (Id_pasillo)
ON DELETE CASCADE; 

ALTER TABLE Movimiento
ADD CONSTRAINT Id_gondola_original_fk 
FOREIGN KEY (Id_gondola_original) 
REFERENCES Gondola (Id_gondola)
ON DELETE CASCADE; 

ALTER TABLE Movimiento
ADD CONSTRAINT Id_gondola_destino_fk 
FOREIGN KEY (Id_gondola_destino) 
REFERENCES Gondola (Id_gondola)
ON DELETE CASCADE; 

ALTER TABLE Movimiento
ADD CONSTRAINT Id_producto_fk 
FOREIGN KEY (Id_producto) 
REFERENCES Producto(Id_producto)
ON DELETE CASCADE; 

ALTER TABLE Promocion
ADD CONSTRAINT Id_gondola_fk 
FOREIGN KEY (Id_gondola) 
REFERENCES Gondola(Id_gondola)
ON DELETE CASCADE;

ALTER TABLE Cajero
ADD CONSTRAINT Id_local_fk 
FOREIGN KEY (Id_local) 
REFERENCES Local(Id_local)
ON DELETE CASCADE;

INSERT INTO Categoria (Id_categoria, nombre, cantidad_cambios)
Values (1,'Dulces',0), (2,'Congelados',0), (3,'Bebidas',0), (4,'Limpieza',0), (5,'Despensa',0);

INSERT INTO Tamano (Id_tamano, cantidad, unidad)
VALUES (1,'100','gramos'), (2,'1','kilogramos'), (3,'500','gramos'), (4,'800','gramos'), (5,'1','litro'), 
       (6,'500','mililitros'), (7,'250','mililitros'), (8,'8','gramos'), (9,'800','mililitros'), (10,'100','unidades'), (11,'50','metros');

INSERT INTO Producto (Id_producto, Id_categoria, Id_tamano, nombre, marca)
VALUES (1,1,1,'Azucar','IANSA'),(2,1,1,'Gelatina','LIVEAN'),(3,1,1,'Flan','SOPROLE'),(4,1,3,'Cereal','QUAKER'),(5,1,1,'Chocolate','TRENCITO'),
       (6,1,3,'Manjar','COLUN'),(7,1,3,'Mermelada','WATTS'),(8,1,3,'Miel','MONJITAS'),(9,2,1,'Hamburguesas de Pavo','SP'),(10,2,1,'Hamburguesas de Pollo','SP'),
       (11,2,1,'Hamburguesas de Cerdo','SC'),(12,2,3,'Nuggets','Pollito'),(13,2,3,'Choclo','DEL CAMPO'),(14,2,4,'Pizza','GREATVALUE'),(15,2,2,'Papas','DEL CAMPO'),
       (16,2,5,'Helado','SAVORY'),(17,3,5,'Agua_con_gas','VITAL'),(18,3,6,'Agua_sin_gas','CACHANTUN'),(19,3,7,'Bebida_light','CCU'),(20,3,7,'Bebida_energetica','Redbull'),
       (21,3,7,'Bebida_invidividual','Coca-Cola'),(22,3,5,'Jugo_Fresco','ZUKO'),(23,3,8,'Jugo_en_polvo','LIVEAN'),(24,3,6,'NECTAR','WATTS'),(25,4,5,'Cloro','Clorinda'),
       (26,4,7,'Desodorante','Glade'),(27,4,6,'Antigrasa','CIF'),(28,4,9,'Lavaloza','CIF'),(29,4,6,'Limpia_vidrios','WINDEX'),(30,4,10,'Pañuelos','ELITE'),
       (31,4,11,'Papel Higienico','SCOTT'),(32,4,9,'Desinfectante','LYSOL'),(33,5,5,'Aceite','CHEF'),(34,5,5,'Vinagre','CHEF'),(35,5,2,'Arroz','TUCAPEL'),
       (36,5,3,'Lenteja','DEL CAMPO'),(37,5,2,'Poroto','DEL CAMPO'),(38,5,1,'Caldo','MAGGI'),(39,5,1,'Sopa','MAGGI'),(40,5,1,'Atun','FRESCO');


INSERT INTO Local (Id_local, clasificacion, direccion, comuna)
VALUES (1,'Hipermercado Vitacura','Avda. Vitacura 2222','Vitacura'), (2,'Hipermercado Las Condes','Avda.Las Condes 1111','Las Condes'),
       (3,'Supermercado Lo Curro','Lo Curro 2223','Vitacura'),(5,'Supermercado Estoril','Estoril 1112','Las Condes'),
       (4,'Almacen Maria', 'Santa Maria 2224', 'Vitacura'),(6,'Almacen Alba','El Alba 1113','Las Condes');

INSERT INTO Pasillo (Id_pasillo, Id_categoria, Id_local, numero)
VALUES 
/* PRIMER HIPERMERCADO*/
(1,1,1,1),(2,2,1,2),(3,3,1,3),(4,4,1,4),(5,5,1,5),
/* SEGUNDO HIPERMERCADO*/
(6,1,2,1),(7,2,2,2),(8,3,2,3),(9,4,2,4),(10,5,2,5),
/* PRIMER SUPERMERCADO*/
(11,1,3,1),(12,2,3,2),(13,3,3,3),(14,4,3,4),(15,5,3,5),
/* SEGUNDO SUPERMERCADO*/
(16,1,5,1),(17,2,5,2),(18,3,5,3),(19,4,5,4),(20,5,5,5),
/* PRIMER ALMACEN*/
(21,1,6,1),(22,2,6,2),(23,3,6,3),(24,4,6,4),(25,5,6,5),
/* SEGUNDO ALMACEN*/
(26,1,4,1),(27,2,4,2),(28,3,4,3),(29,4,4,4),(30,5,4,5);
       
INSERT INTO Gondola (Id_gondola, Id_pasillo, Nivel, tipo)
VALUES
/*ESTE ES EL PRIMER HIPERMERCADO*/ 
(1,1,2,'Normal'), (2,1,2,'Normal'),(3,1,2,'Normal'),(4,1,2,'Normal'),(5,1,1,'Preferencial'),
(6,2,1,'Preferencial'),(7,2,2,'Normal'),(8,2,2,'Normal'),(9,2,2,'Normal'),(10,2,2,'Normal'),
(11,3,2,'Normal'),(12,3,2,'Normal'),(13,3,2,'Normal'),(14,3,2,'Normal'),(15,3,1,'Preferencial'),
(16,4,1,'Preferencial'),(17,4,2,'Normal'),(18,4,2,'Normal'),(19,4,2,'Normal'),(20,4,2,'Normal'),
(21,5,2,'Normal'),(22,5,2,'Normal'),(23,5,2,'Normal'),(24,5,2,'Normal'),(25,5,1,'Preferencial'),
/*ESTE ES EL SEGUNDO HIPERMERCADO*/ 
(26,6,2,'Normal'), (27,6,2,'Normal'),(28,6,2,'Normal'),(29,6,2,'Normal'),(30,6,1,'Preferencial'),
(31,7,1,'Preferencial'),(32,7,2,'Normal'),(33,7,2,'Normal'),(34,7,2,'Normal'),(35,7,2,'Normal'),
(36,8,2,'Normal'),(37,8,2,'Normal'),(38,8,2,'Normal'),(39,8,2,'Normal'),(40,8,1,'Preferencial'),
(41,9,1,'Preferencial'),(42,9,2,'Normal'),(43,9,2,'Normal'),(44,9,2,'Normal'),(45,9,2,'Normal'),
(46,10,2,'Normal'),(47,10,2,'Normal'),(48,10,2,'Normal'),(49,10,2,'Normal'),(50,10,1,'Preferencial'),
/*ESTE ES EL PRIMER SUPERMERCADO*/ 
(51,11,2,'Normal'),(52,11,2,'Normal'),(53,11,2,'Normal'),(54,11,1,'Preferencial'),
(55,12,1,'Preferencial'),(56,12,2,'Normal'),(57,12,2,'Normal'),(58,12,2,'Normal'),
(59,13,2,'Normal'),(60,13,2,'Normal'),(61,13,2,'Normal'),(62,13,1,'Preferencial'),
(63,14,1,'Preferencial'),(64,14,2,'Normal'),(65,14,2,'Normal'),(66,14,2,'Normal'),
(67,15,2,'Normal'),(68,15,2,'Normal'),(69,15,2,'Normal'),(70,15,1,'Preferencial'),
/*ESTE ES EL SEGUNDO SUPERMERCADO*/
(71,16,2,'Normal'),(72,16,2,'Normal'),(73,16,2,'Normal'),(74,16,1,'Preferencial'),
(75,17,1,'Preferencial'),(76,17,2,'Normal'),(77,17,2,'Normal'),(78,17,2,'Normal'),
(79,18,2,'Normal'),(80,18,2,'Normal'),(81,18,2,'Normal'),(82,18,1,'Preferencial'),
(83,19,1,'Preferencial'),(84,19,2,'Normal'),(85,19,2,'Normal'),(86,19,2,'Normal'),
(87,20,2,'Normal'),(88,20,2,'Normal'),(89,20,2,'Normal'),(90,20,1,'Preferencial'),
/*ESTE ES EL PRIMER ALMACEN*/
(91,21,2,'Normal'),(92,21,2,'Normal'),(93,21,1,'Preferencial'),
(94,22,1,'Preferencial'),(95,22,2,'Normal'),(96,22,2,'Normal'),
(97,23,2,'Normal'),(98,23,2,'Normal'),(99,23,1,'Preferencial'),
(100,24,1,'Preferencial'),(101,24,2,'Normal'),(102,24,2,'Normal'),
(103,25,2,'Normal'),(104,25,2,'Normal'),(105,25,1,'Preferencial'),
/*ESTE ES EL SEGUNDO ALMACEN*/
(106,26,2,'Normal'),(107,26,2,'Normal'),(108,26,1,'Preferencial'),
(109,27,2,'Normal'),(110,27,2,'Normal'),(111,27,1,'Preferencial'),
(112,28,1,'Preferencial'),(113,28,2,'Normal'),(114,28,2,'Normal'),
(115,29,1,'Preferencial'),(116,29,2,'Normal'),(117,29,2,'Normal'),
(118,30,2,'Normal'),(119,30,2,'Normal'),(120,30,1,'Preferencial');

INSERT INTO Cajero (rut_cajero, id_local,nombre, apellido, hora_inicio, hora_fin, sueldo)
VALUES
(7575757,1,'Godofredo','Muralla','8:00:00','20:00:00','500000'),/*Atiende el Hipermercado 1*/
(7878787,2,'Arnaldo','Melo','8:00:00','20:00:00','480000'),/*Atiende el Hipermercado 2*/
(8383838,3,'Cecilia','Prina','8:00:00','19:00:00','400000'),/*Atiende el Supermercado 1*/
(9494949,4,'Alfonso','Guerra','8:00:00','19:00:00','390000'),/*Atiende el Supermercado 2*/
(5454545,5,'Patricia','Funda','9:00:00','19:00:00','320000'),/*Atiende el Almacen 1*/
(6262626,6,'Carla','Belen','9:00:00','19:00:00','300000');/*Atiende el Almacen 2*/

INSERT INTO Cliente (rut_cliente, nombre, apellido, fecha_nacimiento, comuna_trabajo, comuna_residencia)
VALUES
(9874564,'Diego','Rodriguez','1976-09-12','La Granja','Las Condes'),
(6854364,'Marlon','Brando','1946-01-18','Penaflor','Vitacura'),
(17844552,'Kobe','Bryant','1933-12-30','Las Condes','Las Condes'),
(19377864,'Jorge','Valdivia','1962-03-01','Vitacura','Vitacura'),
(11370444,'Lou','Reed','1942-10-11','Las Condes','Providencia'),
(10987654,'Ritchie','Blackmore','1956-03-11','Las Condes','Huechuraba'),
(21191817,'Milovan','Mirosevic','1971-01-11','Las Condes','Las Condes'),
(4324908,'Michael','Jordan','1971-07-24','Vitacura','Las Condes'),
(16874564,'Neil','Young','1991-05-31','Las Condes','Providencia'),
(11954111,'Paul','Giamatti','1956-11-12','Vitacura','La Reina'),
(10101010,'Edward','Norton','1936-05-22','Vitacura','Las Condes'),
(14971064,'Joaquin','Phoenix','1944-04-24','Provdencia','Las Condes'),
(11871514,'Bruce','Wayne','1971-11-11','Las Condes','La Reina'),
(14176664,'John','Cale','1944-08-18','Vitacura','La Granja'),
(17555321,'Rivers','Cuomo','1981-08-18','Las Condes','Las Condes'),
(11222333,'Michael','Keaton','1966-06-16','La Reina','Las Condes'),
(3833534,'Johnny','Greenwood','1990-01-22','Vitacura','Providencia'),
(3444111,'Julian','Casablancas','1976-10-10','La Florida','Vitacura'),
(16111564,'Terry','Kath','1940-07-29','Las Condes','Las Condes'),
(10871568,'James','Hetfield','1981-11-02','Vitacura','Vitacura'),
(9999564,'Jerry','Cantrell','1992-01-25','La Florida','Las Condes'),
(7777564,'Layne','Staley','1933-09-30','Vitacura','Providencia'),
(2224524,'Bradford','Cox','1965-10-20','La Granja','Vitacura'),
(4874999,'Nick','Valensi','1988-08-12','La Reina','Vitacura'),
(19777564,'Jack','White','1988-09-11','Las Condes','Las Condes'),
(16822561,'Tuco','Salamanca','1970-11-14','Vitacura','La Reina'),
(9000111,'Walter','White','1971-11-10','Las Condes','Las Condes'),
(14111562,'Juanita','Ringeling','1970-02-13','Vitacura','Vitacura'),
(10999234,'Megan','Fox','1990-06-01','Vitacura','La Florida'),
(11333560,'Katy','Perry','1966-06-12','La Granja','Las Condes'),
(16333564,'Jennifer','Conelly','1976-11-12','Vitacura','Huechuraba'),
(23333564,'Sofia','Vergara','1971-10-12','Las Condes','Las Condes'),
(16222000,'Penelope','Cruz','1970-02-19','Vitacura','Providencia'),
(17555333,'Patti','Smith','1936-03-31','Las Condes','Vitacura'),
(13951012,'Madonna','Perez','1956-05-05','Las Condes','La Reina'),
(10874564,'Cristina','Aguilera','1996-04-12','La Reina','Vitacura'),
(3444555,'Britney','Spears','1980-01-29','La Florida','Las Condes'),
(6324561,'Angelina','Jolie','1960-02-21','Las Condes','Las Condes'),
(8874666,'Courteney','Cox','1966-06-12','Vitacura','Las Condes'),
(5874888,'Emily','Ratajkowsky','1980-09-12','La Florida','Vitacura'),
(14444444,'Jessica','Alba','1933-03-13','Las Condes','La Florida'),
(9888222,'Luisana','Lopilato','1971-11-14','Vitacura','Huechuraba'),
(7777777,'Lucila','Vit','1990-11-14','Vitacura','La Reina'),
(6666666,'Beyonce','Knowles','1980-03-12','Vitacura','Las Condes'),
(1112223,'Jennifer','Lopez','1971-01-11','Las Condes','Vitacura'),
(4445556,'Emilia','Clarke','1999-07-14','Las Condes','Las Condes'),
(13141516,'Blake','Lively','1971-01-13','Vitacura','Vitacura'),
(9222777,'Marilyn','Monroe','1981-09-12','La Reina','Las Condes'),
(9854965,'Tim','Duncan','1975-02-03','Vitacura','Las Condes'),
(4000564,'Amber','Heard','1981-03-12','Vitacura','La Granja');

INSERT INTO Promocion (Id_promocion, Id_gondola, descuento, fecha_inicio, fecha_fin)
VALUES 
(1,9,'15%','2015-10-01 12:00:00','2015-10-01 12:00:00'),
(2,17,'10%','2015-12-20 09:00:00','2015-12-25 17:30:00'),
(3,37,'20%','2016-03-01 08:00:00','2016-03-15 20:00:00'),
(4,46,'15%','2016-02-07 08:00:00','2016-02-15 17:30:00'),
(5,59,'30%','2016-04-15 12:00:00','2016-04-30 24:00:00'),
(6,86,'25%','2016-01-01 09:00:00','2016-01-30 21:00:00');

INSERT INTO Gondola_Producto (Id_gondola_producto, Id_gondola, Id_producto, Nivel)
VALUES
/*PARA EL PRIMER HIPERMERCADO*/
(1,1,3,1),(2,1,4,2),(3,2,5,1),(4,2,5,2),(5,3,1,1),(6,3,1,2),(7,4,2,1),(8,4,6,2),(9,5,8,1),
(10,6,12,1),(11,7,13,1),(12,7,13,2),(13,8,9,1),(14,8,9,2),(15,9,10,1),(16,9,12,2),(17,10,11,1),(18,10,14,2),
(19,11,17,1),(20,11,17,2),(21,12,19,1),(22,12,20,2),(23,13,22,1),(24,13,22,2),(25,14,24,1),(26,14,24,2),(27,15,23,1),
(28,16,30,1),(29,17,31,1),(30,17,31,2),(31,18,27,1),(32,18,27,2),(33,19,25,1),(34,19,26,2),(35,20,28,1),(36,20,29,2),
(37,21,40,1),(38,21,40,2),(39,22,35,1),(40,22,36,2),(41,23,38,1),(42,23,38,2),(43,24,34,1),(44,24,37,2),(45,25,33,1),
/*PARA EL SEGUNDO HIPERMERCADO*/
(46,26,3,1),(47,26,4,2),(48,27,5,1),(49,27,5,2),(50,28,1,1),(51,28,1,2),(52,29,2,1),(53,29,6,2),(54,30,7,1),
(55,31,12,1),(56,32,13,1),(57,32,13,2),(58,33,9,1),(59,33,9,2),(60,34,10,1),(61,34,12,2),(62,35,11,1),(63,35,14,2),
(64,36,17,1),(65,36,18,2),(66,37,19,1),(67,37,20,2),(68,38,22,1),(69,38,22,2),(70,39,24,1),(71,39,21,2),(72,40,23,1),
(73,41,30,1),(74,42,31,1),(75,42,31,2),(76,43,32,1),(77,43,32,2),(78,44,25,1),(79,44,26,2),(80,45,28,1),(81,45,29,2),
(82,46,40,1),(83,46,39,2),(84,47,36,1),(85,47,36,2),(86,48,33,1),(87,48,33,2),(88,49,34,1),(89,49,37,2),(90,50,38,1),
/*PARA EL PRIMER SUPERMERCADO*/
(91,51,4,1),(92,51,3,2),(93,52,2,1),(94,52,5,2),(95,53,1,1),(96,53,8,2),(97,54,7,1),
(98,55,15,1),(99,56,13,1),(100,56,13,2),(101,57,16,1),(102,57,16,2),(103,58,10,1),(104,58,12,2),
(105,59,17,1),(106,59,18,2),(107,60,19,1),(108,60,20,2),(109,61,22,1),(110,61,22,2),(111,62,21,1),
(112,63,30,1),(113,64,32,1),(114,64,32,2),(115,65,27,1),(116,65,27,2),(117,66,25,1),(118,66,26,2),
(119,67,39,1),(120,67,39,2),(121,68,35,1),(122,68,35,2),(123,69,37,1),(124,69,33,2),(125,70,34,1),
/*PARA EL SEGUNDO SUPERMERCADO*/
(126,71,4,1),(127,71,3,2),(128,72,2,1),(129,72,6,2),(130,73,8,1),(131,73,8,2),(132,74,1,1),
(133,75,14,1),(134,76,13,1),(135,76,13,2),(136,77,16,1),(137,77,16,2),(138,78,15,1),(139,78,15,2),
(140,79,18,1),(141,79,18,2),(142,80,19,1),(143,80,20,2),(144,81,22,1),(145,81,22,2),(146,82,17,1),
(147,83,30,1),(148,84,32,1),(149,84,28,2),(150,85,29,1),(151,85,29,2),(152,86,25,1),(153,86,26,2),
(154,87,36,1),(155,87,36,2),(156,88,35,1),(157,88,35,2),(158,89,34,1),(159,89,33,2),(160,90,37,1),
/*PARA EL PRIMER ALMACEN*/
(161,91,3,1),(162,91,3,2),(163,92,2,1),(164,92,2,2),(165,93,4,1),
(166,94,16,1),(167,95,13,1),(168,95,13,2),(169,96,15,1),(170,96,15,2),
(171,97,23,1),(172,97,23,2),(173,98,19,1),(174,98,20,2),(175,99,22,1),
(176,100,28,1),(177,101,29,1),(178,101,29,2),(179,102,31,1),(180,102,31,2),
(181,103,35,1),(182,103,35,2),(183,104,40,1),(184,104,40,2),(185,105,36,1),
/*PARA EL SEGUNDO ALMACEN*/
(186,106,4,1),(187,106,4,2),(188,107,2,1),(189,107,5,2),(190,108,8,1),
(191,109,9,1),(192,109,9,2),(193,110,10,1),(194,110,10,2),(195,111,11,1),
(196,112,22,1),(197,113,24,1),(198,113,24,2),(199,114,18,1),(200,114,18,2),
(201,115,30,1),(202,116,32,1),(203,116,32,2),(204,117,26,1),(205,117,26,2),
(206,118,35,1),(207,118,36,2),(208,119,34,1),(209,119,34,2),(210,120,40,1);

INSERT INTO Venta (rut_cliente, id_gondola_producto, rut_cajero, fecha,cantidad)
VALUES
(9874564,148,9494949,'2015-10-01 13:27:23',4),(9874564,179,5454545,'2015-01-20 17:29:30',2),(9874564,170,5454545,'2015-02-28 17:29:30',1),(9874564,130,9494949,'2015-03-06 17:29:30',5),
(6854364,40,7575757,'2015-09-01 12:12:00',4),(6854364,50,7878787,'2015-10-01 10:05:05',5),(6854364,100,8383838,'2015-11-08 12:15:55',3),(6854364,130,9494949,'2015-12-30 16:15:00',5),
(17844552,82,7878787,'2015-08-11 18:00:00',3),(17844552,112,8383838,'2015-12-12 17:24:54',5),(17844552,170,5454545,'2016-01-15 14:56:25',5),(17844552,50,7878787,'2016-02-19 12:45:00',4),
(19377864,46,7878787,'2015-10-10 15:23:12',2),(19377864,93,8383838,'2015-12-1 09:24:00',2),(19377864,127,9494949,'2016-01-18 16:32:12',3),(19377864,188,6262626,'2016-02-27 19:56:00',5),
(11370444,33,7575757,'2015-11-22 12:54:21',5),(11370444,123,8383838,'2015-12-24 19:21:00',5),(11370444,185,5454545,'2016-02-26 20:55:00',3),(11370444,164,5454545,'2016-03-11 09:25:00', 4),
(10987654,88,7878787,'2016-01-02 15:45:00',2),(10987654,120,8383838,'2016-02-03 16:45:00',3),(10987654,132,9494949,'2016-03-12 19:45:00',4),(10987654,42,7575757,'2016-04-02 15:45:00',5),
(21191817,93,8383838,'2015-11-11 16:58:58',5),(21191817,126,9494949,'2015-12-11 10:58:45',3),(21191817,89,7878787,'2016-01-15 16:50:58',2),(21191817,187,6262626,'2016-03-03 14:08:58',4),
(4324908,33,7575757,'2015-11-22 18:21:00',3),(4324908,111,8383838,'2015-12-20 18:21:00',5),(4324908,144,9494949,'2015-12-24 18:21:00',1),(4324908,3,7575757,'2016-01-02 18:21:00',4),
(16874564,22,7575757,'2015-10-23 10:54:00',1),(16874564,92,8383838,'2015-11-23 10:54:00',3),(16874564,124,8383838,'2015-12-13 09:54:00',3),(16874564,164,5454545,'2015-12-23 10:54:00',2),
(11954111,36,7575757,'2015-11-3 20:00:00',2),(11954111,136,9494949,'2015-12-3 19:00:00',1),(11954111,146,9494949,'2015-12-23 18:00:00',3),(11954111,209,6262626,'2016-01-3 13:00:00',2),
(10101010,38,7575757,'2015-08-12 15:22:00',3),(10101010,96,8383838,'2015-08-12 12:22:00',2),(10101010,127,9494949,'2015-09-12 13:23:00',5),(10101010,138,9494949,'2015-12-12 15:22:00',5),
(14971064,42,7575757,'2015-11-23 18:45:15',5),(14971064,142,9494949,'2015-12-23 12:45:15',4),(14971064,160,9494949,'2015-12-30 18:30:15',3),(14971064,189,6262626,'2016-01-12 18:45:30',2),
(11871514,75,7878787,'2015-12-01 19:45:00',3),(11871514,127,9494949,'2016-01-01 10:45:00',5),(11871514,180,5454545,'2016-02-01 12:45:00',3),(11871514,210,6262626,'2015-04-01 19:45:00',4),
(14176664,85,7878787,'2016-01-01 10:00:00',5),(14176664,99,8383838,'2016-02-01 11:00:00',4),(14176664,185,5454545,'2016-03-01 12:00:00',2),(14176664,199,6262626,'2016-04-11 18:00:02',3),
(17555321,89,7878787,'2016-01-22 16:45:47',3),(17555321,2,7575757,'2016-02-22 15:45:47',1),(17555321,5,7575757,'2016-03-22 16:55:48',2),(17555321,15,7575757,'2016-04-22 15:32:47',4),
(11222333,90,7878787,'2015-10-10 10:21:00',5),(11222333,164,5454545,'2015-11-10 10:28:00',4),(11222333,178,5454545,'2015-12-25 11:11:00',4),(11222333,89,7878787,'2016-02-10 13:21:00',3),
(3833534,69,7878787,'2015-11-11 10:54:32',5),(3833534,111,8383838,'2015-11-21 18:54:32',4),(3833534,158,5454545,'2016-01-11 13:54:36',2),(3833534,193,6262626,'2016-02-02 19:54:32',1),
(3444111,43,7575757,'2015-12-12 19:32:00',5),(3444111,92,8383838,'2015-12-24 09:32:00',3),(3444111,168,5454545,'2016-01-12 11:22:00',5),(3444111,167,5454545,'206-04-04 11:32:32',4),
(16111564,55,7878787,'2015-11-03 13:25:00',4),(16111564,99,8383838,'2015-12-13 14:25:00',5),(16111564,121,8383838,'2016-01-03 11:15:00',1),(16111564,188,6262626,'2016-03-11 18:55:00',5),
(10871568,2,7575757,'2016-02-26 18:56:23',1),(10871568,100,8383838,'2016-04-11 12:53:34',4),(10871568,120,8383838,'2016-01-14 11:15:48',4),(10871568,42,7575757,'2015-12-24 16:12:04',5),
(9999564,200,6262626,'2015-11-30 19:41:23',3),(9999564,92,8383838,'2015-09-18 19:21:14',1),(9999564,208,6262626,'2016-02-11 18:32:29',3),(9999564,201,6262626,'2015-12-08 13:26:23',3),
(7777564,17,7575757,'2016-01-31 16:33:57',2),(7777564,38,7575757,'2016-04-02 10:11:27',2),(7777564,191,6262626,'2015-09-30 16:33:57',4),(7777564,199,6262626,'2016-03-29 12:49:13',2),
(2224524,111,8383838,'2015-08-12 09:49:51',2),(2224524,205,6262626,'2016-02-06 11:22:07',5),(2224524,101,8383838,'2016-01-29 19:19:19',4),(2224524,188,6262626,'2015-10-17 16:23:51',5),
(4874999,78,7878787,'2015-12-12 18:26:31',5),(4874999,62,7878787,'2016-04-09 08:51:12',5),(4874999,150,9494949,'2015-10-12 18:49:18',5),(4874999,160,9494949,'2015-08-03 19:03:51',5),
(19777564,203,6262626,'2015-08-21 17:32:30',4),(19777564,142,9494949,'2016-03-31 10:34:38',3),(19777564,160,9494949,'2016-03-29 14:43:38',1),(19777564,209,6262626,'2015-09-30 12:22:39',3),
(16822561,173,5454545,'2016-01-12 19:53:21',5),(16822561,153,9494949,'2016-01-18 13:33:33',3),(16822561,184,5454545,'2016-01-02 11:11:11',1),(16822561,151,9494949,'2016-04-09 15:53:21',4),
(9000111,12,7575757,'2016-04-15 18:52:32',2),(9000111,143,9494949,'2015-11-29 12:41:37',4),(9000111,43,7575757,'2016-02-09 09:33:10',4),(9000111,133,9494949,'2016-01-24 13:59:59',3),
(14111562,72,7878787,'2015-11-03 08:33:48',5),(14111562,207,6262626,'2015-08-03 18:21:11',2),(14111562,200,6262626,'2015-08-01 09:29:12',5),(14111562,90,7878787,'2016-04-28 10:41:48',2),
(10999234,81,7878787,'2015-10-04 14:14:41',4),(10999234,86,7878787,'2016-02-16 13:52:25',2),(10999234,170,5454545,'2016-01-10 19:11:49',1),(10999234,182,5454545,'2016-03-07 15:15:51',1),
(11333560,199,6262626,'2015-12-21 19:12:36',3),(11333560,210,6262626,'2016-02-05 18:33:51',1),(11333560,129,9494949,'2016-04-26 19:04:20',5),(11333560,139,9494949,'2015-12-14 15:15:15',5),
(16333564,88,7878787,'2016-04-29 12:19:44',4),(16333564,53,7878787,'2016-03-31 13:22:48',3),(16333564,142,9494949,'2015-12-17 15:52:43',3),(16333564,127,9494949,'2016-03-22 13:44:58',2),
(23333564,93,8383838,'2016-02-25 19:04:38',5),(23333564,97,8383838,'2016-03-19 21:04:38',2),(23333564,208,6262626,'2015-10-25 19:22:54',2),(23333564,200,6262626,'2016-02-17 19:46:23',4),
(16222000,69,7878787,'2016-01-30 18:06:41',4),(16222000,55,7878787,'2016-04-19 08:12:31',5),(16222000,147,9494949,'2015-08-27 14:57:23',3),(16222000,156,9494949,'2016-03-21 13:15:54',3),
(17555333,132,9494949,'2015-09-30 08:53:30',2),(17555333,156,9494949,'2016-03-09 09:11:37',4),(17555333,163,5454545,'2015-11-29 14:52:12',4),(17555333,182,5454545,'2015-04-10 15:52:20',5),
(13951012,71,7878787,'2015-12-02 11:42:46',4),(13951012,86,7878787,'2016-03-10 12:10:32',5),(13951012,201,6262626,'2016-03-08 16:55:42',3),(13951012,208,6262626,'2015-08-04 10:10:10',3),
(10874564,129,9494949,'2015-11-26 14:13:12',1),(10874564,143,9494949,'2016-04-23 15:53:14',4),(10874564,163,5454545,'2015-11-21 17:14:13',5),(10874564,177,5454545,'2015-09-16 17:05:53',3),
(3444555,183,5454545,'2015-09-12 09:14:30',4),(3444555,180,5454545,'2016-04-19 19:44:25',3),(3444555,82,7878787,'2015-08-18 08:06:11',5),(3444555,89,7878787,'2016-02-18 11:25:53',5),
(6324561,13,7575757,'2015-12-06 17:29:21',4),(6324561,41,7575757,'2016-02-17 13:33:23',2),(6324561,136,9494949,'2015-12-01 18:23:10',3),(6324561,147,9494949,'2016-01-14 12:36:03',5),
(8874666,126,9494949,'2016-04-09 10:59:32',4),(8874666,160,9494949,'2016-03-11 17:09:28',3),(8874666,166,5454545,'2015-09-27 18:42:11',2),(8874666,180,5454545,'2016-02-19 11:03:44',5),
(5874888,77,7878787,'2015-08-13 13:44:06',4),(5874888,90,7878787,'2015-10-13 15:12:06',5),(5874888,135,9494949,'2015-10-12 16:45:02',3),(5874888,139,9494949,'2015-12-26 14:07:22',5),
(14444444,157,9494949,'2015-11-21 12:03:00',4),(14444444,137,9494949,'2015-12-23 15:20:03',3),(14444444,183,5454545,'2015-09-12 16:52:10',2),(14444444,170,5454545,'2016-04-11 09:22:01',5),
(9888222,88,7878787,'2015-09-20 11:32:47',5),(9888222,57,7878787,'2015-11-05 12:03:42',4),(9888222,100,8383838,'2016-04-11 12:47:47',3),(9888222,110,8383838,'2016-02-09 10:12:59',1),
(7777777,144,9494949,'2015-08-06 18:03:35',3),(7777777,128,9494949,'2016-04-28 18:08:12',4),(7777777,161,5454545,'2015-11-02 14:32:07',5),(7777777,183,5454545,'2015-09-16 19:32:18',4),
(6666666,182,5454545,'2015-10-26 18:21:43',1),(6666666,181,5454545,'2015-12-12 12:09:03',3),(6666666,1,7575757,'2016-01-12 17:39:20',2),(6666666,9,7575757,'2015-11-02 14:42:20',3),
(1112223,203,6262626,'2015-08-30 09:03:59',3),(1112223,193,6262626,'2016-04-08 19:34:59',1),(1112223,108,8383838,'2016-03-22 19:26:54',4),(1112223,112,8383838,'2015-12-04 13:36:32',1),
(4445556,66,7878787,'2015-11-04 14:39:31',4),(4445556,90,7878787,'2015-12-04 13:12:27',5),(4445556,201,6262626,'2015-08-27 13:39:33',1),(4445556,194,6262626,'2016-02-27 09:24:35',3),
(13141516,130,9494949,'2016-03-24 17:42:31',4),(13141516,140,9494949,'2016-04-12 13:05:28',5),(13141516,70,7878787,'2015-09-27 12:32:12',2),(13141516,80,7878787,'2016-03-18 09:41:56',5),
(9222777,170,5454545,'2016-01-31 17:51:14',4),(9222777,183,5454545,'2016-04-26 12:51:12',1),(9222777,98,8383838,'2016-02-09 17:51:43',4),(9222777,99,8383838,'2016-02-10 17:32:00',4),
(9854965,77,7878787,'2016-01-19 09:11:42',2),(9854965,89,7878787,'2015-11-12 17:56:12',4),(9854965,101,8383838,'2016-04-05 19:11:46',3),(9854965,114,8383838,'2015-11-12 19:22:44',1),
(4000564,23,7575757,'2015-09-02 17:53:30',3),(4000564,43,7575757,'2016-03-22 18:23:35',1),(4000564,210,6262626,'2015-08-17 19:13:34',4),(4000564,197,6262626,'2015-12-13 08:13:45',2);

/*CAMBIO DE PRODUCTOS EN GONDOLAS NORMALES*/
UPDATE Gondola_Producto SET id_producto = 40
WHERE id_gondola_producto=83;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(46,46,1,2,40,'2015-09-20 10:30:00');

UPDATE Gondola_Producto SET id_producto = 39
WHERE id_gondola_producto=82;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(46,46,2,1,39,'2015-09-20 10:35:00');

UPDATE Gondola_Producto SET id_producto =32
WHERE id_gondola_producto=149;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(64,64,1,2,32,'2015-10-15 12:00:00');

UPDATE Gondola_Producto SET id_producto =28
WHERE id_gondola_producto=148;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(64,64,2,1,28,'2015-10-15 12:05:00');

UPDATE Gondola_Producto SET id_producto = 32
WHERE id_gondola_producto=204;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(116,117,1,1,32,'2016-02-01 09:30:00');

UPDATE Gondola_Producto SET id_producto = 26
WHERE id_gondola_producto=202;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(117,116,1,1,26,'2016-02-01 09:35:00');

UPDATE Gondola_Producto SET id_producto = 19
WHERE id_gondola_producto=22;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(12,12,1,2,19,'2016-03-15 13:30:00');

UPDATE Gondola_Producto SET id_producto = 20
WHERE id_gondola_producto=21;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(12,12,2,1,20,'2016-03-15 13:35:00');

UPDATE Gondola_Producto SET id_producto = 10
WHERE id_gondola_producto=63;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(34,35,1,2,10,'2016-04-16 09:55:00');

UPDATE Gondola_Producto SET id_producto = 14
WHERE id_gondola_producto=60;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(35,34,2,1,14,'2016-04-16 10:00:00');

/*CAMBIO GONDOLA PREFERENCIAL*/
UPDATE Gondola_Producto SET id_producto = 31
WHERE id_gondola_producto= 27;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(17,15,1,1,27,'2015-09-30 09:00:00');

UPDATE Gondola_Producto SET id_producto = 36
WHERE id_gondola_producto= 54;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(47,30,2,1,36,'2015-10-28 20:00:00');

UPDATE Gondola_Producto SET id_producto = 13
WHERE id_gondola_producto= 111;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(56,62,1,1,13,'2015-11-28 12:00:00');

UPDATE Gondola_Producto SET id_producto = 29
WHERE id_gondola_producto= 133;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(65,55,2,1,29,'2015-12-15 09:00:00');

UPDATE Gondola_Producto SET id_producto = 9
WHERE id_gondola_producto= 190;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(109,108,1,1,9,'2016-01-01 20:00:00');

UPDATE Gondola_Producto SET id_producto = 2
WHERE id_gondola_producto= 201;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(107,115,1,1,2,'2016-02-15 12:00:00');

UPDATE Gondola_Producto SET id_producto = 32 
WHERE id_gondola_producto= 28;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(20,16,1,1,32,'2016-03-20 09:00:00');

UPDATE Gondola_Producto SET id_producto = 6
WHERE id_gondola_producto= 73;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(29,41,2,1,6,'2016-04-01 12:00:00');

UPDATE Gondola_Producto SET id_producto = 15 
WHERE id_gondola_producto= 160;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(58,70,1,1,15,'2015-11-15 20:00:00');

UPDATE Gondola_Producto SET id_producto =  16
WHERE id_gondola_producto= 112;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(57,63,1,1,16,'2015-12-01 12:00:00');

UPDATE Gondola_Producto SET id_producto =  18
WHERE id_gondola_producto= 210;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(114,120,1,1,18,'2015-12-15 09:00:00');

UPDATE Gondola_Producto SET id_producto = 5  
WHERE id_gondola_producto= 196;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(107,112,2,1,5,'2015-12-25 09:30:00');

UPDATE Gondola_Producto SET id_producto = 36  
WHERE id_gondola_producto= 195;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(118,111,2,1,36,'2016-01-01 20:00:00');

UPDATE Gondola_Producto SET id_producto = 19 
WHERE id_gondola_producto= 166;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(98,94,1,1,19,'2015-11-01 12:00:00');

UPDATE Gondola_Producto SET id_producto = 34 
WHERE id_gondola_producto= 147;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(69,63,1,1,34,'2015-10-01 09:00:00');

UPDATE Gondola_Producto SET id_producto = 2 
WHERE id_gondola_producto= 98;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(52,55,1,1,2,'2016-03-15 12:00:00');

UPDATE Gondola_Producto SET id_producto = 37 
WHERE id_gondola_producto= 55;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(49,31,2,1,37,'2015-09-01 09:00:00');

UPDATE Gondola_Producto SET id_producto = 39 
WHERE id_gondola_producto= 72;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(46,40,2,1,39,'2016-02-15 19:00:00');

UPDATE Gondola_Producto SET id_producto = 3 
WHERE id_gondola_producto= 90;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(26,50,1,1,3,'2015-12-20 12:00:00');

UPDATE Gondola_Producto SET id_producto = 25 
WHERE id_gondola_producto= 45;

INSERT INTO Movimiento (Id_gondola_original, Id_gondola_destino, Nivel_original, Nivel_destino, Id_producto, Fecha)
VALUES
(19,25,1,1,25,'2015-08-15 09:00:00');


