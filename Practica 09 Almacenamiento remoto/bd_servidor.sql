/*
SQLyog Community v13.1.7 (64 bit)
MySQL - 10.5.4-MariaDB : Database - datos_servidor
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`datos_servidor` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `datos_servidor`;

/*Table structure for table `clima` */

DROP TABLE IF EXISTS `clima`;

CREATE TABLE `clima` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_sensor` text NOT NULL,
  `certificado` text NOT NULL,
  `latitud` text NOT NULL,
  `longitud` text NOT NULL,
  `utc` int(11) NOT NULL,
  `fecha` text NOT NULL,
  `hora` text NOT NULL,
  `variable` text NOT NULL,
  `valor` float NOT NULL,
  `revisado` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `clima` */

/*Table structure for table `firma_sensores` */

DROP TABLE IF EXISTS `firma_sensores`;

CREATE TABLE `firma_sensores` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_sensor` text NOT NULL,
  `firma` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `firma_sensores` */

insert  into `firma_sensores`(`id`,`id_sensor`,`firma`) values 
(1,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
