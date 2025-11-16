"""
Módulo principal para concatenar cada N-ésimo carácter maiúsculo de um texto.

"""

# src/nth_upper.py

def nth_upper(text: str, n: int) -> str:
    """
    Retorna cada N-ésimo carácter maiúsculo do texto.
    Implementação mínima inicial para passar o primeiro teste (N=1).
    """
    
    if n <= 0 or not text:
        return ""
    
    result = []
    for i in range(n-1, len(text), n):  # começa na posição N-1 e pula N cada vez
        if text[i].isupper():
            result.append(text[i])

    return "".join(result)

