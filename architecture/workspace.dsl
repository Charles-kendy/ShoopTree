workspace {

    model {
        cliente = person "Cliente" "Cliente que utiliza a plataforma ShoopTree para realizar compras."

        shoptree = softwareSystem "ShoopTree" "Plataforma de e-commerce responsável pelo catálogo, compras e pagamentos." {

            productService = container "Serviço de Produtos" "Responsável pelo catálogo e gerenciamento de produtos." "Python / FastAPI"

            paymentService = container "Serviço de Pagamentos" "Responsável pelo processamento e gerenciamento dos pagamentos." "Python / FastAPI"

            eventService = container "Simulação de Eventos" "Responsável pela publicação e consumo de eventos de compra." "Python"

            notificationService = container "Serviço de Notificações" "Responsável por consumir eventos e gerar notificações." "Python"
        }

        cliente -> shoptree "Realiza compras e consulta produtos"

        cliente -> productService "Consulta e cadastra produtos"
        cliente -> paymentService "Realiza pagamentos"

        productService -> eventService "Publica evento de compra"
        eventService -> paymentService "Envia evento para processamento do pagamento"
        eventService -> notificationService "Envia evento para notificação"
    }

    views {

        systemContext shoptree {
            include *
            autolayout lr
        }

        container shoptree {
            include *
            autolayout lr
        }

        theme default
    }
}