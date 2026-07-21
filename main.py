from fastapi import FastAPI 
from passlib.context import CryptContext
app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

    # uvicorn main:app --reload para rodar
    # endpoints:
    # dominio.com/orders/list - Retorna uma lista de pedidos

    # /orders/ - Retorna uma lista de pedidos
    # REST API - Representational State Transfer Application Programming Interface
    # GET / - Retorna uma mensagem de boas-vindas
    # POST /items/ - Cria um novo item
    # Put/Patch /items/{item_id} - Atualiza um item existente
    # Delete /items/{item_id} - Remove um item existente