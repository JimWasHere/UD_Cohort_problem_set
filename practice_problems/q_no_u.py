with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# [ ] What are all of the words containing a Q but not a U?


def q_no_u(words):
    lst = []
    for x in words:
        if "Q" in x and "U" not in x:
            lst.append(x)
    return lst


print(q_no_u(data))
