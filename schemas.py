from pydantic import BaseModel, Field
from typing import Optional, List

class UsuarioSchema(BaseModel): 
    nome: str 
    senha: str 
    email: str 
    ativo: Optional[bool] 
    admin: Optional[bool] 
    
    class Config:
        from_attributes = True
        
class PedidoSchema(BaseModel):
    usuario: int  #"ID do usuário que fez o pedido")
    class Config:
        from_attributes = True