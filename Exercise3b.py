for i in range(1, 1001):
    binaryNum = '{0:b}'.format(i)
    if str(binaryNum) == str(binaryNum)[::-1]:
        print(i, binaryNum)