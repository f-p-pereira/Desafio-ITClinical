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
    
    # Filtra todas as maiúsculas
    return "".join([c for c in text if c.isupper()])

