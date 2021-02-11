# test_hello_add.py
from app import app
from flask import json


# run test via py.test command
def test_add():        
    response = app.test_client().post(
        '/process_payment',
        data=json.dumps({
            "credit_card_number":"4242424242424242",
            "card_holder": "sssfsdfsfsf",
            "expiration_date": "2021-05",
            "security_code": "123",
            "amount": 2000
        }),
        content_type='application/json',
    )
    print(response)
    assert response.status_code == 201
