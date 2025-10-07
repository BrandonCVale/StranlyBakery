class FinanzasPresenter:

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def handle_fecha_seleccionada(self, e):
        fecha = e.control.value  # datetime.date
        if fecha:
            datos = self.model.obtener_datos_por_fecha(fecha)
            self.view.actualizar_datos(datos)
