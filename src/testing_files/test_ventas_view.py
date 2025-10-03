import flet as ft
from src.views.ventas_view import VentasView


def main(page: ft.Page):
    page.title = "Vista Ventas - Prueba"
    # page.window_width = 1200
    # page.window_height = 700
    page.theme_mode = "light"

    ventas_view = VentasView(page)

    # Agregar al layout principal
    page.add(ventas_view)


if __name__ == "__main__":
    ft.app(target=main)
