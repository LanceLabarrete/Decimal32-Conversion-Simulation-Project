from main_window import Ui_MainWindow
from gui import MainWindow
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore, QtGui, QtWidgets
import sys
import math


ERR_EMPTY_USERINPUT = 1
ERR_EMPTY_EXPONENT = 2
ERR_EMPTY_USER_EXPONENT = 3

ERR_EXTRA_CHAR_USERINPUT = 4
ERR_EXTRA_CHAR_EXPONENT = 5
ERR_EXTRA_CHAR_USER_EXPONENT = 6

SUCCESS = 0


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Lb_errorMessage.setStyleSheet("color: red;")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()


def main():
    user_input = window.ui.LnEd_userInput.text()
    base_number = window.ui.LnEd_baseInput.text()

    error = check_empty_string(user_input, base_number)

    if error:
        generate_error(error)
        return

    valid_user_input = True
    valid_base_number = True

    try:
        user_input = float(user_input)
    except ValueError:
        valid_user_input = False

    try:
        base_number = int(base_number)
    except ValueError:
        valid_base_number = False

    if not valid_user_input and not valid_base_number:
        generate_error(ERR_EXTRA_CHAR_USER_EXPONENT)
        return
    elif not valid_user_input:
        generate_error(ERR_EXTRA_CHAR_USERINPUT)
        return
    elif not valid_base_number:
        generate_error(ERR_EXTRA_CHAR_EXPONENT)
        return

    hide_error()

    user_input = list(str(user_input))
    signBit = sign_bit(user_input[0])  # Gets the sign bit
    print("user_input =", user_input)
    print("signBit =", signBit)
    if user_input[0] == '-':
        user_input.remove('-')

    user_input = normalize(user_input, base_number)
    if user_input[-1] == "True":
        user_input.pop()
        base_number = int(user_input[-1])
        user_input.pop()

    elif user_input[-1] == "False":
        user_input.pop()

    print(user_input)
    output = [int(num) for num in user_input]
    # -------------------------------------------

    msb = most_significant_bit(output[0])
    exponentPrime = exponent_prime_hexadecimal(base_number)
    combination_field = find_combination_field(
        output[0], msb, exponentPrime)

    exponent_continuation = get_exponent_continuation(exponentPrime)

    coefficient_continuation = get_coefficient_field(output[1:])

    output_binary(signBit, combination_field,
                  exponent_continuation, coefficient_continuation)
    output_hex(signBit, combination_field,
               exponent_continuation, coefficient_continuation)


def generate_error(error):
    errorMessage = {
        ERR_EMPTY_USERINPUT:
            "The input for the Decimal-32 Floating Point " +
            "data is empty. Please input a number.",
        ERR_EMPTY_EXPONENT:
            "The input for the exponent is empty. Please input a number.",
        ERR_EMPTY_USER_EXPONENT:
            "The input for the Decimal-32 Floating + " +
            "Point data and the exponent are empty. " +
            "Please input a number in both" +
            " of the empty textboxes.",
        ERR_EXTRA_CHAR_USERINPUT:
            "A signed decimal floating point number is expected.",
        ERR_EXTRA_CHAR_EXPONENT:
            "A signed integer is only expected in the exponent box.",
        ERR_EXTRA_CHAR_USER_EXPONENT:
            "Both have invalid input. " +
            "A signed decimal number is expected in the Decimal-32 Floating " +
            "Point data input, and a signed integer is only expected in the " +
            "exponent box."
    }
    window.ui.Lb_errorMessage.show()
    window.ui.Lb_errorMessage.setText("Error: " + errorMessage[error])


def hide_error():
    window.ui.Lb_errorMessage.setText("")
    window.ui.Lb_errorMessage.hide()


