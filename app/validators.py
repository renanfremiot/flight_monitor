def somente_letras(texto: str) -> bool:
    return texto.replace(" ", "").isalpha()


def somente_numeros(texto: str) -> bool:
    return texto.isdigit()
