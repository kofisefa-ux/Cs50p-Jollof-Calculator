def main():
    while True:
        money = get_money()
        interest = float(input("What is your interest in %? "))
        time = float(input("How long are you investing? "))
        total = calculate_total(money, interest, time)
        print(f"Total after {time} years = ${total:.2f}")

        while True:
            end = input("Would you like to reinvest? ").strip().lower()
            if end == "yes" or end == "y":
                break
            elif end == "no" or end == "n":
                return
def get_money():
    while True:
        n = float(input("How much are you investing? "))
        if n > 0:
            return n
        print("Money must be greater than 0.")


def calculate_total(money, interest, time):
    earned_interest = money * (interest / 100) * time
    return money + earned_interest

main()
