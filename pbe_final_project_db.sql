-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 14, 2021 at 03:48 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbe_final_project_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `accesscard`
--

CREATE TABLE `accesscard` (
  `IdAccess` varchar(11) NOT NULL,
  `IdFasilitas1` varchar(11) DEFAULT NULL,
  `IdFasilitas2` varchar(11) DEFAULT NULL,
  `IdFasilitas3` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accesscard`
--

INSERT INTO `accesscard` (`IdAccess`, `IdFasilitas1`, `IdFasilitas2`, `IdFasilitas3`) VALUES
('', '', '', ''),
('AC0001', 'G001', 'SP001', 'TN001'),
('AC0002', 'G001', '', ''),
('AC0003', 'TN001', 'SP001', ''),
('AC0004', 'TN001', 'G001', ''),
('AC0005', 'GL001', 'G001', 'SP001');

-- --------------------------------------------------------

--
-- Table structure for table `fasilitas`
--

CREATE TABLE `fasilitas` (
  `IdFasilitas` varchar(11) NOT NULL,
  `Nama` varchar(30) NOT NULL,
  `JamBuka` varchar(10) NOT NULL,
  `JamTutup` varchar(10) NOT NULL,
  `Kapasitas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fasilitas`
--

INSERT INTO `fasilitas` (`IdFasilitas`, `Nama`, `JamBuka`, `JamTutup`, `Kapasitas`) VALUES
('', '', '', '', 0),
('G001', 'Gym', '08:30', '17:30', 0),
('GL001', 'Golf1', '08:00', '18:00', 20),
('GL002', 'Golf South area', '08:00', '18:00', 20),
('P001', 'Parkir Mobil', '00:00', '23:59', 500),
('P002', 'Parkir Motor', '00:00', '23:59', 250),
('SP001', 'Swimming Pool', '10:00', '18:00', 20),
('TN001', 'Tennis', '08:00', '17:00', 6);

-- --------------------------------------------------------

--
-- Table structure for table `kendaraan`
--

CREATE TABLE `kendaraan` (
  `NoPlat` varchar(10) NOT NULL,
  `JenisKendaraan` text NOT NULL,
  `Warna` varchar(20) NOT NULL,
  `IdParkir` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kendaraan`
--

INSERT INTO `kendaraan` (`NoPlat`, `JenisKendaraan`, `Warna`, `IdParkir`) VALUES
('', '', '', ''),
('B1234EV', 'Sedan', 'Biru', 'PMAB1001'),
('B2345BEP', 'Hilux', 'Abu-abu', 'PMAB1002'),
('B3456TEG', 'Minibus', 'Putih', 'PMAB1003'),
('B4567TES', 'Sedan', 'Merah', 'PMBB1001'),
('B5678TES', 'Sedan', 'Biru', 'PMBB1002');

-- --------------------------------------------------------

--
-- Table structure for table `owner`
--

CREATE TABLE `owner` (
  `IdOwner` varchar(4) NOT NULL,
  `Nama` varchar(30) NOT NULL,
  `TempatLahir` varchar(30) NOT NULL,
  `TanggalLahir` date NOT NULL,
  `Kelamin` text NOT NULL,
  `Telepon` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `owner`
--

INSERT INTO `owner` (`IdOwner`, `Nama`, `TempatLahir`, `TanggalLahir`, `Kelamin`, `Telepon`) VALUES
('', '', '', '0000-00-00', '', ''),
('001', 'eko', 'Jakarta', '2000-11-30', 'Laki-Laki', '087812345678'),
('002', 'eka', 'Tangerang', '2009-12-15', 'Laki-Laki', '081212345678'),
('003', 'Ika', '', '0000-00-00', 'Perempuan', '089812635547'),
('004', 'Ratih', '', '0000-00-00', 'Perempuan', '087756734231'),
('005', 'Fata', '', '0000-00-00', 'Laki-laki', '081223653398'),
('006', 'Dudu', '', '0000-00-00', 'Laki-laki', '089753247754'),
('007', 'Diah', '', '0000-00-00', 'Perempuan', '089854345223'),
('008', 'Anto', '', '0000-00-00', 'Laki-laki', '081551451116'),
('009', 'Fathi', '', '0000-00-00', 'Laki-laki', '0813316477778'),
('010', 'Ika Juga', '', '0000-00-00', 'Perempuan', '081335673345');

-- --------------------------------------------------------

--
-- Table structure for table `parkir`
--

CREATE TABLE `parkir` (
  `IdParkir` varchar(10) NOT NULL,
  `Block` varchar(11) NOT NULL,
  `Lantai` varchar(11) NOT NULL,
  `No` int(11) NOT NULL,
  `status` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `parkir`
--

INSERT INTO `parkir` (`IdParkir`, `Block`, `Lantai`, `No`, `status`) VALUES
('', '', '', 0, ''),
('PMAB1001', 'A', 'B1', 1, 'Kosong'),
('PMAB1002', 'A', 'B1', 2, 'Kosong'),
('PMAB1003', 'A', 'B1', 3, 'Kosong'),
('PMAB1004', 'A', 'B1', 4, 'Kosong'),
('PMAB1005', 'A', 'B1', 5, 'Kosong'),
('PMAG001', 'A', 'G', 1, 'kosong'),
('PMAG002', 'A', 'G', 2, 'kosong'),
('PMAG003', 'A', 'G', 3, 'kosong'),
('PMAG004', 'A', 'G', 4, 'kosong'),
('PMAG005', 'A', 'G', 5, 'kosong'),
('PMBB1001', 'B', 'B1', 1, 'Kosong'),
('PMBB1002', 'B', 'B1', 2, 'Kosong'),
('PMBB1003', 'B', 'B1', 3, 'Kosong'),
('PMBB1004', 'B', 'B1', 4, 'Kosong'),
('PMBB1005', 'B', 'B1', 5, 'Kosong'),
('PMBG001', 'B', 'G', 1, 'kosong'),
('PMBG002', 'B', 'G', 2, 'kosong'),
('PMBG003', 'B', 'G', 3, 'kosong'),
('PMBG004', 'B', 'G', 4, 'kosong'),
('PMBG005', 'B', 'G', 5, 'kosong');

-- --------------------------------------------------------

--
-- Table structure for table `tanggallahir`
--

CREATE TABLE `tanggallahir` (
  `tanggallahir` date NOT NULL,
  `tempat` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tanggallahir`
--

INSERT INTO `tanggallahir` (`tanggallahir`, `tempat`) VALUES
('2021-09-02', ''),
('2000-01-01', ''),
('2000-01-05', ''),
('2000-01-15', ''),
('2000-01-06', 'Jakarta');

-- --------------------------------------------------------

--
-- Table structure for table `unit`
--

CREATE TABLE `unit` (
  `NoUnit` varchar(6) NOT NULL,
  `Tipe` varchar(10) NOT NULL,
  `Luas` int(11) NOT NULL,
  `IdOwner` varchar(4) DEFAULT NULL,
  `IdAksesCard1` varchar(10) DEFAULT NULL,
  `IdAksesCard2` varchar(10) DEFAULT NULL,
  `IdAksesCard3` varchar(10) DEFAULT NULL,
  `IdAksesCard4` varchar(10) DEFAULT NULL,
  `IdAksesCard5` varchar(10) DEFAULT NULL,
  `IdKendaraan1` varchar(10) DEFAULT NULL,
  `IdKendaraan2` varchar(10) DEFAULT NULL,
  `IdKendaraan3` varchar(10) DEFAULT NULL,
  `IdKendaraan4` varchar(10) DEFAULT NULL,
  `IdKendaraan5` varchar(10) DEFAULT NULL,
  `IuranStatus` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `unit`
--

INSERT INTO `unit` (`NoUnit`, `Tipe`, `Luas`, `IdOwner`, `IdAksesCard1`, `IdAksesCard2`, `IdAksesCard3`, `IdAksesCard4`, `IdAksesCard5`, `IdKendaraan1`, `IdKendaraan2`, `IdKendaraan3`, `IdKendaraan4`, `IdKendaraan5`, `IuranStatus`) VALUES
('A-G-1', 'Emerald', 100, '001', 'AC0001', '', '', '', '', 'B1234EV', '', '', '', '', 'Clear'),
('A-G-2', 'Diamond', 105, '002', 'AC0002', 'AC0003', '', '', '', 'B2345BEP', 'B3456TEG', '', '', '', 'Clear'),
('A-G-3', 'Emerald', 100, '', '', '', '', '', '', '', '', '', '', '', 'Clear');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `IdUser` varchar(3) NOT NULL,
  `Nama` varchar(30) NOT NULL,
  `Pass` varchar(30) NOT NULL,
  `Role` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`IdUser`, `Nama`, `Pass`, `Role`) VALUES
('1', 'fata', '123', 'Admin'),
('2', 'hanz', '123', 'Admin'),
('3', 'fathi', '123', 'Admin'),
('4', 'hanz2', '345', 'User');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accesscard`
--
ALTER TABLE `accesscard`
  ADD PRIMARY KEY (`IdAccess`),
  ADD KEY `IdAccess` (`IdAccess`),
  ADD KEY `IdFasilitas1` (`IdFasilitas1`),
  ADD KEY `IdFasilitas2` (`IdFasilitas2`),
  ADD KEY `IdFasilitas3` (`IdFasilitas3`);

--
-- Indexes for table `fasilitas`
--
ALTER TABLE `fasilitas`
  ADD PRIMARY KEY (`IdFasilitas`),
  ADD KEY `IdFasilitas` (`IdFasilitas`);

--
-- Indexes for table `kendaraan`
--
ALTER TABLE `kendaraan`
  ADD PRIMARY KEY (`NoPlat`),
  ADD KEY `NoPlat` (`NoPlat`),
  ADD KEY `IdParkir` (`IdParkir`);

--
-- Indexes for table `owner`
--
ALTER TABLE `owner`
  ADD PRIMARY KEY (`IdOwner`),
  ADD KEY `IdOwner` (`IdOwner`);

--
-- Indexes for table `parkir`
--
ALTER TABLE `parkir`
  ADD PRIMARY KEY (`IdParkir`),
  ADD KEY `IdParkir` (`IdParkir`);

--
-- Indexes for table `unit`
--
ALTER TABLE `unit`
  ADD PRIMARY KEY (`NoUnit`),
  ADD KEY `NoUnit` (`NoUnit`),
  ADD KEY `IdOwner` (`IdOwner`),
  ADD KEY `IdAksesCard1` (`IdAksesCard1`),
  ADD KEY `IdAksesCard2` (`IdAksesCard2`),
  ADD KEY `IdAksesCard3` (`IdAksesCard3`),
  ADD KEY `IdAksesCard4` (`IdAksesCard4`),
  ADD KEY `IdAksesCard5` (`IdAksesCard5`),
  ADD KEY `IdKendaraan1` (`IdKendaraan1`),
  ADD KEY `IdKendaraan2` (`IdKendaraan2`),
  ADD KEY `IdKendaraan3` (`IdKendaraan3`),
  ADD KEY `IdKendaraan4` (`IdKendaraan4`),
  ADD KEY `IdKendaraan5` (`IdKendaraan5`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`IdUser`),
  ADD KEY `IdUser` (`IdUser`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accesscard`
--
ALTER TABLE `accesscard`
  ADD CONSTRAINT `accesscard_ibfk_1` FOREIGN KEY (`IdFasilitas1`) REFERENCES `fasilitas` (`IdFasilitas`),
  ADD CONSTRAINT `accesscard_ibfk_2` FOREIGN KEY (`IdFasilitas2`) REFERENCES `fasilitas` (`IdFasilitas`),
  ADD CONSTRAINT `accesscard_ibfk_3` FOREIGN KEY (`IdFasilitas3`) REFERENCES `fasilitas` (`IdFasilitas`);

--
-- Constraints for table `kendaraan`
--
ALTER TABLE `kendaraan`
  ADD CONSTRAINT `parkir` FOREIGN KEY (`IdParkir`) REFERENCES `parkir` (`IdParkir`);

--
-- Constraints for table `unit`
--
ALTER TABLE `unit`
  ADD CONSTRAINT `unit_ibfk_1` FOREIGN KEY (`IdAksesCard1`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `unit_ibfk_10` FOREIGN KEY (`IdKendaraan4`) REFERENCES `kendaraan` (`NoPlat`),
  ADD CONSTRAINT `unit_ibfk_11` FOREIGN KEY (`IdKendaraan5`) REFERENCES `kendaraan` (`NoPlat`),
  ADD CONSTRAINT `unit_ibfk_2` FOREIGN KEY (`IdAksesCard2`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `unit_ibfk_3` FOREIGN KEY (`IdAksesCard3`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `unit_ibfk_4` FOREIGN KEY (`IdAksesCard4`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `unit_ibfk_5` FOREIGN KEY (`IdAksesCard5`) REFERENCES `accesscard` (`IdAccess`),
  ADD CONSTRAINT `unit_ibfk_6` FOREIGN KEY (`IdOwner`) REFERENCES `owner` (`IdOwner`),
  ADD CONSTRAINT `unit_ibfk_7` FOREIGN KEY (`IdKendaraan1`) REFERENCES `kendaraan` (`NoPlat`),
  ADD CONSTRAINT `unit_ibfk_8` FOREIGN KEY (`IdKendaraan2`) REFERENCES `kendaraan` (`NoPlat`),
  ADD CONSTRAINT `unit_ibfk_9` FOREIGN KEY (`IdKendaraan3`) REFERENCES `kendaraan` (`NoPlat`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
