
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


def getExponentContinuation(exponent_prime):
    exponent_continuation = exponent_prime[2:]
    return exponent_continuation


if __name__ == '__main__':
    # Main function
    stop = 0
    while stop != 1:
        user_input = float(input("Input a decimal number: "))
        base_number = int(input("Input the base number: "))
        user_input = list(str(user_input))
        signBit = sign_bit(user_input[0])  # Gets the sign bit
        print("Sign bit: ", signBit)

        if user_input[0] == '-':
            user_input.remove('-')
        user_input.remove('.')
        user_input.pop()
        output = [int(num) for num in user_input]
        # -------------------------------------------

        msb = most_significant_bit(output[0])
        exponentPrime = exponent_prime_hexadecimal(base_number)
        combination_field = find_combination_field(output[0], msb, exponentPrime)
        print("Combination field: ", combination_field)

        exponent_continuation = getExponentContinuation(exponentPrime)
        print("Exponent Continuation: ", exponent_continuation)
        stop = int(input("Do you want to quit?: "))  # Input 1 to end the loop. This is for test purposes
