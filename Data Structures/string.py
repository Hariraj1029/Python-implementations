# String Methods and Operations Documentation

# Basic String Operations

s = str("Hariraj")  # create a string object and assign it to the variable
print(s)    # Hariraj

# String Manipulation

s.replace("Hariraj", "Hariraj Rathod")  # Return a new string by replacing the old string with the new string
s.upper()  # Return a new string by converting all the characters to uppercase
s.lower()  # Return a new string by converting all the characters to lowercase
s.title()  # Return a new string by converting the first character of each word to uppercase
s.capitalize()  # Return a new string by converting the first character to uppercase
s.swapcase()  # Return a new string by swapping the cases of all the characters

# String Checks

s.startswith("H")  # Check if the string starts with the specified substring
s.endswith("j")  # Check if the string ends with the specified substring
s.find("r")  # Return the index of the first occurrence of the substring
s.rfind("r")  # Return the index of the last occurrence of the substring
s.index("r")  # Return the index of the first occurrence of the substring
s.rindex("r")  # Return the index of the last occurrence of the substring
s.count("r")  # Return the number of occurrences of the substring
s.isalnum()  # Check if the string is alphanumeric
s.isalpha()  # Check if the string is alphabetic
s.isdecimal()  # Check if the string is decimal
s.isdigit()  # Check if the string is digit
s.islower()  # Check if the string is lowercase
s.isupper()  # Check if the string is uppercase
s.isspace()  # Check if the string is whitespace
s.istitle()  # Check if the string is titlecase

# String Stripping

s.strip()  # Return a new string by removing the leading and trailing whitespace
s.lstrip()  # Return a new string by removing the leading whitespace
s.rstrip()  # Return a new string by removing the trailing whitespace

# String Splitting and Joining

s.split()  # Return a new list of strings by splitting the string at the whitespace
s.split(",")  # Return a new list of strings by splitting the string at the specified separator
s.join(["H", "a", "r", "i", "r", "a", "j"])  # Return a new string by joining the elements of the list using the string as the separator

# Slicing with Step Count

# String Slicing
s[1:5]  # Get a substring from index 1 to 4 (5 is not included)
s[:5]   # Get a substring from the start to index 4
s[1:]   # Get a substring from index 1 to the end
s[:]    # Get a copy of the entire string

# Slicing with Step (Stride) Count
s[::2]  # Get every second character
s[::-1]  # Reverse the string

# Custom Step Count
s[1:8:2]  # Get characters at even indices starting from index 1
s[::3]  # Get every third character starting from index 0
s[1::3]  # Get every third character starting from index 1
s[:8:3]  # Get every third character starting from index 0 and ending at index 7


# String Justification and Padding

s.center(10)  # Return a new string by centering the string with the specified width
s.ljust(10)  # Return a new string by justifying the string to the left with the specified width
s.rjust(10)  # Return a new string by justifying the string to the right with the specified width
s.zfill(10)  # Return a new string by filling the string with zeros from the left with the specified width

# String Encoding and Formatting

s.encode()  # Return a new string by encoding the string using the default encoding
s.encode("utf-8")  # Return a new string by encoding the string using the specified encoding
s.format()  # Return a new string by replacing the placeholders with the values
s.format_map({"name": "Hariraj"})  # Return a new string by replacing the placeholders with the values from the dictionary

# String Translation and Partitioning

s.maketrans("H", "R")  # Return a new translation table by mapping the characters
s.translate(s.maketrans("H", "R"))  # Return a new string by translating the string using the translation table
s.partition("r")  # Return a new tuple of strings by partitioning the string at the first occurrence of the separator
s.rpartition("r")  # Return a new tuple of strings by partitioning the string at the last occurrence of the separator
s.rsplit()  # Return a new list of strings by splitting the string at the whitespace
s.rsplit(",", 1)  # Return a new list of strings by splitting the string at the specified separator
s.splitlines()  # Return a new list of strings by splitting the string at the line boundaries

