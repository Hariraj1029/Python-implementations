l = list([1, 2, 3, 4, 5])
l1 = list([6, 7, 8, 9, 10])
l + l1 # Concatenate two lists
l * 2 # Repeat the list two times

# Printing Lists
print(l)

# List Operations
l.append(6)  # Add an element to the end of the list
l.sort()  # Sort the list
l.reverse()  # Reverse the list
l.extend(l)  # Extend the list by another list
l.pop()  # Remove and return the element from the end of the list
l.pop(0)  # Remove and return the element at the specified index
l.remove(3)  # Remove the first occurrence of the element
l.count(2)  # Return the number of occurrences of the element
l.index(2)  # Return the index of the first occurrence of the element
l.insert(0, 10)  # Insert the element before the index
l.clear()  # Remove all the elements from the list

# List Access and Slicing
first_element = l[0]  # Access the element at the specified index
slice1 = l[1:3]  # Access the elements from the start index to the end index
slice2 = l[1:]  # Access the elements from the start index to the end of the list
slice3 = l[:3]  # Access the elements from the start of the list to the end index
last_element = l[-1]  # Access the last element of the list
last_three_elements = l[-3:]  # Access the last three elements of the list
all_except_last_two = l[:-2]  # Access all the elements of the list except the last two
every_second_element = l[::2]  # Access every second element of the list
reverse_list = l[::-1]  # Access all the elements of the list in reverse order
l[1] = 10  # Update the element at the specified index
del l[1]  # Delete the element at the specified index
del l[1:3]  # Delete the elements from the start index to the end index
del l[1:]  # Delete the elements from the start index to the end of the list
del l[:3]  # Delete the elements from the start of the list to the end index
del l[-1]  # Delete the last element of the list
del l[-3:]  # Delete the last three elements of the list
del l[:-2]  # Delete all the elements of the list except the last two
del l[::2]  # Delete every second element of the list
del l[::-1]  # Delete all the elements of the list in reverse order

# Iterating Over Lists
for element in l:  # Iterate over the elements of the list
    print(element)
for i, element in enumerate(l):  # Iterate over the indices and elements of the list
    print(i, element)
for i in range(len(l)):  # Iterate over the indices of the list
    print(l[i])
for i in l[::-1]:  # Iterate over the elements of the list in reverse order
    print(i)
for i in l[::2]:  # Iterate over every second element of the list
    print(i)
for i in l[:-2]:  # Iterate over all the elements of the list except the last two
    print(i)


# List Iterators
list_iterator = iter(l)  # Get an iterator for the list
list_reverse_iterator = reversed(l)  # Get a reverse iterator for the list

# List Comprehensions
list_comprehension = [i for i in l]  # Create a new list from an existing list
list_comprehension_with_condition = [i for i in l if i % 2 == 0]  # Create a new list from an existing list with a condition
list_comprehension_with_operation = [i * 2 for i in l]  # Create a new list from an existing list with an operation
list_comprehension_with_operation_and_condition = [i * 2 for i in l if i % 2 == 0]  # Create a new list from an existing list with an operation and a condition

# List Functions
sum_of_elements = sum(l)  # Get the sum of all the elements of the list
all_elements_true = all(l)  # Check if all the elements of the list are True
any_element_true = any(l)  # Check if any element of the list is True
sorted_list = sorted(l)  # Return a new sorted list
reversed_list = list(reversed(l))  # Return a new reversed list
enumerated_list = list(enumerate(l))  # Return a new list of tuples containing the indices and elements of the list
filtered_list = list(filter(lambda x: x % 2 == 0, l))  # Return a new list of elements that satisfy the condition
mapped_list = list(map(lambda x: x * 2, l))  # Return a new list of elements after applying the function to each element
zipped_list = list(zip(l, l1))  # Return a new list of tuples by zipping the lists

