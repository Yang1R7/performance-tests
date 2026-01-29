from enum import StrEnum

from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from tools.fakers import fake


class OperationStatus(StrEnum):
    FAILED = "FAILED",
    COMPLETED = "COMPLETED",
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationType(StrEnum):
    FEE = "FEE",
    TOP_UP = "TOP_UP",
    PURCHASE = "PURCHASE",
    CASHBACK = "CASHBACK",
    TRANSFER = "TRANSFER",
    BILL_PAYMENT = "BILL_PAYMENT",
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL",


class OperationSchema(BaseModel):
    """
    TypedDict для представления структуры одной операции.
    """
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    cardId: str = Field(alias='cardId')
    category: str
    createdAt: str = Field(alias='createdAt')
    accountId: str = Field(alias='accountId')


class OperationReceiptSchema(BaseModel):
    """
    TypedDict для представления структуры чека операции.
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    TypedDict для представления структуры сводки операций.
    """
    model_config = ConfigDict(populate_by_name=True)
    spentAmount: int = Field(alias='spentAmount')
    receivedAmount: int = Field(alias='receivedAmount')
    cashbackAmount: int = Field(alias='cashbackAmount')


class GetOperationResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на запрос одной операции.
    """
    operation: OperationSchema


class GetOperationsResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на запрос списка операций.
    """
    operations: list[OperationSchema]


class GetOperationReceiptResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на запрос чека операции.
    """
    receipt: OperationReceiptSchema


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на запрос сводки операций.
    """
    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на создание операции комиссии.
    """
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на создание операции пополнения.
    """
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на создание операции кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на создание операции перевода.
    """
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на создание операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на создание операции оплаты счетов.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    TypedDict для представления ответа на создание операции снятия наличных.
    """
    operation: OperationSchema


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    TypedDict для параметров запроса сводки операций.
    """
    accountId: str


class GetOperationsQueryParamsSchema(BaseModel):
    """
    TypedDict для параметров запроса списка операций.
    """
    accountId: str


class MakeOperationRequestSchema(BaseModel):
    """
    Базовый TypedDict для запросов на создание операции.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    cardId: str = Field(alias='cardId')
    accountId: str = Field(alias='accountId')


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    TypedDict для запроса на создание операции покупки.
    """
    category: str = Field(default_factory=fake.category)


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    TypedDict для запроса на создание операции комиссии.
    """
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    TypedDict для запроса на создание операции пополнения.
    """
    pass


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    TypedDict для запроса на создание операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    TypedDict для запроса на создание операции перевода.
    """
    pass


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    TypedDict для запроса на создание операции оплаты счетов.
    """
    pass


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    TypedDict для запроса на создание операции снятия наличных.
    """
    pass
