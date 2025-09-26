import flet as ft
from src.views.login_view import LoginView


def main(page: ft.Page):
    page.title = "Stranly Bakery"
    page.theme_mode = "light"

    # --- Defaults ---
    page.window.maximized = False
    page.window.width = 1320
    page.window.height = 700
    page.window.min_width = 1320
    page.window.min_height = 700
    page.window.resizable = False

    page.window.center()

    login_view = LoginView(page)
    page.add(
        ft.Container(
            expand=True,
            content=login_view,
            alignment=ft.alignment.center
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
