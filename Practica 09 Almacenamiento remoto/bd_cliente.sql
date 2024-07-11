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
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_sensor` text NOT NULL,
  `firma` text NOT NULL,
  `latitud` text NOT NULL,
  `longitud` text NOT NULL,
  `utc` int(11) NOT NULL,
  `fecha` text NOT NULL,
  `hora` text NOT NULL,
  `variable` text NOT NULL,
  `valor` float NOT NULL,
  `enviado` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `clima` */

insert  into `clima`(`id`,`id_sensor`,`firma`,`latitud`,`longitud`,`utc`,`fecha`,`hora`,`variable`,`valor`,`enviado`) values 
(1,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723363','-101.185096',-6,'2021-05-11','20:50:46.895239','temperatura',21,0),
(2,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723467','-101.185192',-6,'2021-05-11','20:50:51.933010','temperatura',21,0),
(3,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723413','-101.185110',-6,'2021-05-11','20:50:56.945295','temperatura',21,0),
(4,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723409','-101.185265',-6,'2021-05-11','20:51:01.953311','temperatura',20,0),
(5,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723421','-101.185039',-6,'2021-05-11','20:51:06.966710','temperatura',20,0),
(6,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723520','-101.185082',-6,'2021-05-11','20:51:11.978320','temperatura',20,0),
(7,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723595','-101.185241',-6,'2021-05-11','20:51:16.991433','temperatura',21,0),
(8,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723434','-101.184950',-6,'2021-05-11','20:51:22.001255','temperatura',20,0),
(9,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723594','-101.184958',-6,'2021-05-11','20:51:27.017278','temperatura',21,0),
(10,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723516','-101.184959',-6,'2021-05-11','20:51:32.038696','temperatura',20,0),
(11,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723481','-101.185213',-6,'2021-05-11','20:51:37.060066','temperatura',20,0),
(12,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723418','-101.185082',-6,'2021-05-11','20:51:42.114183','temperatura',21,0),
(13,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723549','-101.185029',-6,'2021-05-11','20:51:47.134202','temperatura',20,0),
(14,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723441','-101.184862',-6,'2021-05-11','20:51:52.142497','temperatura',21,0),
(15,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723563','-101.185068',-6,'2021-05-11','20:51:57.162781','temperatura',21,0),
(16,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723532','-101.185014',-6,'2021-05-11','20:52:02.174785','temperatura',21,0),
(17,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723391','-101.185060',-6,'2021-05-11','20:52:07.203609','temperatura',21,0),
(18,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723503','-101.185122',-6,'2021-05-11','20:52:12.228464','temperatura',21,0),
(19,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723334','-101.185162',-6,'2021-05-11','20:52:17.238731','temperatura',21,0),
(20,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723348','-101.184994',-6,'2021-05-11','20:52:22.256443','temperatura',21,0),
(21,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723367','-101.185265',-6,'2021-05-11','20:52:27.274226','temperatura',20,0),
(22,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723582','-101.185046',-6,'2021-05-11','20:52:32.700943','temperatura',21,0),
(23,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723350','-101.185236',-6,'2021-05-11','21:15:19.386139','temperatura',20,0),
(24,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723527','-101.185184',-6,'2021-05-11','21:15:24.409348','temperatura',20,0),
(25,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723529','-101.185222',-6,'2021-05-11','21:15:29.415621','temperatura',20,0),
(26,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723437','-101.185238',-6,'2021-05-11','21:15:34.425571','temperatura',21,0),
(27,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723501','-101.184894',-6,'2021-05-11','21:15:39.437224','temperatura',20,0),
(28,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723543','-101.185271',-6,'2021-05-11','21:15:44.461861','temperatura',21,0),
(29,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723371','-101.184996',-6,'2021-05-11','21:15:53.762296','temperatura',21,0),
(30,'Sen-Temp-V-01','562d6c962e80f8cbce1caf2163eb44c4','19.723435','-101.185148',-6,'2021-05-11','21:17:33.458817','temperatura',21,0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
