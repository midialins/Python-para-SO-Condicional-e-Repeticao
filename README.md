# Python para SO - Condicional e Repetição

Atividade prática da disciplina de Sistemas Operacionais

## Parte 1 - Exercícios em Python

Desenvolvimento dos exercícios propostos utilizando estruturas condicionais e de repetição em Python.

Os exercícios trabalham conceitos como:

- Estruturas condicionais (`if`, `elif` e `else`)
- Estruturas de repetição (`for` e `while`)
- Operadores aritméticos e relacionais
- Cálculo de fatorial
- Sequência de Fibonacci
- Números primos
- Séries numéricas
- Cálculos matemáticos diversos

Foram realizados os exercícios da lista entre 18 e 45, conforme o material fornecido.

## Parte 2 - Docker

Criação de um contêiner a partir da imagem `python:3.10.20`, com mapeamento da pasta dos projetos da Parte 1 para o contêiner.

### Criação do contêiner

```bash
sudo docker run -dit --name python310 -v "$(pwd):/app" -w /app python:3.10.20 bash
```

### Execução da aplicação

Para testar o funcionamento do contêiner foi utilizado o programa `primo.py`.

```bash
sudo docker exec -it python310 python primo.py
```

Exemplo de execução:

```text
Digite um número inteiro: 7
O número é primo
```

## Evidências

Foram adicionados ao repositório os registros da criação do contêiner e da execução da aplicação dentro do Docker.
