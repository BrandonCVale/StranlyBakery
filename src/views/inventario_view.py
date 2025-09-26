import flet as ft


# import future model
# import future presenter

class InventarioView(ft.Column):
    # InventarioInterface(Column, expand=True)
    # │
    # ├── SearchBar_Row(Row)
    # │   ├── SearchIcon(Icon)
    # │   ├── SearchField(TextField)
    # │   ├── AddButton(Button +)
    # │   └── RemoveButton(Button -)
    # │
    # ├── Table_Container(Container
    # o
    # Card)
    # │   └── DataTable(Tabla
    # inventario)
    # │
    # └── Alerts_Column(Column)
    # ├── Text("Alertas:")
    # ├── Row(Icon + Text("Bajo stock de: Huevos"))
    # └── Row(Icon + Text("Bajo stock de: Flanes"))

    def __init__(self, page: ft.Page):
        super().__init__(expand=True, spacing=20)
        self.page = page

        # ----- CONTROLS -----
        # --- Search Bar ---
        self.search_field = ft.TextField(
            label='Buscar producto...',
            width=700,
            prefix_icon=ft.Icons.SEARCH
        )
        # --- Btn add ---
        self.btn_add = ft.IconButton(
            icon=ft.Icons.ADD_BOX,
            tooltip="Agregar producto"
        )
        # --- Btn remove ---
        self.btn_remove = ft.IconButton(
            icon=ft.Icons.REMOVE_CIRCLE,
            tooltip='Eliminar producto'
        )
        # --- Btn update ---
        self.btn_update = ft.IconButton(
            icon=ft.Icons.AUTORENEW,
            tooltip='Actualizar producto'
        )
        # --- Inventory table ---
        self.inventory_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(value='ID')),
                ft.DataColumn(ft.Text(value='Producto')),
                ft.DataColumn(ft.Text(value='Stock')),
                ft.DataColumn(ft.Text(value='Precio'))
            ],
            rows=[]
        )

        # ----- CONTAINERS -----
        # --- Search Bar ---
        search_bar = ft.Row(
            controls=[self.search_field,
                      ft.Column(controls=[self.btn_add, ft.Text('Agregar producto', size=12)],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                      ft.Column(controls=[self.btn_update, ft.Text('Actualizar producto', size=12)],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                      ft.Column(controls=[self.btn_remove, ft.Text('Eliminar producto', size=12)],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                      ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20
        )
        # --- Table ---
        table_container = ft.Container(
            content=self.inventory_table,
            expand=True,
            width=self.page.width,
            border_radius=10,
            bgcolor="#DCE0D9",
            padding=10
        )
        # --- Alerts ---
        alerts = ft.Column(
            controls=[ft.Text(value="Alertas:", size=16),
                      ft.Row(controls=[ft.Icon(ft.Icons.WARNING, color='orange'), ft.Text(value='Bajo stock de: ...')]),
                      ft.Row(controls=[ft.Icon(ft.Icons.WARNING, color='orange'), ft.Text(value='Bajo stock de: ...')]),
                      ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START
        )

        # ----- LAYOUT PRINCIPAL -----
        self.controls = [
            search_bar,
            table_container,
            alerts
        ]
