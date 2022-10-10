with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What are all of the words containing an X and a Y and a Z?

def xyz(words):
    lst = []
    for x in words:
        if "X" in x and "Y" in x and "Z" in x:
            lst.append(x)
    return lst


print(xyz(data))
