from locust import HttpUser, task, task, between

from tools.fakers import fake



class OpenDebitCardUser(HttpUser):
    wait_time = between(1, 3)
    user_data: dict


    def on_start(self) -> None:
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number(),
        }
        response = self.client.post("/api/v1/users", json=request)
        self.user_data = response.json()

    @task
    def open_debit_card(self):
        self.client.post("/api/v1/accounts/open-debit-card-account", json=self.user_data['user']['id'])
