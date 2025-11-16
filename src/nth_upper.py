"""
Módulo principal para concatenar cada N-ésimo carácter maiúsculo de um texto.

"""


def nth_upper(text: str, n: int) -> str:
    """
    Retorna cada N-ésimo carácter maiúsculo do texto.
    Implementação mínima inicial para passar o primeiro teste (N=1).
    """
    
    if n < 1:
        raise ValueError("N must be >= 1")
    
    result = []
    for i in range(n-1, len(text), n):  # começa na posição N-1 e pula N cada vez
        if text[i].isupper():
            result.append(text[i])

    return "".join(result)

