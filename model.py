# model.py
import mysql.connector
from config import DB_CONFIG
from datetime import datetime
from service import random_numbers, guessA

class GameModel:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def add_game(self):
        random = random_numbers()
        sql = "INSERT INTO Game (Answer) VALUES (%s)"
        self.cursor.execute(sql, (random,))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_games(self):
        self.cursor.execute("SELECT * FROM Game")
        return self.cursor.fetchall()

    def get_game(self, gameId):
        self.cursor.execute("SELECT * FROM Game WHERE GameId = %s", (gameId,))
        return self.cursor.fetchone()

class RoundModel:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def add_round(self, gameId, guess):
        sql = "SELECT Answer FROM Game WHERE GameId = %s"
        self.cursor.execute(sql, (gameId,))
        row = self.cursor.fetchone()
        answer = row['Answer']

        round = guessA(guess, answer)
        sql = "INSERT INTO Round (GameId, Guess) VALUES (%s, %s)"
        self.cursor.execute(sql, (gameId, round))
        self.conn.commit()
        roundId = self.cursor.lastrowid

        if (round == 'e:e:e:e'):
            sql = "UPDATE Game SET Status = 0 WHERE GameId = %s;"
            self.cursor.execute(sql, (gameId,))
            self.conn.commit()

        return roundId
    
    def get_rounds(self, gameId):
            self.cursor.execute("SELECT * FROM Round WHERE GameId = %s", (gameId,))
            return self.cursor.fetchall()