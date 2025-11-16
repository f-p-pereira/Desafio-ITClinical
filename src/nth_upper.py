"""
Módulo principal para concatenar cada N-ésimo carácter maiúsculo de um texto.

"""


def nth_upper(text: str, n: int) -> str:
    """
    Devolve todos os caracteres maiúsculos que surgem a cada N posições no texto.

    A função percorre o texto da esquerda para a direita e devolve apenas
    os caracteres que:
      - estejam numa posição múltipla de N (contagem iniciada em 1)
      - sejam letras maiúsculas

    Args:
        text (str): Texto de entrada.
        n (int): Intervalo de seleção. Deve ser um número inteiro >= 1.

    Returns:
        str: Uma string contendo os caracteres maiúsculos selecionados.

    Raises:
        ValueError: Se n for menor do que 1.

    Exemplos:
        >>> nth_upper("ITCLiNicAl", 1)
        'ITCLNA'
        >>> nth_upper("ITCLiNicAl", 2)
        'TLN'
        >>> nth_upper("ITCLiNicAl", 3)
        'CNA'
    """
    
    if n < 1:
        raise ValueError("N tem de ser ≥ 1")
    
    result = [
        char
        for index, char in enumerate(text, start=1)
        if index % n == 0 and char.isupper()
    ]

    return "".join(result)

