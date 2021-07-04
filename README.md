# Nalutha

Repositório destinado ao desenvolvimento da Nalutha - uma linguagem simplificada para bancos de dados relacionais, com comandos em português-brasileiro. A Nalutha está sendo projetada por Luciana Souza @lufscar, Natasha Graifman @natashagraifman e Thaís Dordan @thagd, com orientação do professor Daniel Lucrédio @dlucredio

## Objetivo

A linguagem desenvolvida neste projeto foi feita para facilitar o desenvolvimento de uma API utilizando a linguagem Python e Django Rest Framework, gerando todo o projeto do banco de dados e vinculando o admin do Django com a API. Tudo isso, seguindo boas práticas de programação.

Para os que não tiveram contato com essas tecnologias ainda, vem aprender um pouquinho o que são!

### O que é Django?

O Django é um framework gratuito e de código aberto escrito em Python para desenvolvimento web. Sua utilização permite a construção de aplicações web de alto desempenho.

_Para saber mais, acesse: [Introdução ao Django](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Introduction)_

### O que é API?

A sigla API deriva da expressão inglesa Application Programming Interface que, traduzida para o português, pode ser compreendida como uma interface de programação de aplicação. Ou seja, API é um conjunto de normas que possibilita a comunicação entre plataformas através de uma série de padrões e protocolos.

_Para saber mais, acesse: [Introdução às Web APIs](https://developer.mozilla.org/pt-BR/docs/Glossary/API)_

## Linguagem

A linguagem Nalutha tem como principal objetivo ser clara e fácil de utilizar. Temos basicamente 2 passos a serem seguidos para programar utilizando essa linguagem:

### Adicionar informações referentes a configuração do projeto gerado

O usuário precisa informar o nome do projeto que será gerado em Django e o nome da api desenvolvida:

```
Project: nome-projeto
Api name: nome-api
```

### Adicionar informações referentes a cada entidade da api

O usuário precisa informar a configuração da sua api, nome e tipo dos campos das entidades do banco dados. Temos como exemplo a crição de duas entidades: Game e Platform e de seus campos, respectivamente, name e publisher e name. Além disso temos que definir o tipo de cada campo, como por exemplo stringe number.

Para os tipos string ainda é possível adicionar a quantidade máxima de caracteres aceitas pelo banco utilizando [].

```
Model {

    Entity Game {
        name: string [20]
        publisher: string
    }

    Entity Platform {
        name: string [2]
    }

}
```

## Dependências

Como o projeto foi desenvolvido em python, vamos precisar da instalação do `python3`. Além disso, para instalar as outras dependênciais de forma mais fácil, vamos precisar instalar o `pip3`.

```
sudo apt install python3.8
sudo apt-get -y install python3-pip
```

Os programas necessários para o funcionamento do compilador estão listados no arquivo _requirements.txt_.

Para instalar todas as dependências a partir do arquivo:

```
pip3 install -r requirements.txt.
```

## Como utilizar

Temos um arquivo _Documentacao_ na pasta do projeto com **todos** os códigos que você vai precisar utilizar para compilar/rodar o código desenvolvido por você ou algum exemplo disponibilizado na pasta _casos-de-teste_ utilizando o compilador Nalutha.

## Próximas features

- [ ] Implementar Relações.
