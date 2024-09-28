Alunos: Bel Cogo, Bruno Hoffmann, João V. Accorsi e Rafael Klauck.

Disciplina: Teoria da Informação: Compressão e Criptografia.

Professor: Elvandi da Silva Junior

# Trabalho GA - Teoria da Informação: Compressão e Criptografia

## Objetivo do Trabalho
O objetivo do trabalho consite em fazer uma interface onde o usuário possa fazer a codificação e decodificação de símbolos usando os algoritmos:
- Golomb
- Elias-Gamma
- Fibonacci/Zeckendorf
- Huffman

A partir disso, o usuário seleciona se deseja fazer a codificação ou decodificação, além de qual algoritmos que deseja executar.

## Como executar a interface

Para executar a interface visual, é necessário executar o comando abaixo:

```shell
python main.py
```

## Como executar os testes de unidade

Para executar todos os testes de unidade, é necessário executar o comando abaixo:
```shell
python -m unittest discover -s tests -v
```

Além disso, é possível executar os testes de um módulo específico, executando o comando:

```shell
python -m unittest tests/<<arquivo-teste>>.py
```

## Estrutura

A estrutura do projeto consiste em uma pasta `src` contendo todos os arquivos relacionados aos algoritmos para realizar a codificação e decodificação. Uma pasta `tests` contendo os testes de unidade para validar os fluxos desenvolvidos. Um arquivo `main.py` contendo o código para gerar as interfaces visuais, como também as chamadas dos algoritmos.

Visão da árvore de arquivos:
- `src`: contém arquivos dos sistema.
  - `fibonacci`: codificação de fibonacci.
  - `parser`: helper para fazer a conversão de símbolos para ASCII.
- `tests`: contém arquivos de testes do sistema.
  - `test_fibonacci`: testes da codificação de fibonacci.
  - `test_parser`: testes da codificação do parser.