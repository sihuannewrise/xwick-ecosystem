from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, text, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base
from ._selectchoice import EntityStatus


class EntityBase(Base):
    __abstract__ = True

    name: Mapped[str] = mapped_column(String(160), unique=True)
    address: Mapped[Optional[str]] = mapped_column(String(200))
    status: Mapped[Optional[EntityStatus]]
    inn: Mapped[Optional[str]] = mapped_column(String(12))
    kpp: Mapped[Optional[str]] = mapped_column(String(9))
    __table_args__ = (UniqueConstraint('inn', 'kpp', name='_inn_kpp_unique'),)

    actuality_date: Mapped[Optional[datetime]]
    registration_date: Mapped[Optional[datetime]]
    liquidation_date: Mapped[Optional[datetime]]

    is_archived: Mapped[bool] = mapped_column(
        default=False,
        server_default=text('FALSE'))


class SupplementaryBase(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(String(50), unique=True)


class BankAccountType(SupplementaryBase):
    """
    основной, инвест, спецсчет
    """
    accounts: Mapped[List['BankAccount']] = relationship(
        backref='bankaccounttype',
    )


class PaymentType(SupplementaryBase):
    """
    контрагенту, в бюджет, инвест
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='paymenttype',
    )


class KFP(SupplementaryBase):
    """
    код финансовой позиции
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='kfp',
    )


class PayerStatus(SupplementaryBase):
    """
    Статус плательщика
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='payerstatus',
    )


class KBK(SupplementaryBase):
    """
    КБК
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='kbk',
    )


class OKTMO(SupplementaryBase):
    """
    ОКТМО
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='oktmo',
    )


class Prepayment(SupplementaryBase):
    """
    Платеж авансовый или по факту
    """
    pr_list: Mapped[List['PaymentRequest']] = relationship(
        backref='prepayment',
    )


class PaymentStatus(SupplementaryBase):
    """
    статус платежа: у исполнителя, на подписи, на исполнении
    """
    register: Mapped[List['PaymentRegister']] = relationship(
        backref='paymentstatus',
    )


class PaymentVerdict(SupplementaryBase):
    """
    решение подписанта: согласовано, на доработку, отклонено
    """
    proc: Mapped[List['PaymentProcessing']] = relationship(
        backref='paymentverdict',
    )
