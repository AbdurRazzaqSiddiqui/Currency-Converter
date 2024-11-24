from flask import Blueprint, request, render_template
import requests

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    conversion_result = None
    if request.method == 'POST':
        amount = request.form.get('amount', type=float)
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
        rates = response.json().get('rates')
        conversion_result = rates[to_currency] * amount
    return render_template('index.html', result=conversion_result)
