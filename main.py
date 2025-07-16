from calculator import (
    calculate_monthly_payment,
    calculate_total_repayment,
    calculate_total_interest,
    calculate_impact_of_extra_payments,
)

#Second section - working out extra monthly payments and their effect on loan term, amount and interest saved
def handle_extra_payments(principal, annual_interest_rate, loan_term_years, monthly_payment):
    extra = input( "Are you aware that not all mortgage lenders allow extra monthly payments without conditions, "
    "and some require permission or specific contract terms? Would you still like to explore this option? (yes/no): ").strip().lower()

    if extra == "yes":
        try:
            extra_payment = float(input("Enter the extra monthly payment amount: £"))
            results = calculate_impact_of_extra_payments(principal, annual_interest_rate, loan_term_years, extra_payment)

            years = results["new_months"] // 12
            months = results["new_months"] % 12

            print("\nWITH EXTRA PAYMENTS:")
            print(f"New Monthly Payment (including extra): £{results['actual_monthly_outgoing']:,.2f}")
            print(f"New Loan Term: {results['new_months']} months ({years} years and {months} months)")
            print(f"Total Payment with Extra: £{results['total_paid']:,.2f}")
            print(f"Interest Saved: £{results['interest_saved']:,.2f}")

        except ValueError:
            print("Invalid input for extra payments.")
    else:
        print("No extra payments applied.")


# First section - working out monthly mortgage repayment amount, total mortgage due, and interest inccurred
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

        next_section = input("\nWould you like to explore how extra monthly payments could reduce your loan term? (yes/no): ").strip().lower()

        if next_section == "yes":
            handle_extra_payments(principal, annual_interest_rate, loan_term_years, monthly_payment)
        else:
            print("\nThank you for using RepayRite. Goodbye!")

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
