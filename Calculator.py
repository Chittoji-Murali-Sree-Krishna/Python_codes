# importing math module as m
import math as m
# importing sys
import sys
# importing the required functions from module
from termcolor import colored, cprint
# importing time functions
import time
# importing random functions
from tqdm import tqdm, trange
# this for windows to show colors
import os


# defining colors , so that we can use again
def print_blue(x): return cprint(x, 'cyan', attrs=['bold'])

# class for basic rules so that we can call again with out entering codes again


class calculator:
    def __init__(self, name):
        self.name = name  # taking the name of the user

    # list of options for the calculator
    options = '0.prime-number', '1.addition', '2.sutraction', '3.multiply', '4.division', '5.even-odd', '6.range_of_numbers', '7.exponential-power', '8.fibonacci-series', '9.fibonacci_or_not', '10.constatns', '11.trignometry', '12.squareroot', '13.degrees&radians'
    # trignometric list
    subs = '1.cos', '2.sin', '3.tan', '4.cosh', '5.sinh', '6.tanh', '7.acosh', '8.asinh', '9.atanh'
    # degrees & radians
    degs = '1.Degrees to radians', '2.Radians to degrees'
    # it will be automatically called when ever a new object is called

    def rules(self):  # type of rules
        print("\u001b[34;1m hey",  self.name,
              "enter only the number aka integers")

    def error(self):  # String or charector insert instead of number
        print("\u001b[31;1m hey", self.name, "it is not a number, try again")

    def error1(self):  # if the option is not available
        print(
            "\u001b[31m hey", self.name, "this not a correct option, choose the proper one next time")

    def zeroerror(self):
        print("\u001b[34;1m hey",  self.name,
              "values connot be divided with zero")

    # num values start from here aka the values which you wanna print out and take in

    def inum(self):  # for int type input
        return int(input("\u001b[35m enter the value: "))

    def fnum1(self):  # for float type first input
        return float(input("\u001b[35m enter your first value: "))

    def fnum2(self):  # for float type second input
        return float(input("\u001b[35m enter your second value: "))

    def fnum(self):  # for float type only those need single input
        return float(input("\u001b[35m enter the value: "))

    def inum1(self):  # for int type used for options
        return int(input("\u001b[33;1m enter the option: "))

    def fnum3(self):
        return float(input("\u001b[35m enter your third value: "))

    def fnum4(self):
        return float(input("\u001b[35m enter your forth value: "))

    def fnum5(self):
        return float(input("\u001b[35m enter your fifth value: "))

    def fnum6(self):
        return float(input("\u001b[35m enter your sixth value: "))

    @classmethod
    def Options(cls):  # for options
        for option in cls.options:
            print("\u001b[32m", option)

    @classmethod
    def Subs(cls):  # for trignometry options
        for sub in cls.subs:
            print("\u001b[32m", sub)

    @classmethod
    def Deg(cls):  # for degrees and radians options
        for deg in cls.degs:
            print("\u001b[32m", deg)


class add_values:
    add = '1.add two-num', '2.add three-num', '3.add four-num', '4.add five-num', '5.add six-num', '6.more than six'

    @classmethod
    def adds(cls):
        for ad in cls.add:
            print("\u001b[32m", ad)

    @classmethod
    def Add(cls):  # for sum(2)
        return num1+num2

    @classmethod
    def Add1(cls):  # for sum(3)
        return (num1+num2)+num3

    @classmethod
    def Add2(cls):  # for sum(4)
        return ((num1+num2)+num3)+num4

    @classmethod
    def Add3(cls):  # for sum(5)
        return (((num1+num2)+num3)+num4)+num5

    @classmethod
    def Add4(cls):  # for sum(5)
        return ((((num1+num2)+num3)+num4)+num5)+num6


class sub_values:
    sub = '1.sub two-num', '2.sub three-num', '3.sub four-num', '4.sub five-num', '5.sub six-num', '6.more than six'

    @classmethod
    def subt(cls):
        for su in cls.sub:
            print("\u001b[32m", su)

    @classmethod
    def Subt(cls):  # for sub(2)
        return num1-num2

    @classmethod
    def Subt1(cls):  # for sub(3)
        return (num1-num2)-num3

    @classmethod
    def Subt2(cls):  # for sub(4)
        return ((num1-num2)-num3)-num4

    @classmethod
    def Subt3(cls):  # for sub(5)
        return (((num1-num2)-num3)-num4)-num5

    @classmethod
    def Subt4(cls):  # for sub(6)
        return ((((num1-num2)-num3)-num4)-num5)-num6


