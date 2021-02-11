from datetime import datetime
from stripe import issuing, Token, Charge
from os import environ

STRIPE_SK_KEY = environ.get('SK_KEY').strip()


# - PremiumPaymentGateway
# - ExpensivePaymentGateway
# - CheapPaymentGateway


class PaymentGateway:
    def __init__(self, card_number, card_holder, exp_month, exp_year, cvc, amount):
        self.card_number = card_number
        self.card_holder = card_holder
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.cvc = cvc
        self.amount = amount

    def make_payment(self):
        holder = None
        try:
            holder = issuing.Cardholder.create(
                type="individual",
                name=self.card_holder,
                api_key=STRIPE_SK_KEY,
                billing={
                    "address": {
                        "line1": "Jhangirpura",
                        "city": "Surat",
                        "state": "Gujarat",
                        "country": "IN",
                        "postal_code": "395005",
                    }
                }
            )
        except Exception as e:
            print(e)

        token = Token.create(
            card={
                "number": self.card_number,
                "exp_month": self.exp_month,
                "exp_year": self.exp_year,
                "cvc": self.cvc
            },
            api_key=STRIPE_SK_KEY
        )

        charge = Charge.create(
            amount=self.amount,
            currency="inr",
            source=token.id,
            description=f"[{datetime.now().isoformat()}] holder_obj = {holder} holder_name={self.card_holder}",
            api_key=STRIPE_SK_KEY
        )

        return charge
