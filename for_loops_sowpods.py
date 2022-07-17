# For Loops and if conditions
# sowpods.txt #


with open("data/sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}
    # print(data)


# [ ] What are all of the words containing UU?
def uu(words):
    lst = []
    for x in words:
        if "UU" in x:
            lst.append(x)
    return lst


# [ ] What are all of the words containing an X and a Y and a Z?
def xyz(words):
    lst = []
    for x in words:
        if "X" in x and "Y" in x and "Z" in x:
            lst.append(x)
    return lst


# [ ] What are all of the words containing a Q but not a U?
def q_no_u(words):
    lst = []
    for x in words:
        if "Q" in x and "U" not in x:
            lst.append(x)
    return lst


# [ ] What are all of the words that contain the word CAT and are exactly 5 letters long?
def cat(words):
    lst = []
    for x in words:
        if len(x) == 5 and "CAT" in x:
            lst.append(x)
    return lst


# [ ] What are all of the words that have no E or A and are at least 15 letters long?
def no_e_a_15(words):
    lst = []
    for x in words:
        if len(x) >= 15 and "E" not in x and "A" not in x:
            lst.append(x)
    return lst


# [ ] What are all of the words that have a B and an X and are less than 5 letters long?
def b_x_5(words):
    lst = []
    for x in words:
        if len(x) < 5 and "B" in x and "X" in x:
            lst.append(x)
    return lst


# [ ] What are all of the words that both start and end with a Y?
def y_y(words):
    lst = []
    for x in words:
        if x.startswith("Y") and x.endswith("Y"):
            lst.append(x)
    return lst


# [ ] What are all of the words with no vowel and not even a Y?
def no_vowels(words):
    lst = []
    for x in words:
        if "A" not in x and "E" not in x and "I" not in x and "O" not in x and "U" not in x and "Y" not in x:
            lst.append(x)
    return lst


# [ ] What are all of the words that have all 5 vowels, in any order?
def all_vowels(words):
    lst = []
    for x in words:
        if "A" in x and "E" in x and "I" in x and "O" in x and "U" in x:
            lst.append(x)
    return lst


# [ ] What are all of the words that have all 5 vowels, in alphabetical order?
def alphabetical_vowels(words):
    lst = []
    for x in all_vowels(words):
        temp = []
        for y in x:
            if y in "AEIOU":
                temp.append(y)
        if sorted(temp) == temp:
            lst.append(x)
    return lst


#
# Setting up storage to use during a for loop, including counters and arrays
#
# [ ] How many words contain the substring "TYPE”?
def type(words):
    count = 0
    for x in words:
        if "TYPE" in x:
            count += 1
    return count


# [ ] Create and print an array containing all of the words that end in "GHTLY"
def ghtly(words):
    lst = []
    for x in words:
        if x.endswith("GHTLY"):
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



# [ ] What is the longest word that contains no vowels?
def longest_no_vowels(words):
    longest = ""
    for x in no_vowels(words):
        if len(x) > len(longest):
            longest = x
    return longest


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


# [ ] What is the longest palindrome?
def longest_palindrome(words):
    lst = []
    for x in words:
        if x == x[::-1]:
            lst.append(x)
    longest = lst[0]
    for x in lst:
        if len(x) > len(longest):
            longest = x
    return longest


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

# print(no_consecutive_letters(data))
# print(longest_palindrome(data))
# print(q_x_z(data))
# print(longest_no_vowels(data))
# print(shortest_all_vowels(data))
# print(ghtly(data))
# print(type(data))
# print(alphabetical_vowels(data))
# print(all_vowels(data))
# print(no_vowels(data))
# print(y_y(data))
# print(b_x_5(data))
# print(no_e_a_15(data))
# print(cat(data))
# print(q_no_u(data))
# print(xyz(data))
# print(uu(data))
