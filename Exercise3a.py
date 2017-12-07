def six_by_seven(num):
    if num % 42 == 0:
        return 'Universe'
    elif num % 7 == 0:
        return 'Good'
    elif num % 6 == 0:
        return 'Food'
    else:
        return 'Oops'
    