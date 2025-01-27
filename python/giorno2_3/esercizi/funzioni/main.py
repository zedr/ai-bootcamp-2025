# Scrivere il codice dell'esercizi qui dentro
def mydivmod(num,den):
    """ This function make a division num/den, and return a tuple with (quotient,remainder)
    Input: num type int or float. the dividend
           den type int or float. the divisor
    Output: tuple (quotient num//den, remainder num % den)
    Error in case of division by zero (if den is 0)
    Example (2,1) = (2,0) """
    if den == 0:
        raise ZeroDivisionError("Second argument to a division operation was zero")
    q = num//den #quotient
    r = num % den #remainder
    return q,r

#list_of_number = [1,4,5] #test
def pow_list(list_of_number):
    """ This function takes a list and returns another
    list with each value raised to the power of 2
    input: list of number
    output: list of input number squared

    Example pow_list([1, 2, 3] == [1, 4, 9])
    """
    squared_list = [] #output list
    for x in list_of_number:
        squared_list.append(x ** 2) #squared each element
    return squared_list

def count_words(s):
    """ This trivial function counts the
    number of words in the given string.
    Hint: try executing the following command in the
    Python console: 'hello world'.split(' ')
    Input: string
    Output: number of words """
    #count = len(s.split(' '))  #NOTE if there is a final space it find a word more (error)
    #return count
    count = 0
    word = False
    for chr in s:
        if chr != ' ':
            if not word:
                count += 1
                word = True #i'm in a word
        else:
            word = False
    return count

def reverse_string(s):

    """ This function  takes a string and returns it reversed.
    For example, 'hello' becomes 'olleh'
    reverse_string("hello") == "olleh" """
    s = s[::-1]
    return s

def factorial(num):
    """ This function computes the factorial of a
     given number. Factorial of n (n!) is the product of all
     positive integers from 1 to n.
     For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120 """
    """  
    while num > 0:
        num_2 = num - 1
        fact = num * num_2
        num = num_2
    return fact  """
    fact=1 #init
    for i in range(1,num+1):
        fact *= i
    return fact

def is_palindrome(s):
    """ This function checks if a given string is
    a palindrome.A palindrome reads the same forwards and
    backwards, e.g., 'racecar'.  [::-1].
    is_palindrome("racecar") == True """
    s_1 = s[::-1]
    if s_1==s:
        return True
    else:
        return False

def sum_even_numbers(ls):
    """ This function takes a list of numbers
     and returns the sum of all even numbers in the list
      Example: sum_even_numbers([1, 2, 3, 4, 5]) == 6
      Input: list of number
      Output: sum of the even number in the list  """
    sum = 0
    for x in ls:
        if x % 2 == 0:
            sum += x
    return sum

def find_max(ls):
    """ This function takes a list of numbers
    and returns the largest number in the list.
    Example: find_max([3, 1, 4, 1, 5]) == 5  """
    return max(ls)

def count_vowels(s):
    """ This function takes a string and returns the count of vowels in it.
    ('a', 'e', 'i', 'o', 'u')
    For example, count_vowels("hello world") == 3
    'hello world' contains 3 vowels. """
    count = 0
    for char in s:
        if char in 'aeiou':
            count += 1

    return count

"""%%%%%%%%%%%%%% esercizio di gruppo
class Account:
    def __init__(self,name):
        self.name = name

account = Account(name= "Martina")
assert account.name == "Martina"

class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0 #attributo di istanza
    def deposit(self, credit):
        self.balance += credit
        
account = Account(name="Martina", balance = 500)
assert account.balance == 500 """
