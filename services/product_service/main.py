from fastapi import FastAPI, HTTPException, Query
from services.product_service.schemas import Produto, ProdutoCreate, ProdutoUpdate


app = FastAPI(
    title="ShoopTree - Serviço de Produtos",
    description="API responsável pelo catálogo de produtos da ShoopTree",
    version="1.0.0"
)
produtos = [
    {
        "id": 1,
        "nome": "Smartphone Nova X Pro",
        "descricao": "Smartphone com 256 GB de armazenamento e câmera de alta resolução",
        "categoria": "Smartphones",
        "marca": "NovaTech",
        "preco": 3299.90,
        "estoque": 25,
        "ativo": True
    },
    {
        "id": 2,
        "nome": "Notebook Ultra 15",
        "descricao": "Notebook com 16 GB de RAM e SSD de 512 GB",
        "categoria": "Notebooks",
        "marca": "TechVision",
        "preco": 4899.90,
        "estoque": 12,
        "ativo": True
    },
    {
        "id": 3,
        "nome": "Fone Sound Pro",
        "descricao": "Fone sem fio com cancelamento ativo de ruído",
        "categoria": "Áudio",
        "marca": "SoundMax",
        "preco": 799.90,
        "estoque": 40,
        "ativo": True
    },
    {
        "id": 4,
        "nome": "Smart TV Vision 55",
        "descricao": "Smart TV 4K de 55 polegadas com sistema integrado",
        "categoria": "Televisores",
        "marca": "VisionTech",
        "preco": 3199.90,
        "estoque": 8,
        "ativo": True
    },
    {
        "id": 5,
        "nome": "Monitor UltraView 27",
        "descricao": "Monitor de 27 polegadas com resolução QHD",
        "categoria": "Monitores",
        "marca": "DisplayPro",
        "preco": 1899.90,
        "estoque": 15,
        "ativo": True
    }
]


@app.get("/produtos")
def listar_produtos():
    return produtos

@app.post("/produtos", response_model=Produto)
def criar_produto(novo_produto: ProdutoCreate):
    novo_id = max(produto["id"] for produto in produtos) + 1

    produto = {
        "id": novo_id,
        **novo_produto.model_dump()
    }

    produtos.append(produto)

    return produto
@app.get("/produtos/busca", response_model=list[Produto])
def buscar_produtos(
    nome: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    preco_min: float | None = Query(default=None, ge=0),
    preco_max: float | None = Query(default=None, ge=0),
    estoque_min: int | None = Query(default=None, ge=0),
    ativo: bool | None = Query(default=None)
):
    resultados = produtos

    if nome:
        resultados = [
            produto for produto in resultados
            if nome.lower() in produto["nome"].lower()
        ]

    if categoria:
        resultados = [
            produto for produto in resultados
            if produto["categoria"].lower() == categoria.lower()
        ]

    if preco_min is not None:
        resultados = [
            produto for produto in resultados
            if produto["preco"] >= preco_min
        ]

    if preco_max is not None:
        resultados = [
            produto for produto in resultados
            if produto["preco"] <= preco_max
        ]

    if estoque_min is not None:
        resultados = [
            produto for produto in resultados
            if produto["estoque"] >= estoque_min
        ]

    if ativo is not None:
        resultados = [
            produto for produto in resultados
            if produto["ativo"] == ativo
        ]

    return resultados

@app.get("/produtos/{produto_id}", response_model=Produto)
def buscar_produto(produto_id: int):

    for produto in produtos:
        if produto["id"] == produto_id:
            return produto

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )

@app.put("/produtos/{produto_id}", response_model=Produto)
def atualizar_produto(
    produto_id: int,
    dados_atualizacao: ProdutoUpdate
):
    for indice, produto in enumerate(produtos):

        if produto["id"] == produto_id:

            produto_atualizado = {
                "id": produto_id,
                **dados_atualizacao.model_dump()
            }

            produtos[indice] = produto_atualizado

            return produto_atualizado

    raise HTTPException(
        status_code=404,
        detail="Produto não encontrado"
    )