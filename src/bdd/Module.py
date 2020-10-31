from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from bdd.bdd import Base


class Module(Base):
    __tablename__ = 'module'

    id = Column(Integer, primary_key=True)

    name = Column(String(50))
    path = Column(String(200))

    project_id = Column(Integer, ForeignKey("project.id"))
    project = relationship("Project", back_populates="module")
    scopes = relationship("Scope", back_populates="module")
