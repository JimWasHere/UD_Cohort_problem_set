with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}



def all_vowels(words):
    lst = []
    for x in words:
        if "A" in x and "E" in x and "I" in x and "O" in x and "U" in x:
            lst.append(x)
    return lst


# [ ] What is the shortest word that contains all 5 vowels?
def shortest_all_vowels(words):
    lst = all_vowels(words)
    shortest = lst[0]
    for x in lst:
        if len(x) < len(shortest):
            shortest = x
    return shortest


print(shortest_all_vowels(data))
