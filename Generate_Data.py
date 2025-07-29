import pandas as pd
import random
from datetime import datetime, timedelta

num_loans = 100000
loan_types = ['Home', 'Personal', 'Auto', 'Education', 'Gold']
loan_statuses = ['Active', 'Closed', 'Overdue']
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))


data = []
for i in range(1, num_loans + 1):
    loan_id = f"L{i:04}"
    customer_id = f"C{random.randint(1, 30):03}"
    loan_amount = random.randint(50000, 1000000)
    interest_rate = round(random.uniform(7.0, 14.5), 2)
    loan_type = random.choice(loan_types)
    tenure_months = random.choice([12, 24, 36, 48, 60])
    start_date = random_date(datetime(2020, 1, 1), datetime(2023, 12, 1))
    emi_amount = round((loan_amount * (1 + (interest_rate / 100))) / tenure_months, 2)
    months_passed = (datetime.today().year - start_date.year) * 12 + (datetime.today().month - start_date.month)
    emi_paid = min(months_passed, tenure_months)
    next_due_date = start_date + timedelta(days=30 * (emi_paid + 1))
    status = 'Closed' if emi_paid == tenure_months else random.choices(
        ['Active', 'Overdue'], weights=[0.8, 0.2])[0]

    data.append([
        loan_id, customer_id, loan_amount, interest_rate, loan_type,
        tenure_months, start_date.date(), emi_amount, emi_paid,
        next_due_date.date(), status
    ])

columns = [
    "loan_id", "customer_id", "loan_amount", "interest_rate", "loan_type",
    "tenure_months", "start_date", "emi_amount", "emi_paid_till_date",
    "next_due_date", "status"
]
df = pd.DataFrame(data, columns=columns)

df.to_csv("loan_data_1.csv", index=False)
print("✅ Mock loan data generated and saved as 'mock_loan_portfolio.csv'")