def check_empty_string(user_input, base_number):
    if not user_input and not base_number:
        return ERR_EMPTY_USER_EXPONENT
    elif not user_input:
        return ERR_EMPTY_USERINPUT
    elif not base_number:
        return ERR_EMPTY_EXPONENT

    return SUCCESS


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
        updated_section1.append(section1[9])  # j
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
        updated_section2.append(section2[9])  # j
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
    # print(nums)
    decimal1 = most_significant_bit(nums[0])
    decimal2 = most_significant_bit(nums[1])
    decimal3 = most_significant_bit(nums[2])
    mergedlist = []
    mergedlist.extend(decimal1)
    mergedlist.extend(decimal2)
    mergedlist.extend(decimal3)
    return mergedlist


def normalize(decimalnumbers, basenumber):
    raw_string = "----normalize({0}, {1})-----"
    format_string = raw_string.format(decimalnumbers, basenumber)
    print(format_string)
    print("Before Line 433")
    print("decimalnumbers = {0}".format(decimalnumbers))
    print("(str)decimalnumbers = {0}".format(''.join(decimalnumbers)))
    print("basenumber = {0}".format(basenumber))
    isBaseNumberUpdated = "False"

    if decimalnumbers[-2] == '.' and decimalnumbers[-1] == '0':
        decimalnumbers.pop()
        decimalnumbers.pop()
    else:  # move decimal dot to the right
        # temp = decimalnumbers
        decimalnumbers = move_decimal_dot(decimalnumbers)
        # basenumber = update_base_number(temp, basenumber)
        basenumber = update_base_number(decimalnumbers, basenumber)
        isBaseNumberUpdated = "True"
        decimalnumbers.pop()

    print("----Line 442----")
    print("decimalnumbers = {0}".format(decimalnumbers))
    print("(str)decimalnumbers = {0}".format(''.join(decimalnumbers)))
    print("basenumber = {0}".format(basenumber))
    count_digits = len(decimalnumbers)

    if count_digits < 7:  # if there are less than 7 digits, pad zeros on the left
        # "max" is a function under math library
        # not a good idea to use it as a variable
        max_digits = 7
        while count_digits < max_digits:
            decimalnumbers.insert(0, '0')
            count_digits += 1

        print("----Line 455----")
        print("decimalnumbers = {0}".format(decimalnumbers))
        print("(str)decimalnumbers = {0}".format(''.join(decimalnumbers)))
        print("basenumber = {0}".format(basenumber))
        count_digits = len(decimalnumbers)

    elif count_digits > 7:  # if there are more than 7 digits, move decimal dot to the right and round off
        decimalnumbers.append('.')
        while True:
            if count_digits > 7:
                indexM = decimalnumbers.index('.') - 1
                indexN = decimalnumbers.index('.')
                decimalnumbers[indexM], decimalnumbers[indexN] = decimalnumbers[indexN], decimalnumbers[indexM]
                count_digits -= 1
                basenumber += 1
            else:
                isBaseNumberUpdated = "True"
                break

        print("----Line 473----")
        print("decimalnumbers = {0}".format(decimalnumbers))
        print("(str)decimalnumbers = {0}".format(''.join(decimalnumbers)))
        print("basenumber = {0}".format(basenumber))
        count_digits = len(decimalnumbers)

        float_digits = list_to_float(decimalnumbers)

        print("----Line 480----")
        print("decimalnumbers = {0}".format(decimalnumbers))
        print("(str)decimalnumbers = {0}".format(''.join(decimalnumbers)))
        print("float_digits = {0}".format(float_digits))
        print("basenumber = {0}".format(basenumber))
        count_digits = len(decimalnumbers)

        # float_digits = round(float_digits)
        # lets the user decide which rounding method
        float_digits = which_rounding_method(float_digits)
        decimalnumbers = list(str(float_digits))

        print("----Line 490----")
        print("decimalnumbers = {0}".format(decimalnumbers))
        print("basenumber = {0}".format(basenumber))
        count_digits = len(decimalnumbers)

    if isBaseNumberUpdated == "True":
        decimalnumbers.append(str(basenumber))
        decimalnumbers.append(isBaseNumberUpdated)
        return decimalnumbers
    else:
        decimalnumbers.append(isBaseNumberUpdated)
        return decimalnumbers


