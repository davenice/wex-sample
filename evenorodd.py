
# returns the word 'even' if the provided number is even, or 'odd' if it's odd
def even_or_odd(number):
    result = number%2
    if result == 0:
        return "even"
    else:
        return "odd"
