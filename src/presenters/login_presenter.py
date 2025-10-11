class LoginPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handle_login(self, username, password):
        if self.model.authenticate_user(username, password):
            self.view.show_message("Login exitoso!")
            self.view.go_to_main_view()
        else:
            self.view.show_message("Usuario o contraseña incorrectos")

    def handle_forgot_password(self, username):
        if self.model.authenticate_only_user(username):
            self.view.go_to_forgot_password_view()
        else:
            self.view.show_message("Ingresa tu usuario")
