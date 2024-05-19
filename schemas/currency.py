from sqlalchemy import Column, String, Date, Float, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Currency(Base):
    __tablename__ = 'currency'

    currency_symbol = Column(String, nullable=False)
    currency_date = Column(Date, nullable=False)
    currency_rate = Column(Float, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('currency_date', 'currency_symbol', name='currency_pk', sqlite_on_conflict="REPLACE"),
    )

    def __repr__(self):
        return f"<Currency(currency_symbol='{self.currency_symbol}', currency_date='{self.currency_date}', currency_rate={self.currency_rate})>"
