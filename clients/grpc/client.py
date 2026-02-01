# Импортируем поддержку работы gRPC с потоками (greenlets)
import grpc.experimental.gevent as grpc_gevent

# Импортируем тип канала связи (channel), через который будем общаться с сервером
from grpc import Channel, insecure_channel, intercept_channel
from locust.env import Environment

from clients.grpc.interceptors.locust_interceptor import LocustInterceptor

# Инициализируем поддержку gevent в gRPC.
# Это обязательно, если вы используете gevent-базированный фреймворк (например, Locust).
# Без этой инициализации gRPC будет использовать потоковую модель (threading),
# что приведёт к блокировке greenlet'ов и нарушит конкурентное выполнение.
# Инициализация позволяет gRPC использовать совместимую с gevent реализацию
# для работы с сокетами, таймерами и I/O, даже если код написан в синхронном стиле.
grpc_gevent.init_gevent()


class GRPCClient:
    """
    Базовый класс gRPC-клиента.

    Этот класс хранит общий канал (Channel) для связи с gRPC-сервером.
    От него будут наследоваться все остальные специфические клиенты.
    """

    def __init__(self, channel: Channel):
        """
        Конструктор базового клиента.

        :param channel: gRPC-канал, через который происходит подключение к серверу.
                        Обычно создаётся один раз и переиспользуется.
        """
        self.channel = channel  # Сохраняем канал внутри объекта для последующего использования

def build_gateway_grpc_client() -> Channel:
    """
    Фабричная функция (билдер) для создания gRPC-канала к сервису grpc-gateway.

    :return: gRPC-канал (Channel), настроенный на адрес localhost:9003.
    """
    # Создаём небезопасное (без TLS) соединение с gRPC-сервером по адресу localhost:9003
    return insecure_channel("localhost:9003")


def build_gateway_locust_grpc_client(environment: Environment) -> Channel:
    """
    Фабричная функция для создания gRPC-канала, адаптированного для Locust.
    В канал автоматически встраивается интерцептор LocustInterceptor,
    который регистрирует вызовы в системе метрик Locust.

    :param environment: Среда выполнения Locust (необходима для отправки событий).
    :return: gRPC-канал с интерцептором, пригодный для нагрузочного тестирования.
    """
    # Создаём экземпляр интерцептора, передаём в него окружение Locust
    locust_interceptor = LocustInterceptor(environment=environment)

    # Создаём обычный канал
    channel = insecure_channel("localhost:9003")

    # Оборачиваем канал интерцептором, чтобы все запросы проходили через него
    return intercept_channel(channel, locust_interceptor)
