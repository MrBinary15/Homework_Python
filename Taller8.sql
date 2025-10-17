--! =========================Taller n° 7 ====================================
-- * Nombre: Arturo Parra
--? Fecha: 20/09/2025
-- Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
-- Empresa: Codins Academy

--===== Ejercicio 1: Crear la base de datos====
CREATE DATABASE biblioteca_simple;
USE biblioteca_simple;

--===== Ejercicio 2: Crear tabla libros======
"""id (entero, clave primaria, autoincremental)
titulo (texto, máximo 100 caracteres, no nulo)
autor (texto, máximo 100 caracteres, no nulo)
anio_publicacion (entero)
disponible (booleano, valor por defecto: verdadero)"""
CREATE TABLE libros (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    anio_publicacion INT,
    disponible BOOLEAN DEFAULT TRUE
);
--=====Ejercicio 3: Crear la tabla socios con los campos:=========
"""id (entero, clave primaria, autoincremental)
nombre (texto, máximo 50 caracteres, no nulo)
apellido (texto, máximo 50 caracteres, no nulo)
email (texto, máximo 100 caracteres, único)
fecha_registro (fecha, valor por defecto: fecha actual)"""
CREATE TABLE socios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(50) not NULL,
    apellido varchar(50) not NULL,
    email VARCHAR(100) UNIQUE,
    fecha_registro DATE DEFAULT(CURRENT_TIME)
);
--====Ejercicio 4: Crear la tabla prestamos con los campos:========
""" Crear la tabla prestamos con los campos:
id (entero, clave primaria, autoincremental)
libro_id (entero, clave foránea referencia libros.id)
socio_id (entero, clave foránea referencia socios.id)
fecha_prestamo (fecha, no nulo)"""
CREATE TABLE prestamos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    libro_id INT,
    socio_id INT,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE NULL,
    FOREIGN KEY (libro_id) REFERENCES libros(id),
    FOREIGN KEY (socio_id) REFERENCES socios(id)
);

--===========Ejercicio 5: Insertar 5 libros============
INSERT INTO libros (titulo, autor, anio_publicacion, disponible) VALUES
('Cien años de soledad', 'Gabriel García Márquez', 1967, TRUE),
('1984', 'George Orwell', 1949, TRUE),
('El principito', 'Antoine de Saint-Exupéry', 1943, TRUE),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605, TRUE),
('Harry Potter y la piedra filosofal', 'J.K. Rowling', 1997, TRUE);

--===========Ejercicio 6: Insertar 3 socios========
INSERT INTO socios (nombre, apellido, email) VALUES
('María', 'González', 'maria@email.com'),
('Carlos', 'Rodríguez', 'carlos@email.com'),
('Ana', 'Fernández', 'ana@email.com');

--=============Ejercicio 7: Registrar 2 préstamos==========
INSERT INTO prestamos (libro_id, socio_id, fecha_prestamo, fecha_devolucion) VALUES
(2, 1, '2024-01-15', NULL),  -- María tiene prestado "Cien años de soledad"
(3, 2, '2024-01-18', NULL);  -- Carlos tiene prestado "El principito"

--==============Ejercicio 8: Actualizar el estado de disponibilidad a falso para los libros prestados=========
UPDATE libros set disponible = FAlSE WHERE id IN(2,3); 
--======Ejercicio 9: Registrar la devolución de uno de los libros prestados============
UPDATE prestamos SET fecha_devolucion = '2024-01-25' WHERE id =2 ;
update libros set disponible = TRUE  WHERE id = 3;
--===========Ejercicio 10: Mostrar todos los libros disponibles==========
SELECT * FROM libros WHERE disponible=TRUE;
--==========Ejercicio 11: Mostrar todos los libros actualmente prestados===========
SELECT * FROM libros WHERE disponible = FALSE;
--==========Ejercicio 12: Mostrar los socios que tienen libros prestados==========
SELECT socios.nombre, socios.apellido from socios
JOIN prestamos on socios.id = prestamos.socio_id
WHERE prestamos.fecha_devolucion is NULL;
--=========Ejercicio 13: Mostrar el libro más reciente de la biblioteca===========
SELECT titulo, autor, anio_publicacion
from libros
ORDER BY anio_publicacion DESC
LIMIT 1;
--Ejercicio 14: Mostrar cuántos libros tiene prestados cada socio
SELECT CONCAT(socios.nombre,' ' ,socios.apellido) as Socio, COUNT(prestamos.id) as libros_prestados
from socios
join prestamos on socios.id = prestamos.socio_id and prestamos.fecha_devolucion is NULL
GROUP BY socio_id


UPDATE libros 
SET disponible = FALSE 
WHERE id IN (SELECT libro_id FROM prestamos WHERE fecha_devolucion IS NULL);
"""

