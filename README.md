Alunos: Bel Cogo, Bruno Hoffmann, João V. Accorsi e Rafael Klauck.

Disciplina: Teoria da Informação: Compressão e Criptografia.

Professor: Elvandi da Silva Junior.

# Trabalho GB - Prático - Teoria da Informação: Compressão e Criptografia

## Objetivo do Trabalho
O objetivo do trabalho consite em fazer uma interface onde o usuário possa fazer a codificação, a decodificação, a verificação e correção de erros, de símbolos usando os algoritmos:
- Hamming;
- Repetição Ri;

A partir disso, o usuário seleciona se deseja fazer a codificação ou decodificação, além de qual algoritmos que deseja executar.

## Requisitos para executar
- Ter python instalado na máquina;
- Ter a biblioteca streamlit instalada: `pip install streamlit` 

## Como executar a interface

Para executar a interface visual, é necessário executar o comando abaixo:

```shell
streamlit run app.py
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