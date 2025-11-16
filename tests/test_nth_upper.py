"""
Testes para a função nth_upper presente no módulo src/nth_upper.py

"""

import sys
import os

# Adiciona a pasta src ao path para conseguir importar o módulo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from nth_upper import nth_upper  # importa a função que vamos criar

def test_nth_upper_n1():
    """
    Teste TDD: N = 1, deve retornar todas as maiúsculas do texto
    """
    text = "ITCLiNicAl"
    n = 1
    expected = "ITCLNA"
    assert nth_upper(text, n) == expected


def test_nth_upper_n2():
    """
    Teste TDD: N = 2, deve retornar cada 2º carácter maiúsculo do texto
    """
    text = "ITCLiNicAl"
    n = 2
    expected = "TLN"
    assert nth_upper(text, n) == expected