def move_decimal_dot(decimalnumbers):
    while True:
        if decimalnumbers[-1] != '.':
            indexM = decimalnumbers.index('.')
            indexN = decimalnumbers.index('.') + 1
            decimalnumbers[indexM], decimalnumbers[indexN] = decimalnumbers[indexN], decimalnumbers[indexM]
        else:
            break
    return decimalnumbers


def update_base_number(decimalnumbers, basenumber):
    while True:
        if decimalnumbers[-1] != '.':
            indexM = decimalnumbers.index('.')
            indexN = decimalnumbers.index('.') + 1
            decimalnumbers[indexM], decimalnumbers[indexN] = decimalnumbers[indexN], decimalnumbers[indexM]
            basenumber -= 1
        else:
            break
    return basenumber


def list_to_float(digits):
    # Join the list elements into a single string
    number_str = ''.join(digits)

    # If there is no decimal point in the string, add one at the end
    if '.' not in number_str:
        number_str += '.'

    # Convert the string to a float
    return float(number_str)


def output_binary(signbit, combinationfield, exponentcont, coefficientcont):

    combinedstring1 = str(signbit)
    combinedstring2 = ''.join(map(str, combinationfield))
    combinedstring3 = ''.join(map(str, exponentcont))
    combinedstring4 = ''.join(map(str, coefficientcont))

    if combinedstring2 == "11111":
        window.ui.LnEd_binary.setText("NaN")
        return
    elif combinedstring2 == "11110":
        if combinedstring1 == "0":
            window.ui.LnEd_binary.setText("+Infinity")
        elif combinedstring1 == "1":
            window.ui.LnEd_binary.setText("-Infinity")
        return

    print(combinedstring1, combinedstring2, combinedstring3, combinedstring4)

    finalString = combinedstring1 + " " + combinedstring2 + \
        " " + combinedstring3 + " " + combinedstring4

    window.ui.LnEd_binary.setText(finalString)


def output_hex(signbit, combinationfield, exponentcont, coefficientcont):
    combinedstring1 = str(signbit)
    combinedstring2 = ''.join(map(str, combinationfield))

    if combinedstring2 == "11111":
        window.ui.LnEd_hexadecimal.setText("NaN")
        return
    elif combinedstring2 == "11110":
        if combinedstring1 == "0":
            window.ui.LnEd_hexadecimal.setText("+Infinity")
        elif combinedstring1 == "1":
            window.ui.LnEd_hexadecimal.setText("-Infinity")
        return

    combined_list = [signbit]
    combined_list.extend(combinationfield)
    combined_list.extend(exponentcont)
    combined_list.extend(coefficientcont)
    hex_output = [hex_converter(combined_list[0:4]),
                  hex_converter(combined_list[4:8]),
                  hex_converter(combined_list[8:12]),
                  hex_converter(combined_list[12:16]),
                  hex_converter(combined_list[16:20]),
                  hex_converter(combined_list[20:24]),
                  hex_converter(combined_list[24:28]),
                  hex_converter(combined_list[28:])]
    final_output = ''.join(map(str, hex_output))
    print(final_output)

    window.ui.LnEd_hexadecimal.setText(final_output)


def hex_converter(decimaldigits):
    decimalDictionary = {
        "0000": '0',
        "0001": '1',
        "0010": '2',
        "0011": '3',
        "0100": '4',
        "0101": '5',
        "0110": '6',
        "0111": '7',
        "1000": '8',
        "1001": '9',
        "1010": 'A',
        "1011": 'B',
        "1100": 'C',
        "1101": 'D',
        "1111": 'E',
        "1110": 'F'
    }
    decimalStr = ''.join(map(str, decimaldigits))
    return decimalDictionary[decimalStr]


