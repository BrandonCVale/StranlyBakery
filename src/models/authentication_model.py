import os
import psycopg2
from dotenv import load_dotenv
from passlib.hash import bcrypt

# load the data from the .env file
load_dotenv()


class AuthenticationModel:

    def __init__(self):
        self.usuario_actual = None  # guarda el usuario logueado

    # --- Conexion ---
    def get_conn(self):
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )

    # --- Autenticacion ---
    def authenticate_user(self, username, plain_password):
        try:
            # --- 1. Conexión a la base de datos ---
            conn = self.get_conn()
            cur = conn.cursor()

            # --- 2. Consulta SQL ---
            cur.execute("""
                SELECT username, password_hash, rol
                FROM ventas_2025.usuarios
                WHERE username = %s
            """, (username,))

            row = cur.fetchone()

            # --- 3. Cierre de conexión ---
            cur.close()
            conn.close()

            # --- 4. Validación del resultado ---
            if not row:
                print(f"[INFO] Usuario '{username}' no encontrado en la base de datos.")
                return False

            # Desempaquetado seguro
            username_db, stored_hash, rol = row

            # --- 5. Verificación del password ---
            if bcrypt.verify(plain_password, stored_hash):
                self.usuario_actual = {"username": username_db, "rol": rol}
                print(f"[OK] Usuario autenticado correctamente: {username_db} (rol: {rol})")
                return True
            else:
                print(f"[WARN] Contraseña incorrecta para usuario '{username}'.")
                return False

        except Exception as e:
            # --- 6. Captura de errores generales ---
            print("[ERROR] Error autenticando usuario:", e)
            return False
