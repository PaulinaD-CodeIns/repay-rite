from calculator import (
    calculate_monthly_payment,
    calculate_total_repayment,
    calculate_total_interest,
)

def main():
    print("Welcome to RepayRite!")

    try:
        principal = float(input("Enter the loan amount (Principal): £"))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        loan_term_years = int(input("Enter the loan term in years: "))

        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, loan_term_years)
        total_repayment = calculate_total_repayment(monthly_payment, loan_term_years)
        total_interest = calculate_total_interest(total_repayment, principal)

        print(f"\nYour monthly payment is: £{monthly_payment:,.2f}")
        print(f"Total repayment over {loan_term_years} years: £{total_repayment:,.2f}")
        print(f"Total interest paid: £{total_interest:,.2f}")

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
