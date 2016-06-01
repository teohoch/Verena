DROP TABLE IF EXISTS Venta
CASCADE;
DROP TABLE IF EXISTS Venta_Producto
CASCADE;



CREATE TABLE Venta (
  Id SERIAL PRIMARY KEY,
  Rut_cliente INTEGER,
  id_local INTEGER,
  Fecha TIMESTAMP,
  Cantidad INTEGER,
  Rut_cajero INTEGER
);

CREATE TABLE Venta_Producto (
  Id SERIAL PRIMARY KEY,
  id_venta INTEGER,
  id_producto INTEGER,
  cantidad INTEGER
);

ALTER TABLE Venta
  ADD CONSTRAINT id_cajero_fk
  FOREIGN KEY (Rut_cajero)
  REFERENCES cajero(rut_cajero)
  ON DELETE RESTRICT ;

ALTER TABLE Venta
  ADD CONSTRAINT id_local_fk
  FOREIGN KEY (id_local)
  REFERENCES local (id_local)
  ON DELETE RESTRICT ;

ALTER TABLE Venta
  ADD CONSTRAINT id_cliente_fk
  FOREIGN KEY (Rut_cliente)
  REFERENCES cliente (rut_cliente)
  ON DELETE RESTRICT ;

ALTER TABLE Venta_Producto
  ADD CONSTRAINT id_producto_fk
  FOREIGN KEY (id_producto)
  REFERENCES producto(id_producto)
  ON DELETE CASCADE;

ALTER TABLE Venta_Producto
  ADD CONSTRAINT id_venta_fk
  FOREIGN KEY (id_venta)
  REFERENCES Venta (Id)
  ON DELETE CASCADE;
