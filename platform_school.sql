-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Jul 21, 2020 at 05:38 PM
-- Server version: 5.7.28
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `platform_school`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `studentId` varchar(255) NOT NULL,
  `password` varchar(45) NOT NULL,
  `firstname` longtext,
  `lastname` longtext,
  `isActive` tinyint(1) NOT NULL DEFAULT '1',
  `gender` varchar(20) NOT NULL DEFAULT 'Male',
  `createdOn` datetime(6) NOT NULL,
  `updatedOn` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`studentId`, `password`, `firstname`, `lastname`, `isActive`, `gender`, `createdOn`, `updatedOn`) VALUES
('abhishakv', '0k8Jahh9QFYtlsApJZ60gg==', 'C5QydpQeo/soeE7aNLaOlQ==', 'C5QydpQeo/soeE7aNLaOlQ==', 1, '', '2020-07-21 17:29:07.218111', '2020-07-21 17:32:12.883864');

-- --------------------------------------------------------

--
-- Table structure for table `student_teacher`
--

CREATE TABLE `student_teacher` (
  `mapId` varchar(255) NOT NULL,
  `isStarMarked` tinyint(1) NOT NULL,
  `isStudentActive` tinyint(1) NOT NULL,
  `studentId` varchar(255) NOT NULL,
  `teacherId` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `teacherId` varchar(255) NOT NULL,
  `password` varchar(45) NOT NULL,
  `firstname` longtext,
  `lastname` longtext,
  `isActive` tinyint(1) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `createdOn` datetime(6) NOT NULL,
  `updatedOn` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`studentId`);

--
-- Indexes for table `student_teacher`
--
ALTER TABLE `student_teacher`
  ADD PRIMARY KEY (`mapId`),
  ADD KEY `student_teacher_studentId_bfb7100d_fk_student_studentId` (`studentId`),
  ADD KEY `student_teacher_teacherId_0a7dffaa_fk_teacher_teacherId` (`teacherId`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`teacherId`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `student_teacher`
--
ALTER TABLE `student_teacher`
  ADD CONSTRAINT `student_teacher_studentId_bfb7100d_fk_student_studentId` FOREIGN KEY (`studentId`) REFERENCES `student` (`studentId`),
  ADD CONSTRAINT `student_teacher_teacherId_0a7dffaa_fk_teacher_teacherId` FOREIGN KEY (`teacherId`) REFERENCES `teacher` (`teacherId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
