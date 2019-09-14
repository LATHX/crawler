/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50714
 Source Host           : localhost:3306
 Source Schema         : qunar

 Target Server Type    : MySQL
 Target Server Version : 50714
 File Encoding         : 65001

 Date: 14/09/2019 12:25:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for qunar
-- ----------------------------
DROP TABLE IF EXISTS `qunar`;
CREATE TABLE `qunar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `sale` int(11) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `hot` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

SET FOREIGN_KEY_CHECKS = 1;
