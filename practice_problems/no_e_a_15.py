with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What are all of the words that have no E or A and are at least 15 letters long?


def no_e_a_15(words):
    lst = []
    for x in words:
        if len(x) >= 15 and "E" not in x and "A" not in x:
            lst.append(x)
    return lst


print(no_e_a_15(data))
