# Python para SO - Condicional e Repetição

Atividade prática de Sistemas Operacionais utilizando Python e Docker.

## Objetivo

Criar um contêiner a partir da imagem `python:3.10.20`, mapear a pasta do projeto do hospedeiro para o contêiner e executar uma aplicação Python dentro dele.

## Programa utilizado

O arquivo `primo.py` solicita um número inteiro e verifica se ele é primo.

## Criação do contêiner

```bash
sudo docker run -dit --name python310 -v "$(pwd):/app" -w /app python:3.10.20 bash
```

## Execução da aplicação no contêiner

```bash
sudo docker exec -it python310 python primo.py
```

Exemplo de execução:

```text
Digite um numero inteiro: 7
O numero e primo
```

## Evidências

- Criação do contêiner Python 3.10.20 com mapeamento do volume.
- Execução do programa `primo.py` dentro do contêiner Docker.
