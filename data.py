import requests

parameters = {
    "type" : "boolean",
    "amount": 10,
    "category": 18,
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
