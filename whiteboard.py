# Write a function that will remove all vowels from a given string. The function should return a string.
# Examples:
# Input: ‘Joel’
# Output: ‘Jl’
# Input: ‘Shoha’
# Output: ‘Shh’

def vowels(st):
    empty = []
    #or ""

    vowels =['a','e','i','o','u']

    for char in st:
        if char.lower() not in vowels:
            empty.append(char)
            #or emty +=
    print("".join(empty))

vowels ('Joel')
vowels ('shoha')
            




