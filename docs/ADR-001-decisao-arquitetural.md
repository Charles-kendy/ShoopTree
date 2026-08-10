# ADR-001 — Modernização Arquitetural da ShoopTree

## Status

Aceito

## Contexto

A ShoopTree foi inicialmente desenvolvida como uma aplicação monolítica,
concentrando em um único sistema funcionalidades como cadastro de usuários,
catálogo de produtos, carrinho de compras, processamento de pagamentos e
integrações com parceiros externos.

Com o crescimento da plataforma, o modelo monolítico passou a apresentar
limitações relacionadas à escalabilidade, manutenção, implantação e isolamento
de falhas.

Entre os principais problemas identificados estão:

- dificuldade para escalar funcionalidades específicas;
- aumento do tempo de implantação;
- possibilidade de falhas em um módulo afetarem todo o sistema;
- dificuldade de manutenção e evolução do código;
- crescimento desorganizado das integrações externas;
- baixa clareza sobre as responsabilidades dos componentes.

Diante desse cenário, tornou-se necessário propor uma arquitetura mais modular,
evolutiva e preparada para o crescimento da plataforma.

## Problema Arquitetural

Como modernizar a arquitetura da ShoopTree de forma que os principais
componentes possam evoluir e escalar de maneira independente, reduzindo o
acoplamento existente no modelo monolítico?

## Alternativas Avaliadas

### 1. Manter o Monólito

A primeira alternativa seria manter a arquitetura atual, realizando apenas
melhorias internas no código.

Essa abordagem apresenta menor complexidade inicial, porém mantém problemas
relacionados ao acoplamento entre funcionalidades e à dificuldade de escalar
componentes individualmente.

### 2. Monólito Modular

A segunda alternativa seria reorganizar o sistema monolítico em módulos bem
definidos, mantendo uma única aplicação.

Essa abordagem melhora a organização interna e reduz parte do acoplamento,
porém os módulos continuam compartilhando o mesmo processo de execução e
implantação.

### 3. Microsserviços com Comunicação Orientada a Eventos

A terceira alternativa consiste em separar funcionalidades importantes em
serviços independentes, utilizando APIs para comunicação síncrona e eventos
para comunicação assíncrona.

Essa abordagem permite maior independência entre os serviços, possibilitando
que cada componente evolua e seja escalado de acordo com suas necessidades.

## Decisão

Foi escolhida uma arquitetura baseada em **serviços independentes**, combinada
com princípios de **Arquitetura Orientada a Eventos**.

Para a prova de conceito foram definidos os seguintes componentes:

- Serviço de Produtos;
- Serviço de Pagamentos;
- Simulação de Eventos;
- Serviço de Notificações.

Os serviços de Produtos e Pagamentos foram implementados utilizando
Python e FastAPI.

A comunicação orientada a eventos foi simulada em Python por meio de classes
representando um produtor de eventos e consumidores.

O fluxo implementado consiste em:

1. uma compra gera um evento;
2. o evento é consumido pelo serviço de pagamentos;
3. o pagamento é processado;
4. o evento também é consumido pelo serviço de notificações;
5. uma notificação é gerada para o cliente.

## Justificativa Técnica

A arquitetura escolhida permite separar responsabilidades e reduzir o
acoplamento entre os componentes da plataforma.

O Serviço de Produtos fica responsável pelo catálogo e gerenciamento dos
produtos, enquanto o Serviço de Pagamentos concentra as operações relacionadas
a pagamentos.

A comunicação orientada a eventos permite que diferentes consumidores
reajam ao mesmo evento sem que o produtor precise conhecer diretamente todos
os componentes envolvidos.

Essa abordagem também facilita futuras evoluções da plataforma, permitindo
a substituição da simulação atual por uma tecnologia de mensageria, como
Apache Kafka, caso exista necessidade de maior escala.

## Consequências Positivas

- maior separação de responsabilidades;
- possibilidade de evolução independente dos serviços;
- melhor capacidade de escalabilidade;
- redução do acoplamento entre componentes;
- possibilidade de adicionar novos consumidores aos eventos;
- maior facilidade de manutenção;
- melhor preparação para futuras integrações.

## Consequências Negativas

- aumento da complexidade arquitetural;
- necessidade de gerenciar múltiplos serviços;
- maior complexidade de monitoramento;
- necessidade de definir contratos claros entre os serviços;
- comunicação distribuída pode exigir mecanismos adicionais de tratamento
  de falhas.

## Design Pattern Relacionado

O projeto utiliza o padrão comportamental **Observer** na simulação da
arquitetura orientada a eventos.

Nesse modelo, o produtor publica um evento e diferentes consumidores podem
recebê-lo e executar suas próprias ações.

No projeto, o serviço de pagamentos e o serviço de notificações atuam como
consumidores independentes do evento de compra.

Essa abordagem permite adicionar novos consumidores sem alterar diretamente
o produtor do evento.

## Resultado Esperado

A arquitetura proposta fornece uma base mais organizada e evolutiva para a
ShoopTree, permitindo que funcionalidades sejam desenvolvidas e escaladas de
forma mais independente.

A prova de conceito demonstra, em pequena escala, como os serviços
independentes e a comunicação orientada a eventos podem ser utilizados na
modernização da plataforma.