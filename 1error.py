class InvalidInputError(Exception):
    def __init__(self, message="Некоректне введення. Очікується число."):
        self.message = message
        super().__init__(self.message)

class OutOfRangeError(Exception):
    def __init__(self, message="Число виходить за межі допустимого діапазону."):
        self.message = message
        super().__init__(self.message)

def get_user_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                raise OutOfRangeError(f"Число має бути не менше {min_value}.")
            if max_value is not None and value > max_value:
                raise OutOfRangeError(f"Число має бути не більше {max_value}.")
            return value
        except ValueError:
            print("Помилка: Очікується числове значення.")
        except OutOfRangeError as e:
            print(f"Помилка: {e}")
        except InvalidInputError as e:
            print(f"Помилка: {e}")


min_age = 18
max_age = 99
user_age = get_user_input(f"Введіть свій вік (від {min_age} до {max_age}): ", min_value=min_age, max_value=max_age)
print(f"Ваш вік: {user_age}")