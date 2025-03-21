import logging
from datetime import datetime

# Налаштування логера
logging.basicConfig(
    filename="application.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def log_transaction(transaction_id, amount, currency, category):
    """
    Записує інформацію про транзакцію до логу.
    """
    message = (f"Транзакція ID: {transaction_id}, "
               f"Сума: {amount} {currency}, "
               f"Категорія: {category}")
    logging.info(message)

def log_error(exception, context=""):
    """
    Логує винятки (exceptions) з додатковим контекстом.
    """
    error_message = f"Помилка: {str(exception)}"
    if context:
        error_message += f" | Контекст: {context}"
    logging.error(error_message)