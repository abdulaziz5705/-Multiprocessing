import os


import psycopg2 as psql
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database=os.getenv("database"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port"),
        )

        cursor = db.cursor()
        data = ["insert", "delete", "update", "alter"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "insert data succesful"
        else:
            return cursor.fetchall()
