"""Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number """

def increment_string(strng):
    if strng == "":
        return "1"    
    letters= strng.rstrip('0123456789')
    numbers= strng[len(letters):]
    if numbers== "" :
        return letters + "1"
    increment= str(int(numbers)+ 1)
    #for zeroes before a number
    increment= increment.zfill(len(numbers))
    return letters+increment

"""
implement the function below to :
    return a diction with the count of each letter in the string
    example: "aba" -> {"a": 2, "b": 1}
"""
def count_letters(string):
    if not isinstance(string, str):
        raise TypeError("Enter a string")
    number = {}
    for char in string:
        if char.isalpha():
            number[char]= number.get(char,0) +1
    return number
    
"""implement the function below to :
    return a list of sums of each consecutive pair in the list
    example: [1, 2, 3] -> [3, 5]
    """
    
def sum_consecutives(s):
    sumlist=[]
    first_second= len(s) -1
    for i in range(first_second):
        sumlist.append(s[i]+ s[i+1])
    return sumlist
    
"""implement the function below to :
    return the number of unique words in a string
    and throw a value-exception if the input is not a string
    example: 'no example ;)'
    """
    
def count_unique(string):
    if not isinstance(string, str):
        raise TypeError("Enter a string.")
    
    split_string= string.split()
    new_string=set(split_string)
    count= len(new_string)
    return count