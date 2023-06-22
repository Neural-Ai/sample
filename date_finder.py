from datetime import datetime
from dateutil.relativedelta import relativedelta

def past_12_months():
    current_date = datetime.now()
    months = []
    for i in range(1, 13):
        past_month = current_date - relativedelta(months=i)
        months.append(past_month.strftime("%Y-%m"))

    return months

months_list = past_12_months()
print(months_list)
