# Desafio ITClinical
Este projeto foi desenvolvido como resposta ao desafio técnico proposto pela ITClinical, utilizando uma abordagem Test-Driven Development (TDD) em Python.


## Objetivo do Desafio
Implementar uma função que, dado um texto e um valor N, devolve todos os caracteres maiúsculos que surgem a cada N posições no texto.

Exemplos:
| Texto        | N   | Resultado         |
| ------------ | --- | ----------------- |
| `ITCLiNicAl` | 1   | `ITCLNA`          |
| `ITCLiNicAl` | 2   | `TLN`             |
| `ITCLiNicAl` | 3   | `CNA`             |
| `ITCLiNicAl` | 100 | `` (vazio)        |
| `ITCLiNicAl` | -1  | erro (N inválido) |


## Abordagem: TDD (Test-Driven Development)
Este projeto segue as três fases fundamentais do TDD:

1. **Red**

   - Escrevem-se testes antes de existir código funcional.
   - O teste falha (como esperado).

2. **Green**

   - Escreve-se o código mínimo necessário para que os testes passem.
   - O foco aqui é funcionalidade, não otimização.

3. **Refactor**

   Melhorias ao código:
   - legibilidade  
   - clareza  
   - documentação  
   - simplificação  

   Os testes garantem que nada foi quebrado.
