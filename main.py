import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from gui import MainWindow

def sign_bit(index):
    if index == '-':
        return 1
    else:
        return 0


def most_significant_bit(decimal):
    stop = 1
    num = 8
    binary = []
    while stop <= 4:
        if decimal >= num:
            decimal = decimal - num
            num = num / 2
            binary.append(1)
            stop += 1
        else:
            binary.append(0)
            num = num / 2
            stop += 1
    return binary


def exponent_prime_hexadecimal(base):
    base = base + 101
    stop = 1
    num = 128
    binary = []
    while stop <= 8:
        if base >= num:
            base = base - num
            num = num / 2
            binary.append(1)
            stop += 1
        else:
            binary.append(0)
            num = num / 2
            stop += 1
    return binary


def find_combination_field(msb_decimal, msb_hexadecimal, exponent_prime):
    combination_field = []
    if 0 <= msb_decimal <= 7:
        combination_field.append(exponent_prime[0])
        combination_field.append(exponent_prime[1])
        combination_field.append(msb_hexadecimal[1])
        combination_field.append(msb_hexadecimal[2])
        combination_field.append(msb_hexadecimal[3])
    else:
        combination_field.append(1)
        combination_field.append(1)
        combination_field.append(exponent_prime[0])
        combination_field.append(exponent_prime[1])
        combination_field.append(msb_hexadecimal[3])
    return combination_field


def get_exponent_continuation(exponent_prime):
    exponent_prime = exponent_prime[2:]
    return exponent_prime


def get_coefficient_field(nums):
    # print(nums)
    section1 = merge_num_list(nums[0:3])
    section2 = merge_num_list(nums[3:])
    updated_section1 = []
    updated_section2 = []
    final_section = []

    if section1[0] == 0 and section1[4] == 0 and section1[8] == 0:
        updated_section1.append(section1[1])  # b
        updated_section1.append(section1[2])  # c
        updated_section1.append(section1[3])  # d
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[7])  # h
        updated_section1.append(0)  # v
        updated_section1.append(section1[9])   # j
        updated_section1.append(section1[10])  # k
        updated_section1.append(section1[11])  # m
    elif section1[0] == 0 and section1[4] == 0 and section1[8] == 1:
        updated_section1.append(section1[1])  # b
        updated_section1.append(section1[2])  # c
        updated_section1.append(section1[3])  # d
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(0)
        updated_section1.append(0)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 0 and section1[4] == 1 and section1[8] == 0:
        updated_section1.append(section1[1])  # b
        updated_section1.append(section1[2])  # c
        updated_section1.append(section1[3])  # d
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(0)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 0 and section1[4] == 1 and section1[8] == 1:
        updated_section1.append(section1[1])  # b
        updated_section1.append(section1[2])  # c
        updated_section1.append(section1[3])  # d
        updated_section1.append(1)
        updated_section1.append(0)
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 1 and section1[4] == 0 and section1[8] == 0:
        updated_section1.append(section1[9])  # j
        updated_section1.append(section1[10])  # k
        updated_section1.append(section1[3])  # d
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(0)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 1 and section1[4] == 0 and section1[8] == 1:
        updated_section1.append(section1[5])  # f
        updated_section1.append(section1[6])  # g
        updated_section1.append(section1[3])  # d
        updated_section1.append(0)
        updated_section1.append(1)
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 1 and section1[4] == 1 and section1[8] == 0:
        updated_section1.append(section1[9])  # j
        updated_section1.append(section1[10])  # k
        updated_section1.append(section1[3])  # d
        updated_section1.append(0)
        updated_section1.append(0)
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    elif section1[0] == 1 and section1[4] == 1 and section1[8] == 1:
        updated_section1.append(0)
        updated_section1.append(0)
        updated_section1.append(section1[3])  # d
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[7])  # h
        updated_section1.append(1)  # v
        updated_section1.append(1)
        updated_section1.append(1)
        updated_section1.append(section1[11])  # m

    if section2[0] == 0 and section2[4] == 0 and section2[8] == 0:
        updated_section2.append(section2[1])  # b
        updated_section2.append(section2[2])  # c
        updated_section2.append(section2[3])  # d
        updated_section2.append(section2[5])  # f
        updated_section2.append(section2[6])  # g
        updated_section2.append(section2[7])  # h
        updated_section2.append(0)  # v
        updated_section2.append(section2[9])   # j
        updated_section2.append(section2[10])  # k
        updated_section2.append(section2[11])  # m

    elif section2[0] == 0 and section2[4] == 0 and section2[8] == 1:
        updated_section2.append(section2[1])  # b
        updated_section2.append(section2[2])  # c
        updated_section2.append(section2[3])  # d
        updated_section2.append(section2[5])  # f
        updated_section2.append(section2[6])  # g
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(0)
        updated_section2.append(0)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 0 and section2[4] == 1 and section2[8] == 0:
        updated_section2.append(section2[1])  # b
        updated_section2.append(section2[2])  # c
        updated_section2.append(section2[3])  # d
        updated_section2.append(section2[9])  # j
        updated_section2.append(section2[10])  # k
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(0)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 0 and section2[4] == 1 and section2[8] == 1:
        updated_section2.append(section2[1])  # b
        updated_section2.append(section2[2])  # c
        updated_section2.append(section2[3])  # d
        updated_section2.append(1)
        updated_section2.append(0)
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 1 and section2[4] == 0 and section2[8] == 0:
        updated_section2.append(section2[9])  # j
        updated_section2.append(section2[10])  # k
        updated_section2.append(section2[3])  # d
        updated_section2.append(section2[5])  # f
        updated_section2.append(section2[6])  # g
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(0)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 1 and section2[4] == 0 and section2[8] == 1:
        updated_section2.append(section2[5])  # f
        updated_section2.append(section2[6])  # g
        updated_section2.append(section2[3])  # d
        updated_section2.append(0)
        updated_section2.append(1)
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 1 and section2[4] == 1 and section2[8] == 0:
        updated_section2.append(section2[9])  # j
        updated_section2.append(section2[10])  # k
        updated_section2.append(section2[3])  # d
        updated_section2.append(0)
        updated_section2.append(0)
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    elif section2[0] == 1 and section2[4] == 1 and section2[8] == 1:
        updated_section2.append(0)
        updated_section2.append(0)
        updated_section2.append(section2[3])  # d
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[7])  # h
        updated_section2.append(1)  # v
        updated_section2.append(1)
        updated_section2.append(1)
        updated_section2.append(section2[11])  # m

    final_section.extend(updated_section1)
    final_section.extend(updated_section2)
    return final_section


