transactions = {}
exchange_rates = {
    'USD': 1.0,      # базова валюта
    'EUR': 0.93,
    'UAH': 38.0,
    'PLN': 4.0
}

def convert_currency(amount, from_currency, to_currency='USD'):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Невідома валюта")
    amount_usd = amount / exchange_rates[from_currency]
    return amount_usd * exchange_rates[to_currency]

def add_transaction(transaction_id, amount, date, category, currency='USD'):
    if transaction_id in transactions:
        print("Трансакція з таким ІД вже існує")
    else:
        amount_usd = convert_currency(amount, currency)
        transactions[transaction_id] = {
            "amount": amount,
            "amount_usd": amount_usd,
            "currency": currency,
            "date": date,
            "category": category,
        }
        print(f"Трансакція {transaction_id} успішно додана у валюті {currency} (USD: {amount_usd:.2f})")
       
def edit_transaction(transaction_id, amount=None, date=None, category=None, currency=None):
    if transaction_id in transactions:
        if amount and currency:
            transactions[transaction_id]['amount'] = amount
            transactions[transaction_id]['currency'] = currency
            transactions[transaction_id]['amount_usd'] = convert_currency(amount, currency)
        if date:
            transactions[transaction_id]['date'] = date
        if category:
            transactions[transaction_id]['category'] = category
        print(f"Транзакція {transaction_id} успішно відредагована.")
    else:
        print("Транзакція з таким ID не знайдена.")

def delete_transaction(transaction_id):
    if transaction_id in transactions:
        del transactions[transaction_id]
        print(f"Транзакція {transaction_id} успішно видалена.")
    else:
        print("Транзакція з таким ID не знайдена.")

def calculate_total(category=None, currency='USD', index=0, total=0):
    keys = list(transactions.keys())
    if index == len(keys):
        return convert_currency(total, 'USD', currency)
    if category:
        if transactions[keys[index]]['category'] == category:
            total += transactions[keys[index]]['amount_usd']
    else:
        total += transactions[keys[index]]['amount_usd']
    return calculate_total(category, currency, index + 1, total)