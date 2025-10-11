import flet as ft


# Ingresos
class KpiIncomeCard(ft.Card):

    def __init__(self, value):
        self.label = ft.Text(value=f"Ingresos: ${value}", size=16)
        super().__init__(
            content=ft.Container(
                content=self.label,
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )

    def actualizar_valor(self, nuevo_valor):
        self.label.value = f"Ingresos: ${nuevo_valor:,.2f}"


# Egresos
class KpiExpensesCard(ft.Card):

    def __init__(self, value=0):
        self.label = ft.Text(value=f"Egresos: ${value}", size=16)
        super().__init__(
            content=ft.Container(
                content=self.label,
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )

    def actualizar_valor(self, nuevo_valor):
        self.label.value = f"Egresos: ${nuevo_valor:,.2f}"


# Ultima Venta
class KpiLastSaleCard(ft.Card):

    def __init__(self, value=0):
        self.label = ft.Text(value=f"Última venta: ${value}", size=16)
        super().__init__(
            content=ft.Container(
                content=self.label,
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
        self.label = ft.Text(value=f"Balance mensual: ${value}", size=16)
        super().__init__(
            content=ft.Container(
                content=self.label,
                padding=15,
                alignment=ft.alignment.center,
                bgcolor='#EFE5DC',
                border_radius=10,
                expand=True
            )
        )

    def actualizar_valor(self, nuevo_valor):
        signo = "+" if nuevo_valor >= 0 else "-"
        color = "#1D8348" if nuevo_valor >= 0 else "#C0392B"
        self.label.value = f"Balance mensual: {signo}${abs(nuevo_valor):,.2f}"
        self.label.color = color
