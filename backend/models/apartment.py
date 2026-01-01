from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class Apartment(Base):
    __tablename__ = "apartments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"))
    number: Mapped[str] = mapped_column(String(50))
    floor: Mapped[int] = mapped_column(Integer)

    building = relationship("Building", back_populates="apartments")
    residents = relationship("User", back_populates="apartment")
