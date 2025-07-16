from calculator import (
    calculate_monthly_payment,
    calculate_total_repayment,
    calculate_total_interest,
    calculate_impact_of_extra_payments,
    simulate_refinancing,
)


# Second section - extra monthly payments and their effect
def handle_extra_payments(principal, annual_interest_rate, loan_term_years, monthly_payment, total_repayment):
    extra = input(
        "Are you aware that not all mortgage lenders allow extra monthly payments without conditions, "
        "and some require permission or specific contract terms? Would you still like to explore this option? (yes/no): "
    ).strip().lower()

    if extra == "yes":
        try:
            extra_payment = float(input("Enter the extra monthly payment amount: £"))
            results = calculate_impact_of_extra_payments(
                principal, annual_interest_rate, loan_term_years, extra_payment
            )

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


# Third section - refinancing simulation
def handle_refinancing(principal, original_total_repayment):
    try:
        print("\nREFINANCING SIMULATION:")
        new_rate = float(input("Enter the new annual interest rate (in %): "))
        new_term = int(input("Enter the new loan term in years: "))

        results = simulate_refinancing(
            principal, new_rate, new_term, original_total_repayment
        )

        print("\nRESULTS OF REFINANCING:")
        print(f"New Monthly Payment: £{results['new_monthly_payment']:,.2f}")
        print(f"New Total Repayment: £{results['new_total_repayment']:,.2f}")
        print(f"New Total Interest: £{results['new_total_interest']:,.2f}")

        if results["interest_difference"] > 0:
            print(f"You would save £{results['interest_difference']:,.2f} in interest compared to your original plan.")
        else:
            print(f"This refinancing would cost you an extra £{abs(results['interest_difference']):,.2f} in interest.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


# First section - basic mortgage calculation
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

        # Extra payments section
        extra_section = input(
            "\nWould you like to explore how extra monthly payments could reduce your loan term? (yes/no): "
        ).strip().lower()

        if extra_section == "yes":
            handle_extra_payments(
                principal, annual_interest_rate, loan_term_years, monthly_payment, total_repayment
            )

        # Refinancing section
        refinance_section = input(
            "\nWould you like to explore how refinancing might impact your repayment? (yes/no): "
        ).strip().lower()

        if refinance_section == "yes":
            handle_refinancing(principal, total_repayment)

        print("\nThank you for using RepayRite. Goodbye!")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
