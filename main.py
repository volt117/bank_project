from user_management import register_user, authenticate_user
from finance import add_transaction, edit_transaction, delete_transaction, calculate_total
from budget import create_budget_tracker, track_expense, update_budget, get_remaining_budget
from currency_management import set_exchange_rate, convert_currency, get_exchange_rate
from datetime_management import days_until_end_of_month, days_until_end_of_week, calculate_daily_budget
from logging_management import log_transaction, log_error
from input_validation import get_user_input

def main():
    while True:
        print("\nОберіть опцію:")
        print("1 - Реєстрація")
        print("2 - Авторизація")
        print("3 - Додати транзакцію")
        print("4 - Розрахунок бюджету")
        print("0 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            username = input("Ім'я користувача: ")
            password = input("Пароль: ")
            register_user(username, password)

        elif choice == "2":
            username = input("Ім'я користувача: ")
            password = input("Пароль: ")
            if authenticate_user(username, password):
                print("Авторизація успішна.")

        elif choice == "3":
            transaction_id = input("ID транзакції: ")
            amount = float(input("Сума: "))
            currency = input("Валюта: ")
            date = input("Дата (YYYY-MM-DD): ")
            category = input("Категорія: ")

            try:
                converted_amount = convert_currency(amount, currency, "USD")
                add_transaction(transaction_id, converted_amount, date, category)
                log_transaction(transaction_id, converted_amount, "USD", category)
            except Exception as e:
                log_error(e, "Додавання транзакції")

        elif choice == "4":
            monthly_budget = get_user_input("Загальний місячний бюджет: ", 0)
            spent_so_far = calculate_total()
            daily_budget, days_left = calculate_daily_budget(monthly_budget, spent_so_far)
            print(f"Залишок бюджету на день: {daily_budget:.2f}, Днів до кінця місяця: {days_left}")

        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невідомий вибір. Повторіть спробу.")

        print("\n---\n")

if __name__ == "__main__":
    main()