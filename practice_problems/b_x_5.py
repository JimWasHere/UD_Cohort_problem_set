with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}


# [ ] What are all of the words that have a B and an X and are less than 5 letters long?


def b_x_5(words):
    lst = []
    for x in words:
        if len(x) < 5 and "B" in x and "X" in x:
            lst.append(x)
    return lst


print(b_x_5(data))
