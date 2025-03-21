categories = {}
categories = {}

def create_budget_tracker(category, budget):
    categories[category] = {
        "budget": budget,
        "spent": 0
    }

def update_budget(category, new_budget):
    if category in categories:
        categories[category]["budget"] = new_budget
        print(f"Бюджет для категорії '{category}' оновлено до {new_budget}")
    else:
        print(f"Категорія '{category}' не знайдена.")

def track_expense(category, amount):
    if category in categories:
        categories[category]["spent"] += amount
        budget = categories[category]["budget"]
        spent = categories[category]["spent"]
        if spent > budget:
            print(f"⚠️ Бюджет перевищено у категорії '{category}'! Витрачено: {spent}, Ліміт: {budget}")
        else:
            print(f"✅ Витрати у категорії '{category}': {spent}/{budget}")
    else:
        print(f"Категорія '{category}' не знайдена.")

def get_remaining_budget(category):
    if category in categories:
        budget = categories[category]["budget"]
        spent = categories[category]["spent"]
        remaining = budget - spent
        print(f"📌 Залишок бюджету у категорії '{category}': {remaining}")
        return remaining
    else:
        print(f"Категорія '{category}' не знайдена.")
        return None