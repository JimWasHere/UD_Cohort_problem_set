with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What are all of the words containing UU?


def uu(words):
    lst = []
    for x in words:
        if "UU" in x:
            lst.append(x)
    return lst


print(uu(data))
