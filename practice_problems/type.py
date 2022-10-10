with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}

# Setting up storage to use during a for loop, including counters and arrays
#
# [ ] How many words contain the substring "TYPE”?


def type(words):
    count = 0
    for x in words:
        if "TYPE" in x:
            count += 1
    return count


print(type(data))
