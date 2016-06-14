DROP TABLE IF EXISTS bloque_horario;
DROP TABLE IF EXISTS rating;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER AUTO_INCREMENT,
  username VARCHAR(30),
  name VARCHAR(30),
  password VARCHAR(30),
  isTeacher BOOLEAN,
  PRIMARY KEY (id));

CREATE TABLE bloque_horario (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  dia INTEGER NOT NULL,
  bloque INTEGER NOT NULL,
  disponible BOOLEAN DEFAULT FALSE,
  userIDTeacher INTEGER,
  userIDStudent INTEGER,
  FOREIGN KEY (userIDTeacher) REFERENCES users(id) ON DELETE CASCADE ,
  FOREIGN KEY (userIDStudent) REFERENCES users(id) ON DELETE CASCADE
);
CREATE TABLE rating (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  userIDTeacher INTEGER,
  userIDStudent INTEGER,
  FOREIGN KEY (userIDTeacher) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (userIDStudent) REFERENCES users(id) ON DELETE CASCADE,
  value INTEGER
);

INSERT INTO users (username, name, password, isTeacher) VALUES ("test","tester testing","testing",FALSE );
INSERT INTO users (username, name, password, isTeacher) VALUES ("bmorales","Sra. Brenda Morales R.","teacher",TRUE ) ;
INSERT INTO users (username, name, password, isTeacher) VALUES ("cramirez","Sr. Claudio Ramírez","teacher",TRUE ) ;
INSERT INTO users (username, name, password, isTeacher) VALUES ("aruiz","Andrea Ruiz O.","teacher",TRUE ) ;
INSERT INTO users (username, name, password, isTeacher) VALUES ("prueba","tester testing","testing",FALSE );
INSERT INTO users (username, name, password, isTeacher) VALUES ("tester","tester testing","testing",FALSE );

