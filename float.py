
def f(string):
    """
    :converts strings to floating-point numbers.
    """
    try:
        return float(string)
    except ValueError:
        print("could not convert string to a float")

#to use, put any number inside the brackets remember to put quotes around the numbers!
c = f("")
print(c)
