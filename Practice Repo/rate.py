def main():
    money = get_money()
    interest = int(input("What is your interest in %? "))
    time = int(input("How long are you investing? "))
    total = calculate_total(money, interest, time)
    print(f"Total after {time} years = ${total:.2f}")
def get_money():
    while True:
        n = int(input("How much are you investing? "))
        if n > 0:
            return n
        print("Money must be greater than 0.")
def calculate_total(money, interest, time):

    earned_interest = money * (interest / 100) * time
    return money + earned_interest