class mul_values:
    mul = '1.mul two-num', '2.mul three-num', '3.mul four-num', '4.mul five-num', '5.mul six-num', '6.more than six'

    @classmethod
    def mult(cls):
        for mu in cls.mul:
            print("\u001b[32m", mu)

    @classmethod
    def Mult(cls):  # for sub(2)
        return num1*num2

    @classmethod
    def Mult1(cls):  # for sub(3)
        return (num1*num2)*num3

    @classmethod
    def Mult2(cls):  # for sub(4)
        return ((num1*num2)*num3)*num4

    @classmethod
    def Mult3(cls):  # for sub(5)
        return (((num1*num2)*num3)*num4)*num5

    @classmethod
    def Mult4(cls):  # for sub(6)
        return ((((num1*num2)*num3)*num4)*num5)*num6


class div_values:
    div = '1.div two-num', '2.div three-num', '3.div four-num', '4.div five-num', '5.div six-num', '6.more than six'

    @classmethod
    def divs(cls):
        for di in cls.div:
            print("\u001b[32m", di)

    @classmethod
    def Div(cls):  # for sub(2)
        return num1/num2

    @classmethod
    def Div1(cls):  # for sub(3)
        return (num1/num2)/num3

    @classmethod
    def Div2(cls):  # for sub(4)
        return ((num1/num2)/num3)/num4

    @classmethod
    def Div3(cls):  # for sub(5)
        return (((num1/num2)/num3)/num4)/num5

    @classmethod
    def Mult4(cls):  # for sub(6)
        return ((((num1/num2)/num3)/num4)/num5)/num6


# private class

# for loading bar


def loading():
    for i in trange(10):
        time.sleep(0.1)  # if your system is slow increase the sleep time
    print()


# this is object for the class which is used to call the attributes of it
base = calculator(input("\u001b[37;1m your name: "))
fun = add_values()
# just for fun
loading()
# from here the actual part starts
print_blue(" %% some basic math functions %%")
# now we are calling the object here
calculator.rules(base)
# setting localtime
localtime = time.asctime(time.localtime(time.time()))
# this will print the time
print("\u001b[37;1m time :", localtime)
# just using it for gap
print(" ")
# list of options
calculator.Options()
# juat using this for gap
print(" ")


# catching the value errors
while True:
    try:
        option = calculator.inum1(base)
        break
    except ValueError:
        calculator.error(base)

# prime-number
if option == 0:
    print_blue("prime-number")
    while True:
        try:
            num = calculator.inum(base)
            break
        except ValueError:
            calculator.error(base)
    # num must be grater than 1 ,because when we try to run with 1 all the numbers get divided
    if num > 1:
        # taking i with range from 2 to given value , so that it keeps incrimenting from 2 - number which we have provided
        for i in range(2, num):
            # checking for the given number % i returns 0 or not
            if (num % i) == 0:
                # loading()
                print("\u001b[37;1m", num, " is not a prime number")
                break
        else:
            # loading()
            print("\u001b[37;1m", num, " is a prime number")
    else:
        # loading()
        print("\u001b[37;1m", num, " is a prime number")

