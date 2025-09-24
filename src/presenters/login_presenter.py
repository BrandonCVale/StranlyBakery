class LoginPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handle_login(self, username, password):
        if self.model.authenticate_user(username, password):
            self.view.show_message("✅ Login exitoso")
        else:
            self.view.show_message("❌ Usuario o contraseña incorrectos")

    def handle_forgot_password(self, username):
        self.view.show_message("🔑 Funcionalidad en construcción")
