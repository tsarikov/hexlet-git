
def length_of_last_word(string_1):
    string_1 = string_1.strip()
    string_1 = string_1.replace('\t', ' ')
    string_1 = string_1.replace('\n', ' ')
    if len(string_1) == 0:
        return 0
    list1 = string_1.split()
    return len(list1[-1])

print(length_of_last_word('')) # 0
print(length_of_last_word(' '))
print(length_of_last_word('man in Black')) # 5
print(length_of_last_word('hello, world!     ')) # 6
print(length_of_last_word(' \t\n ')) # 5