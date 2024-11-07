--
-- Estructura de tabla para la tabla `course`
--

CREATE TABLE IF NOT EXISTS `course` (
  `course_id` int NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `course`
--

INSERT INTO `course` (`course_id`, `title`, `department`) VALUES
(1, 'Databases', 'Computer Science'),
(2, 'Calculus', 'Mathematics'),
(3, 'Mechanics', 'Physics');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enrollments`
--

CREATE TABLE IF NOT EXISTS `enrollments` (
  `student_id` int NOT NULL,
  `course_id` int NOT NULL,
  `grade` char(2) DEFAULT NULL,
  PRIMARY KEY (`student_id`,`course_id`),
  KEY `course_id` (`course_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `enrollments`
--

INSERT INTO `enrollments` (`student_id`, `course_id`, `grade`) VALUES
(1, 1, 'A'),
(2, 2, 'B'),
(3, 3, 'A'),
(1, 2, 'B');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instructor`
--

CREATE TABLE IF NOT EXISTS `instructor` (
  `instructor_id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `major` varchar(50) DEFAULT NULL,
  `department_id` int NOT NULL,
  `salary` decimal(8,2) NOT NULL,
  PRIMARY KEY (`instructor_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `instructor`
--

INSERT INTO `instructor` (`instructor_id`, `name`, `major`, `department_id`, `salary`) VALUES
(1, 'Peter', 'Computer Science', 2, '7000.00'),
(2, 'Jhon', 'History', 1, '8000.00'),
(3, 'Solange', 'Ancient Art', 3, '400.00'),
(4, 'Alan Turing', 'Mathematics', 4, '2889.00'),
(5, 'Alan Turing', 'Computer Science', 2, '7000.00'),
(6, 'Peter', 'Physics', 5, '2999.00'),
(7, 'Jhon', 'Mathematics', 4, '8000.00'),
(8, 'Charlie', 'null', 4, '2999.00');
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `student_id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `major` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `student`
--

INSERT INTO `student` (`student_id`, `name`, `major`) VALUES
(1, 'Alice', 'Computer Science'),
(2, 'Bob', 'Mathematics'),
(3, 'Charlie', 'Physics'),
(4, 'Frederic von der Leyen', 'Sociology'),
(5, 'Ursula von der Leyen', 'Computer Science');
COMMIT;
