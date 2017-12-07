def str_anagram(string1, string2):
    string1 = list(string1.lower())
    string2 = list(string2.lower())
    string1.sort()
    string2.sort()
    string1 = ''.join(string1)
    string2 = ''.join(string2)
    return string1 == string2

string1 = input("Enter your first word: ")
string2 = input("Enter your second word: ")

print(str_anagram(string1, string2))
