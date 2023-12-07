USE ponderadaSemana7

-- ponderadaSemana7.bd_user definition

CREATE TABLE `bd_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nickname` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `password_salt` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- ponderadaSemana7.bd_history definition

CREATE TABLE `bd_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `summary` varchar(500) DEFAULT NULL,
  `category` varchar(100) NOT NULL,
  `content` text,
  `user_id` int NOT NULL,
  `moment` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `bd_history_FK` (`user_id`),
  CONSTRAINT `bd_history_FK` FOREIGN KEY (`user_id`) REFERENCES `bd_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;