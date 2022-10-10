with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What is the longest word that contains no vowels?


def no_vowels(words):
    lst = []
    for x in words:
        if "A" not in x and "E" not in x and "I" not in x and "O" not in x and "U" not in x and "Y" not in x:
            lst.append(x)
    return lst


def longest_no_vowels(words):
    longest = ""
    for x in no_vowels(words):
        if len(x) > len(longest):
            longest = x
    return longest


print(longest_no_vowels(data))
