import requests

BASE_URL = "http://localhost:8000/transactionservice"


def test_put_transaction(transaction_id, amount, type_, parent_id=None):
    url = f"{BASE_URL}/transaction/{transaction_id}"
    payload = {"amount": amount, "type": type_, "parent_id": parent_id}
    response = requests.put(url, json=payload)
    print(f"PUT {url}: {response.status_code}")
    print(f"PUT {url}: {response.json()}")


def test_get_transaction(transaction_id):
    url = f"{BASE_URL}/transaction/{transaction_id}"
    response = requests.get(url)
    print(f"GET {url}: {response.json()}")


def test_get_transactions_by_type(type_):
    url = f"{BASE_URL}/types/{type_}"
    response = requests.get(url)
    print(f"GET {url}: {response.json()}")


def test_get_sum(transaction_id):
    url = f"{BASE_URL}/sum/{transaction_id}"
    response = requests.get(url)
    print(f"GET {url}: {response.json()}")


def main():
    # Test creating transactions
    test_put_transaction(10, 5000, "cars")
    test_put_transaction(502, 10000, "shopping", parent_id=10)

    # Test retrieving transactions
    test_get_transaction(502)
    test_get_transaction(10)

    # Test retrieving transactions by type
    test_get_transactions_by_type("cars")

    # Test retrieving sum of transactions
    test_get_sum(10)
    test_get_sum(502)


if __name__ == "__main__":
    main()
