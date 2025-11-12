import sys

def calculate_simple_interest(Principal, Rate, Time):
    """Calculate Simple Interest given principal, rate, and time."""
    return (Principal * Rate * Time) / 100

if __name__ == "__main__":
    print("Simple Interest Calculator:")

    try:
        if len(sys.argv) == 4:
            # Case 1: Arguments passed from command line
            P = float(sys.argv[1])
            R = float(sys.argv[2])
            T = float(sys.argv[3])
        else:
            # Case 2: No arguments passed — take input from user
            P = float(input("Enter the principal amount: "))
            R = float(input("Enter the rate of interest (%): "))
            T = float(input("Enter the time (in years): "))

        print("\nProgram parameters:")
        print("Principal Amount:", P)
        print("Rate of Interest:", R)
        print("Time in years:", T)

        interest = calculate_simple_interest(P, R, T)
        print(f"\nSimple Interest = {interest:.2f}")

    except ValueError:
        print("Error: Please enter valid numeric values for principal, rate, and time.")
