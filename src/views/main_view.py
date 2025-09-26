import flet as ft
from src.views.principal_view import PrincipalInterface


class SideMenuView(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.page.theme_mode = 'light'

        # --- Side Menu with NavigationRail ---
        self.nav = ft.NavigationRail(
            selected_index=0,  # start selecting the 1st option in the menu
            label_type=ft.NavigationRailLabelType.ALL,  # Handle how the labels are shown, eg:all, selected, none
            extended=False,  # If we define as True, will show the next format:icon + txt
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
            ],
            on_change=self.handle_navigation
        )

        # --- Main Content ---
        self.main_content = ft.Column(
            controls=[
                PrincipalInterface(self.page)
            ], expand=True
        )

        # --- Layout ---
        self.content = ft.Row(
            expand=True,
            controls=[
                ft.Container(self.nav, height=self.page.height), # or instead of height, expand = True
                ft.VerticalDivider(width=1),
                self.main_content
            ]
        )

    # Methods
    def handle_navigation(self, e: ft.ControlEvent):
        selected_index = e.control.selected_index
        selected_label = self.nav.destinations[selected_index].label

        views = {
            "Principal": PrincipalInterface
            # "Inventario": class
        }

        self.main_content.controls = [views[selected_label](self.page)]
        self.update()
