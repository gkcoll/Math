"""
Description: The Implementation of Bisection Method by Python.
Writed by @灰尘疾客
Date: 2022/12/10
"""
# from math import log


def f(x:float) ->float:
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


def legality(f, a, b):
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) have the same sign!")
        return False
    else:
        return True


def find_zero(f, a, b, eps):
    '''
    A function for find the zero point.
    Some code of this function is provided by ChatGPT(the logical body code).
    I just tried it after other's introduce, but the result make a big surprise to me.
    The neatness, logic and readability of the code are really better than those I wrote before.
    I sure it was also a good code refactoring tool for programmers(It can be compared with the Copilot)..
    ——The developer'''

    # Judge whether the absolute value of a-b is less than the accuracy.
    while abs(a - b) > eps:

        c = (a + b) / 2  # Get the midpoint.
        if c % 1 == 0:
            c = int(c)
        else:
            pass
        print("c=("+str(a) + "+" + str(b)+")/2="+str(c))

        if f(c) == 0:
            # If f(c) = 0, assign c to a and break the looping, then print the zero point: x = a.
            print("∵f(c)=0")
            a = c
            print("∴a=c=" + str(a))
            # return a
            break
        elif f(a) * f(c) < 0:
            # If f(a)f(c) < 0, assign c to b.
            print("∵f(a)f(c)=" + str(f(a)) + "×" +
                  str(f(c)) + "=" + str(f(a)*f(c)) + "<0")
            b = c
            print("∴b=c=" + str(b))
        else:
            # If f(c) > 0, assign c to a and continue looping.
            # print("∵f(c)="+str(f(c)) +">0")
            print("∵f(b)f(c)=" + str(f(b)) + "×" +
                  str(f(c)) + "=" + str(f(b)*f(c)) + "<0")
            a = c
            print("∴a=c=" + str(a))

        # Output the zero point range.
        print("∴x₀∈""(" + str(a) + "," + str(b) + ")")

    if abs(a - b) < eps:
        print("∵|" + str(a) + "-" + str(b) + "|"+"<"+str(eps))

    # return (a + b) / 2  # This line of code is write by ChatGPT.
    # But according to the textbook(General senior high textbook, Math, People's Education Press, China):
    # Because the exact value of the midpoint function is less than the specified exact value,
    # any point in the interval can be used as an approximation of the zero point.
    # But for convenience, we usually take an startpoint of the interval
    # as the approximate value of the zero point.
    return a


def main():
    '''Main function'''
    eps = float(input("ε= "))  # Accuracy
    a = float(input("a="))  # Start of range
    b = float(input("b="))  # End of range

    # Humanize the presentation of number values(a & b).
    if a % 1 == 0:
        a = int(a)
    if b % 1 == 0:
        b = int(b)

    # Judge the legality of the values.
    if legality(f, a, b):
        # All outputs will form a mathematical proof process,
        # so the program can "Solve" math problems (only bisection method).
        a = find_zero(f, a, b, eps)
        x = a
        if x % 1 == 0:
            x = int(x)
        print("∴x=a=" + str(x))
    else:
        pass


if __name__ == "__main__":
    main()
