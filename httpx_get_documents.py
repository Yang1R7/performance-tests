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

open_credit_account_payload = {
    "userId": crate_user_response_data["user"]["id"],
}
open_credit_account_response = client.post(
    "/api/v1/accounts/open-credit-card-account",
    json=open_credit_account_payload
)

open_credit_account_response_data = open_credit_account_response.json()

print("Open credit account response:", open_credit_account_response_data)
print("Status code:", open_credit_account_response.status_code)


get_tariff_document_response = client.get(
    f"/api/v1/documents/tariff-document/"
    f"{open_credit_account_response_data["account"]["id"]}")

get_tariff_document_response_data = get_tariff_document_response.json()

print("Get tarif document response:", get_tariff_document_response_data)
print("Status code:", get_tariff_document_response.status_code)

get_contract_document_response = client.get(
    f"/api/v1/documents/contract-document/"
    f"{open_credit_account_response_data["account"]["id"]}")

get_contract_document_response_data = get_contract_document_response.json()

print("Get contract document response:", get_contract_document_response_data)
print("Status code:", get_contract_document_response.status_code)