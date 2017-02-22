# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:
#   1. If the number is a multiple of 4, print out a different message.
#   2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a
# different appropriate message.


def even_odd(n):
    """
    ...
    """
    if n % 4 == 0:
        print("This number is can be divided by 4!")
    elif n % 2 == 0:
        print("This number is EVEN!")
    else:
        print("This number is ODD!")


def check_(num, check):
    """
    ...
    """
    if num % check == 0:
        print(num, "can be divided evenly by", check, ".")
    else:
        print(num, "can not be divided evenly by", check, ".")


if __name__ == "__main__":
    num = "Give me one number to check: "
    check = "Give me one number to divide by check: "
    even_odd(num)
    even_odd(check)
    check_(num, check)
