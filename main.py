def find_n(x, y):
    # number that we are dividing
    z = float(int(x) * int(y))

    # makes a list of digits in y
    y_digits = [int(y) for y in y]

    # creates the decimal portion of the number
    r = ""
    for i in range(len(y) - 1):
        r = r + str(y_digits[i + 1])

    """ first part creates the final number,
    adding the decimal portion to the end of a 1
    the second part divides decimal portion of number 
    by first digit of second number and removes the decimal point """
    n = float("1." + str(int(r) / y_digits[0]).replace(".", ""))

    # checks to make sure n works even if Python isn't precise enough
    q = round((z / n), 2)

    print("\nCHECKING\n")
    print("x * y = z\n")
    print("z =", str(z))
    print("q =", str(q))
    print("n =", str(n), "\n")
    print("z / n = q")
    
    return n


x = input("X value : ")
y = input("Y value : ")

if __name__ == "__main__":
    find_n(x, y)
