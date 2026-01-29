from pydantic import BaseModel, Field, ConfigDict, HttpUrl


class ContractSchema(BaseModel):
    """
    Представляет структуру контракта с URL и содержимым документа.
    """
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Представляет структуру ответа при получении тарифного документа.
    """
    tariff: ContractSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Представляет структуру ответа при получении документа контракта.
    """
    contract: ContractSchema
