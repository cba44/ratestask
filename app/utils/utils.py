import os
import psycopg2

class Utils:
    def get_db_connection():
        db_host = os.getenv('DB_HOST') or 'localhost'
        db_database = os.getenv('DB_DATABASE') or 'postgres'
        db_user = os.getenv('DB_USER') or 'postgres'
        db_password = os.getenv('DB_PASSWORD') or 'ratestask'

        conn = psycopg2.connect(host = db_host,
                                database = db_database,
                                user = db_user,
                                password = db_password)
        return conn