from sqlalchemy import Column, DateTime, ForeignKey, Float, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class PaymentRequest(Base):
    type_id = Column(Integer, ForeignKey('paymenttype.id'), nullable=False)
    payer_id = Column(Integer, ForeignKey('payer.id'), nullable=False)
    recipient_id = Column(Integer, ForeignKey('counteragent.id'), nullable=False)

    kfp_id = Column(Integer, ForeignKey('kfp.id'))
    due_date = Column(DateTime, nullable=False)
    purpose = Column(String(50), nullable=False)
    amount_netto = Column(Float)
    amount_vat = Column(Float)
    amount_total = Column(Float, nullable=False)
    attachement = Column(String(150))

    field_101_id = Column(Integer, ForeignKey('payerstatus.id'))
    field_104_id = Column(Integer, ForeignKey('kbk.id'))
    field_105_id = Column(Integer, ForeignKey('oktmo.id'))
    field_106 = Column(String(20))  # Основание платежа
    field_107 = Column(String(20))  # Налоговый период 
    field_108 = Column(String(20))  # Номер документа-основания платежа
    field_109 = Column(String(20))  # Дата документа-основания платежа

    project = Column(String(50))
    contract = Column(String(50))
    contract_date = Column(DateTime)
    sub_contract = Column(String(50))
    sub_contract_date = Column(DateTime)
    prepayment_id = Column(Integer, ForeignKey('prepayment.id'))
    
    register = relationship('PaymentRegister')
