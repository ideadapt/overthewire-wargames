CREATE TABLE `BasketItems`
(
    `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
    `quantity`  INTEGER,
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL,
    `BasketId`  INTEGER REFERENCES `Baskets` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    `ProductId` INTEGER REFERENCES `Products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (`BasketId`, `ProductId`)
)
CREATE TABLE `Baskets`
(
    `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
    `coupon`    VARCHAR(255),
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL,
    `UserId`    INTEGER REFERENCES `Users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
)
CREATE TABLE `Captchas`
(
    `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
    `captchaId` INTEGER,
    `captcha`   VARCHAR(255),
    `answer`    VARCHAR(255),
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL
)
CREATE TABLE `Challenges`
(
    `id`          INTEGER PRIMARY KEY AUTOINCREMENT,
    `key`         VARCHAR(255),
    `name`        VARCHAR(255),
    `category`    VARCHAR(255),
    `description` VARCHAR(255),
    `difficulty`  INTEGER,
    `hint`        VARCHAR(255),
    `hintUrl`     VARCHAR(255),
    `solved`      TINYINT(1),
    `disabledEnv` VARCHAR(255),
    `createdAt`   DATETIME NOT NULL,
    `updatedAt`   DATETIME NOT NULL
)
CREATE TABLE `Complaints`
(
    `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
    `message`   VARCHAR(255),
    `file`      VARCHAR(255),
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL,
    `UserId`    INTEGER REFERENCES `Users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
)
CREATE TABLE `Feedbacks`
(
    `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
    `comment`   VARCHAR(255),
    `rating`    INTEGER  NOT NULL,
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL,
    `UserId`    INTEGER REFERENCES `Users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
)
CREATE TABLE `ImageCaptchas`
(
    `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
    `image`     VARCHAR(255),
    `answer`    VARCHAR(255),
    `UserId`    INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL
)
CREATE TABLE `PrivacyRequests`
(
    `id`                INTEGER PRIMARY KEY AUTOINCREMENT,
    `UserId`            INTEGER REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
    `deletionRequested` TINYINT(1) DEFAULT 0,
    `createdAt`         DATETIME NOT NULL,
    `updatedAt`         DATETIME NOT NULL
)
CREATE TABLE `Products`
(
    `id`          INTEGER PRIMARY KEY AUTOINCREMENT,
    `name`        VARCHAR(255),
    `description` VARCHAR(255),
    `price`       DECIMAL,
    `image`       VARCHAR(255),
    `createdAt`   DATETIME NOT NULL,
    `updatedAt`   DATETIME NOT NULL,
    `deletedAt`   DATETIME
)
CREATE TABLE `Recycles`
(
    `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
    `quantity`  INTEGER(4),
    `address`   VARCHAR(180),
    `isPickup`  TINYINT(1) DEFAULT 0,
    `date`      DATETIME,
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL,
    `UserId`    INTEGER REFERENCES `Users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
)
CREATE TABLE `SecurityAnswers`
(
    `id`                 INTEGER PRIMARY KEY AUTOINCREMENT,
    `answer`             VARCHAR(255),
    `UserId`             INTEGER UNIQUE REFERENCES `Users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE,
    `createdAt`          DATETIME NOT NULL,
    `updatedAt`          DATETIME NOT NULL,
    `SecurityQuestionId` INTEGER REFERENCES `SecurityQuestions` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
)
CREATE TABLE `SecurityQuestions`
(
    `id`        INTEGER PRIMARY KEY AUTOINCREMENT,
    `question`  VARCHAR(255),
    `createdAt` DATETIME NOT NULL,
    `updatedAt` DATETIME NOT NULL
)
CREATE TABLE `Users`
(
    `id`           INTEGER PRIMARY KEY AUTOINCREMENT,
    `username`     VARCHAR(255) DEFAULT '',
    `email`        VARCHAR(255) UNIQUE,
    `password`     VARCHAR(255),
    `isAdmin`      TINYINT(1)   DEFAULT 0,
    `lastLoginIp`  VARCHAR(255) DEFAULT '0.0.0.0',
    `profileImage` VARCHAR(255) DEFAULT 'default.svg',
    `totpSecret`   VARCHAR(255) DEFAULT '',
    `isActive`     TINYINT(1)   DEFAULT 1,
    `createdAt`    DATETIME NOT NULL,
    `updatedAt`    DATETIME NOT NULL,
    `deletedAt`    DATETIME
)
CREATE TABLE sqlite_sequence
(
    name,
    seq
)
