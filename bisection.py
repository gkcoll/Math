"""
Description: The Implementation of Bisection Method by Python.
Writed by @灰尘疾客
Date: 2022/11/26
"""
# from math import log


def f(x):
    x = float(x)
    # You need to define the math function that you want to calculate here first.
    # The function expression should be a program expression, that is, shortcuts such as omitting the multiplication sign cannot be used.
    
    # y = 2**x + 3*x - 7  # exponential function test
    # y = log(x) + 2 * x - 6  # logarithmic function test
    # y = x ** 3 + 1.1 * x ** 2 + 0.9 * x - 1.4  # A question in textbook..
    # y = 1 * x  # linear function test
    # y = 3 - log(x, 10) - x  # A question in textbook
    # y = log(x) - 2 / x  # A question in textbook

    # Example:
    y = x

    return y


def main():  # Define the main function
    epsilon = float(input("ε= "))  # Accuracy
    a = float(input("a="))  # Start of range
    b = float(input("b="))  # End of range

    if a % 1 == 0:
        a = int(a)
    if b % 1 == 0:
        b = int(b)

    # All outputs will form a mathematical proof process,
    # so the program can "Solve" math problems (only bisection method).
    while abs(a-b) >= epsilon:  # Judge whether the absolute value of a-b is less than the accuracy.

        c = (a+b)/2  # Get the midpoint.
        if c % 1 == 0:
            c = int(c)
        else:
            pass
        print("c=("+str(a) + "+" + str(b)+")/2="+str(c))

        if f(a) * f(c) < 0:
            # If f(a)f(c) < 0, assign c to b.
            print("∵f(a)f(c)=" + str(f(a)) + "×" +
                  str(f(c)) + "=" + str(f(a)*f(c)) + "<0")
            b = c
            print("∴b=c=" + str(b))
        else:
            if f(c) == 0:
                # If f(c) = 0, assign c to a and break the looping, then print the zero point: x = a.
                print("∵f(c)=0")
                a = c
                print("∴a=c=" + str(a))
                break
            else:
                # If f(c) > 0, assign c to a and continue looping.
                # print("∵f(c)="+str(f(c)) +">0")
                print("∵f(b)f(c)=" + str(f(b)) + "×" +
                      str(f(c)) + "=" + str(f(b)*f(c)) + "<0")
                a = c
                print("∴a=c=" + str(a))

        # Output the zero point range.
        print("∴x₀∈""(" + str(a) + "," + str(b) + ")")

    if abs(a - b) < epsilon:
        print("∵|" + str(a) + "-" + str(b) + "|"+"<"+str(epsilon))
    

    x = a
    if x % 1 == 0:
        x = int(x)
    else:
        pass
    print("∴x=a=" + str(x))


if __name__ == "__main__":
    main()
