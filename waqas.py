# -*- coding: utf-8 -*-
"""waqas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S-k_p-On-iCjKDDxZMdmM4DIZ3eXjXWr
"""

""" Name: Muhammad Waqas Ahmed
    Role NO. = 23-AI-53
    Section = A1
"""


# Function to find the longest palindrome length from the given string 's'
def longestPalindrome(s: str) -> int:

    char_counts = {
    }  # Create an empty dictionary to store the counts of each character in the string

    # Loop through the string and count occurrences of each character
    for char in s:
        # If the character is already in the dictionary, increment its count
        if char in char_counts:
            char_counts[char] += 1
        else:
            # Otherwise, add the character to the dictionary with an initial count of 1
            char_counts[char] = 1

    palindrome_len = 0  # Initialize a variable to store the length of the longest palindrome

    # Flag to check if there is any character with an odd count
    has_odd_count = False

    # Loop through the character counts in the dictionary
    for count in char_counts.values():
        # If the count of the character is even, it can be fully used to form a palindrome
        if count % 2 == 0:
            palindrome_len += count
        else:
            # If the count is odd, add the largest even number of occurrences (count - 1)
            palindrome_len += count - 1
            # Set the flag indicating that there is at least one character with an odd count
            has_odd_count = True

    # If there is at least one character with an odd count, we can place one of them
    # in the center of the palindrome, thus increasing the palindrome length by 1
    if has_odd_count:
        palindrome_len += 1

    # Step 6: Return the total length of the longest possible palindrome that can be formed
    return palindrome_len


# Example test cases to check the function behavior

# Test case 1: Input string "abccccdd"
a = longestPalindrome("abccccdd")
# Test case 2: Input string "a"
b = longestPalindrome("a")

print(a)
print(b)