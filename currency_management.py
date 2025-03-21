exchange_rates = {
    'USD': 1.0  # валюта за замовчуванням
}

def set_exchange_rate(currency, rate):
    """
    Встановлює курс валюти відносно базової валюти (USD).
    """
    exchange_rates[currency.upper()] = rate
    print(f"Курс валюти {currency.upper()} встановлено як {rate}.")

def get_exchange_rate(currency):
    """
    Повертає курс вказаної валюти.
    """
    rate = exchange_rates.get(currency.upper())
    if rate is None:
        raise ValueError(f"Курс валюти {currency.upper()} не встановлено.")
    return rate

def convert_currency(amount, from_currency, to_currency):
    """
    Конвертує суму з однієї валюти в іншу.
    """
    from_rate = get_exchange_rate(from_currency)
    to_rate = get_exchange_rate(to_currency)
    converted_amount = amount * (to_rate / from_rate)
    print(f"{amount:.2f} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
    return converted_amount