class Event:
    def __init__(self, tipo, dados):
        self.tipo = tipo
        self.dados = dados


class Producer:
    def publicar_compra(self, compra):
        evento = Event("compra_realizada", compra)

        print("\n[PRODUCER]")
        print("Evento de compra publicado:")
        print(evento.dados)

        return evento


class PaymentConsumer:
    def processar(self, evento):
        print("\n[PAYMENT CONSUMER]")
        print("Evento recebido pelo serviço de pagamentos.")

        pagamento = {
            "pedido_id": evento.dados["pedido_id"],
            "valor": evento.dados["valor"],
            "status": "pagamento_processado"
        }

        print("Pagamento processado:")
        print(pagamento)

        return pagamento


class NotificationConsumer:
    def notificar(self, evento):
        print("\n[NOTIFICATION CONSUMER]")
        print("Evento recebido pelo serviço de notificações.")
        print(
            f"Notificação enviada: "
            f"Compra do pedido {evento.dados['pedido_id']} "
            f"no valor de R$ {evento.dados['valor']:.2f} realizada com sucesso."
        )


if __name__ == "__main__":
    compra = {
        "pedido_id": 103,
        "cliente": "Cliente ShoopTree",
        "valor": 2499.90
    }

    producer = Producer()
    payment_consumer = PaymentConsumer()
    notification_consumer = NotificationConsumer()

    evento = producer.publicar_compra(compra)

    payment_consumer.processar(evento)

    notification_consumer.notificar(evento)