from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# cria a conexão com o banco de dados SQLite
db = create_engine("sqlite:///orders.db")

# cria a classe base para os modelos
Base = declarative_base()

# cria as classes/tabelas do banco de dados
# usuário
class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("name", String, unique=True, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    status = Column("status", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)
    
    def _init__(self, username, email, password, status=True, admin=False): 
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.admin = admin
        
# pedidos
class Order(Base):
    __tablename__ = "orders"
    
    STATUS_ORDER = [
        ("PENDENTE", "Pendente"),
        ("CANCELADO", "Cancelado"),
        ("FINALIZADO", "Finalizado")
    ]
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(STATUS_ORDER), default="PENDENTE")
    user = Column("user", String, ForeignKey("users.id"), nullable=False,)
    price = Column("price", Float, nullable=False)
    
       
    def _init__(self, user, status="PENDENTE", price=0.0):
        self.user = user    
        self.status = status
        self.price = price

# itens do pedido

class OrderItem(Base):
    __tablename__ = "order_items"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer, nullable=False)
    flavor = Column("flavor", String, nullable=False) 
    size = Column("size", String, nullable=False)
    unit_price = Column("unit_price", Float, nullable=False)
    order = Column("order", String, ForeignKey("orders.id"), nullable=False) 
        
    def _init__(self, quantity, flavor, size, unit_price, order):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size            
        self.unit_price = unit_price
        self.order = order
        

# executa a criação dos métodos no banco de dados