import flet as ft
from src.views.principal_view import PrincipalInterface


def main(page: ft.Page):
    page.title = "Prueba PrincipalView"
    page.add(PrincipalInterface(page))


ft.app(target=main)
