drop database if exists Guess_The_Number_db;

CREATE DATABASE Guess_The_Number_db;
USE Guess_The_Number_db;

CREATE TABLE Game (
GameId INT AUTO_INCREMENT PRIMARY KEY,
Answer VARCHAR(7) NOT NULL,
Status BOOLEAN DEFAULT TRUE
);

CREATE TABLE Round (
RoundId INT AUTO_INCREMENT PRIMARY KEY,
GameId INT NOT NULL,
Guess VARCHAR(7) NOT NULL,
Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (GameId) REFERENCES Game(GameId)
);

INSERT INTO Game (Answer) values ('1:2:3:4');
SELECT * FROM Game;

INSERT INTO Round (GameId, Guess) values (1, '1:2:3:4');
SELECT * FROM Round;

SELECT * FROM Round
WHERE GameId = 1;