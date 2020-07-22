-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Jul 22, 2020 at 11:50 AM
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
  `isActive` tinyint(1) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `createdOn` datetime(6) NOT NULL,
  `updatedOn` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`studentId`, `password`, `firstname`, `lastname`, `isActive`, `gender`, `createdOn`, `updatedOn`) VALUES
('abhishakv', '0k8Jahh9QFYtlsApJZ60gg==', 'mtB+4BCR2JbCyo3mK9/9AQ==', '5hE7UdBrLMfYWBlano2KBw==', 1, '', '2020-07-21 04:08:34.024593', '2020-07-22 07:34:21.596940'),
('anchitj', 'k90rC6I1kHDS7vgPlhx69A==', 'X9chpLFHMuVW3bS4RdLI6Q==', '70prrwVXv79d42xz7tTa6g==', 1, '', '2020-07-21 04:08:21.436404', '2020-07-22 04:08:21.436426'),
('ankit', 'k90rC6I1kHDS7vgPlhx69A==', 'zFXSD1VGQk0GayUTGczkkw==', 'CAvKJqsUwAVQQ5mydlpqQw==', 1, '', '2020-07-22 04:07:49.146175', '2020-07-22 04:07:49.146209'),
('bhavya', 'k90rC6I1kHDS7vgPlhx69A==', 'mT9/Y1Q3DaZ6PRRFEkta5A==', 'Ax/XCJkSGP0v1TnvrZQRMg==', 1, '', '2020-07-21 04:09:46.352046', '2020-07-22 04:09:46.352074'),
('rajata', 'k90rC6I1kHDS7vgPlhx69A==', 'gap98es/3346pzlWLLnnWg==', 'SBJ0ggrI/yi1xLZqvz3ksA==', 1, '', '2020-07-22 04:09:18.820264', '2020-07-22 04:09:18.820295'),
('test', 'k90rC6I1kHDS7vgPlhx69A==', 'Oip+XQJuqZTDpAcJzhF5rA==', 'Oip+XQJuqZTDpAcJzhF5rA==', 0, '', '2020-07-22 04:11:31.324260', '2020-07-22 04:13:41.298566');

-- --------------------------------------------------------

--
-- Table structure for table `student_teacher`
--

CREATE TABLE `student_teacher` (
  `mapId` varchar(255) NOT NULL,
  `isStarMarked` tinyint(1) NOT NULL,
  `isStudentActive` tinyint(1) NOT NULL,
  `studentId` varchar(255) NOT NULL,
  `teacherId` varchar(255) NOT NULL,
  `isTeacherActive` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_teacher`
--

INSERT INTO `student_teacher` (`mapId`, `isStarMarked`, `isStudentActive`, `studentId`, `teacherId`, `isTeacherActive`) VALUES
('28d2862c-7537-4f1f-9eee-2dc8841f8cf2', 0, 1, 'anchitj', 'akb', 0),
('340bbd51-bc46-468e-a27d-b54454550786', 1, 1, 'rajata', 'akb', 0),
('6f6195a5-7449-4b9a-acd1-75e25d8944b8', 0, 1, 'rajata', 'narang', 0),
('86ae4b1e-c619-4911-870b-cc892a6cdb4a', 1, 1, 'bhavya', 'narang', 0),
('bfc12a16-558c-4446-84c1-abd6ac4c9fae', 1, 1, 'ankit', 'akb', 0),
('ceaf9646-fdf8-48a0-97d0-d08139f32289', 1, 1, 'abhishakv', 'narang', 0);

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
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`teacherId`, `password`, `firstname`, `lastname`, `isActive`, `gender`, `createdOn`, `updatedOn`) VALUES
('akb', 'k90rC6I1kHDS7vgPlhx69A==', 'HWVh/tbG/hoNALLBzMQL6g==', '4HUadZGP0qMwC3AfG/YAFA==', 1, '', '2020-07-22 07:37:59.989546', '2020-07-22 07:37:59.989650'),
('narang', 'k90rC6I1kHDS7vgPlhx69A==', 'GJ9mxslD/u2IMmla1yjGvw==', 'iCrU/x8dVMcuY+6sh9y6CQ==', 1, '', '2020-07-22 07:37:23.812321', '2020-07-22 07:37:23.812541'),
('test', 'k90rC6I1kHDS7vgPlhx69A==', 'VOr/h2jWQjWxlyQOvYZ5uQ==', 'qUoubLtakgwEd5IwaaloJg==', 0, '', '2020-07-22 07:37:37.694047', '2020-07-22 07:39:50.464904');

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
