from grpc import Channel
from locust.env import Environment

from clients.grpc.client import GRPCClient, build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationResponse, GetOperationRequest
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptResponse, GetOperationReceiptRequest
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsResponse, GetOperationsRequest
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryResponse, GetOperationsSummaryRequest
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import MakeBillPaymentOperationResponse, MakeBillPaymentOperationRequest
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import \
    MakeCashWithdrawalOperationResponse, MakeCashWithdrawalOperationRequest
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationResponse, MakeCashbackOperationRequest
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationResponse, MakeFeeOperationRequest
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import MakePurchaseOperationResponse, MakePurchaseOperationRequest
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationResponse, MakeTopUpOperationRequest
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationResponse, MakeTransferOperationRequest
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет высокоуровневые методы для работы с финансовыми операциями.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)

        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов метода GetOperation через gRPC.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ от сервиса с данными конкретной операции.
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов метода GetOperationReceipt через gRPC.

        :param request: gRPC-запрос с ID чека операции.
        :return: Ответ от сервиса с данными чека операции.
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов метода GetOperations через gRPC.

        :param request: gRPC-запрос для получения списка операций.
        :return: Ответ от сервиса со списком операций.
        """
        return self.stub.GetOperations(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов метода GetOperationsSummary через gRPC.

        :param request: gRPC-запрос для получения сводки операций.
        :return: Ответ от сервиса со сводкой операций.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов метода MakeFeeOperation через gRPC.

        :param request: gRPC-запрос для создания операции комиссии.
        :return: Ответ от сервиса с результатом создания операции комиссии.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self,request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов метода MakeTopUpOperation через gRPC.

        :param request: gRPC-запрос для создания операции пополнения.
        :return: Ответ от сервиса с результатом создания операции пополнения.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashbackOperation через gRPC.

        :param request: gRPC-запрос для создания операции кэшбэка.
        :return: Ответ от сервиса с результатом создания операции кэшбэка.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов метода MakeTransferOperation через gRPC.

        :param request: gRPC-запрос для создания операции перевода.
        :return: Ответ от сервиса с результатом создания операции перевода.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов метода MakePurchaseOperation через gRPC.

        :param request: gRPC-запрос для создания операции покупки.
        :return: Ответ от сервиса с результатом создания операции покупки.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов метода MakeBillPaymentOperation через gRPC.

        :param request: gRPC-запрос для создания операции оплаты счетов.
        :return: Ответ от сервиса с результатом создания операции оплаты счетов.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashWithdrawalOperation через gRPC.

        :param request: gRPC-запрос для создания операции снятия наличных.
        :return: Ответ от сервиса с результатом создания операции снятия наличных.
        """
        return self.stub.MakeCashWithdrawalOperation(request)


    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Получает информацию о конкретной операции по её ID.

        :param operation_id: Уникальный идентификатор операции.
        :return: Ответ от сервиса с данными об операции.
        """
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Получает чек для указанной операции.

        :param operation_id: Уникальный идентификатор операции, для которой нужен чек.
        :return: Ответ от сервиса с данными чека операции.
        """
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self,account_id: str) -> GetOperationsResponse:
        """
        Получает список операций для указанного счета.

        :param account_id: Идентификатор счета, для которого нужно получить операции.
        :return: Ответ от сервиса со списком операций счета.
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Получает сводку операций для указанного счета.

        :param account_id: Идентификатор счета, для которого нужно получить сводку.
        :return: Ответ от сервиса со сводкой операций счета.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """
        Создает операцию по начислению комиссии на счет.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, на который будет начислена комиссия.
        :return: Ответ от сервиса с результатом создания операции.
        """
        request = MakeFeeOperationRequest(
            card_id=card_id,
            account_id=account_id,
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount())
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """
        Создает операцию пополнения счета.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, который будет пополнен.
        :return: Ответ от сервиса с результатом создания операции.
        """
        request = MakeTopUpOperationRequest(
            card_id=card_id,
            account_id=account_id,
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount()
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        """
        Создает операцию по начислению кэшбэка на счет.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, на который будет начислен кэшбэк.
        :return: Ответ от сервиса с результатом создания операции.
        """
        request = MakeCashbackOperationRequest(
            card_id=card_id,
            account_id=account_id,
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount()
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        """
        Создает операцию перевода средств между счетами.

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета отправителя перевода.
        :return: Ответ от сервиса с результатом создания операции.
        """
        request = MakeTransferOperationRequest(
            card_id=card_id,
            account_id=account_id,
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount()
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        """
        Создает операцию покупки товаров или услуг.

        :param card_id: Идентификатор карты, связанной с покупкой.
        :param account_id: Идентификатор счета, с которого будет совершена покупка.
        :return: Ответ от сервиса с результатом создания операции.
        """
        request = MakePurchaseOperationRequest(
            card_id=card_id,
            account_id=account_id,
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            category=fake.category()
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        """
        Создает операцию по оплате счета (например, коммунальных услуг).

        :param card_id: Идентификатор карты, связанной с операцией.
        :param account_id: Идентификатор счета, с которого будет произведена оплата.
        :return: Ответ от сервиса с результатом создания операции.
        """
        request = MakeBillPaymentOperationRequest(
            card_id=card_id,
            account_id=account_id,
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount()
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        """
        Создает операцию снятия наличных средств.

        :param card_id: Идентификатор карты, используемой для снятия наличных.
        :param account_id: Идентификатор счета, с которого будут сняты наличные.
        :return: Ответ от сервиса с результатом создания операции.
        """
        request = MakeCashWithdrawalOperationRequest(
            card_id=card_id,
            account_id=account_id,
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount()
        )
        return self.make_cash_withdrawal_operation_api(request)

def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayGRPCClient.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())


def build_operations_gateway_locust_grpc_client(environment: Environment) -> OperationsGatewayGRPCClient:
    """
    Функция создаёт экземпляр OperationsGatewayGRPCClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayGRPCClient с хуками сбора метрик.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))