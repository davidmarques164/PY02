from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def list_orders():
    return {"message": "Você acessou a lista de pedidos"}
    