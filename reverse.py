# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    digits = list(str(n))
    digits.reverse()
    numbers = [int(x) for x in digits]
    return numbers


print(digitize(45678))

# Write a function that accepts an integer n and a string s as parameters,
#  and returns a string of s repeated exactly n times.


def repeated_str(n, s):
    return s * n


a = repeated_str(10, 'lole')
print(a)

# Removing spaces from string


def no_space(s):
    return s.replace(' ', '')


test = no_space('hfg kkfjjf ifikkf j')
print(test)
