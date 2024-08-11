# Concept:
# Regular expressions(regex) are sequences of characters that define search patterns. They are powerful tools for string matching, searching, and manipulation. Python's re module provides support for working with regular expressions.

# Basic Functions in re Module:

# re.match():

# Checks for a match only at the beginning of the string.
# Returns a match object if successful, None otherwise.

import re
result = re.match(r'hello', 'hello world')
print(result)  # Output: <re.Match object; span=(0, 5), match='hello'>

# re.search()

# Searches the entire string for a match.
# Returns a match object if a match is found anywhere in the string.

result = re.search(r'world', 'hello world')
print(result)  # Output: <re.Match object; span=(6, 11), match='world'>

# re.findall():

# Returns a list of all matches found in the string.
# If no match is found, it returns an empty list.

result = re.findall(r'\d+', 'There are 2 cats and 3 dogs.')
print(result)  # Output: ['2', '3']

# re.sub():

# Substitutes all matches in the string with another string.
# Useful for replacing patterns.

result = re.sub(r'\d+', 'number', 'There are 2 cats and 3 dogs.')
print(result)  # Output: 'There are number cats and number dogs.'

# Common Regex Patterns:
# .: Matches any character except a newline.
# \d: Matches any digit (0-9).
# \D: Matches any non-digit character.
# \w: Matches any alphanumeric character (letters and digits).
# \W: Matches any non-alphanumeric character.
# \s: Matches any whitespace character (spaces, tabs, etc.).
# \S: Matches any non-whitespace character.
# ^: Matches the start of the string.
# $: Matches the end of the string.
# [abc]: Matches any one of the characters a, b, or c.
# [a-z]: Matches any character from a to z.
# [^abc]: Matches any character except a, b, or c.
# *: Matches 0 or more repetitions of the preceding pattern.
# +: Matches 1 or more repetitions of the preceding pattern.
# ?: Matches 0 or 1 repetition of the preceding pattern.
# {n}: Matches exactly n repetitions of the preceding pattern.
# {n,m}: Matches between n and m repetitions of the preceding pattern.
