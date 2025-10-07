import flet as ft


class ProveedoresView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True, spacing=20)
        self.page = page

        # ----- 1. CONTROLS -----
        # --- HEADER ---
        # --- SearchBar ---
        self.buscar_proveedor = ft.TextField(
            label="Buscar proveedor",
            width=500,
            prefix_icon=ft.Icons.SEARCH)
        # --- Btn add proveedor ---
        self.btn_add_proveedor = ft.ElevatedButton(
            text="Agregar proveedor",
            icon=ft.Icons.ADD
        )
        # --- Btn editar proveedor ---
        self.btn_edit_proveedor = ft.ElevatedButton(
            text="Editar proveedor",
            icon=ft.Icons.AUTORENEW
        )
        # --- Btn eliminar proveedor ---
        self.btn_delete_proveedor = ft.ElevatedButton(
            text="Eliminar proveedor",
            icon=ft.Icons.DELETE
        )

        # --- BODY ---
        self.tbl_proveedores = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(value="ID")),
                ft.DataColumn(ft.Text(value="Proveedor")),
                ft.DataColumn(ft.Text(value="Email")),
                ft.DataColumn(ft.Text(value="Telefono")),
                ft.DataColumn(ft.Text(value="Direccion"))
            ],
            rows=[]
        )

        # ----- 2. CONTAINER -----
        header_container = ft.Row(
            controls=[self.buscar_proveedor, self.btn_add_proveedor, self.btn_edit_proveedor,
                      self.btn_delete_proveedor],
            alignment=ft.MainAxisAlignment.START,
            spacing=20
        )
        body_container = ft.Container(
            content=self.tbl_proveedores,
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
