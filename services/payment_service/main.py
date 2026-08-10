from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="ShoopTree - Serviço de Pagamentos",
    description="API responsável pelo processamento de pagamentos da ShoopTree",
    version="1.0.0"
)


class Pagamento(BaseModel):
    id: int
    pedido_id: int
    valor: float = Field(gt=0)
    metodo: str
    status: str


class PagamentoCreate(BaseModel):
    pedido_id: int
    valor: float = Field(gt=0)
    metodo: str
    status: str = "pendente"


pagamentos = [
    {
        "id": 1,
        "pedido_id": 101,
        "valor": 3299.90,
        "metodo": "Cartão de Crédito",
        "status": "aprovado"
    }
]


@app.get("/pagamentos", response_model=list[Pagamento])
def listar_pagamentos():
    return pagamentos


@app.post("/pagamentos", response_model=Pagamento)
def criar_pagamento(novo_pagamento: PagamentoCreate):
    novo_id = max(pagamento["id"] for pagamento in pagamentos) + 1

    pagamento = {
        "id": novo_id,
        **novo_pagamento.model_dump()
    }

    pagamentos.append(pagamento)

    return pagamento