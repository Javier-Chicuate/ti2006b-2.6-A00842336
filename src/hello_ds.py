"""Calcula la venta diaria promedio de una tabla pequeña y sintética."""

import pandas as pd


def main():
    # Datos inventados para practicar; no representan un negocio real.
    ventas = pd.DataFrame({
        "dia": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
        "unidades": [12, 15, 9, 18, 16],
    })
    promedio = ventas["unidades"].mean()
    print(f"Promedio diario de ventas (datos sintéticos): {promedio:.2f} unidades")


if __name__ == "__main__":
    main()
