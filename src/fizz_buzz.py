

def fizz_buzz(n: int) -> str:

    if n % 15 == 0:
        return "fizz buzz"
    elif n % 5 == 0:
        return "buzz"
    elif n % 3 == 0:
        return "fizz"
    else:
        return str(n)
