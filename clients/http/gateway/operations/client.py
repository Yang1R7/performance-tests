from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

from clients.http.client import HTTPClient, QueryParams


class GetOperationsSummaryQueryDict(TypedDict):
    accountId: str


class GetOperationsQueryParamsDict(TypedDict):
    accountId: str


class MakeOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    category: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    pass


class OperationsGatewayHTTPClient(HTTPClient):

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по operation_id.
        """
        return self.get(url=f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на Получение чека по операции по operation_id.
        """
        return self.get(url=f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryParamsDict) -> Response:
        """
        Выполняет GET-запрос на Получение списка операций для определенного.
        """
        return self.get(url="/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на Получение статистики по операциям для определенного счета.
        """
        return self.get(url="/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на Создание операции комиссии.
        """
        return self.post(url="/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на Создание операции пополнения.
        """
        return self.post(url="/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на Создание операции кэшбэка.
        """
        return self.post(url="/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на Создание операции перевода.
        """
        return self.post(url="/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на Создание операции покупки.
        """
        return self.post(url="/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на Создание операции оплаты по счету.
        """
        return self.post(url="/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на Создание операции снятия наличных денег.
        """
        return self.post(url="/api/v1/operations/make-cash-withdrawal-operation", json=request)
