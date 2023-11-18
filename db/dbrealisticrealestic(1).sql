-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 07, 2022 at 09:16 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dbrealistic`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE IF NOT EXISTS `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` varchar(110) NOT NULL,
  `acc_no` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `card_no` varchar(25) NOT NULL,
  `cvv` int(11) NOT NULL,
  `exp_date` varchar(15) NOT NULL,
  `upi` int(11) NOT NULL,
  `bal` int(11) NOT NULL,
  `st` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `account`
--


-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE IF NOT EXISTS `booking` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `sid` varchar(90) NOT NULL,
  `pid` varchar(90) NOT NULL,
  `q` varchar(90) NOT NULL,
  `uid` varchar(90) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `booking`
--


-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE IF NOT EXISTS `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(50) NOT NULL,
  `feedback` varchar(50) NOT NULL,
  `uid` varchar(50) NOT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `feedback`
--


-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE IF NOT EXISTS `product` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `sid` varchar(90) NOT NULL,
  `pname` varchar(90) NOT NULL,
  `price` varchar(90) NOT NULL,
  `description` varchar(90) NOT NULL,
  `image` varchar(90) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `product`
--


-- --------------------------------------------------------

--
-- Table structure for table `shop`
--

CREATE TABLE IF NOT EXISTS `shop` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` varchar(89) NOT NULL,
  `saddress` varchar(99) NOT NULL,
  `scontact` varchar(99) NOT NULL,
  `simage` varchar(99) NOT NULL,
  `semail` varchar(99) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `shop`
--


-- --------------------------------------------------------

--
-- Table structure for table `tblallocation`
--

CREATE TABLE IF NOT EXISTS `tblallocation` (
  `allocid` int(11) NOT NULL AUTO_INCREMENT,
  `requid` varchar(50) NOT NULL,
  `archid` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`allocid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `tblallocation`
--


-- --------------------------------------------------------

--
-- Table structure for table `tblarchitect`
--

CREATE TABLE IF NOT EXISTS `tblarchitect` (
  `aName` varchar(50) NOT NULL,
  `aAddress` varchar(100) NOT NULL,
  `aContact` varchar(50) NOT NULL,
  `aEmail` varchar(50) NOT NULL,
  `aPhoto` varchar(100) NOT NULL,
  `aqualification` varchar(500) NOT NULL,
  `aqproof` varchar(500) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`aEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblarchitect`
--


-- --------------------------------------------------------

--
-- Table structure for table `tblcontractor`
--

CREATE TABLE IF NOT EXISTS `tblcontractor` (
  `cName` varchar(50) NOT NULL,
  `cAddress` varchar(100) NOT NULL,
  `cContact` varchar(50) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `cPhoto` varchar(100) NOT NULL,
  `cprework` varchar(500) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`cEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcontractor`
--


-- --------------------------------------------------------

--
-- Table structure for table `tblcustomer`
--

CREATE TABLE IF NOT EXISTS `tblcustomer` (
  `cName` varchar(50) NOT NULL,
  `cAddress` varchar(50) NOT NULL,
  `cContact` varchar(50) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `aadhar` varchar(500) NOT NULL,
  PRIMARY KEY (`cEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblcustomer`
--


-- --------------------------------------------------------

--
-- Table structure for table `tbldesigner`
--

CREATE TABLE IF NOT EXISTS `tbldesigner` (
  `dName` varchar(50) NOT NULL,
  `dAddress` varchar(100) NOT NULL,
  `dContact` varchar(50) NOT NULL,
  `dEmail` varchar(50) NOT NULL,
  `dPhoto` varchar(100) NOT NULL,
  `dqualification` varchar(500) NOT NULL,
  `dqproof` varchar(500) NOT NULL,
  `description` varchar(200) NOT NULL,
  PRIMARY KEY (`dEmail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbldesigner`
--


-- --------------------------------------------------------

--
-- Table structure for table `tbldesignrequest`
--

CREATE TABLE IF NOT EXISTS `tbldesignrequest` (
  `dreqId` int(11) NOT NULL AUTO_INCREMENT,
  `planId` int(11) NOT NULL,
  `dEmail` varchar(50) NOT NULL,
  `dreqStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`dreqId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `tbldesignrequest`
--


-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE IF NOT EXISTS `tbllogin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`username`, `password`, `utype`, `status`) VALUES
('admin@gmail.com', 'admin', 'admin', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblplan`
--

CREATE TABLE IF NOT EXISTS `tblplan` (
  `planId` int(11) NOT NULL AUTO_INCREMENT,
  `aEmail` varchar(50) NOT NULL,
  `reqId` int(11) NOT NULL,
  `plan` varchar(100) NOT NULL,
  `sqft` int(11) NOT NULL,
  `cost` bigint(20) NOT NULL,
  `planStatus` varchar(50) NOT NULL,
  `fees` int(11) NOT NULL,
  `feesstatus` varchar(11) NOT NULL,
  PRIMARY KEY (`planId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `tblplan`
--


-- --------------------------------------------------------

--
-- Table structure for table `tblrequirement`
--

CREATE TABLE IF NOT EXISTS `tblrequirement` (
  `reqId` int(11) NOT NULL AUTO_INCREMENT,
  `cEmail` varchar(50) NOT NULL,
  `bedroom` varchar(50) NOT NULL,
  `bathroom` varchar(50) NOT NULL,
  `attached` varchar(50) NOT NULL,
  `carporch` varchar(50) NOT NULL,
  `kitchen` varchar(50) NOT NULL,
  `sitout` varchar(50) NOT NULL,
  `workarea` varchar(50) NOT NULL,
  `floor` varchar(50) NOT NULL,
  `sqft` varchar(50) NOT NULL,
  `other` varchar(100) NOT NULL,
  `reqDate` datetime NOT NULL,
  `reqStatus` varchar(50) NOT NULL,
  PRIMARY KEY (`reqId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `tblrequirement`
--


-- --------------------------------------------------------

--
-- Table structure for table `tblvideo`
--

CREATE TABLE IF NOT EXISTS `tblvideo` (
  `videoId` int(11) NOT NULL AUTO_INCREMENT,
  `dreqId` int(11) NOT NULL,
  `video` varchar(100) NOT NULL,
  `videoStatus` varchar(50) NOT NULL,
  `amount` int(11) NOT NULL,
  `paymentstatus` varchar(50) NOT NULL,
  PRIMARY KEY (`videoId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `tblvideo`
--


-- --------------------------------------------------------

--
-- Table structure for table `tblwork`
--

CREATE TABLE IF NOT EXISTS `tblwork` (
  `workId` int(11) NOT NULL AUTO_INCREMENT,
  `videoId` int(11) NOT NULL,
  `cEmail` varchar(50) NOT NULL,
  `wDate` date NOT NULL,
  `wStatus` varchar(50) NOT NULL,
  `cost` int(11) NOT NULL,
  PRIMARY KEY (`workId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tblwork`
--

