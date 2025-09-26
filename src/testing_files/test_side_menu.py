import flet as ft
from src.views.main_view import SideMenuView


def main(page: ft.Page):
    page.title = "Prueba NavigationRail"
    page.window_width = 1000
    page.window_height = 600
    page.add(SideMenuView(page))


ft.app(target=main)
