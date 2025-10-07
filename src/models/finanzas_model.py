import io
import base64
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import date
from src.database.connection import get_connection


class FinanzasModel:

    def obtener_datos_por_fecha(self, fecha: date):
        conn = get_connection()
        cur = conn.cursor()

        # Ingresos del día
        cur.execute("""
            SELECT COALESCE(SUM(total), 0)
            FROM ventas_2025.ventas_principal
            WHERE DATE(fecha) = %s;
        """, (fecha,))
        ingresos = cur.fetchone()[0]

        # Egresos del día
        cur.execute("""
            SELECT COALESCE(SUM(cantidad * precio_unitario), 0)
            FROM ventas_2025.compras_a_proveedores
            WHERE DATE(fecha_compra) = %s;
        """, (fecha,))
        egresos = cur.fetchone()[0]

        cur.close()
        conn.close()

        balance = ingresos - egresos

        # Grafico
        grafico_base_64 = self.generar_grafico(ingresos, egresos, fecha)

        return {
            "fecha": fecha.strftime("%d/%m/%Y"),
            "ingresos": ingresos,
            "egresos": egresos,
            "balance": balance,
            "grafico": grafico_base_64
        }

    def generar_grafico(self, ingresos, egresos, fecha):
        data = pd.DataFrame({
            "Categoria": ["Ingresos", "Egresos"],
            "Monto": [ingresos, egresos]
        })

        ax = sns.barplot(
            data=data,
            x="Categoria",
            y="Monto"
        )

        plt.title(f"Ingresos vs Egresos ({fecha.strftime('%d/%m/%Y')})")
        plt.ylabel("Monto ($)")
        plt.tight_layout()

        # Convertir la figura a base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format="png")
        plt.close()
        data64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        buffer.close()

        return f"data:image/png;base64,{data64}"
