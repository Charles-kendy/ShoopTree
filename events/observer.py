from abc import ABC, abstractmethod


# Observer
class Observer(ABC):

    @abstractmethod
    def atualizar(self, evento):
        pass


# Subject
class EventPublisher:

    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def publicar(self, evento):
        print("\n[EVENT PUBLISHER]")
        print(f"Evento publicado: {evento}")

        for observador in self.observadores:
            observador.atualizar(evento)


# Observer concreto: Pagamento
class PaymentConsumer(Observer):

    def atualizar(self, evento):
        print("\n[PAYMENT CONSUMER]")
        print("Pagamento recebeu o evento.")
        print(f"Processando pagamento do pedido {evento['pedido_id']}...")


# Observer concreto: Notificação
class NotificationConsumer(Observer):

    def atualizar(self, evento):
        print("\n[NOTIFICATION CONSUMER]")
        print("Notificação recebeu o evento.")
        print(
            f"Enviando notificação: "
            f"Compra do pedido {evento['pedido_id']} "
            f"no valor de R$ {evento['valor']:.2f}."
        )


# Teste do Observer Pattern
if __name__ == "__main__":

    publisher = EventPublisher()

    pagamento = PaymentConsumer()
    notificacao = NotificationConsumer()

    publisher.adicionar_observador(pagamento)
    publisher.adicionar_observador(notificacao)

    evento_compra = {
        "pedido_id": 104,
        "cliente": "Cliente ShoopTree",
        "valor": 1599.90
    }

    publisher.publicar(evento_compra)