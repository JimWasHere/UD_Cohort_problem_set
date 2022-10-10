with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}


# [ ] Which of the letters Q, X, and Z is the least common?
def q_x_z(words):
    letters = {
        "Q": 0,
        "X": 0,
        "Z": 0
    }
    for word in words:
        for char in word:
            if char in letters:
                letters[char] += 1
    return min(letters)


print(q_x_z(data))
