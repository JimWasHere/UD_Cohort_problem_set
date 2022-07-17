# For loops and if conditions
#
# countries.txt #



# [ ] What country names are > 50% vowels?
#
# Setting up storage to use during a for loop, including counters and arrays
#
# [ ] What is the shortest country name? Make sure your solution can handle ties.
# [ ] What countries use only one vowel in their name (the vowel can be used multiple times)
#     - For example, if the word “BEEKEEPER” were a country, it would be an answer, because it only uses “E”.
# [ ] There is at least one country name that contains another country name. Find all of these cases.

with open("data/countries.txt") as data:
    data = {x.strip() for x in data.readlines()}
    # print(data)

# [ ] What are all of the countries that have “United” in the name?
def united(words):
    lst = []
    for x in words:
        if "United" in x:
            lst.append(x)
    return lst


# [ ] What countries both begin and end with a vowel?
def beg_end_vowel(words):
    lst = []
    for x in words:
        if x.lower().startswith("a") or x.lower().startswith("e") or x.lower().startswith("i") or \
                x.lower().startswith("o") or x.lower().startswith("u"):
            if x.lower().endswith("a") or x.lower().endswith("e") or x.lower().endswith("i") or \
                    x.lower().endswith("o") or x.lower().endswith("u"):
                lst.append(x)
    return lst

print(beg_end_vowel(data))
# print(united(data))