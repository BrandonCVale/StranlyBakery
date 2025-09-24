import flet as ft
from src.presenters.login_presenter import LoginPresenter
from src.models.login_model import AuthenticationModel


class LoginView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        # Saving the reference to the page
        self.page = page

        # MVP: Model and Presenter
        model = AuthenticationModel()
        self.presenter = LoginPresenter(self, model)

        # --- Controls ---
        self.user_name = ft.TextField(
            label="Username",
            width=400,
            autofocus=True,
            prefix_icon=ft.Icons.PERSON
        )

        self.password = ft.TextField(
            label="Password",
            width=400,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK
        )

        self.btn_login = ft.ElevatedButton(
            text="Log In",
            width=400,
            on_click=self.on_login
        )

        self.btn_forgot_password = ft.ElevatedButton(
            text="Forgot your password?",
            width=400,
            on_click=self.on_forgot_password
        )

        # Adding all the controls to the column
        self.controls = [
            self.user_name,
            self.password,
            self.btn_login,
            self.btn_forgot_password
        ]

    # --- Methods ---
    def on_login(self, e):
        username = self.user_name.value.strip()
        password = self.password.value.strip()
        self.presenter.handle_login(username, password)

    def on_forgot_password(self, e):
        username = self.user_name.value.strip()
        self.presenter.handle_forgot_password(username)

    # --- Interface exposed to the presenter ---
    def show_message(self, text):
        self.page.open(ft.SnackBar(content=ft.Text(text)))
