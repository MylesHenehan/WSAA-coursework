-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: MylesHenehan.mysql.pythonanywhere-services.com    Database: MylesHenehan$freelance_linguists
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `linguists`
--

DROP TABLE IF EXISTS `linguists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `linguists` (
  `LinguistID` int NOT NULL AUTO_INCREMENT,
  `LinguistName` varchar(100) NOT NULL,
  `LinguistEmail` varchar(100) NOT NULL,
  `TargetLocale` varchar(10) NOT NULL,
  PRIMARY KEY (`LinguistID`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linguists`
--

LOCK TABLES `linguists` WRITE;
/*!40000 ALTER TABLE `linguists` DISABLE KEYS */;
INSERT INTO `linguists` VALUES (3,'Carla Gomez','carla.gomez@example.com','es-ES'),(4,'David Lee','david.lee@example.com','zh-CN'),(5,'Elena Petrova','elena.petrova@example.com','ru-RU'),(6,'Fatima Khan','fatima.khan@example.com','ar-SA'),(7,'George Brown','george.brown@example.com','en-GB'),(8,'Hiro Tanaka','hiro.tanaka@example.com','ja-JP'),(9,'Isabella Rossi','isabella.rossi@example.com','it-IT'),(10,'Jack Wilson','jack.wilson@example.com','en-GB'),(11,'Katarina Novak','katarina.novak@example.com','ru-RU'),(12,'Liam Murphy','liam.murphy@example.com','en-GB'),(13,'Marta Silva','marta.silva@example.com','pt-BR'),(14,'Nina Müller','nina.muller@example.com','de-DE'),(15,'Oscar Martinez','oscar.martinez@example.com','es-LA'),(16,'Paula Hernandez','paula.hernandez@example.com','es-ES'),(17,'Quinn Taylor','quinn.taylor@example.com','en-US'),(18,'Ravi Singh','ravi.singh@example.com','hi-IN'),(19,'Sofia Andersson','sofia.andersson@example.com','sv-SE'),(20,'Takeshi Saito','takeshi.saito@example.com','ja-JP'),(21,'Ursula Schmidt','ursula.schmidt@example.com','de-DE'),(22,'Victor Lopez','victor.lopez@example.com','es-LA'),(23,'Wendy Clark','wendy.clark@example.com','en-GB'),(24,'Xiang Liu','xiang.liu@example.com','zh-CN'),(25,'Yasmin Al-Farsi','yasmin.alfarsi@example.com','ar-SA'),(26,'Zachary King','zachary.king@example.com','en-US'),(27,'Anna Kowalska','anna.kowalska@example.com','ru-RU'),(28,'Bruno Carvalho','bruno.carvalho@example.com','pt-BR'),(38,'Rafael Torres','r.torres@example.com','pt-BR');
/*!40000 ALTER TABLE `linguists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rates`
--

DROP TABLE IF EXISTS `rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rates` (
  `RateID` int NOT NULL AUTO_INCREMENT,
  `LinguistID` int DEFAULT NULL,
  `PerWordRate` decimal(5,3) DEFAULT NULL,
  `HourlyRate` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`RateID`),
  KEY `LinguistID` (`LinguistID`),
  CONSTRAINT `rates_ibfk_1` FOREIGN KEY (`LinguistID`) REFERENCES `linguists` (`LinguistID`) ON DELETE CASCADE,
  CONSTRAINT `rates_chk_1` CHECK ((`PerWordRate` between 0.05 and 0.12))
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rates`
--

LOCK TABLES `rates` WRITE;
/*!40000 ALTER TABLE `rates` DISABLE KEYS */;
INSERT INTO `rates` VALUES (37,3,0.090,40.00),(38,4,0.070,28.00),(39,5,0.065,27.50),(40,6,0.115,50.00),(41,7,0.100,45.00),(42,8,0.085,35.00),(43,9,0.060,20.00),(44,10,0.075,32.00),(45,11,0.110,48.00),(46,12,0.058,22.00),(47,13,0.105,42.00),(48,14,0.068,29.00),(49,15,0.072,31.00),(50,16,0.095,38.00),(51,17,0.062,24.00),(52,18,0.085,33.00),(53,19,0.115,50.00),(54,20,0.055,26.00),(55,21,0.080,30.00),(56,22,0.070,28.00),(57,23,0.065,27.50),(58,24,0.090,40.00),(59,25,0.060,22.00),(60,26,0.100,45.00),(61,27,0.058,23.00),(62,28,0.110,47.00),(64,38,0.095,32.00);
/*!40000 ALTER TABLE `rates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-25 19:26:47
