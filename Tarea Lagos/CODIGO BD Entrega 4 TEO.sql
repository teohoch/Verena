DROP TABLE IF EXISTS Local
CASCADE;
DROP TABLE IF EXISTS Pasillo
CASCADE;
DROP TABLE IF EXISTS Gondola
CASCADE;
DROP TABLE IF EXISTS Categoria
CASCADE;

DROP TABLE IF EXISTS Producto
CASCADE;
DROP TABLE IF EXISTS Cliente
CASCADE;
DROP TABLE IF EXISTS Venta
CASCADE;
DROP TABLE IF EXISTS Gondola_Producto
CASCADE;
DROP TABLE IF EXISTS Venta_Producto
CASCADE;


CREATE TABLE Local (
  Id SERIAL PRIMARY KEY,
  Clasificacion VARCHAR(255),
  Direccion VARCHAR (255),
  Comuna VARCHAR (255)
);

CREATE TABLE Pasillo (
  Id SERIAL PRIMARY KEY,
  Id_categoria INTEGER,
  Id_local  INTEGER,
  Numero INTEGER
);

CREATE TABLE Gondola (
  Id SERIAL PRIMARY KEY,
  Id_pasillo INTEGER,
  Preferencial BOOLEAN,
  Activa BOOLEAN,
  Largo INTEGER,
  Niveles INTEGER
);

CREATE TABLE Categoria (
  Id SERIAL PRIMARY KEY,
  Nombre VARCHAR(255)
);


CREATE TABLE Producto (
  Id SERIAL PRIMARY KEY,
  Id_categoria INTEGER,
  Nombre VARCHAR(255),
  Marca VARCHAR(255),
  Precio INTEGER
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
  Id SERIAL PRIMARY KEY,
  Rut_cliente INTEGER,
  Fecha TIMESTAMP,
  Cantidad INTEGER,
  Precio_total INTEGER
);

CREATE TABLE Venta_Producto (
  Id SERIAL PRIMARY KEY,
  id_venta INTEGER,
  id_producto INTEGER,
  precio_unidad INTEGER,
  cantidad INTEGER
);

CREATE TABLE Gondola_Producto (
  Id SERIAL PRIMARY KEY,
  Id_gondola INTEGER,
  Id_producto INTEGER,
  Nivel INTEGER,
  Posicion_x INTEGER
);




ALTER TABLE Pasillo
ADD CONSTRAINT Id_categoria_fk 
FOREIGN KEY (Id_categoria) 
REFERENCES Categoria (Id)
ON DELETE CASCADE;

ALTER TABLE Pasillo
ADD CONSTRAINT Id_local_fk 
FOREIGN KEY (Id_local) 
REFERENCES Local (Id)
ON DELETE CASCADE;

ALTER TABLE Producto 
ADD CONSTRAINT Id_categoria_fk 
FOREIGN KEY (Id_categoria) 
REFERENCES Categoria (Id)
ON DELETE CASCADE;

ALTER TABLE Venta
ADD CONSTRAINT Rut_cliente_fk 
FOREIGN KEY (Rut_cliente) 
REFERENCES Cliente (Rut_cliente)
ON DELETE CASCADE;


ALTER TABLE Gondola_Producto
ADD CONSTRAINT Id_gondola_fk 
FOREIGN KEY (Id_gondola) 
REFERENCES Gondola (Id)
ON DELETE CASCADE;  

ALTER TABLE Gondola_Producto
ADD CONSTRAINT Id_producto_fk 
FOREIGN KEY (Id_producto) 
REFERENCES Producto (Id)
ON DELETE CASCADE;  

ALTER TABLE Gondola
  ADD CONSTRAINT Id_pasillo_fk
  FOREIGN KEY (Id_pasillo)
  REFERENCES Pasillo (Id)
  ON DELETE CASCADE;

ALTER TABLE Venta_Producto
  ADD CONSTRAINT id_producto_fk
  FOREIGN KEY (id_producto)
  REFERENCES Producto (Id)
  ON DELETE CASCADE;

ALTER TABLE Venta_Producto
  ADD CONSTRAINT id_venta_fk
  FOREIGN KEY (id_venta)
  REFERENCES Venta (Id)
  ON DELETE CASCADE;





