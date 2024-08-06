from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    Price = Column(Integer, nullable=False)
    img =Column(String, nullable=True)
    Supplier_id = Column(Integer, nullable=False)
    id_category = Column(Integer, nullable=False)
    id_warehouse = Column(Integer, nullable=False)


class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Quantity = Column(Integer, nullable=False)
    Product_id = Column(Integer, nullable=False)


class Purchase_order(Base):
    __tablename__ = 'purchase_order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(Integer, nullable=False)
    Order_quantity = Column(Integer, nullable=False)
    Supplier_id = Column(Integer, nullable=False)


class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    Address = Column(String, nullable=False)
    Phone = Column(String, nullable=False)
    Email = Column(String, nullable=False)


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)


class Warehouse(Base):
    __tablename__ = 'warehouse'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(Integer, nullable=False)
    location = Column(String, nullable=False)

