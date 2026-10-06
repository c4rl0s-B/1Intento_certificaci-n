-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema CinePedia
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema CinePedia
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `CinePedia` DEFAULT CHARACTER SET utf8 ;
USE `CinePedia` ;

-- -----------------------------------------------------
-- Table `CinePedia`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `CinePedia`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `E-email_UNIQUE` (`E-email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CinePedia`.`peliculas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `CinePedia`.`peliculas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `director` VARCHAR(255) NULL,
  `sinopsi` VARCHAR(500) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `CinePedia`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `CinePedia`.`comentarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usuario_id` INT NOT NULL,
  `pelicula_id` INT NOT NULL,
  `texto` TEXT NULL,
  `fecha_publicada` DATETIME NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`, `usuario_id`, `pelicula_id`),
  INDEX `fk_usuarios_has_peliculas_peliculas1_idx` (`pelicula_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_peliculas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_peliculas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `CinePedia`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_peliculas_peliculas1`
    FOREIGN KEY (`pelicula_id`)
    REFERENCES `CinePedia`.`peliculas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
