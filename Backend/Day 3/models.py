# models.py
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Float, DateTime, func
from database import Base
import datetime

class PredictionRecord(Base):
    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    feature1: Mapped[float] = mapped_column(Float, nullable=False)
    feature2: Mapped[float] = mapped_column(Float, nullable=False)
    prediction_result: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())