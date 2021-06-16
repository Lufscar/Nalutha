# Documentação dos comandos utilizados

Dentro da pasta do projeto, rodar os seguintes comandos:

## Compilar a linguagem

```
antlr4 -Dlanguage=Python3 Nalutha.g4
```

## Compilar a linguagem com visitor

```
antlr4 -Dlanguage=Python3 -visitor Nalutha.g4
```

## Instalar os requirements
```
pip install -r requirements.txt
```

## Rodar o código teste como entrada

```
python3 Nalutha.py codigo <nome_projeto>
```
