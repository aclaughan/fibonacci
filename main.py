import logging

logging.basicConfig(level=logging.INFO, filename="app.log")

NUMBER_OF_FIBS = 27


def main():
    print("--[while loop]-------")
    while_fib(NUMBER_OF_FIBS)

    print("\n\n--[recursion]--------")
    for x in range(NUMBER_OF_FIBS):
        print(f"{recur_fib(x)}, ", end='')

    print()


def recur_fib(number):
    if number <= 1:
        return number
    else:
        return (recur_fib(number - 1) + recur_fib(number - 2))


def while_fib(number):
    x = 0
    y = 1

    while number:
        print(f"{x}, ", end='')
        z = x + y
        x = y
        y = z
        number -= 1


if __name__ == '__main__':
    main()

# logging.debug(stuff)