# addition
elif option == 1:
    print_blue("addition")
    print("")
    add_values.adds()
    print("")

    while True:
        try:
            adds = calculator.inum1(base)
            break
        except ValueError:
            calculator.error(base)

    if adds == 1:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "+", num2, "=", add_values.Add())

    elif adds == 2:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "+", num2,
              "+", num3, "=", add_values.Add1())

    elif adds == 3:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "+", num2,
              "+", num3, "+", num4, "=", add_values.Add2())

    elif adds == 4:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num5 = calculator.fnum5(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "+", num2,
              "+", num3, "+", num4, "+", num5, "=", add_values.Add3())

    elif adds == 5:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num5 = calculator.fnum5(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num6 = calculator.fnum6(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "+", num2,
              "+", num3, "+", num4, "+", num5, "+", num6, "=", add_values.Add4())

    elif adds == 6:
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        result = 0
        while num > 0:
            digit = num % 10
            result = result + digit
            num = num // 10
        print(result)

    else:
        calculator.error1(base)

# subtraction
elif option == 2:
    print_blue("subtraction")
    print("")
    sub_values.subt()
    print("")

    while True:
        try:
            subt = calculator.inum1(base)
            break
        except ValueError:
            calculator.error(base)

    if subt == 1:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "-", num2, "=", sub_values.Subt())

    elif subt == 2:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "+", num2,
              "+", num3, "=", sub_values.Subt1())

    elif subt == 3:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "-", num2,
              "-", num3, "-", num4, "=", sub_values.Subt2())

    elif subt == 4:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num5 = calculator.fnum5(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "-", num2,
              "-", num3, "-", num4, "-", num5, "=", sub_values.Subt3())

    elif subt == 5:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num5 = calculator.fnum5(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num6 = calculator.fnum6(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "-", num2,
              "-", num3, "-", num4, "-", num5, "-", num6, "=", sub_values.Subt4())

    elif subt == 6:
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        result = 0
        while num > 0:
            digit = num % 10
            result = result - digit
            num = num // 10
        print(result)

    else:
        calculator.error1(base)

# multiplication
elif option == 3:
    print_blue("multiply")
    print("")
    mul_values.mult()
    print("")

    while True:
        try:
            mult = calculator.inum1(base)
            break
        except ValueError:
            calculator.error(base)

    if mult == 1:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "x", num2, "=", mul_values.Mult())

    elif mult == 2:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "x", num2,
              "x", num3, "=", add_values.Add1())

    elif mult == 3:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "x", num2,
              "x", num3, "x", num4, "=", mul_values.Mult2())

    elif mult == 4:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num5 = calculator.fnum5(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "x", num2,
              "x", num3, "x", num4, "x", num5, "=", mul_values.Mult3())

    elif mult == 5:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num5 = calculator.fnum5(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num6 = calculator.fnum6(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print(" \u001b[37;1m ", num1, "x", num2,
              "x", num3, "x", num4, "x", num5, "x", num6, "=", mul_values.Mult4())

    elif mult == 6:
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        result = 1
        while num > 0:
            digit = num % 10
            result = result * digit
            num = num // 10
        print(result)

    else:
        calculator.error1(base)

# division
elif option == 4:
    print_blue("division")
    print("")
    div_values.divs()
    print("")

    while True:
        try:
            divs = calculator.inum1(base)
            break
        except ValueError:
            calculator.error(base)

    if divs == 1:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        while True:
            try:
                print(" \u001b[37;1m ", num1, "/", num2, "=", div_values.Div())
                break
            except ZeroDivisionError:
                calculator.zeroerror(base)
                break

    elif divs == 2:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        while True:
            try:
                print(" \u001b[37;1m ", num1, "/", num2,
                      "/", num3, "=", div_values.Div1())
                break
            except ZeroDivisionError:
                calculator.zeroerror(base)
                break

    elif divs == 3:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        while True:
            try:
                print(" \u001b[37;1m ", num1, "/", num2,
                      "/", num3, "/", num4, "=", div_values.Div2())
                break
            except ZeroDivisionError:
                calculator.zeroerror(base)
                break

    elif divs == 4:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num5 = calculator.fnum5(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        while True:
            try:
                print(" \u001b[37;1m ", num1, "/", num2,
                      "/", num3, "/", num4, "/", num5, "=", div_values.Div3())
                break
            except ZeroDivisionError:
                calculator.zeroerror(base)
                break

    elif divs == 5:
        while True:
            try:
                num1 = calculator.fnum1(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num2 = calculator.fnum2(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num3 = calculator.fnum3(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num4 = calculator.fnum4(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num5 = calculator.fnum5(base)
                break
            except ValueError:
                calculator.error(base)
        while True:
            try:
                num6 = calculator.fnum6(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        while True:
            try:
                print(" \u001b[37;1m ", num1, "/", num2,
                      "/", num3, "/", num4, "/", num5, "/", num6, "=", add_values.Add4())
                break
            except ZeroDivisionError:
                calculator.zeroerror(base)

    elif adds == 6:
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        result = 0
        while num > 0:
            digit = num % 10
            result = result / digit
            num = num // 10
        print(result)

    else:
        calculator.error(base)
        # even-odd

# even-odd
elif option == 5:
    print_blue("even-odd")
    while True:
        try:
            num = calculator.fnum(base)
            break
        except ValueError:
            calculator.error(base)
    if num % 2 == 0:
        # loading()
        print("\u001b[37;1m", num, " is a even number")
    else:
        # loading()
        print("\u001b[37;1m", num, " is a odd number")

# range_of_numbers
elif option == 6:
    print_blue("range_of_numbers")
    while True:
        try:
            num = calculator.inum(base)
            break
        except ValueError:
            calculator.error(base)
    for i in range(-1, num):
        if i != num:
            print("\u001b[37m", i+1)
        else:
            print("this is end")

# exponential power
elif option == 7:
    print_blue("exponential-power")
    while True:
        try:
            num1 = calculator.fnum1(base)
            break
        except ValueError:
            calculator.error(base)
    while True:
        try:
            num2 = calculator.fnum2(base)
            break
        except ValueError:
            calculator.error(base)
    # loading()
    print("\u001b[37;1m exponent: ", num1, "^", num2, "=", m.pow(num1, num2))

# fibonacci-series
elif option == 8:
    print_blue("fibonacci-series")
    while True:
        try:
            num = calculator.inum(base)
            break
        except ValueError:
            calculator.error(base)
    var1 = 0
    var2 = 1
    for i in range(num):
        var3 = var1
        var1 = var2
        var2 = var3+var2
        print("\u001b[37;1m", var3)

# fibonacci or not
elif option == 9:
    print_blue("fibonacci-or-not")

    def perfectsquare(value):
        var = int(m.sqrt(value))
        return var*var == value
    while True:
        try:
            num = calculator.inum(base)
            break
        except ValueError:
            calculator.error(base)
    var1 = 5*(num*num)+4
    var2 = 5*(num*num)-4
    if perfectsquare(var1) or perfectsquare(var2):
        # loading()
        print(num, "\u001b[37;1m is a fibonacci number")
    else:
        # loading()
        print(num, "\u001b[37;1m is not a fibonacci number")

#  constants
elif option == 10:
    # loading()
    print_blue("constants")
    print("\u001b[37;1m 1.the value of pi: ", m.pi)
    print("\u001b[37;1m 2.the value of eplison: ", m.e)
    print("\u001b[37;1m 3.the value of tau: ", m.tau)

# trignometry
elif option == 11:
    calculator.rules(base)
    print_blue(" trignometry")
    print('')
    calculator.Subs()
    print('')
    while True:
        try:
            sub = calculator.inum1(base)
            break
        except ValueError:
            calculator.error(base)
    if sub == 1:
        print_blue("cos()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print("\u001b[37;1m cos( ", num, ")=", m.cos(num))
    elif sub == 2:
        print_blue("sin()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        # loading()
        print("\u001b[37;1m sin( ", num, ")=", m.sin(num))
    elif sub == 3:
        print_blue("tan()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m tan( ", num, ")=", m.tan(num))
        # loading()
    elif sub == 4:
        print_blue("cosh()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m cosh( ", num, ")=", m.cosh(num))
    elif sub == 5:
        print_blue("sinh()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m sinh( ", num, ")=", m.sinh(num))
    elif sub == 6:
        print_blue("tanh()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m tanh( ", num, ")=", m.tanh(num))
    elif sub == 7:
        print_blue("acosh()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m acosh( ", num, ")=", m.acosh(num))
    elif sub == 8:
        print_blue("asinh()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m asinh( ", num, ")=", m.asinh(num))
    elif sub == 9:
        print_blue("atanh()")
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m atanh( ", num, ")=", m.atanh(num))
    else:
        calculator.error1(base)

# square-root
elif option == 12:
    print_blue("square-root")
    while True:
        try:
            num = calculator.fnum(base)
            break
        except ValueError:
            calculator.error(base)
    # loading()
    print("\u001b[37;1m the squareroot of", num, "=", m.sqrt(num))

# degrees and radians
elif option == 13:
    print_blue("degrees to radians")
    calculator.rules(base)
    print("")
    calculator.Deg()
    print("")
    while True:
        try:
            deg = calculator.fnum(base)
            break
        except ValueError:
            calculator.error(base)
    if deg == 1:
        print_blue("radians to degrees")
        while True:
            try:
                num = calculator.num3(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m the degrees(", num,
              ")" "radians =", m.degrees(num))
    elif deg == 2:
        while True:
            try:
                num = calculator.fnum(base)
                break
            except ValueError:
                calculator.error(base)
        print("\u001b[37;1m the radians(", num,
              ")" "degrees =", m.radians(num))
    else:
        calculator.error1(base)

# if option is out of bound
else:
    calculator.error1(base)
