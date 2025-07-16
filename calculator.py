#All the calculations, keeping math seperate to it's easier to amend.

def calculate_monthly_payment(principal, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / 100 / 12
    number_of_payments = loan_term_years * 12

    if monthly_interest_rate == 0:
        monthly_payment = principal / number_of_payments
    else:
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments) / ((1 + monthly_interest_rate)**number_of_payments - 1)

    return monthly_payment


def calculate_total_repayment(monthly_payment, loan_term_years):
    return monthly_payment * loan_term_years * 12


def calculate_total_interest(total_repayment, principal):
    return total_repayment - principal