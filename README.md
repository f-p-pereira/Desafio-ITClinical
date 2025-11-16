# Desafio ITClinical

O desafio técnico proposto pela ITClinical, que consiste em:

- Criar um programa em Python que, dado um texto, retorna cada N-ésimo carácter maiúsculo.
- Utilizar **Test-Driven Development (TDD)** para desenvolver a solução.
- Tratar casos limite, como N ≤ 0, texto vazio ou N maior que o comprimento do texto.

Exemplo:
 - Texto = "ITCLiNicAl" and N = 1, the return value will be "ITCLNA";
 - Texto = "ITCLiNicAl" and N = 2, the return value will be "TLN";
 - Texto = "ITCLiNicAl" and N = 3, the return value will be "CNA";
 - Texto = "ITCLiNicAl" and N = 100, the return value will be ""; ==> N > len(Texto) = ""
 - Texto = "ITCLiNicAl" and N = -1, the return value will be "";

O objetivo deste projeto é demonstrar organização do código, testes unitários e boas práticas no uso de Git/GitHub.

## TDD (Test-Driven Development)

Este projeto segue a metodologia TDD (Test-Driven Development), que consiste em:

1. **Red**: Escrever testes que inicialmente falham, definindo o comportamento esperado.
2. **Green**: Implementar o código mínimo necessário para que os testes passem.
3. **Refactor**: Melhorar o código mantendo todos os testes a passar.

Vantagens desta abordagem incluem:
- Código confiável e menos propenso a bugs
- Design mais claro e modular
- Facilidade para refatorar sem medo de quebrar funcionalidades

No desenvolvimento deste desafio, cada funcionalidade da função `nth_upper` foi primeiro testada antes de ser implementada.