def merge_num_list(nums):
    print(nums)
    decimal1 = most_significant_bit(nums[0])
    decimal2 = most_significant_bit(nums[1])
    decimal3 = most_significant_bit(nums[2])
    mergedlist = []
    mergedlist.extend(decimal1)
    mergedlist.extend(decimal2)
    mergedlist.extend(decimal3)
    return mergedlist
    

if __name__ == '__main__':
    # Main function
    #stop = 0
    #while stop != 1:
    #    user_input = float(input("Input a decimal number: "))
    #    base_number = int(input("Input the base number: "))
    #    user_input = list(str(user_input))
    #    signBit = sign_bit(user_input[0])  # Gets the sign bit
    #    print("Sign bit: ", signBit)

    #    if user_input[0] == '-':
    #        user_input.remove('-')
    #    user_input.remove('.')
    #    user_input.pop()
    #    output = [int(num) for num in user_input]
    #    # -------------------------------------------

    #    msb = most_significant_bit(output[0])
    #    exponentPrime = exponent_prime_hexadecimal(base_number)
    #    combination_field = find_combination_field(output[0], msb, exponentPrime)
    #    print("Combination field: ", combination_field)

    #    exponent_continuation = get_exponent_continuation(exponentPrime)
    #    print("Exponent Continuation: ", exponent_continuation)

    #    coefficient_continuation = get_coefficient_field(output[1:])
    #    print(coefficient_continuation)
    #    stop = int(input("Do you want to quit?: "))  # Input 1 to end the loop. This is for test purposes
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    app.exec_()
