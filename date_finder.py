from datetime import datetime, timedelta

def past_12_months():
    current_date = datetime.now()
    months = []
    for i in range(1, 13):
        past_month = current_date - timedelta(days=i*30)
        months.append(past_month.strftime("%Y-%m"))

    return months

months_list = past_12_months()
print(months_list)
