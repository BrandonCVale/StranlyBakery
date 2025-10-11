import flet as ft


class ForgotPasswordPresenter:
    def __init__(self, view):
        self.view = view

    def on_email_change(self, e):
        email = e.control.value.strip()
        self.view.btn_enviar_codigo.disabled = not bool(email)  # return True si email tiene txt, False si esta vacio
        self.view.update()

    def on_send_code(self, e):
        self.view.page.snack_bar = ft.SnackBar(ft.Text("Código enviado (simulado)."))
        self.view.page.snack_bar.open = True
        self.view.page.update()
