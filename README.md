# ShopTree – Modernização Arquitetural

## 1. Descrição do Projeto

O ShopTree é uma plataforma de e-commerce responsável pelo catálogo de produtos, realização de compras e processamento de pagamentos.

O projeto apresenta uma proposta de modernização arquitetural baseada na separação de responsabilidades em serviços independentes e na utilização de comunicação orientada a eventos.

A arquitetura proposta busca reduzir o acoplamento entre os componentes, facilitar a manutenção e permitir maior escalabilidade da plataforma.

## 2. Objetivo

O objetivo do projeto é demonstrar, por meio de uma prova de conceito, como a plataforma ShopTree pode ser modernizada utilizando uma arquitetura baseada em serviços independentes e comunicação orientada a eventos.

## 3. Arquitetura

A solução foi organizada nos seguintes componentes:

- Serviço de Produtos;
- Serviço de Pagamentos;
- Simulação de Eventos;
- Serviço de Notificações.

O relacionamento entre os componentes é apresentado nos diagramas arquiteturais desenvolvidos utilizando Structurizr DSL.

### Visão de Contexto

A visão de contexto apresenta o relacionamento entre o cliente e a plataforma ShopTree.

### Visão de Containers

A visão de containers apresenta a divisão da plataforma em serviços independentes e o fluxo de comunicação entre eles.

## 4.  Tecnologias e Conceitos Utilizados

- Python
- FastAPI
- Structurizr DSL
- Visual Studio Code
- Arquitetura Orientada a Eventos
- Design Pattern Observer

## 5. Comunicação Orientada a Eventos

O projeto utiliza uma simulação de comunicação orientada a eventos.

O fluxo implementado ocorre da seguinte maneira:

1. Uma compra gera um evento;
2. O evento é recebido pelo serviço de pagamentos;
3. O pagamento é processado;
4. O evento também é recebido pelo serviço de notificações;
5. Uma notificação é gerada para o cliente.

## 6. Design Pattern Observer

O padrão comportamental Observer foi utilizado na simulação da arquitetura orientada a eventos.

Nesse modelo, um produtor publica um evento e diferentes consumidores podem receber esse evento e executar suas próprias ações.

No projeto, o serviço de pagamentos e o serviço de notificações funcionam como consumidores independentes do evento de compra.

## 7. Serviços Implementados

### Serviço de Produtos

Responsável pelo catálogo e gerenciamento dos produtos.

### Serviço de Pagamentos

Responsável pelo processamento e gerenciamento dos pagamentos.

### Simulação de Eventos

Responsável pela publicação e distribuição dos eventos de compra.

### Serviço de Notificações

Responsável por consumir eventos e gerar notificações relacionadas às compras.

## 8. Execução da Prova de Conceito

A prova de conceito foi executada utilizando Python.

Durante a execução, foi possível observar:

- publicação do evento de compra;
- recebimento do evento pelo serviço de pagamentos;
- processamento do pagamento;
- recebimento do evento pelo serviço de notificações;
- geração da notificação ao cliente.

## 9. Decisão Arquitetural

A decisão arquitetural está documentada no arquivo:

`docs/ADR-001-decisao-arquitetural.md`

A decisão adotada foi utilizar serviços independentes combinados com princípios de arquitetura orientada a eventos.

## 10. Estrutura do Projeto


por este:

```text
SHOOPTREE/
├── architecture/
│   ├── .gitignore.txt
│   └── workspace.dsl
│
├── docs/
│   └── ADR-001-decisao-arquitetural.md
│
├── events/
│   ├── event_simulation.py
│   └── observer.py
│
├── services/
│   ├── payment_service/
│   │   └── main.py
│   │
│   └── product_service/
│       ├── main.py
│       └── schemas.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 11. Como Executar o Projeto

### 11.1 Pré-requisitos

Para executar o projeto, é necessário ter instalado:

- Python 3.10 ou superior;
- Git;
- Visual Studio Code (opcional).

### 11.2 Clonar o Repositório

```bash
git clone https://github.com/Charles-kendy/ShoopTree.git
cd ShoopTree
```
### 11.3 Instalar as Dependências

Com o projeto aberto no terminal, instale as dependências utilizando:

```bash
pip install -r requirements.txt
```
### 11.4 Executar o Projeto

Após a instalação das dependências, execute a prova de conceito com:

```bash
python events/event_simulation.py
```

### 11.5 Resultado da Execução

Ao executar a prova de conceito, o sistema simula o fluxo de uma compra e a comunicação entre os serviços.

Durante a execução, é possível acompanhar:

- geração do evento de compra;
- recebimento do evento pelo serviço de pagamentos;
- processamento do pagamento;
- recebimento do evento pelo serviço de notificações;
- geração da notificação ao cliente.

Esse fluxo demonstra, de forma simplificada, como os serviços podem trabalhar de maneira independente utilizando comunicação orientada a eventos.


## 12. Conclusão

O projeto ShopTree apresenta uma proposta de modernização arquitetural baseada na separação de responsabilidades e na comunicação orientada a eventos.

A prova de conceito permitiu demonstrar, de forma prática, como os serviços de produtos, pagamentos e notificações podem trabalhar de maneira independente, reduzindo o acoplamento entre os componentes.

A solução também facilita futuras evoluções da plataforma, permitindo que novos serviços sejam adicionados sem exigir grandes alterações nos componentes existentes.