def which_rounding_method(number: float):
    # selected_id = window.ui.btnGrp_roundMeth.checkedId()
    selected_button = window.ui.btnGrp_roundMeth.checkedButton()
    # print("selected_id = {0}".format(selected_id))
    print("selected_button = {0}".format(selected_button))

    print("---which_rounding_method({0})---".format(number))

    selected_id = {
        window.ui.rdBtn_nearZero: 0,
        window.ui.rdBtn_floor: 1,
        window.ui.rdBtn_ceil: 2,
        window.ui.rdBtn_nearEven: 3,
    }
    print("selected_id = {0}".format(selected_id[selected_button]))

    # number = ''.join(number)

    if selected_id[selected_button] == 0:  # nearest zero
        if number >= 0:
            number = int(number)
            print("number = {0}".format(number))
            # return number
        else:
            number = -int(-number)
            print("number = {0}".format(number))
    elif selected_id[selected_button] == 1:  # floor
        number = math.floor(number)
        print("number = {0}".format(number))
        # return math.floor(number)
    elif selected_id[selected_button] == 2:  # ceiling
        number = math.floor(number)
        print("number = {0}".format(number))
        # return math.ceil(number)
    elif selected_id[selected_button] == 3:  # ties to nearest even
        number = round(number)
        print("number = {0}".format(number))

    return number


def toggle_visibility_layout(layout: QtWidgets.QLayout, show):
    size = layout.count() - 1
    while size >= 0:
        item = layout.itemAt(size)
        if isinstance(item, QtWidgets.QLayout):
            print("is a layout")
            toggle_visibility_layout(item, show)
            size -= 1
            continue

        item = item.widget()

        if show:
            item.show()
        else:
            item.hide()
        size -= 1


def toggle_enable_buttongroup(group: QtWidgets.QButtonGroup, enable):
    for button in group.buttons():
        button.setEnabled(enable)


def show_rounding_method(input_string):
    print(input_string)
    input_string = input_string.replace(".", "")

    if len(input_string) > 7:
        # window.ui.vrtLO_roundingMeth.show()
        # toggle_visibility_layout(window.ui.vrtLO_roundingMeth, True)
        toggle_enable_buttongroup(window.ui.btnGrp_roundMeth, True)
        return

    # toggle_visibility_layout(window.ui.vrtLO_roundingMeth, False)
    toggle_enable_buttongroup(window.ui.btnGrp_roundMeth, False)


def print_into_file():
    filename = "output.txt"

    binary_output = window.ui.LnEd_binary.text()
    hexadecimal_output = window.ui.LnEd_hexadecimal.text()

    popup = QtWidgets.QMessageBox()

    if not binary_output or not hexadecimal_output:
        popup.setText("Nothing has been inputted yet! "
                      + "Saving text file aborted.")
        popup.exec_()
        return

    text_file = open(filename, "w")

    text_file.write("Binary representation: {0}\n".format(binary_output))
    text_file.write(
        "Hexadecimal representation: {0}".format(hexadecimal_output))
    text_file.close()

    popup.setText("An output file ({0}) has been saved!".format(filename))
    popup.exec_()


if __name__ == '__main__':
    window.show()
    window.ui.Lb_errorMessage.hide()
    # toggle_visibility_layout(window.ui.vrtLO_roundingMeth, False)
    toggle_enable_buttongroup(window.ui.btnGrp_roundMeth, False)

    window.ui.Btn_convert.pressed.connect(main)
    window.ui.LnEd_userInput.returnPressed.connect(main)
    window.ui.LnEd_baseInput.returnPressed.connect(main)
    window.ui.LnEd_userInput.textChanged.connect(show_rounding_method)
    window.ui.PshBtn_printText.pressed.connect(print_into_file)
    app.exec_()
