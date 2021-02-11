from cerberus import Validator
from datetime import datetime

# - CreditCardNumber (mandatory, string, it should be a valid credit card number)
# - CardHolder: (mandatory, string)
# - ExpirationDate (mandatory, DateTime, it cannot be in the past)
# - SecurityCode (optional, string, 3 digits)
# - Amount (mandatoy decimal, positive amount)

to_date = lambda s: datetime.strptime(s, "%Y-%m")

schema = {
    "credit_card_number": {"type": "string", "regex": "[0-9]+", "minlength": 16, "maxlength": 16, "required": True},
    "card_holder": {"type": "string", "maxlength": 255, "required": True},
    "expiration_date": {"type": "datetime", "coerce": to_date, "required": True},
    "security_code": {"type": "string", "regex": "[0-9]+", "minlength": 3, "maxlength": 3, "required": False},
    "amount": {"type": "integer", "min": 1, "required": True}
}
schema_validate = Validator(schema)