# String Tab Expansion

s.expandtabs()  # Return a new string by replacing the tab characters with the spaces

# String Operators and Built-in Functions

s.__add__(" Rathod")  # Return a new string by concatenating the strings
s.__mul__(2)  # Return a new string by repeating the string two times
s.__contains__("H")  # Check if the string contains the specified substring
len(s)  # Get the number of characters in the string
max(s)  # Get the maximum character in the string
min(s)  # Get the minimum character in the string

# String Indexing and Slicing

s.__getitem__(0)  # Access the character at the specified index
s.__getitem__(slice(0, 3))  # Access the characters from the start index to the end index
s.__getitem__(slice(0, None))  # Access the characters from the start index to the end of the string
s.__getitem__(slice(None, 3))  # Access the characters from the start of the string to the end index
s.__getitem__(slice(-1, None))  # Access the last character of the string
s.__getitem__(slice(-3, None))  # Access the last three characters of the string
s.__getitem__(slice(None, -2))  # Access all the characters of the string except the last two
s.__getitem__(slice(None, None, 2))  # Access every second character of the string
s.__getitem__(slice(None, None, -1))  # Access all the characters of the string in reverse order

# String Modification

s.__setitem__(0, "R")  # Update the character at the specified index
s.__delitem__(0)  # Delete the character at the specified index
s.__delitem__(slice(0, 3))  # Delete the characters from the start index to the end index
s.__delitem__(slice(0, None))  # Delete the characters from the start index to the end of the string
s.__delitem__(slice(None, 3))  # Delete the characters from the start of the string to the end index
s.__delitem__(slice(-1, None))  # Delete the last character of the string
s.__delitem__(slice(-3, None))  # Delete the last three characters of the string
s.__delitem__(slice(None, -2))  # Delete all the characters of the string except the last two
s.__delitem__(slice(None, None, 2))  # Delete every second character of the string
s.__delitem__(slice(None, None, -1))  # Delete all the characters of the string in reverse order

# String Iteration

for i in s:  # Iterate over the characters of the string
    print(i)
for i in range(len(s)):  # Iterate over the indices of the string
    print(s[i])
for i, v in enumerate(s):  # Iterate over the indices and characters of the string
    print(i, v)

s.__iter__()  # Get an iterator for the string
s.__reversed__()  # Get a reverse iterator for the string

# String Comparison and Hashing

s.__eq__("Hariraj")  # Check if the strings are equal
s.__ne__("Hariraj")  # Check if the strings are not equal
s.__lt__("Hariraj")  # Check if the string is less than the other string
s.__le__("Hariraj")  # Check if the string is less than or equal to the other string
s.__gt__("Hariraj")  # Check if the string is greater than the other string
s.__ge__("Hariraj")  # Check if the string is greater than or equal to the other string

s.__hash__()  # Get the hash of the string

# String Information

s.__len__()  # Get the number of characters in the string
s.__repr__()  # Get the printable representation of the string
s.__str__()  # Get the string representation of the string

# String Formatting

s.__format__()  # Get the formatted representation of the string
s.__format__("{name}")  # Get the formatted representation of the string by replacing the placeholders with the values
s.__format__("{name}", name="Hariraj")  # Get the formatted representation of the string by replacing the placeholders with the values from the dictionary

# String Attribute Operations

s.__setattr__("name", "Hariraj")  # Set the attribute of the string
s.__delattr__("name")  # Delete the attribute of the string
s.__getattribute__("name")  # Get the attribute of the string

# String Information and Size

s.__dir__()  # Get the list of attributes of the string
s.__sizeof__()  # Get the size of the string

# String Miscellaneous

s.__doc__  # Get the documentation of the string
s.__dict__  # Get the dictionary of the string
s.__class__  # Get the class of the string

# String Creation

s.__new__(str, "Hariraj")  # Create a new string

# String Serialization and Deserialization

s.__reduce__()  # Get the tuple of the string
s.__reduce_ex__()  # Get the tuple of the string

