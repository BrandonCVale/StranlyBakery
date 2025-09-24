import flet as ft
from views.login_view import LoginView


def main(page):
    LoginView(page)


# Punto de entrada
if __name__ == "__main__":
    ft.app(target=main)
