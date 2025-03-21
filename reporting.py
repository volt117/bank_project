from datetime import datetime, timedelta

def generate_monthly_report(transactions, year, month):
    start_date = datetime(year, month, 1)
    next_month = start_date + timedelta(days=32)
    end_date = next_month.replace(day=1) - timedelta(days=1)

    report = []
    total_income = 0
    total_expenses = 0

    for t_id, t_data in transactions.items():
        trans_date = datetime.strptime(t_data['date'], "%Y-%m-%d")
        if start_date <= trans_date <= end_date:
            amount = transactions[t_id]['amount']
            category = transactions[t_id]['category']
            report.append(f"ID: {t_id}, сума: {amount}, дата: {transactions[t_id]['date']}, категорія: {category}")
            if amount > 0:
                total_income += amount
            else:
                total_expenses += abs(amount)

    summary = (
        f"\nЗвіт за {year}-{month}:\n"
        f"Загальний дохід: {total_income}\n"
        f"Загальні витрати: {total_expenses}\n"
    )

    return "\n".join(report) + summary

def export_report_to_file(report, filename):
    with open(filename, 'w') as f:
        f.write(report)
    print(f"Звіт збережено у файл '{filename}'")