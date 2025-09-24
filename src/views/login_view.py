import flet as ft
from src.presenters.login_presenter import LoginPresenter
from src.models.login_model import AuthenticationModel


class LoginView:

    def __init__(self, page: ft.Page):
        # Setting the attributes
        self.page = page
        self.page.theme_mode = 'light'
        self.page.title = 'Stranly Bakery'
        self.page.vertical_alignment = 'center'
        self.page.horizontal_alignment = 'center'

        # Presenter
        model = AuthenticationModel()
        self.presenter = LoginPresenter(self, model)

        # Fields
        self.user_name = ft.TextField(
            label="Username",
            width=400,
            autofocus=True,
            prefix_icon=ft.Icons.PERSON
        )
        self.password = ft.TextField(
            label='Password',
            width=400,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK
        )

        # Buttons
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

        # Layout
        self.page.add(
            self.user_name,
            self.password,
            self.btn_login,
            self.btn_forgot_password
        )

    # Methods
    def on_login(self, e):
        username = self.user_name.value.strip()
        password = self.password.value.strip()
        self.presenter.handle_login(username, password)

    def on_forgot_password(self, e):
        username = self.user_name.value.strip()
        self.presenter.handle_forgot_password(username)

    def show_message(self, text):
        print(text)
        self.page.snack_bar = ft.SnackBar(content=ft.Text(text))
        self.page.snack_bar.open = True
        self.page.update()
