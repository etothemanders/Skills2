string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""

def count_unique(string1):
    d = {}
    for word in string1:
        if d.get(word, 0) != 0:
            d[word] += 1
        else:
            d[word] = 1
    return d

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    common = []
    # assuming that we don't want duplicates
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                common.append(list1[i])
            j += 1
        i += 1

    return list(set(common))

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    common = []
    d = {}

    for word in list1:
        #if it's not in the dictionary, add it with a value of 1
        if d.get(word, 0) == 0:
            d[word] = 1
        else:
            pass

    for word in list2:
        #if the word is already in the dictionary, add it to the common list
        if d.get(word, 0) != 0:
            common.append(word)

    return common

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    pairs = []
    d = {}

    for num in list1:
        if d.get(num, 0) == 0:
            d[num] = 1
        else:
            d[num] += 1

    for num in list1:
        if d.get(num, 0) > 0 and d.get(-num, 0) > 0:
            pairs.append([num, -num])
            d[num] -= 1
            d[(-num)] -= 1

    return pairs


"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    return list(set(words))

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
