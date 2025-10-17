-- setup_gestion_pacientes.sql

-- Crear BD
CREATE DATABASE IF NOT EXISTS gestion_pacientes_simple
  DEFAULT CHARACTER SET utf8mb4;
USE gestion_pacientes_simple;

-- Tabla: pacientes
CREATE TABLE IF NOT EXISTS pacientes (
  id_paciente INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  telefono VARCHAR(15),
  email VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: doctores
CREATE TABLE IF NOT EXISTS doctores (
  id_doctor INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  especialidad VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla: citas (sin CHECK para compatibilidad 5.7)
CREATE TABLE IF NOT EXISTS citas (
  id_cita INT AUTO_INCREMENT PRIMARY KEY,
  id_paciente INT,
  id_doctor INT,
  fecha_cita DATETIME NOT NULL,
  motivo TEXT,
  estado VARCHAR(20) NOT NULL,
  CONSTRAINT fk_cita_paciente
    FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT fk_cita_doctor
    FOREIGN KEY (id_doctor) REFERENCES doctores(id_doctor)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insertar 2 pacientes
INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, telefono, email) VALUES
('Ana', 'Paredes', '1995-06-10', '099111222', 'ana.paredes@example.com'),
('Luis', 'Mora', '1988-12-22', '098333444', 'luis.mora@example.com');

-- Insertar 2 doctores
INSERT INTO doctores (nombre, apellido, especialidad) VALUES
('Carla', 'Vega', 'Pediatría'),
('Marco', 'Salas', 'Cardiología');

-- Insertar 2 citas (usando los IDs 1 y 2 creados arriba)
INSERT INTO citas (id_paciente, id_doctor, fecha_cita, motivo, estado) VALUES
(1, 1, '2025-10-01 09:30:00', 'Control pediátrico', 'Programada'),
(2, 2, '2025-10-02 14:00:00', 'Chequeo cardiaco', 'Programada');
