import flet as ft


class ConfiguracionView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True, spacing=20)
        self.page = page

        # ----- 1. CONTROLS -----
        # --- Header ---
        self.titulo_principal = ft.Text(value="Configuracion", size=20)
        # --- Btns de accion ---
        self.btn_editar = ft.ElevatedButton(
            text="Editar",
            icon=ft.Icons.EDIT,
            tooltip="Editar información"
        )

        self.btn_guardar = ft.ElevatedButton(
            text="Guardar",
            icon=ft.Icons.SAVE,
            tooltip="Guardar cambios"
        )

        self.btn_cancelar = ft.ElevatedButton(
            text="Cancelar",
            icon=ft.Icons.CANCEL,
            tooltip="Cancelar edición"
        )

        # --- Body ---
        # Nombre del negocio
        self.nombre_negocio = ft.Text("Nombre del Negocio")
        self.valor_nombre_negocio = ft.Text("Stranly Bakery")

        # Logotipo
        self.logotipo = ft.Text("Logotipo:")
        self.icono_logotipo = ft.Icon(ft.Icons.IMAGE_OUTLINED, size=80, color=ft.Colors.GREY)

        # Apariencia
        self.apariencia = ft.Text("Apariencia:")
        self.valor_apariencia = ft.Text("Modo claro")

        # Dirección
        self.direccion = ft.Text("Dirección:")
        self.valor_direccion = ft.Text("#Calle dulce 3")

        # ----- 2. CONTAINERS -----
        header_container = ft.Row(
            controls=[self.titulo_principal, self.btn_editar],
            alignment=ft.MainAxisAlignment.START
        )
        body_container = ft.Column(
            controls=[
                ft.Row(controls=[self.nombre_negocio, self.valor_nombre_negocio], spacing=10),
                ft.Row(controls=[self.logotipo, self.icono_logotipo], spacing=10),
                ft.Row(controls=[self.apariencia, self.valor_apariencia], spacing=10),
                ft.Row(controls=[self.direccion, self.valor_direccion], spacing=10)
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=30
        )
        logotipo_container = ft.Container(
            content=ft.Column(
                controls=[self.icono_logotipo],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor="#FBFEFB",
            border_radius=10,
            padding=10,
            expand=False
        )

        # ----- 3. LAYOUT -----
        self.controls = [
            header_container,
            body_container
        ]
