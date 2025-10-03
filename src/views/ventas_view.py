import flet as ft


# VentasInterface(Column, expand=True)
# │
# ├── Header(Row)
# │   ├── SelectorCliente(Dropdown, prefixIcon)
# │   ├── AddButton(Button +)
# │
# ├── Body(Row)
# │   └── Tabla_Productos_Disponibles(Container, DataTable)
# |   └── Ticket(Container, Card)
# |         └──Compartir_comprobante(ElevatedButton)


class VentasView(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True, spacing=20)
        self.page = page

        # ----- CONTROLS -----
        # --- Header ---
        self.selector_cliente = ft.Dropdown(
            label='Selecciona el cliente',
            width=300,
            options=[]  # It will be getting with the db
        )
        # --- Btn Anadir Venta ---
        self.btn_register_sale = ft.ElevatedButton(
            text="Registrar venta",
            icon=ft.Icons.ADD_BOX,
            # on_click=
        )
        # --- Btn Cancelar Venta ---
        self.btn_cancel_sale = ft.ElevatedButton(
            text='Cancelar Operacion',
            icon=ft.Icons.CANCEL_OUTLINED,
            # on_click=
        )
        # --- Btn editar pedido ---
        self.btn_update_order = ft.ElevatedButton(
            text="Editar orden",
            icon=ft.Icons.AUTORENEW
        )

        # ----- Body ------
        # --- Table Productos Disponibles----
        self.products = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text(value='ID')),
                ft.DataColumn(ft.Text(value='Producto')),
                ft.DataColumn(ft.Text(value='Stock')),
                ft.DataColumn(ft.Text(value='Precio'))
            ],
            rows=[]
        )
        # --- Btn Share ticket ---
        self.btn_share_ticket = ft.ElevatedButton(
            icon=ft.Icons.SHARE,
            text='Compartir ticket',
            # on_click=
        )
        # --- Ticket Card ---
        self.ticket = ft.Card(
            content=ft.Container(
                ft.Column(
                    controls=[
                        ft.Text(value="Ticket de: ...", size=20),
                        # metodo que muestre el resumen de la orden
                        self.btn_share_ticket
                    ]
                )
            )
        )

        # ----- CONTAINERS -----
        header = ft.Row(
            controls=[
                self.selector_cliente, self.btn_register_sale,
                self.btn_update_order, self.btn_cancel_sale
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20
        )

        body = ft.Row(
            controls=[
                ft.Container(
                    content=self.products,
                    expand=True,
                    border_radius=10,
                    padding=10
                ),

                self.ticket
            ]
        )

        # ----- LAYOUT PRINCIPAL -----
        self.controls = [
            header,
            body
        ]
