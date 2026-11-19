def main():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            break
    meow(n)

def meow(n):
    for _ in range(n):
        print("Meow")