INSERT INTO bloque_horario (dia, bloque, disponible, userIDTeacher) VALUES
  (1,1,TRUE ,2),  (1,2,TRUE ,2),  (1,3,TRUE ,2),  (1,4,TRUE ,2),  (1,5,TRUE ,2),  (1,6,TRUE ,2),  (1,7,TRUE ,2),  (1,8,TRUE ,2),  (1,9,TRUE ,2),  (1,10,TRUE ,2),  (1,11,TRUE ,2),  (1,12,TRUE ,2),
  (2,1,TRUE ,2),  (2,2,TRUE ,2),  (2,3,TRUE ,2),  (2,4,TRUE ,2),  (2,5,TRUE ,2),  (2,6,TRUE ,2),  (2,7,TRUE ,2),  (2,8,TRUE ,2),  (2,9,TRUE ,2),  (2,10,TRUE ,2),  (2,11,TRUE ,2),  (2,12,TRUE ,2),
  (3,1,TRUE ,2),  (3,2,TRUE ,2),  (3,3,TRUE ,2),  (3,4,TRUE ,2),  (3,5,TRUE ,2),  (3,6,TRUE ,2),  (3,7,TRUE ,2),  (3,8,TRUE ,2),  (3,9,TRUE ,2),  (3,10,TRUE ,2),  (3,11,TRUE ,2),  (3,12,TRUE ,2),
  (4,1,TRUE ,2),  (4,2,TRUE ,2),  (4,3,TRUE ,2),  (4,4,TRUE ,2),  (4,5,TRUE ,2),  (4,6,TRUE ,2),  (4,7,TRUE ,2),  (4,8,TRUE ,2),  (4,9,TRUE ,2),  (4,10,TRUE ,2),  (4,11,TRUE ,2),  (4,12,TRUE ,2),
  (5,1,TRUE ,2),  (5,2,TRUE ,2),  (5,3,TRUE ,2),  (5,4,TRUE ,2),  (5,5,TRUE ,2),  (5,6,TRUE ,2),  (5,7,TRUE ,2),  (5,8,TRUE ,2),  (5,9,TRUE ,2),  (5,10,TRUE ,2),  (5,11,TRUE ,2),  (5,12,TRUE ,2),
  (6,1,TRUE ,2),  (6,2,TRUE ,2),  (6,3,TRUE ,2),  (6,4,TRUE ,2),  (6,5,TRUE ,2),  (6,6,TRUE ,2),  (6,7,TRUE ,2),  (6,8,TRUE ,2),  (6,9,TRUE ,2),  (6,10,TRUE ,2),  (6,11,TRUE ,2),  (6,12,TRUE ,2),
  (7,1,TRUE ,2),  (7,2,TRUE ,2),  (7,3,TRUE ,2),  (7,4,TRUE ,2),  (7,5,TRUE ,2),  (7,6,TRUE ,2),  (7,7,TRUE ,2),  (7,8,TRUE ,2),  (7,9,TRUE ,2),  (7,10,TRUE ,2),  (7,11,TRUE ,2),  (7,12,TRUE ,2),

  (1,1,TRUE ,3),  (1,2,TRUE ,3),  (1,3,TRUE ,3),  (1,4,TRUE ,3),  (1,5,TRUE ,3),  (1,6,TRUE ,3),  (1,7,TRUE ,3),  (1,8,TRUE ,3),  (1,9,TRUE ,3),  (1,10,TRUE ,3),  (1,11,TRUE ,3),  (1,12,TRUE ,3),
  (2,1,TRUE ,3),  (2,2,TRUE ,3),  (2,3,TRUE ,3),  (2,4,TRUE ,3),  (2,5,TRUE ,3),  (2,6,TRUE ,3),  (2,7,TRUE ,3),  (2,8,TRUE ,3),  (2,9,TRUE ,3),  (2,10,TRUE ,3),  (2,11,TRUE ,3),  (2,12,TRUE ,3),
  (3,1,TRUE ,3),  (3,2,TRUE ,3),  (3,3,TRUE ,3),  (3,4,TRUE ,3),  (3,5,TRUE ,3),  (3,6,TRUE ,3),  (3,7,TRUE ,3),  (3,8,TRUE ,3),  (3,9,TRUE ,3),  (3,10,TRUE ,3),  (3,11,TRUE ,3),  (3,12,TRUE ,3),
  (4,1,TRUE ,3),  (4,2,TRUE ,3),  (4,3,TRUE ,3),  (4,4,TRUE ,3),  (4,5,TRUE ,3),  (4,6,TRUE ,3),  (4,7,TRUE ,3),  (4,8,TRUE ,3),  (4,9,TRUE ,3),  (4,10,TRUE ,3),  (4,11,TRUE ,3),  (4,12,TRUE ,3),
  (5,1,TRUE ,3),  (5,2,TRUE ,3),  (5,3,TRUE ,3),  (5,4,TRUE ,3),  (5,5,TRUE ,3),  (5,6,TRUE ,3),  (5,7,TRUE ,3),  (5,8,TRUE ,3),  (5,9,TRUE ,3),  (5,10,TRUE ,3),  (5,11,TRUE ,3),  (5,12,TRUE ,3),
  (6,1,TRUE ,3),  (6,2,TRUE ,3),  (6,3,TRUE ,3),  (6,4,TRUE ,3),  (6,5,TRUE ,3),  (6,6,TRUE ,3),  (6,7,TRUE ,3),  (6,8,TRUE ,3),  (6,9,TRUE ,3),  (6,10,TRUE ,3),  (6,11,TRUE ,3),  (6,12,TRUE ,3),
  (7,1,TRUE ,3),  (7,2,TRUE ,3),  (7,3,TRUE ,3),  (7,4,TRUE ,3),  (7,5,TRUE ,3),  (7,6,TRUE ,3),  (7,7,TRUE ,3),  (7,8,TRUE ,3),  (7,9,TRUE ,3),  (7,10,TRUE ,3),  (7,11,TRUE ,3),  (7,12,TRUE ,3),

  (1,1,TRUE ,4),  (1,2,TRUE ,4),  (1,3,TRUE ,4),  (1,4,TRUE ,4),  (1,5,TRUE ,4),  (1,6,TRUE ,4),  (1,7,TRUE ,4),  (1,8,TRUE ,4),  (1,9,TRUE ,4),  (1,10,TRUE ,4),  (1,11,TRUE ,4),  (1,12,TRUE ,4),
  (2,1,TRUE ,4),  (2,2,TRUE ,4),  (2,3,TRUE ,4),  (2,4,TRUE ,4),  (2,5,TRUE ,4),  (2,6,TRUE ,4),  (2,7,TRUE ,4),  (2,8,TRUE ,4),  (2,9,TRUE ,4),  (2,10,TRUE ,4),  (2,11,TRUE ,4),  (2,12,TRUE ,4),
  (3,1,TRUE ,4),  (3,2,TRUE ,4),  (3,3,TRUE ,4),  (3,4,TRUE ,4),  (3,5,TRUE ,4),  (3,6,TRUE ,4),  (3,7,TRUE ,4),  (3,8,TRUE ,4),  (3,9,TRUE ,4),  (3,10,TRUE ,4),  (3,11,TRUE ,4),  (3,12,TRUE ,4),
  (4,1,TRUE ,4),  (4,2,TRUE ,4),  (4,3,TRUE ,4),  (4,4,TRUE ,4),  (4,5,TRUE ,4),  (4,6,TRUE ,4),  (4,7,TRUE ,4),  (4,8,TRUE ,4),  (4,9,TRUE ,4),  (4,10,TRUE ,4),  (4,11,TRUE ,4),  (4,12,TRUE ,4),
  (5,1,TRUE ,4),  (5,2,TRUE ,4),  (5,3,TRUE ,4),  (5,4,TRUE ,4),  (5,5,TRUE ,4),  (5,6,TRUE ,4),  (5,7,TRUE ,4),  (5,8,TRUE ,4),  (5,9,TRUE ,4),  (5,10,TRUE ,4),  (5,11,TRUE ,4),  (5,12,TRUE ,4),
  (6,1,TRUE ,4),  (6,2,TRUE ,4),  (6,3,TRUE ,4),  (6,4,TRUE ,4),  (6,5,TRUE ,4),  (6,6,TRUE ,4),  (6,7,TRUE ,4),  (6,8,TRUE ,4),  (6,9,TRUE ,4),  (6,10,TRUE ,4),  (6,11,TRUE ,4),  (6,12,TRUE ,4),
  (7,1,TRUE ,4),  (7,2,TRUE ,4),  (7,3,TRUE ,4),  (7,4,TRUE ,4),  (7,5,TRUE ,4),  (7,6,TRUE ,4),  (7,7,TRUE ,4),  (7,8,TRUE ,4),  (7,9,TRUE ,4),  (7,10,TRUE ,4),  (7,11,TRUE ,4),  (7,12,TRUE ,4);

INSERT INTO rating (userIDTeacher, userIDStudent, value) VALUES (2,5,3),(2,6,5);