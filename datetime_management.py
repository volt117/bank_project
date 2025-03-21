from datetime import datetime, timedelta

def days_until_end_of_month():
    today = datetime.today()
    next_month = today.replace(day=28) + timedelta(days=4)  # наступний місяць гарантовано
    end_of_month = next_month = next_month.replace(day=1) - timedelta(days=1)
    return (end_of_month - today).days

def days_until_end_of_week():
    today = datetime.today()
    days_to_end_of_week = 6 - today.weekday()
    return days_to_end_of_week

def calculate_daily_budget(budget, spent):
    days_left = days_until_end_of_month()
    daily_budget = (budget - spent) / days_left if days_left > 0 else 0
    return daily_budget, days_left