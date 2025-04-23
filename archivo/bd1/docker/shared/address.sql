-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:13306
-- Tiempo de generación: 11-12-2024 a las 10:58:45
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `disen_atributos_complejos_inicio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `address`
--

DROP TABLE IF EXISTS `address`;
CREATE TABLE IF NOT EXISTS `address` (
  `ID` varchar(5) NOT NULL DEFAULT '',
  `name` varchar(40) NOT NULL DEFAULT '',
  `dept_name` varchar(20) DEFAULT NULL,
  `salary or tot_credit` decimal(8,2) DEFAULT NULL,
  `address` varchar(255) NOT NULL DEFAULT '',
  `phones` varchar(100) NOT NULL DEFAULT '',
  `births_day` date NOT NULL DEFAULT '0000-00-00',
  `age` int NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `address`
--

INSERT INTO `address` (`ID`, `name`, `dept_name`, `salary or tot_credit`, `address`, `phones`, `births_day`, `age`) VALUES
('10101', 'Juan Srinivasan Trus', 'Comp. Sci.', '65000.00', '\"231463\",\"Ap #650-1961 Nec Rd.\",\"Ankara\",\"Ireland\"', '(173) 810-1776', '1969-05-20', 53),
('12121', 'Pedro Wu Sánchez', 'Finance', '90000.00', '\"S81 8OX\",\"Ap #111-2659 A Ave\",\"Luxemburg\",\"India\"', '1-628-312-2275', '1970-04-20', 52),
('15151', 'Amadeus Mozart  Rodríguez', 'Music', '40000.00', '\"12346\",\"Ap #996-3042 Semper, Rd.\",\"West Sulawesi\",\"Spain\"', '(178) 393-7591', '1968-12-20', 54),
('22222', 'Hanz Albert Einstein ', 'Physics', '95000.00', '\"513224\",\"255-723 Eget, St.\",\"Lambayeque\",\"Belgium\"', '(266) 257-8491', '1967-06-24', 55),
('32343', 'Muammar El Said Azar', 'History', '60000.00', '\"75785\",\"711-3338 Sem St.\",\"Brussels Hoofdstedelijk Gewest\",\"South Korea\"', '1-157-426-9642', '1968-07-02', 58),
('33456', 'Hanz Gold Silver', 'Physics', '87000.00', '\"53167\",\"P.O. Box 759, 3675 Aliquet Street\",\"Mersin\",\"China\"', '(486) 505-3751', '1968-12-06', 58),
('45565', 'Immanuel Katz Albert', 'Comp. Sci.', '75000.00', '\"44275\",\"Ap #601-6444 Sed Road\",\"Newfoundland and Labrador\",\"Australia\"', '1-224-210-3211', '1969-04-04', 53),
('58583', 'Jorge Califieri Santana', 'History', '62000.00', '\"61775-732\",\"837-1270 Mauris Road\",\"Australian Capital Territory\",\"Austria\"', '(261) 362-4687', '1970-04-20', 52),
('76543', 'Sol Singh Chun', 'Finance', '80000.00', '\"4156\",\"573-8802 Nec St.\",\"Inverness-shire\",\"Italy\"', '1-803-436-3522', '1967-11-24', 55),
('76766', 'Ben Crick Hainer', 'Biology', '72000.00', '\"65-45\",\"Ap #272-7742 Pede. Road\",\"Zhōngnán\",\"France\"', '(583) 385-8788', '1965-06-12', 57),
('83821', 'Amadeus Brandt Sol', 'Comp. Sci.', '92000.00', '\"754328\",\"Ap #825-6940 Sociis Av.\",\"Rogaland\",\"Chile\"', '(529) 205-1539', '1969-07-12', 53),
('98345', 'Sin Kim Sun', 'Elec. Eng.', '80000.00', '\"41612\",\"282-5513 Ante, Rd.\",\"North Island\",\"Belgium\"', '(714) 946-8821', '1970-04-20', 52),
('99762', 'Frederic von der Leyen', 'Personal', '2999.00', 'Address. 60 rue Wiertz / Wiertzstraat 60. B-1047 - Bruxelles/Brussels. ', '00 800 6 7 8 9 10 11,00 32 22 99 96 96', '2076-12-12', 0),
('00128', 'Zhang', 'Comp. Sci.', '102.00', '\"1521 YV\",\"4973 Sit St.\",\"Castilla y León\",\"Costa Rica\"', '(807) 835-2885', '2003-02-11', 19),
('12345', 'Shankar', 'Comp. Sci.', '32.00', '\"82476-613\",\"1942 Aliquet Ave\",\"Vlaams-Brabant\",\"United States\"', '1-570-247-2546', '2003-02-21', 19),
('19991', 'Brandt', 'History', '80.00', '\"819702\",\"P.O. Box 534, 3385 Non Street\",\"Central Luzon\",\"Norway\"', '(537) 384-6343', '2005-09-21', 17),
('23121', 'Chavez', 'Finance', '110.00', '\"5128-5653\",\"P.O. Box 892, 3889 Risus. Rd.\",\"Ulster\",\"Ukraine\"', '1-272-853-9171', '2003-10-01', 19),
('44553', 'Peltier', 'Physics', '56.00', '\"40314\",\"973-2626 Erat St.\",\"Wielkopolskie\",\"Turkey\"', '(448) 238-6474', '2002-04-11', 20),
('45678', 'Levy', 'Physics', '46.00', '\"H6P 1Z5\",\"854-4390 Bibendum Road\",\"Zhōngnán\",\"Vietnam\"', '1-532-552-6921', '2005-05-16', 17),
('54321', 'Williams', 'Comp. Sci.', '54.00', '\"627358\",\"725 Amet Avenue\",\"Queensland\",\"Brazil\"', '(174) 471-3261', '2004-08-12', 18),
('55739', 'Sanchez', 'Music', '38.00', '\"58117-54536\",\"1685 Urna Ave\",\"Huádōng\",\"Pakistan\"', '1-636-321-5885', '2005-12-01', 17),
('70557', 'Snow', 'Physics', '0.00', '\"176238\",\"P.O. Box 194, 633 Dolor Ave\",\"Tyrol\",\"Russian Federation\"', '(827) 724-6034', '2006-01-16', 15),
('76543', 'Brown', 'Comp. Sci.', '58.00', '\"1173 LR\",\"P.O. Box 852, 7014 Aliquam Rd.\",\"Ancash\",\"Vietnam\"', '(316) 763-2487', '2002-07-19', 20),
('76653', 'Aoi', 'Elec. Eng.', '60.00', '\"B4P 4S1\",\"3648 Integer St.\",\"Liguria\",\"Poland\"', '1-517-761-3814', '2004-12-10', 18),
('98765', 'Bourikas', 'Elec. Eng.', '98.00', '\"81359\",\"Ap #445-9634 Fringilla, Avenue\",\"Eastern Visayas\",\"New Zealand\"', '1-906-836-3364', '2001-09-23', 21),
('98988', 'Tanaka', 'Biology', '120.00', '\"7043\",\"297 Nam Street\",\"Central Kalimantan\",\"Poland\"', '(482) 647-7118', '2003-02-11', 19);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
