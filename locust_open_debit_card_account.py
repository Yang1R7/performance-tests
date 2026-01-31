from locust import User, task, task, between

from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema


class CreateUserResponseSchem:
    pass


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    users_gateway_client: UsersGatewayHTTPClient
    create_user_response: CreateUserResponseSchema
    accounts_gateway_client: AccountsGatewayHTTPClient

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)


    @task
    def open_debit_card(self):
        self.accounts_gateway_client.open_debit_card_account(user_id=self.create_user_response.user.id)
