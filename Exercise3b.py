def binary_palindrome(startRange, endRange):
    for i in range(startRange, endRange):
        binaryNum = '{0:b}'.format(i)
        if str(binaryNum) == str(binaryNum)[::-1]:
            print(i, binaryNum)

def octal_palindrome(startRange, endRange):
    return

def hex_palindrome(startRange, endRange):
    return