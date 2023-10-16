my_set = {1, 2, 3} # Creates a set with unique elements.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

empty_set = set() # Creates an empty set.
my_set.add(4) # Adds an element to the set.
my_set.remove(3) # Removes the specified element from the set.
my_set.discard(5) # Removes the specified element from the set (if it exists).
my_set.pop() # Removes and returns an arbitrary element from the set.
my_set.clear() # Removes all elements from the set.

union_set = set1.union(set2) # Returns a set containing all unique elements from both sets.
intersection_set = set1.intersection(set2) # Returns a set containing common elements between sets.
difference_set = set1.difference(set2) # Returns a set containing elements from set1 but not in set2.
symmetric_difference_set = set1.symmetric_difference(set2) # Returns a set containing elements in either set, but not in both.
is_subset = set1.issubset(set2) # Checks if set1 is a subset of set2.
is_superset = set1.issuperset(set2) # Checks if set1 is a superset of set2.
new_set = my_set.copy() # Creates a shallow copy of the set.
set_size = len(my_set) # Returns the number of elements in the set.
# Iterates through the elements of the set.
for element in my_set:
    print(element)

# Set Comprehension
my_set = {x for x in range(1, 6)} # Creates a set with numbers from 1 to 5.
even_set = {x for x in range(1, 6) if x % 2 == 0} # Creates a set with even numbers from 1 to 5
squared_set = {x**2 for x in range(1, 6)} # Creates a set with the squares of numbers from 1 to 5.

my_set.update({4, 5, 6}) # Updates the set with elements from another set.
my_set.intersection_update({4, 5, 6}) # Updates the set with the intersection of elements from another set.
my_set.difference_update({4, 5, 6}) # Updates the set with the difference of elements from another set.
my_set.symmetric_difference_update({4, 5, 6}) # Updates the set with the symmetric difference of elements from another set.
are_disjoint = set1.isdisjoint(set2) # Checks if sets have no common elements.
frozen_set = frozenset([1, 2, 3]) # Creates an immutable set.
set_to_list = list(my_set) # Converts a set to a list.
set_to_tuple = tuple(my_set) # Converts a set to a tuple.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Unique Implementations of Sets

# 1. Finding Unique Elements in a List
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
# Converts a list to a set to automatically remove duplicates.

# 2. Set Union Without Duplicates
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_without_duplicates = set1 | set2
# Finds the union of two sets without duplicates.

# 3. Set Intersection for Multiple Sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6}
set3 = {5, 6, 7, 8}
intersection_of_multiple_sets = set1 & set2 & set3
# Finds the intersection of multiple sets.

# 4. Finding Unique Letters in a Sentence
sentence = "This is a sample sentence with some unique letters."
unique_letters = set(char for char in sentence if char.isalpha())
# Uses a set to find unique letters in a sentence.

# 5. Symmetric Difference of Multiple Sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}
symmetric_difference_of_multiple_sets = set1 ^ set2 ^ set3
# Finds the symmetric difference of multiple sets.

# 6. Set Subtraction for a List of Sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
set3 = {4, 5}
list_of_sets = [set1, set2, set3]
result = list_of_sets[0]
for s in list_of_sets[1:]:
    result -= s
# Performs set subtraction on a list of sets to find the elements unique to the first set.

# 7. Finding Duplicate Elements in Multiple Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [7, 8, 9, 10, 11]
duplicate_elements = set(list1) & set(list2) & set(list3)
# Finds the elements that are duplicates in multiple lists.

# 8. Set-based Counting
text = "This is a sample text for counting characters."
character_count = {char: text.count(char) for char in set(text) if char.isalpha()}
# Uses a set to count the occurrences of each unique character in a text.

# 9. Set Comprehension with Conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {x**2 for x in numbers if x % 2 == 0}
# Creates a set of squares for even numbers in a list.

# 10. Symmetric Difference with Update
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
# Updates set1 with the symmetric difference of set2.

# 11. Set-based Anagrams
word1 = "listen"
word2 = "silent"
is_anagram = set(word1) == set(word2)
# Checks if two words are anagrams using sets.

# 12. Set-based Palindromes
word = "madam"
is_palindrome = set(word) == set(reversed(word))
# Checks if a word is a palindrome using sets.

# 13. Set-based Pangrams
sentence = "The quick brown fox jumps over the lazy dog."
is_pangram = set(sentence.lower()) >= set("abcdefghijklmnopqrstuvwxyz")
# Checks if a sentence is a pangram using sets.

# 14. Set-based Subsequences
word = "python"
subsequences = {word[i:j] for i in range(len(word)) for j in range(i + 1, len(word) + 1)}
# Finds all subsequences of a word using sets.

# 15. Set-based Substrings
word = "python"
substrings = {word[i:j] for i in range(len(word)) for j in range(i + 1, len(word) + 1) if len(word[i:j]) > 1}
# Finds all substrings of a word using sets.

# 16. Set-based Sublists
my_list = [1, 2, 3]
sublists = {tuple(my_list[i:j]) for i in range(len(my_list)) for j in range(i + 1, len(my_list) + 1)}
# Finds all sublists of a list using sets.

# 17. Set-based Subsets
my_set = {1, 2, 3}
subsets = {frozenset(my_set) - frozenset({x}) for x in my_set}
# Finds all subsets of a set using sets.

# 18. Set-based Permutations
from itertools import permutations
my_list = [1, 2, 3]
permutations = {tuple(p) for p in permutations(my_list)}
# Finds all permutations of a list using sets.

# 19. Set-based Combinations
from itertools import combinations
my_list = [1, 2, 3]
combinations = {tuple(c) for i in range(len(my_list)) for c in combinations(my_list, i + 1)}
# Finds all combinations of a list using sets.

# 20. Set-based Combinations with Replacement
from itertools import combinations_with_replacement
my_list = [1, 2, 3]
combinations = {tuple(c) for i in range(len(my_list)) for c in combinations_with_replacement(my_list, i + 1)}
# Finds all combinations with replacement of a list using sets.

# 21. Set-based Cartesian Product
from itertools import product
my_list = [1, 2, 3]
cartesian_product = {tuple(p) for p in product(my_list, repeat=2)}
# Finds the Cartesian product of a list using sets.

# 22. Set-based Power Set
from itertools import chain, combinations
my_list = [1, 2, 3]
power_set = {tuple(chain.from_iterable(combinations(my_list, r))) for r in range(len(my_list) + 1)}
# Finds the power set of a list using sets.

# 23. Set-based Unique Combinations
from itertools import combinations
my_list = [1, 2, 3]
unique_combinations = {tuple(sorted(c)) for i in range(len(my_list)) for c in combinations(my_list, i + 1)}
# Finds all unique combinations of a list using sets.

# 24. Set-based Unique Combinations with Replacement
from itertools import combinations_with_replacement
my_list = [1, 2, 3]
unique_combinations = {tuple(sorted(c)) for i in range(len(my_list)) for c in combinations_with_replacement(my_list, i + 1)}
# Finds all unique combinations with replacement of a list using sets.

# 25. Set-based Unique Permutations
from itertools import permutations
my_list = [1, 2, 3]
unique_permutations = {p for p in permutations(my_list)}
# Finds all unique permutations of a list using sets.

