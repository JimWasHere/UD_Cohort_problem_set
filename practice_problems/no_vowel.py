with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What are all of the words with no vowel and not even a Y?


def no_vowels(words):
    lst = []
    for x in words:
        if "A" not in x and "E" not in x and "I" not in x and "O" not in x and "U" not in x and "Y" not in x:
            lst.append(x)
    return lst


print(no_vowels(data))
