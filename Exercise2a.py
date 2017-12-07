def len_int(n):
    if n.isdigit() == True:
        return len(str(n))
    else:
        return "Please enter an integer."
    