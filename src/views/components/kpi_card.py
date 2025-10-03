import flet as ft


# Ingresos
class KpiIncomeCard(ft.Card):

    def __init__(self, value):
        super().__init__(
            content=ft.Container(
                content=ft.Text(value=f"Ingresos: ${value}", size=16),
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )


# Egresos
class KpiExpensesCard(ft.Card):

    def __init__(self, value=0):
        super().__init__(
            content=ft.Container(
                content=ft.Text(value=f"Egresos: ${value}", size=16),
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )


# Ultima Venta
class KpiLastSaleCard(ft.Card):

    def __init__(self, value=0):
        super().__init__(
            content=ft.Container(
                content=ft.Text(value=f"Ultima Venta: ${value}", size=16),
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )


# Saldo total ganado
class KpiBalanceCard(ft.Card):

    def __init__(self, value=0):
        super().__init__(
            content=ft.Container(
                content=ft.Text(value=f"Balance mensual: ${value}", size=16),
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )
