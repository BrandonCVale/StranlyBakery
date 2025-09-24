import flet as ft
from views.login_view import LoginView


def main(page: ft.Page):
    page.title = "Stranly Bakery"
    page.theme_mode = "light"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    login_view = LoginView(page)
    page.add(login_view)


# Entry point
if __name__ == "__main__":
    ft.app(target=main)
