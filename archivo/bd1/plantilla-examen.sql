-- NOTE: charset disponibles
-- 
-- utf8mb4 99% del uso
-- utf8 admite menos caracteres
-- ascii solo permite caracteres basicos

-- NOTE: collate disponibles
-- 
-- utf8mb4_unicode_ci 99% del uso
-- utf8_spanish2_ci espanol
CREATE TABLE IF NOT EXISTS `` (
  `` varchar(10) CHARACTER SET ascii COLLATE ascii_general_ci NOT NULL,
  `` varchar(15) CHARACTER SET ascii COLLATE ascii_general_ci DEFAULT NULL,
  `` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (``),
) ENGINE=InnoDB DEFAULT CHARSET=ascii COLLATE=ascii_general_ci;

-- NOTE: otro formato de create table
-- CREATE TABLE IF NOT EXISTS `` (
-- `` INT AUTO_INCREMENT PRIMARY KEY,
-- `` VARCHAR(100) NOT NULL,
-- `` VARCHAR(255),
-- `` VARCHAR(20)
-- ) ENGINE=InnoDB DEFALUT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT INTO `` (``, ``, ``) VALUES
('', '', ''),

-- NOTE: para crear el trigger cambiar el nombre
DELIMITER //
CREATE TRIGGER nombre BEFORE INSERT ON sedes FOR EACH ROW
BEGIN
DECLARE msg VARCHAR(255);
IF (NEW.nombre_departamento!='Ingles') THEN SET msg = 'La asignatura impartida es ingles';
SIGNAL SQLSTATE '45000' SET message_text = msg;
END IF;
END;
//
DELIMITER ;

-- NOTE: INTERSECCION
--
-- SELECT * FROM instructor WHERE dept_name = 'Music'
-- INTERSECT
-- SELECT * FROM instructor WHERE salary > 12000;

-- NOTE: UNION
--
-- SELECT ID, Nombre, Departamento, Salario
-- FROM empleados
-- WHERE Departamento = 'Ventas'
-- 
-- UNION
-- 
-- SELECT ID, Nombre, Departamento, Salario
-- FROM empleados
-- WHERE Salario > 6000;

-- NOTE: DIFERENCIA
-- 
-- SELECT course_id
-- FROM section
-- WHERE semester= 'Fall' and year = 2017
-- EXCEPT 
-- SELECT course_id
-- FROM section 
-- WHERE semester= 'Spring' and year = 2018;


-- NOTE: AGREGACION
-- 
-- SELECT SUM(salary) FROM instructor;
--
-- EJEMPLO 2
--
-- SELECT id_sede, COUNT(*) AS cantidad_sedes
-- FROM sedes
-- GROUP BY id_sede;

-- NOTE: REUNION NATURAL
-- 
-- SELECT *
-- FROM empleados
-- NATURAL JOIN departamentos;

-- NOTE: INFO AUSENTE POR LA IZQUIERDA
-- 
-- SELECT empleados.ID, empleados.Nombre, empleados.DepartamentoID
-- FROM empleados
-- LEFT JOIN departamentos
-- ON empleados.DepartamentoID = departamentos.DepartamentoID

-- NOTE: INFO AUSENTE POR LA DERECHA
-- 
-- SELECT empleados.ID, empleados.Nombre, empleados.DepartamentoID
-- FROM empleados
-- RIGHT JOIN departamentos
-- ON empleados.DepartamentoID = departamentos.DepartamentoID

-- NOTE: PRODUCTO CARTESIANO
--
-- SELECT * FROM empleados CROSS JOIN departamentos;
