import hashlib

users_db = {}

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def register_user(username, password):
    if username in users_db:
        print("Цей логін уже використовується. Оберіть інший.")
    else:
        users_db[username] = hash_password(password)
        print(f"Користувача {username} успішно зареєстровано.")

def authenticate_user(username, password):
    if username in users_db:
        hashed_password = hash_password(password)
        if users_db[username] == hashed_password:
            print(f"Ласкаво просимо, {username}!")
        else:
            print("Невірний пароль. Спробуйте ще раз.")
    else:
        print("Користувача з таким логіном не існує.")

def change_password(username, old_password, new_password):
    if username in users_db:
        if users_db[username] == hash_password(old_password):
            users_db[username] = hash_password(new_password)
            print(f"Пароль для користувача {username} успішно змінено.")
        else:
            print("Старий пароль невірний. Спробуйте ще раз.")
    else:
        print("Користувача з таким логіном не існує.")