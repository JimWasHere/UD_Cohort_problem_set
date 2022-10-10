with open("sowpods.txt") as data:
    data = {x.strip() for x in data.readlines()}


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


print(longest_palindrome(data))
