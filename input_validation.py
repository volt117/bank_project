def validate_numeric_input(value, min_value=None, max_value=None):
    """
    Перевіряє числове значення на коректність та допустимий діапазон.
    Повертає число або повідомлення про помилку.
    """
    try:
        num_value = float(value)
    except ValueError:
        return "Помилка: Введене значення не є числом."

    if min_value is not None and num_value < min_value:
        return f"Помилка: Значення має бути не менше {min_value}."
    if max_value is not None and num_value > max_value:
        return f"Помилка: Значення має бути не більше {max_value}."

    return int(num_value) if num_value.is_integer() else num_value

def get_user_input(prompt, min_value=None, max_value=None):
    """
    Запитує введення користувача та перевіряє його на валідність.
    """
    while True:
        user_input = input(prompt)
        result = validate_numeric_input(user_input, min_value, max_value)
        if isinstance(result, (int, float)):
            return result
        else:
            print(result)