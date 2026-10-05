"""Presupuesto de tienda: cálculo de subtotal, IVA y total."""

# La constante del IVA. Se escribe en MAYÚSCULAS porque no debe cambiar.
IVA: int = 21


def a_entero(texto: str) -> int:
    """Convierte un texto a número entero."""
    # TODO: input() devuelve texto; conviértelo a int
    raise NotImplementedError


def a_decimal(texto: str) -> float:
    """Convierte un texto a número decimal."""
    # TODO
    raise NotImplementedError


def calcular_subtotal(unidades: int, precio: float) -> float:
    """Importe antes de impuestos."""
    # TODO
    raise NotImplementedError


def calcular_iva(subtotal: float) -> float:
    """Importe del IVA sobre el subtotal."""
    # TODO: aplica el porcentaje de la constante IVA
    raise NotImplementedError


def formatear_importe(etiqueta: str, valor: float) -> str:
    """Devuelve una línea del tipo  'Subtotal: 30.00 €'  (2 decimales)."""
    # TODO: usa una f-string con :.2f
    raise NotImplementedError


def main() -> None:
    """Programa principal: lee, calcula y muestra."""
    unidades = a_entero(input())
    precio = a_decimal(input())
    subtotal = calcular_subtotal(unidades, precio)
    iva = calcular_iva(subtotal)
    print(formatear_importe("Subtotal", subtotal))
    print(formatear_importe(f"IVA ({IVA}%)", iva))
    print(formatear_importe("Total", subtotal + iva))


if __name__ == "__main__":
    main()
