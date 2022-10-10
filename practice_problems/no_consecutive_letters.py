with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}


# [ ] What are all of the letters that never appear consecutively in an English word? For example, we know that “U”
# isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which
# letters never appear consecutively?
def no_consecutive_letters(words):
    lst = set()
    for word in words:
        for x in word:
            if x not in lst and x + x in word:
                lst.add(x)
    result = []
    for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if x not in lst:
            result.append(x)
    return result


print(no_consecutive_letters(data))
