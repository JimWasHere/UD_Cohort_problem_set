with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}


# [ ] Create and print an array containing all of the words that end in "GHTLY"

def ghtly(words):
    lst = []
    for x in words:
        if x.endswith("GHTLY"):
            lst.append(x)
    print(lst)
    return lst


print(ghtly(data))
