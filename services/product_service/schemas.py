from pydantic import BaseModel, Field


class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    categoria: str
    marca: str
    preco: float = Field(gt=0)
    estoque: int = Field(ge=0)
    ativo: bool = True

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    categoria: str
    marca: str
    preco: float = Field(gt=0)
    estoque: int = Field(ge=0)
    ativo: bool = True

class ProdutoUpdate(BaseModel):
    nome: str
    descricao: str
    categoria: str
    marca: str
    preco: float = Field(gt=0)
    estoque: int = Field(ge=0)
    ativo: bool = True