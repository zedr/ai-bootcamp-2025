from main import (
    pow_list,
    count_words,
    reverse_string,
    factorial,
    is_palindrome,
    sum_even_numbers,
    find_max,
    count_vowels
)

assert pow_list([1, 2, 3] == [1, 4, 9]), (
    "Implement a function that takes a list "
    "and returns another list with each value raised "
    "to the power of 2"
)

assert count_words("hello world"), (
    "Implement a trivial function that counts the "
    "number of words in the given string. "
    "Hint: try executing the following command in the "
    "Python console: 'hello world'.split(' ')"
)

assert reverse_string("hello") == "olleh", (
    "Implement a function that takes a string "
    "and returns it reversed. For example, 'hello' becomes 'olleh'."
)

assert factorial(5) == 120, (
    "Implement a function that computes the factorial of a given number. "
    "Factorial of n (n!) is the product of all positive integers from 1 to n. "
    "For example, factorial(5) = 5 * 4 * 3 * 2 * 1."
)

assert is_palindrome("racecar") == True, (
    "Implement a function that checks if a given string is a palindrome. "
    "A palindrome reads the same forwards and backwards, e.g., 'racecar'. "
    "Hint: try executing the following command in the "
    "Python console: 'racecar'[::-1]"
)

assert sum_even_numbers([1, 2, 3, 4, 5]) == 6, (
    "Implement a function that takes a list of numbers "
    "and returns the sum of all even numbers in the list."
)

assert find_max([3, 1, 4, 1, 5]) == 5, (
    "Implement a function that takes a list of numbers "
    "and returns the largest number in the list."
)

assert count_vowels("hello world") == 3, (
    "Implement a function that takes a string "
    "and returns the count of vowels ('a', 'e', 'i', 'o', 'u') in it. "
    "For example, 'hello world' contains 3 vowels."
)