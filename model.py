# model.py
import mysql.connector
from config import DB_CONFIG
from datetime import datetime

class GameModel:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor(dictionary=True)

    def add_game(self):
        random = '1:2:3:4'
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
        time = datetime.now()
        sql = "INSERT INTO Round (GameId, Guess) VALUES (%s, %s)"
        self.cursor.execute(sql, (gameId, guess))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_rounds(self, gameId):
            self.cursor.execute("SELECT * FROM Round WHERE GameId = %s", (gameId,))
            return self.cursor.fetchone()