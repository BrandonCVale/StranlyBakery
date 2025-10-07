import flet as ft


class ClientesView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True, spacing=20)
        self.page = page

        # ----- 1. CONTROLS -----
        # --- Header ---
        # --- SearchBar Cliente ---
        self.buscar_cliente = ft.TextField(
            label="Buscar cliente",
            width=500,
            prefix_icon=ft.Icons.SEARCH
        )
        # --- Btn add cliente ---
        self.btn_add_cliente = ft.ElevatedButton(
            text="Agregar cliente",
            icon=ft.Icons.ADD
        )
        # --- Btn editar cliente ---
        self.btn_edit_cliente = ft.ElevatedButton(
            text="Editar cliente",
            icon=ft.Icons.AUTORENEW
        )
        # --- Btn eliminar cliente ---
        self.btn_delete_cliente = ft.ElevatedButton(
            text="Eliminar cliente",
            icon=ft.Icons.DELETE
        )

        # --- Body ---
        # --- Tbl clientes ---
        self.tbl_clientes = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(value="ID")),
                ft.DataColumn(ft.Text(value="Cliente")),
                ft.DataColumn(ft.Text(value="Email")),
                ft.DataColumn(ft.Text(value="Telefono")),
                ft.DataColumn(ft.Text(value="Direccion"))
            ],
            rows=[]
        )

        # ----- 2. CONTAINERS -----
        header_container = ft.Row(
            controls=[self.buscar_cliente, self.btn_add_cliente, self.btn_edit_cliente,
                      self.btn_delete_cliente],
            alignment=ft.MainAxisAlignment.START,
            spacing=20
        )
        body_container = ft.Container(
            content=self.tbl_clientes,
            expand=True,
            width=self.page.width,
            border_radius=10,
            padding=10
        )

        # ----- 3. LAYOUT -----
        self.controls = [
            header_container,
            body_container
        ]
