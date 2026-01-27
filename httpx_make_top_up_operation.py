import httpx
import time

client = httpx.Client(base_url="http://localhost:8003")
create_user_payload = {
    "email": f"user{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = client.post("/api/v1/users", json=create_user_payload)
crate_user_response_data = create_user_response.json()

print("Create user response:", crate_user_response_data)
print("Status code:", create_user_response.status_code)

open_debit_account_payload = {
    "userId": crate_user_response_data["user"]["id"],
}
open_debit_account_response = client.post(
    "/api/v1/accounts/open-debit-card-account",
    json=open_debit_account_payload
)

open_debit_account_response_data = open_debit_account_response.json()

make_top_up_operation_payload = {
  "status": "COMPLETED",
  "amount": 1110,
  "cardId": open_debit_account_response_data["account"]["cards"][0]["id"],
  "accountId": open_debit_account_response_data["account"]["id"],
}
make_top_up_operation_response = client.post(
    "/api/v1/operations/make-top-up-operation",
        json=make_top_up_operation_payload)

make_top_up_operation_response_data = make_top_up_operation_response.json()
print("Make top up operation response:", make_top_up_operation_response_data)
print("Status code:", make_top_up_operation_response.status_code)