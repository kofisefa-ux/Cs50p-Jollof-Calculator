def main():
    n = get_number()
    block(n)

def block(n):
    for _ in range(n):
        print("#")

def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            break
    return n

main()