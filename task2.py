"""TUPLE"""
# task 1
"""def pairwise_swap(tup):
    result = []
    for i in range(0, len(tup), 2):
        if i + 1 < len(tup):
            result.append(tup[i+1])
            result.append(tup[i])
        else:
            result.append(tup[i])
    return tuple(result)
print(pairwise_swap((1,2,3,4)))"""

#task 2
"""def unzip_tuples(tup_lst):
    first_elements = ()
    second_elements = ()
    for tup in tup_lst:
        first_elements += (tup[0],)
        second_elements += (tup[1],)
    return first_elements, second_elements
print(unzip_tuples(((1,2),(3,4))))"""

#task 3
"""def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram("jawad","zaheer"))"""

#task4
"""def capitalize_words(sentence):
    words = sentence.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
print(capitalize_words("my name is Jawad"))"""

#task5
"""def compress_string(s):
    if len(s) < 2:
        return s
    compressed = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed += s[i-1] + str(count) if count > 1 else s[i-1]
            count = 1
    compressed += s[-1] + str(count) if count > 1 else s[-1]
    return compressed if len(compressed) < len(s) else s
print(compress_string("qqqqaaaazzzziiiijjjjaaawwaaddddddd"))"""

# SETS
#task 1
"""def find_common_elements(set1, set2):
    return set1.intersection(set2)

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common_elements = find_common_elements(set1, set2)
print(common_elements)  # Output: {4, 5}"""

#task 2
def unique_elements(lst):
    from collections import Counter

    # Count the occurrences of each element in the list
    element_counts = Counter(lst)

    # Create a set of elements that appear exactly once
    unique_set = {element for element, count in element_counts.items() if count == 1}

    return unique_set


# Example usage
lst = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_set = unique_elements(lst)
print(unique_set)  # Output: {1, 3, 5}
