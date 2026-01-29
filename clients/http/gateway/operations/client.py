from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

from clients.http.client import HTTPClient, QueryParams
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import GetOperationsQueryParamsSchema, GetOperationsSummaryQuerySchema, \
    MakeFeeOperationRequestSchema, MakeTopUpOperationRequestSchema, MakeCashbackOperationRequestSchema, \
    MakeTransferOperationRequestSchema, MakePurchaseOperationRequestSchema, MakeBillPaymentOperationRequestSchema, \
    MakeCashWithdrawalOperationRequestSchema, GetOperationResponseSchema, GetOperationReceiptResponseSchema, \
    GetOperationsResponseSchema, GetOperationsSummaryResponseSchema, MakeFeeOperationResponseSchema, OperationType, \
    OperationStatus, MakeTopUpOperationResponseSchema, MakeCashbackOperationResponseSchema, \
    MakeTransferOperationResponseSchema, MakePurchaseOperationResponseSchema, MakeBillPaymentOperationResponseSchema, \
    MakeCashWithdrawalOperationResponseSchema


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Прокси-клиент для взаимодействия с сервисом операций через HTTP-Gateway.
    Содержит методы для получения информации об операциях и создания различных типов операций.
    """

    def get_operations_api(self, query: GetOperationsQueryParamsSchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета.

        :param query: Словарь параметров запроса, содержащий 'accountId'.
        :return: Объект Response от httpx.
        """
        return self.get(url="/api/v1/operations", params=query.model_dump(by_alias=True))

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

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь параметров запроса, содержащий 'accountId'.
        :return: Объект Response от httpx.
        """
        return self.get(url="/api/v1/operations/operations-summary", params=query.model_dump(by_alias=True))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции кэшбэка.

        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции оплаты по счету.

        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос на создание операции снятия наличных денег.

        :param request: Словарь с данными для создания операции снятия наличных.
        :return: Объект Response от httpx.
        """
        return self.post(url="/api/v1/operations/make-cash-withdrawal-operation",
                         json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получает информацию об одной операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Словарь с информацией об операции.
        """
        response = self.get_operation_api(operation_id=operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получает чек операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Словарь с данными чека операции.
        """
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получает список операций для указанного счета.

        :param account_id: Идентификатор счета.
        :return: Словарь со списком операций.
        """
        query = GetOperationsQueryParamsSchema(accountId=account_id)
        response = self.get_operations_api(query=query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получает сводную информацию по операциям для указанного счета.

        :param account_id: Идентификатор счета.
        :return: Словарь со сводной информацией по операциям.
        """
        request = GetOperationsSummaryQuerySchema(accountId=account_id)
        response = self.get_operations_summary_api(query=request)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Создает операцию по снятию комиссии.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции комиссии.
        """
        request = MakeFeeOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """
        Создает операцию пополнения счета.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции пополнения.
        """
        request = MakeTopUpOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """
        Создает операцию начисления кэшбэка.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции кэшбэка.
        """
        request = MakeCashbackOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """
        Создает операцию перевода средств.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции перевода.
        """
        request = MakeTransferOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """
        Создает операцию покупки.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции покупки.
        """
        request = MakePurchaseOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000,
            cardId=card_id,
            accountId=account_id,
            category="Taxi"
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """
        Создает операцию оплаты по счету.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции оплаты по счету.
        """
        request = MakeBillPaymentOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создает операцию снятия наличных денег.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, связанного с операцией.
        :return: Словарь с информацией о созданной операции снятия наличных.
        """
        request = MakeCashWithdrawalOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
