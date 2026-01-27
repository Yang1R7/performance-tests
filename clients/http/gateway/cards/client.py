from httpx import Response

from clients.http.client import HTTPClient
from typing import TypedDict


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для создания виртуальной карты .
    """
    userId: str
    accountId: str


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для создания физической карты .
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Запрос на выпуск виртуальной карты.
.
        :request user_id: Идентификатор пользователя и accountId: Id счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post(url="/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Запрос на выпуск физической карту.

        :request user_id: Идентификатор пользователя и accountId: Id счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post(url="/api/v1/cards/issue-physical-card", json=request)
