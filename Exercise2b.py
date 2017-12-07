def str_cmp(string1, string2):
    if string1.lower() == string2.lower():
        return True
    else:
        return False

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print(str_cmp(string1, string2))