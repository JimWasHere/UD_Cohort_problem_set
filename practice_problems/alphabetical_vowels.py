with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What are all of the words that have all 5 vowels, in alphabetical order?


def all_vowels(words):
    lst = []
    for x in words:
        if "A" in x and "E" in x and "I" in x and "O" in x and "U" in x:
            lst.append(x)
    return lst


def alphabetical_vowels(words):
    lst = []
    for x in all_vowels(words):
        temp = []
        for y in x:
            if y in "AEIOU":
                temp.append(y)
        if sorted(temp) == temp:
            lst.append(x)
    return lst


print(alphabetical_vowels(data))