# List Operators and Built-in Functions
concatenated_lists = l.__add__(l1)  # Concatenate two lists
repeated_list = l.__mul__(2)  # Repeat the list two times
element_exists = l.__contains__(1)  # Check if the element exists in the list
number_of_elements = l.__len__()  # Get the number of elements in the list
element_at_index = l.__getitem__(0)  # Access the element at the specified index
slice1 = l.__getitem__(slice(1, 3))  # Access the elements from the start index to the end index
slice2 = l.__getitem__(slice(1, None))  # Access the elements from the start index to the end of the list
slice3 = l.__getitem__(slice(None, 3))  # Access the elements from the start of the list to the end index
last_element = l.__getitem__(slice(-1, None))  # Access the last element of the list
last_three_elements = l.__getitem__(slice(-3, None))  # Access the last three elements of the list
all_except_last_two = l.__getitem__(slice(None, -2))  # Access all the elements of the list except the last two
every_second_element = l.__getitem__(slice(None, None, 2))  # Access every second element of the list
reverse_list = l.__getitem__(slice(None, None, -1))  # Access all the elements of the list in reverse order
l.__setitem__(0, 10)  # Update the element at the specified index
l.__delitem__(0)  # Delete the element at the specified index
l.__delitem__(slice(1, 3))  # Delete the elements from the start index to the end index
l.__delitem__(slice(1, None))  # Delete the elements from the start index to the end of the list
l.__delitem__(slice(None, 3))  # Delete the elements from the start of the list to the end index
l.__delitem__(slice(-1, None))  # Delete the last element of the list
l.__delitem__(slice(-3, None))  # Delete the last three elements of the list
l.__delitem__(slice(None, -2))  # Delete all the elements of the list except the last two
l.__delitem__(slice(None, None, 2))  # Delete every second element of the list
l.__delitem__(slice(None, None, -1))  # Delete all the elements of the list in reverse order
list_iterator = l.__iter__()  # Get an iterator for the list
list_reverse_iterator = l.__reversed__()  # Get a reverse iterator for the list
lists_equal = l.__eq__(l1)  # Check if the lists are equal
lists_not_equal = l.__ne__(l1)  # Check if the lists are not equal  
list_less_than_other = l.__lt__(l1)  # Check if the list is less than the other list
list_less_than_or_equal = l.__le__(l1)  # Check if the list is less than or equal to the other list
list_greater_than_other = l.__gt__(l1)  # Check if the list is greater than the other list
list_greater_than_or_equal = l.__ge__(l1)  # Check if the list is greater than or equal to the other list
list_hash = l.__hash__()  # Get the hash of the list
list_repr = l.__repr__()  # Get the printable representation of the list
list_str = l.__str__()  # Get the string representation of the list

# List Slicing
l = [1, 2, 3, 4, 5]
first_element = l[0]  # Access the element at the specified index
slice1 = l[1:3]  # Access the elements from the start index to the end index
slice2 = l[1:]  # Access the elements from the start index to the end of the list
slice3 = l[:3]  # Access the elements from the start of the list to the end index
last_element = l[-1]  # Access the last element of the list
last_three_elements = l[-3:]  # Access the last three elements of the list
all_except_last_two = l[:-2]  # Access all the elements of the list except the last two
every_second_element = l[::2]  # Access every second element of the list
reverse_list = l[::-1]  # Access all the elements of the list in reverse order

# Combining and Repeating Lists
l1 = [6, 7, 8, 9, 10]
concatenated_lists = l + l1  # Concatenate two lists
repeated_list = l * 2  # Repeat the list two times

# List Checks and Information
element_exists = 1 in l  # Check if the element exists in the list
element_does_not_exist = 1 not in l  # Check if the element does not exist in the list
number_of_elements = len(l)  # Get the number of elements in the list
maximum_element = max(l)  # Get the maximum element of the list
minimum_element = min(l)  # Get the minimum element of the list

# List Comparison and Hashing
lists_equal = l == l1  # Check if the lists are equal
lists_not_equal = l != l1  # Check if the lists are not equal
list_less_than_other = l < l1  # Check if the list is less than the other list
list_less_than_or_equal = l <= l1  # Check if the list is less than or equal to the other list
list_greater_than_other = l > l1  # Check if the list is greater than the other list
list_greater_than_or_equal = l >= l1  # Check if the list is greater than or equal to the other list
list_hash = hash(l)  # Get the hash of the list

# String Representations
list_repr = repr(l)  # Get the printable representation of the list
list_str = str(l)  # Get the string representation of the list