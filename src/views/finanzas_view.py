import flet as ft
import datetime
from src.views.components.kpi_card import (KpiIncomeCard, KpiExpensesCard, KpiBalanceCard)
from src.models.finanzas_model import FinanzasModel
from src.presenters.finanzas_presenter import FinanzasPresenter


class FinanzasView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True, spacing=20)
        self.page = page

        # ----- MVP -----
        model = FinanzasModel()
        self.presenter = FinanzasPresenter(self, model)

        # ----- CONTROLS -----
        # --- Header ---
        self.date_picker = ft.DatePicker(
            first_date=datetime.datetime(year=2024, month=1, day=1),
            last_date=datetime.datetime(year=2025, month=12, day=31),
            on_change=self.presenter.handle_fecha_seleccionada
        )
        self.texto_fecha = ft.Text(
            value="No se ha seleccionado una fecha!",
            size=14
        )
        self.btn_fecha = ft.ElevatedButton(
            text="Seleccione la fecha",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.open(self.date_picker)
        )
        self.btn_export_pdf = ft.ElevatedButton(
            text="Exportar a PDF",
            icon=ft.Icons.PICTURE_AS_PDF
        )
        self.btn_export_excel = ft.ElevatedButton(
            text="Exportar a Excel",
            icon=ft.Icons.TABLE_VIEW
        )

        # --- KPIs Row ---
        self.kpi_ingresos = KpiIncomeCard(0)
        self.kpi_egresos = KpiExpensesCard(0)
        self.kpi_balance = KpiBalanceCard(0)

        # --- Body ---
        self.grafico_ingresos_egresos = ft.Container(
            content=ft.Text(value="Grafico de Ingresos vs Egresos", size=16, text_align=ft.TextAlign.CENTER),
            bgcolor="#FBFEFB",
            border_radius=10,
            expand=True,
            padding=10
        )
        self.tbl_ingresos = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Producto")),
                ft.DataColumn(ft.Text("Cantidad")),
                ft.DataColumn(ft.Text("Total"))
            ],
            rows=[]
        )
        self.tbl_egresos = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Concepto")),
                ft.DataColumn(ft.Text("Cantidad"))
            ],
            rows=[]
        )

        # ----- CONTAINERS -----
        header = ft.Row(
            controls=[self.btn_fecha, self.texto_fecha, self.btn_export_pdf, self.btn_export_excel],
            spacing=20
        )
        kpis_row = ft.Row(
            controls=[self.kpi_ingresos, self.kpi_egresos, self.kpi_balance],
            spacing=20
        )

        body = ft.Row(
            controls=[self.grafico_ingresos_egresos, self.tbl_ingresos, self.tbl_egresos],
            expand=True,
            spacing=20
        )

        # --- Layout principal ---
        self.controls = [
            header,
            kpis_row,
            body
        ]
