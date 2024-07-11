/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 10.5.4-MariaDB : Database - datos
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`datos` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `datos`;

/*Table structure for table `clima` */

DROP TABLE IF EXISTS `clima`;

CREATE TABLE `clima` (
  `id` text NOT NULL,
  `firma` text NOT NULL,
  `latitud` text NOT NULL,
  `longitud` text NOT NULL,
  `utc` int(11) NOT NULL,
  `fecha` text NOT NULL,
  `hora` text NOT NULL,
  `variable` text NOT NULL,
  `valor` float NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
