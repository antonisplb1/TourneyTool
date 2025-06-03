# backend/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# This sets up the base class for all tables
Base = declarative_base()

# Example table: Tenants
class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Example field: a simple name for the tenant

# Example table: Players
class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tenant_id = Column(Integer, ForeignKey('tenants.id'))
    tenant = relationship("Tenant")
    # Links players to tenants

# Example table: Tournaments
class Tournament(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tenant_id = Column(Integer, ForeignKey('tenants.id'))
    tenant = relationship("Tenant")
    # Links tournaments to tenants
