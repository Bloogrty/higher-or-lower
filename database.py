import sqlite3

DB_NAME = "game.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)""")
    conn.commit()
    conn.close()


def insert_score(name, score):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()


def get_scores():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC")
    scores = cursor.fetchall()
    conn.close()
    return scores
