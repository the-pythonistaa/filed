# using flask_restful
from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from utils import PaymentGateway
from validation import schema_validate, to_date

from os import environ
# creating the flask app
app = Flask(__name__)
app.config.from_object(environ.get('APP_SETTINGS'))

# creating an API object
api = Api(app)


class ProcessPayment(Resource):

    def post(self):
        data = request.get_json()  # status code
        if not data:
            return make_response(jsonify({"error": "Invalid payment process requested"}), 400)
        if not schema_validate.validate(data):
            return make_response(jsonify({"error": schema_validate.errors}), 400)

        dt_obj = to_date(data['expiration_date'])
        card_number = data['credit_card_number']
        card_holder = data['card_holder']
        exp_month = dt_obj.month
        exp_year = dt_obj.year
        cvc = data['security_code']
        amount = data['amount']

        payment = PaymentGateway(card_number, card_holder, exp_month, exp_year, cvc, amount)
        response = payment.make_payment()

        return make_response(jsonify({'response': response, "error": schema_validate.errors}), 201)


# URLs list
api.add_resource(ProcessPayment, '/process_payment')

if __name__ == '__main__':
    app.run(debug=True)