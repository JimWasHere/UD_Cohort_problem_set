
with open("data/baby_names_2020_short.txt") as b_names_2020:
    b_names_2020 = {x.strip() for x in b_names_2020.readlines()}

with open("data/baby_names_1880_short.txt") as b_names_1880:
    b_names_1880 = {x.strip() for x in b_names_1880.readlines()}


#More for loops, if conditions, and storage

# babynames both #


#
# Nested for loops
#
# [ ] There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid
# Scrabble word. Find and print all such names.
#     [ ] Solve this two ways: first with an array to hold the Scrabble words, and then with a dictionary (or set) to
#     hold the Scrabble words. Use timer functions to measure how long it takes to complete this work under each
#     implementation. Why is the time different?
# [ ] What are all of the names that were top 40 baby names in both 1880 and 2020?


# [ ] What is the shortest baby name in the top 40 baby names for 2020?
def shortest_2020(words):
    return min(words, key=len)


# [ ] What are the longest baby names in the top 40 baby names for 2020? Make sure you can handle if there’s a tie.
def longest_2020(words):
    result = []
    longest = max(words, key=len)

    for x in words:
        if len(x) == len(longest):
            result.append(x)
    return result



# print(longest(b_names_2020))
print(shortest_2020(b_names_2020))