with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What are all of the words that contain the word CAT and are exactly 5 letters long?


def cat(words):
    lst = []
    for x in words:
        if len(x) == 5 and "CAT" in x:
            lst.append(x)
    return lst


print(cat(data))
