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

create_deposit_account_response_data = open_debit_account_response.json()

print("Create deposit account response:", create_deposit_account_response_data)
print("Status code:", open_debit_account_response.status_code)

issue_virtual_card_payload = {
    "userId": crate_user_response_data["user"]["id"],
    "accountId": create_deposit_account_response_data["account"]["id"],
}
issue_virtual_card_response = client.post("/api/v1/cards/issue-virtual-card",
                                          json=issue_virtual_card_payload)

issue_virtual_card_response_data = issue_virtual_card_response.json()

print("Issue virtual card response:", issue_virtual_card_response_data)
print("Status code:", issue_virtual_card_response.status_code)