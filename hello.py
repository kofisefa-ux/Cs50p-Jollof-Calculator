def main():
    age = float(input("Enter your age: "))
    days = age * 365.25
    weeks = days / 7
    months = age * 12
    print(f"You have lived for approximately {days:.2f} days, {weeks:.2f} weeks, and {months:.2f} months.")

main()