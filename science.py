def main():
    days = int(input("Enter number of days: "))
    seconds = convert_to_seconds(days)
    print(f"{days} days is equal to {seconds} seconds.")

def convert_to_seconds(days):
    seconds = days * 24 * 60 * 60
    return seconds
main()
