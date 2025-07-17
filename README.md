



## UX

**RepayRite** is a command-line mortgage calculator designed to help users make informed decisions about their mortgage repayments. The interface is styled using color and tables to enhance usability, provide clarity, and deliver a professional experience. 

### Target Users

- First-time homebuyers exploring affordability
- Existing homeowners considering overpayments
- Borrowers curious about refinancing options
- Anyone seeking transparency around total repayment costs

### User Needs Addressed

- **Simplicity**: Step-by-step prompts guide the user clearly through each calculation process.
- **Transparency**: The app displays exact monthly payments, total interest paid, and overall repayment costs in a clear format.
- **Awareness**: The app includes realistic prompts to inform users that not all lenders allow extra payments without conditions.
- **Visual Clarity**: Using the `colorama` and `tabulate` libraries, results are color-coded and formatted in clean tables to improve readability in the terminal.

The user experience prioritises clarity, safety, and empowerment, especially for users who may be unfamiliar with mortgage

## Goals

The primary goal of **RepayRite** is to support users in understanding and managing their mortgage repayment journey through clear, accurate, and accessible terminal-based tools.

### User Goals

- Calculate standard monthly repayments based on inputted loan amount, interest rate, and loan term.
- Understand the long-term cost of the mortgage, including total interest and total repayment.
- Simulate how making **extra monthly payments** could reduce the overall loan term and interest paid.
- Explore **refinancing scenarios** to see how a new interest rate or loan term might improve or worsen repayment costs.
- Receive all results in a clean, color-enhanced, and table-formatted layout for easy interpretation.

### Developer Goals

- Build a modular and maintainable codebase using clean functions.
- Apply external Python libraries (`colorama`, `tabulate`) to enhance UI/UX in the command line.
- Include realistic prompts to educate users about mortgage conditions (e.g., limitations on overpayments).
- Ensure the application is **deployed and functional via Heroku**, and that it is accessible with no local setup required.

## Visual Design


- **Color Coding**: The `colorama` library is used to highlight key sections, warnings, results, and user prompts. For example:
  - Blue for headers and welcome messages.
  - Green for positive financial outcomes or savings.
  - Red for warnings, errors, or increased costs.
  - Yellow and magenta for informative sections.
  
- **Tabular Output**: The `tabulate` library formats key financial figures into clean, easy-to-read tables using the `fancy_grid` style, enhancing readability.

- **Whitespace & Sectioning**: Clear separation between input sections and results improves the flow of interaction, preventing cognitive overload.

- **Minimal Input, Maximum Clarity**: Users are only asked for essential inputs (e.g., loan amount, interest rate, term). Complex results are computed and displayed clearly, without requiring users to interpret raw math.

- **Accessibility Considerations**: 
  - All prompts and results are printed in plain English.
  - Symbols (like £ and %) are used consistently.
  - Tables prevent misreading or confusion around financial metrics.

This approach ensures RepayRite delivers a smooth user experience, even in a non-graphical environment.

## Features

RepayRite includes multiple core features designed to help users better understand and manage their mortgage repayments.

### Core Features

- **Monthly Repayment Calculator**
  - Calculates standard monthly repayments based on user input (loan amount, interest rate, and term).
  - Displays monthly payment, total repayment, and total interest in a formatted table.

- **Extra Monthly Payment Simulation**
  - Allows users to simulate how paying more each month can reduce the loan term and total interest paid.
  - Provides warnings that some lenders may require permission for extra payments.
  - Outputs updated repayment figures in a clearly tabulated format.

- **Refinancing Simulation**
  - Lets users enter a new interest rate and/or loan term to simulate refinancing scenarios.
  - Compares new repayment values to the original plan, highlighting potential savings or extra costs.

- **Clear Output and Styling**
  - Uses `colorama` for color-coded output to highlight warnings, savings, and key information.
  - Uses `tabulate` to present financial metrics in professional, easy-to-read tables.

- **User Guidance and Validation**
  - Input prompts are phrased in friendly, clear language.
  - Invalid inputs (e.g. text instead of numbers) are caught and handled with helpful error messages.

### User Journey

The user experience follows a logical path:

1. Welcome message.
2. Enter mortgage details.
3. View a breakdown of repayment details.
4. Optional: simulate extra monthly payments.
5. Optional: explore refinancing scenarios.
6. Receive a closing message of support.

This combination of functionality and guidance makes RepayRite practical, educational, and user-friendly.
