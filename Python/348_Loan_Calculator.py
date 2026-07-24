# 24-07-2026 | 24-07-2026

def get_loan_schedule(loan_amount, annual_rate, monthly_payment):
    balance = loan_amount
    result = [round(balance)]

    rate = (annual_rate / 100) / 12

    while balance > 0:
        balance = balance + balance * rate
        balance = balance - monthly_payment

        if balance < 0:
            balance = 0

        result.append(round(balance))

    return result
