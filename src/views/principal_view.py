import flet as ft
from src.models.principal_model import Kpis
from src.presenters.principal_presenter import PrincipalPresenter


class PrincipalInterface(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True, spacing=20)  # Constructor reference (ft.Column)

        # Reference to the page
        self.page = page

        # MVP: Model and Presenter
        model = Kpis()
        self.presenter = PrincipalPresenter(self, model)

        # --- Controls ---
        # - KPI cards -
        self.kpi_ingresos = ft.Card(
            content=ft.Container(
                content=ft.Text(value="Ingresos: $1,150", size=16),
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )
        self.kpi_egresos = ft.Card(
            content=ft.Container(
                content=ft.Text(value="Egresos: $200", size=16),
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )
        self.kpi_ultima_venta = ft.Card(
            content=ft.Container(
                content=ft.Text(value='Ultima venta: $160', size=16),
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )

        # --- KPIs container ---
        kpis_container = ft.Row(
            controls=[self.kpi_ingresos, self.kpi_egresos, self.kpi_ultima_venta],

            alignment=ft.MainAxisAlignment.START,
            spacing=20
        )

        # --- Table "Productos vendidos" ---
        self.productos_vendidos = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Producto")),
                ft.DataColumn(ft.Text("Precio")),
                ft.DataColumn(ft.Text("Cantidad"))
            ],
            rows=[]  # start empty
        )
        # --- Table Container ---
        table_container = ft.Column(
            controls=[ft.Text(value="Productos vendidos", size=18),
                      self.productos_vendidos],

            alignment=ft.MainAxisAlignment.START,
            spacing=10
        )

        # -- Layout principal --
        self.controls = [
            kpis_container,
            table_container
        ]
