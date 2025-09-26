import flet as ft
from views.login_view import LoginView


def main(page: ft.Page):
    page.title = "Stranly Bakery"
    page.theme_mode = "light"

    login_view = LoginView(page)

    page.add(ft.Container(
        expand=True,
        bgcolor="#FBFEFB",
        alignment=ft.alignment.center,  # place whatever is inside in the center of the screen
        content=login_view
    ))


# Entry point
if __name__ == "__main__":
    ft.app(target=main)
