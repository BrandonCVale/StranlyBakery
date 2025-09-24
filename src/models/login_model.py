import os
import psycopg2
from dotenv import load_dotenv
from passlib.hash import bcrypt

# load the data from the .env file
load_dotenv()


class AuthenticationModel:
    def get_conn(self):
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )

    def authenticate_user(self, username, plain_password):
        conn = self.get_conn()
        cur = conn.cursor()
        cur.execute("SELECT password_hash FROM ventas_2025.usuarios WHERE username = %s",
                    (username,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            return False

        stored_hash = row[0]
        return bcrypt.verify(plain_password, stored_hash)
