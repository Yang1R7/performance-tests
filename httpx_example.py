import httpx


response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())


data = {
    "title": "New Task",
    "completed": False,
    "userId": 1
}
response = httpx.post("https://jsonplaceholder.typicode.com/todos")

print(response.status_code)
print(response.json())



client = httpx.Client(headers={"Content-Type": "application/json"})
response =client.get("https://jsonplaceholder.typicode.com/todos/1")
response1 =client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response.status_code)
print(response.json())
print(response1.status_code)
print(response1.json())
