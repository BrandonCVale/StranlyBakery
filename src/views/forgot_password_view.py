import flet as ft
from src.presenters.forgot_password_presenter import ForgotPasswordPresenter


class ForgotPasswordView(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True, border_radius=10, bgcolor="#f0f0f0", width=page.width)
        self.page = page
        self.presenter = ForgotPasswordPresenter(self)

        # --- 1. CONTROLS ---
        self.title = ft.Text(
            value="Recupera tu contrasena",
            size=24,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.START
        )
        self.subtitle = ft.Text(
            value="Ingresa el correo registrado para enviarte un código de verificación",
            text_align=ft.TextAlign.START,
            # color=ft.Colors.GREEN_700

        )
        self.campo_correo = ft.TextField(
            label="Correo electronico...",
            hint_text="ejemplo@gmail.com",
            prefix_icon=ft.Icons.MAIL_OUTLINE,
            width=350,
            autofocus=True,
            on_change=self.presenter.on_email_change
        )
        self.btn_volver = ft.TextButton(
            text="Volver",
            on_click=lambda e: self.page.go("/login"),
            # style=ft.ButtonStyle(color=ft.Colors.BLUE_400)
        )
        self.btn_enviar_codigo = ft.ElevatedButton(
            text="Enviar codigo",
            width=200,
            disabled=True,
            on_click=self.presenter.on_send_code,
        )
        # --- 2. CONTAINERS ---
        self.header_container = ft.Column(
            controls=[
                self.btn_volver,
                self.title,
                self.subtitle
            ],
            spacing=10
        )

        self.body_container = ft.Container(
            content=ft.Column(
                controls=[
                    self.campo_correo,
                    ft.Container(height=2),
                    self.btn_enviar_codigo
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center
        )

        # --- 3. LAYOUT ---
        self.content = ft.Column(
            controls=[
                self.header_container,
                ft.Container(height=40),  # separador entre header y body
                self.body_container
            ],
            expand=True
        )
