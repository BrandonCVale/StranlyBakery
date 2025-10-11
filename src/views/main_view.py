import flet as ft
from src.views.principal_view import PrincipalInterface
from src.views.inventario_view import InventarioView
from src.views.ventas_view import VentasView
from src.views.finanzas_view import FinanzasView
from src.views.proveedores_view import ProveedoresView
from src.views.clientes_view import ClientesView
from src.views.configuracion_view import ConfiguracionView
from src.presenters.side_menu_presenter import SideMenuPresenter


class SideMenuView(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)  # Container occupies all the page
        self.page = page

        # --- MVP ---
        self.presenter = SideMenuPresenter(self)

        # ----- 1. CONTROLS -----
        # --- Side Menu with NavigationRail inside a Container ---
        self.menu = ft.NavigationRail(
            selected_index=0,  # start selecting the 1st option in the menu
            label_type=ft.NavigationRailLabelType.ALL,  # Handle how the labels are shown, eg:all, selected, none
            extended=False,  # If we define as True, it will show the next format:icon + txt
            min_width=100,
            min_extended_width=200,
            expand=True,
            # list of the menu options
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.Icons.HOME_OUTLINED,  # Icon when is not selected
                    selected_icon=ft.Icons.HOME,  # Icon when is selected (principal color)
                    label="Principal"
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.INVENTORY_SHARP,
                    selected_icon=ft.Icons.INVENTORY_SHARP,
                    label="Inventario"
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.INVENTORY_2_OUTLINED,
                    selected_icon=ft.Icons.INVENTORY_2,
                    label="Ventas"
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.ACCOUNT_BALANCE_WALLET_OUTLINED,
                    selected_icon=ft.Icons.ACCOUNT_BALANCE_WALLET,
                    label="Finanzas"
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.LOCAL_SHIPPING_OUTLINED,
                    selected_icon=ft.Icons.LOCAL_SHIPPING,
                    label="Proveedores"
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.PEOPLE_OUTLINED,
                    selected_icon=ft.Icons.PEOPLE,
                    label="Clientes"
                ),
                ft.NavigationRailDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icons.SETTINGS,
                    label="Configuración"
                ),
            ], on_change=self.handle_navigation
        )
        # --- Divider ---
        self.divider = ft.VerticalDivider(width=2)
        # --- Main Content ---
        self.main_content = PrincipalInterface(self.page)

        # ----- 2. CONTAINERS -----
        # Cambia a self porque este hereda de Container
        self.menu_container = ft.Container(
            content=self.menu,
            expand=False,
            height=self.page.height
        )
        self.divider_container = ft.Container(
            content=self.divider
        )
        self.main_content_container = ft.Container(
            content=self.main_content,
            expand=True
        )

        # --- Layout ---
        self.content = ft.Row(
            expand=True,
            controls=[self.menu_container, self.divider_container, self.main_content_container]
        )

    # Methods
    def handle_navigation(self, e: ft.ControlEvent):
        selected_index = e.control.selected_index
        selected_label = e.control.destinations[selected_index].label

        views = {
            "Principal": PrincipalInterface,
            "Inventario": InventarioView,
            "Ventas": VentasView,
            "Finanzas": FinanzasView,
            "Proveedores": ProveedoresView,
            "Clientes": ClientesView,
            "Configuración": ConfiguracionView
        }

        if selected_label in views:
            # Crear nueva vista
            new_view = views[selected_label](self.page)

            # Reemplazar el contenido visible
            self.main_content_container.content = new_view

            # Actualizar vista
            self.update()
