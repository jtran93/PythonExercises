def len_int(n):
    if n.isdigit() == True:
        return len(str(n))
    else:
        return "Please enter an integer."

number = input("Enter an integer: ")
output = len_int(number)
print(output)
