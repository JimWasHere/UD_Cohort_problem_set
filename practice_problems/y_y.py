with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What are all of the words that both start and end with a Y?


def y_y(words):
    lst = []
    for x in words:
        if x.startswith("Y") and x.endswith("Y"):
            lst.append(x)
    return lst


print(y_y(data))
