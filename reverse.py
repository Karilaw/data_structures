# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    digits = list(str(n))
    digits.reverse()
    numbers = [int(x) for x in digits]
    return numbers


print(digitize(45678))
