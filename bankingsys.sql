-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: bankingsys
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `acc_details`
--

DROP TABLE IF EXISTS `acc_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acc_details` (
  `accno` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `phoneno` text,
  `email` text,
  `address` text,
  `acctype` varchar(20) NOT NULL,
  `balance` text,
  PRIMARY KEY (`accno`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acc_details`
--

LOCK TABLES `acc_details` WRITE;
/*!40000 ALTER TABLE `acc_details` DISABLE KEYS */;
INSERT INTO `acc_details` VALUES (1,'Varad','0003-12-24','Male','99648763215','abc@gmail.com','Dombivili','Savings','78062.63'),(2,'Manasvi','0003-12-24','Male','8745675432','abc@gmail.com','Dombivili','Current','29636.85'),(3,'Jayesh','0003-12-24','Male','7906467987','abc@gmail.com','Dombivili','Current','4500'),(4,'yuvati','1960-02-11','female','4587124556','yuvati@gmail.com','vashi','Current ','4600.0'),(5,'Mahesh','1965-02-15','male','9869567455','xyz@gmail.com','Kopar','Current ','11057.58'),(6,'Vishnu','1969-06-21','male','7851245786','vishnu123@gmail.com','adasds','Current ','5012.0'),(7,'rajesh','1971-08-21','male','4645456464','rajesh12@gmail.com','karjat','Personal ','500'),(8,'priti','1965-07-16','male','8979879781','priti123@gmail.com','karjat','Personal ','500'),(9,'harsh','2019-07-21','male','7987987945','harsh123@gmail.com','kalyan','Saving ','376.68'),(10,'SUREKHA','1966-04-17','male','7845128956','surekha123@gmail.com','kalyan','Current ','500'),(11,'chetan','1991-05-15','male','2356897412','c@gmail.com','745698mjjiop;','Current ','377.0');
/*!40000 ALTER TABLE `acc_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_answer` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (1,'{\"1\": \"Orange\", \"2\": \"Dombivili\", \"3\": \"1\"}'),(2,'{\"1\": \"Yellow\", \"2\": \"France\", \"3\": \"2\"}'),(3,'{\"1\": \"Red\", \"2\": \"Dubai\", \"3\": \"3\"}'),(4,'{\"1\": \"hot red\", \"2\": \"paris\", \"3\": \"45\"}'),(5,'{\"1\": \"yellow\", \"2\": \"paris\", \"3\": \"785\"}'),(6,'{\"1\": \"hot pink\", \"2\": \"new york\", \"3\": \"4521\"}'),(7,'{\"1\": \"pink\", \"2\": \"karjat\", \"3\": \"4512\"}'),(8,'{\"1\": \"blue\", \"2\": \"karjat\", \"3\": \"1223\"}'),(9,'{\"1\": \"blue\", \"2\": \"kalyan\", \"3\": \"412\"}'),(10,'{\"1\": \"red\", \"2\": \"matheran\", \"3\": \"5\"}'),(11,'{\"1\": \"yellow\", \"2\": \"kopar\", \"3\": \"78\"}');
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `accno` int NOT NULL AUTO_INCREMENT,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`accno`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'1234'),(2,'4501'),(3,'7845'),(5,'1245'),(6,'3265'),(7,'7845'),(8,'4578'),(9,'1232'),(10,'1245'),(11,'1245');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `accno` int DEFAULT NULL,
  `sender_accno` int DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (1,2,'vaarad',45,NULL,NULL,1),(2,2,'varad',75,NULL,NULL,2),(1,3,'jayesh',132,NULL,NULL,3);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_history`
--

DROP TABLE IF EXISTS `transaction_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_history` (
  `accno` int DEFAULT NULL,
  `sender_accno` int DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `amount` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_history`
--

LOCK TABLES `transaction_history` WRITE;
/*!40000 ALTER TABLE `transaction_history` DISABLE KEYS */;
INSERT INTO `transaction_history` VALUES (1,2,'Varad','-20.5','2024-03-30','18:45:03',4),(1,2,'Varad','-25.22','2024-03-30','18:47:36',5),(2,1,'Varad','+25.22','2024-03-30','18:47:36',6),(1,2,'Varad','-45.25','2024-03-30','18:49:54',7),(2,1,'Varad','+45.25','2024-03-30','18:49:54',8),(5,2,'Varad','-25.23','2024-03-30','18:54:49',9),(2,5,'Varad','+25.23','2024-03-30','18:54:49',10),(5,1,'Varad','-20.56','2024-03-30','18:56:30',11),(1,5,'Varad','+20.56','2024-03-30','18:56:30',12),(1,5,'Mahesh','-2000.0','2024-03-30','18:57:03',13),(5,1,'Mahesh','+2000.0','2024-03-30','18:57:03',14),(1,2,'Varad','-500.0','2024-03-30','19:28:09',15),(2,1,'Varad','+500.0','2024-03-30','19:28:09',16),(1,2,'Varad','-124.12','2024-03-31','14:15:56',17),(2,1,'Varad','+124.12','2024-03-31','14:15:56',18),(9,2,'Varad','-45.12','2024-03-31','14:33:35',19),(1,4,'yuvati','-100.0','2024-05-03','18:37:52',45),(4,1,'yuvati','+100.0','2024-05-03','18:37:52',46),(1,5,'Mahesh','-12.0','2024-05-03','18:51:37',47),(5,1,'Mahesh','+12.0','2024-05-03','18:51:37',48),(11,1,'Varad','-45.0','2024-05-03','18:52:51',49),(1,11,'Varad','+45.0','2024-05-03','18:52:51',50),(11,5,'Mahesh','-123.0','2024-05-03','18:53:45',51),(5,11,'Mahesh','+123.0','2024-05-03','18:53:45',52);
/*!40000 ALTER TABLE `transaction_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-03 19:18:10
