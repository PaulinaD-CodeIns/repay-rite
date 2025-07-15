




def calculate_monthly_payment(principal, annual_interest_rate, loan_term_years):
    """
    Calculate the monthly mortgage payment using the standard formula.

    Args:
        principal (float): Loan amount in UK Pound Sterling
        annual_interest_rate (float): Annual interest rate in percent (e.g., 3.5)
        loan_term_years (int): Loan term in years (e.g., 30)

    Returns:
        float: Monthly repayment amount
    """
    # Conversion to monthly
    monthly_rate = annual_interest_rate / 100 / 12
    total_payments = loan_term_years * 12

    if monthly_rate == 0:
        return principal / total_payments 

    monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / \
                      ((1 + monthly_rate) ** total_payments - 1)
    
    return monthly_payment