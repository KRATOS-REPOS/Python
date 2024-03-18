import math
from pystyle import *
def binaryToDecimal(num):
    result = 0
    for i in range(len(num)):
        result += int(num[i]) * math.pow(2, len(num) - 1 - i)
    return int(result)

def decimalToBinary(num):
    result = []
    while True:
        result.append(str(num % 2))
        num = num // 2  # Use integer division here
        if num == 0:
            break
    result.reverse()  # Reverse the result list to get the correct binary representation
    result = "".join(result)
    return result

def hexadecimalToBinary(num):
    decimal_num = int(num, 16)
    binary_num = bin(decimal_num)[2:]  # Remove '0b' prefix from binary representation
    return binary_num

def hexadecimalToDecimal(num):
    return int(num, 16)

def Not(num):
    binary_str = str(num)
    complement_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    return complement_str.zfill(len(binary_str))

def logical_AND(bin1, bin2):
    result = ""
    for i in range(len(bin1)):
        result += '1' if bin1[i] == '1' and bin2[i] == '1' else '0'
    return result

def logical_XOR(bin1, bin2):
    result = ""
    for i in range(len(bin1)):
        result += '1' if bin1[i] != bin2[i] else '0'
    return result

def logical_OR(bin1, bin2):
    result = ""
    for i in range(len(bin1)):
        result += '1' if bin1[i] == '1' or bin2[i] == '1' else '0'
    return result

def run():
    Write.Print('''
  _________                _________
 / _______/     //\\\\      / _______/      //\\\\
| |______      //  \\\\    | |_______      //  \\\\
 \______ \\    ||____||    \\_______ \\    ||____||
        \ \\   ||----||            \ \\   ||----||
 _______/ /   ||    ||      ______/ /   ||    ||
/________/    ||    ||     /_______/    ||    ||

''', Colors.blue_to_purple,interval=0.03)

    
    while True:
        print(f'''\033[92m1- Binary To Decimal
2- Decimal To Binary
3- Hexadecimal To Binary
4- Hexadecimal To Decimal
5- Bitwise NOT
6- Bitwise AND
7- Bitwise XOR
8- Bitwise OR
9- Exit \033[0m
''')
        choice = input('\nChoice from the list: ')
        if choice == '1':
            num = input('Enter the number: ')
            answer = binaryToDecimal(num)
        elif choice == '2':
            num = int(input('Enter the decimal number: '))
            answer = decimalToBinary(num)
        elif choice == '3':
            num = input('Enter the hexadecimal number: ')
            answer = hexadecimalToBinary(num)
        elif choice == '4':
            num = input('Enter the hexadecimal number: ')
            answer = hexadecimalToDecimal(num)
        elif choice == '5':
            num = input('Enter the binary number: ')
            answer = Not(num)
        elif choice == '6':
            num = input('Enter the first binary number: ')
            num2 = input('Enter the second binary number: ')
            answer = logical_AND(num, num2)
        elif choice == '7':
            num = input('Enter the first binary number: ')
            num2 = input('Enter the second binary number: ')
            answer = logical_XOR(num, num2)
        elif choice == '8':
            num = input('Enter the first binary number: ')
            num2 = input('Enter the second binary number: ')
            answer = logical_OR(num, num2)
        elif choice == '9':
            break
        print(f'\nYour Answer: {answer}\n')
run()