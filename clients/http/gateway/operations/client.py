from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

from clients.http.client import HTTPClient, QueryParams
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    TypedDict для представления структуры одной операции.
    """
    id: str
    type: str
    status: str
    amount: int
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    TypedDict для представления структуры чека операции.
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    TypedDict для представления структуры сводки операций.
    """
    spentAmount: int
    receivedAmount: int
    cashbackAmount: int


class GetOperationResponseDict(TypedDict):
    """
    TypedDict для представления ответа на запрос одной операции.
    """
    operation: OperationDict


class GetOperationsResponseDict(TypedDict):
    """
    TypedDict для представления ответа на запрос списка операций.
    """
    operations: list[OperationDict]


class GetOperationReceiptResponseDict(TypedDict):
    """
    TypedDict для представления ответа на запрос чека операции.
    """
    receipt: OperationReceiptDict


class GetOperationsSummaryResponseDict(TypedDict):
    """
    TypedDict для представления ответа на запрос сводки операций.
    """
    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    """
    TypedDict для представления ответа на создание операции комиссии.
    """
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    """
    TypedDict для представления ответа на создание операции пополнения.
    """
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """
    TypedDict для представления ответа на создание операции кэшбэка.
    """
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """
    TypedDict для представления ответа на создание операции перевода.
    """
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """
    TypedDict для представления ответа на создание операции покупки.
    """
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    TypedDict для представления ответа на создание операции оплаты счетов.
    """
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    TypedDict для представления ответа на создание операции снятия наличных.
    """
    operation: OperationDict


class GetOperationsSummaryQueryDict(TypedDict):
    """
    TypedDict для параметров запроса сводки операций.
    """
    accountId: str


class GetOperationsQueryParamsDict(TypedDict):
    """
    TypedDict для параметров запроса списка операций.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Базовый TypedDict для запросов на создание операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    TypedDict для запроса на создание операции покупки.
    """
    category: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    TypedDict для запроса на создание операции комиссии.
    """
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    TypedDict для запроса на создание операции пополнения.
    """
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    TypedDict для запроса на создание операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    TypedDict для запроса на создание операции перевода.
    """
    pass


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    TypedDict для запроса на создание операции оплаты счетов.
    """
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    TypedDict для запроса на создание операции снятия наличных.
    """
    pass


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Прокси-клиент для взаимодействия с сервисом операций через HTTP-Gateway.
    Содержит методы для получения информации об операциях и создания различных типов операций.
    """

    def get_operations_api(self, query: GetOperationsQueryParamsDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.

        :param query: Словарь параметров запроса, содержащий 'accountId'.
        :return: Объект Response от httpx.
        """
        return self.get(url="/api/v1/operations", params=QueryParams(**query))

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Объект Response от httpx.
        """
        return self.get(url=f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Объект Response от httpx.
        """
        return self.get(url=f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь параметров запроса, содержащий 'accountId'.
        :return: Объект Response от httpx.
        """
        return self.get(url="/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции кэшбэка.

        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции оплаты по счету.

        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции снятия наличных денег.

        :param request: Словарь с данными для создания операции снятия наличных.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получает информацию об одной операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Словарь с информацией об операции.
        """
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получает чек операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Словарь с данными чека операции.
        """
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получает список операций для указанного счета.

        :param account_id: Идентификатор счета.
        :return: Словарь со списком операций.
        """
        query = GetOperationsQueryParamsDict(accountId=account_id)
        response = self.get_operations_api(query=query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получает сводную информацию по операциям для указанного счета.

        :param account_id: Идентификатор счета.
        :return: Словарь со сводной информацией по операциям.
        """
        request = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query=request)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Создает операцию по снятию комиссии.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции комиссии.
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Создает операцию пополнения счета.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции пополнения.
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Создает операцию начисления кэшбэка.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции кэшбэка.
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Создает операцию перевода средств.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции перевода.
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        """
        Создает операцию покупки.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции покупки.
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=1000,
            cardId=card_id,
            accountId=account_id,
            category="Taxi"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Создает операцию оплаты по счету.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции оплаты по счету.
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Создает операцию снятия наличных денег.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции снятия наличных.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
