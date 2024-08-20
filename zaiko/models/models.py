from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    password = Column(String(length=100), nullable=False)
    secretQuestion= Column(String, nullable=True)
    secretAnswer= Column(String(length=100), nullable=True)
    role = Column(String, nullable=True, default='user')


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String(length=100) , nullable=False)
    unitPrice = Column(Float, nullable=False)
    image =Column(String, nullable=True)
    supplier = Column(Integer, nullable=False)
    category = Column(Integer, nullable=True)
    ware = Column(Integer, nullable=True)


class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class Warehouse(Base):
    __tablename__ = 'warehouse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)


class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    product = Column(Integer, nullable=False)


class Purchase_order(Base):
    __tablename__ = 'purchase_order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Integer, nullable=False)
    Order_quantity = Column(Integer, nullable=False)
    Supplier_id = Column(Integer, nullable=False)


