#                                         PYTHON   PROGRAMMES

# 1. Write a program to find the length of the string without using inbuilt function (len).
string = "Happy"
counter = 0
for i in string:
    counter += 1
print(counter)

######################################################################################################################

# 2. Write a program to reverse a string without using any inbuilt functions.
string = "computer"
new = ""
for i in string:
    new = i + new
print(new)

######################################################################################################################

# 3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".
string = "Hello World"
res = string.replace("World", "Universe")
print(res)

######################################################################################################################

# 4. How to convert a string to a list and vice-versa.
string = "abcd efgh ijkl mnop"
li = string.split()
print(li)

st = " ".join(li)
print(st)

######################################################################################################################

# 5. Convert the string "Hello welcome to Python" to a comma separated string.
old = "Hello welcome to Python"
new = old.replace(" ",",")
print(new)

######################################################################################################################

# 6. Write a program to print alternate characters in a string.
string = "Hello welcome to Python"
print(string[::2])

######################################################################################################################

# 7. Write a Program to print ascii values of the characters present in a string.
string = "Hello"
char_ascii = [f"{char}->{ord(char)}" for char in string]
print(char_ascii)

######################################################################################################################

# 8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.
def swapcase(string):
    res = ""
    for i in string:
        if ord("a") <= ord(i) <= ord("z"):
            upper = chr(ord(i)-32)
            res += upper
        elif ord("A") <= ord(i) <= ord("Z"):
            lower = chr(ord(i)+32)
            res += lower
    return res


print(swapcase("HelloWorld"))

######################################################################################################################

# 9. Write a program to swap two numbers without using the 3rd variable.
a = 10
b = 20
a, b = b, a
print(a)
print(b)

######################################################################################################################

# 10. Write a program to merge two different lists.
l1 = [1, 2, 3, 4]
l2 = ["one", "two", "three", "four"]
res = l1 + l2
print(res)

######################################################################################################################

# # 11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)
import random

def randomline(filepath):
    with open(filepath) as f:
        lines = f.readlines()
        r_line = random.choice(lines)
        return r_line


path = r"Python_Interview_Questions/source/file_abc.txt"
print(randomline(path))

######################################################################################################################

# 12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)
def file_lines(filepth,start_line,stopline):
    with open(filepth) as file:
        lines = file.readlines()[start_line:stopline]
        for line in lines:
            print(line)


path = r"Python_Interview_Questions/source/file_abc.txt"
file_lines(path,5,15)

######################################################################################################################

# 13 Program to print the last "N" lines of a file.

def last_n(file_path, last_lnes):
    with open(file_path) as file:
        lines = file.readlines()[-(last_lnes):]
        for line in lines:
            print(line)


path = r"Python_Interview_Questions/source/file_abc.txt"
last_n(path,6)

######################################################################################################################

# 14. Write a program to check if the given string is Palindrome or not without using reversed method.

def palindrome(string):
    newstring = ""
    for i in string:
        newstring = i + newstring

    if string == newstring:
        print("palindrome")
    else:
        print("Not a palindrome")


string = "TELUGU"
palindrome(string)

string = "MALAYALAM"
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

######################################################################################################################

# 15. Write a program to search for a character in a given string and return the corresponding index.

def index(string, char):
    indexes = []
    for index,character in enumerate(string):
        if char == character:
            indexes.append(index)
    if len(indexes)>0:
        print(f"Given character is present at the index numbers {indexes}")
    else:
        print("Character is not present in the string")


string = "python programming language"
char = "p"
index(string, char)

######################################################################################################################

# 16. Write a program to get the below output
sentence = "hello world welcome to python programming hi there"
# d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'],  't': ['to', 'there'], 'p': ['python', 'programming'] }
res = {}
for word in sentence.split():
    if word[0] not in res:
        res[word[0]] = [word]
    else:
        res[word[0]] += [word]
print(res)

######################################################################################################################

# 17. Write a program to replace all the characters with “-“, if the character occurs more than once in a string.
string = 'hellohai'  # # O/P should be '-e--o-ai'
list = [char if string.count(char) == 1 else "-" for char in string]
print("".join(list))

######################################################################################################################

# 18. Write a decorator that returns only positive values of subtraction.

def pos(func):
    def wrapper(*args,**kwargs):
        print("Its a positive only Decorator")
        result = func(*args, **kwargs)
        return abs(result)
    return wrapper

@pos
def add(a,b):
    return a+b

print(add(-12,55))

######################################################################################################################

# 19. How to get the count of the number of instances of a class that is being created.

class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1


print(InstanceCounter.count)
a = InstanceCounter()
b = InstanceCounter()
print(InstanceCounter.count)

######################################################################################################################

# 20. Write a function which takes a list of strings and integers.
# If the item is a string it should print as is and if the item is integer or float it should reverse it.
def abcd(li):
    res = []
    for item in li:
        if isinstance(item, str):
            res.append(item)

        elif isinstance(item, int):
            res.append((int(str(item)[::-1])))

        elif isinstance(item, (float)):
            res.append((float(str(item)[::-1])))
    return res


lis = ["hello", "world",5.3,96,3.33]
print(abcd(lis))

######################################################################################################################

# 21. Write a class named Simple and it should have iteration capability.

class Simple:

    def __init__(self, collection):
        self.collection = collection
        self.current=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.collection):
            value = self.collection[self.current]
            self.current += 1
            return value
        else:
            raise StopIteration


s=Simple(("hi", "hello", 2, 3, 4, 5))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
# print(next(s))

t = Simple(["chandu", "deadman", "Bad Lucky Fellow"])
for i in t:
    print(i)

# next(t)

######################################################################################################################

# 22. Write a Custom class which can access the values of dictionaries using d['a'] and d.a.

class MyDict:

    def __init__(self,collection):
        self.collection = collection

    def __getitem__(self, key):         #__getitem__ method (using square brackets)
        return self.collection[key]

    def __getattr__(self, key):         #__getattr__ method (using dot notation)
        if key in self.collection:
            return self.collection[key]
        else:
            raise AttributeError(f"MyDict class has no attribute {key}")


obj = MyDict({"a": 1, "b": 2, "c": 3})
print(obj.c)
print(obj["a"])
# print(obj.r)
# print(obj["r"])

######################################################################################################################

# 23. Write a python program to get the below output.
# sentence = "Hi How are you"
# o/p should be "iH woH era uoy"
sentence = "Hi How are you"
print(len(sentence))
res = ""
words = sentence.split()
for i in words:
    if i is not words[-1]:
        res += i[::-1] + " "
    else:
        res += i[::-1]

print(res)
print(len(res))

######################################################################################################################

# 24. Write a python program to get the below output.
# sentence = "Hi How are you"
# o/p should be "ouy era woH iH"
sentence = "Hi How are you"
print(sentence[::-1])
res = ""
for char in sentence:
    res = char + res
print(res)

######################################################################################################################

# 25. Write a lambda function to add two numbers (a, b).
res = lambda a, b: a+b
print(res(25, 2))

######################################################################################################################

# 26. What is the output of the following?
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print((a, b))
res1 = [[1, 2, 3], [4, 5, 6]]
res2 = ([1, 2, 3],  [4, 5, 6])

######################################################################################################################

# 27. How to remove duplicates from the list without using inbuilt functions.
# 	>>> items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
res = []
for item in items:
    if item not in res:
        res.append(item)

print(res)
# print(list(set(items)))

######################################################################################################################

# 28. Find the longest word in the sentence.
# >>> sentence = "Hello world. Welcome to Python"
def longest(string):
    words = string.split()
    long_word = ""
    for word in words:
        if len(word) > len(long_word):
            long_word = word

    return long_word


sentence = "Hello world. Welcome to Python"
print(longest(sentence))

######################################################################################################################

# 29. write a program to reverse the values in the dictionary if the value is of type String.
# 	>>> d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
res = {}
for key, value in d.items():
    if key not in res:
        if isinstance(value, str):
            res[key] = value[::-1]
        else:
            res[key] = value

print(res)

######################################################################################################################

# 30. write a program to get 1234 from the below tuple.
# t = ('1', '2', '3', '4')
t = ('1', '2', '3', '4')
print("".join(t))

######################################################################################################################

# 31. How to get the elements that are in list b but not in list a.
a = [1, 2, 3]
b = [1, 2, 3, 4]

for i in b:
    if i not in a:
        print(i)

######################################################################################################################

# 32. A function takes variable number of positional arguments as input.
# How to check if the arguments that are passed are more than 5.
def vars(*args, **kwargs):
    if len(args) > 5:
        return "YES Positional Arguments are more than 5"
    else:
        return "No Positional Arguments are equal or less than 5"


a = (1,2,3,5,7,555)
print(vars(*a))

######################################################################################################################

# 33. Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.
# Assume Below is the contents of the log file
# lines =	     """CRITICAL: Hello world
#                 INFO: This is an info
#                 ERROR: This is an error
#                 CRITICAL: This is critical
#                 CRITICAL:Hello world
#                 INFO: This is an info
#                ERROR: This is an error
#                 CRITICAL: This is critical
#                 CRITICAL:Hello world
#                 INFO: This is an info
#                 ERROR: This is an error
#                 CRITICAL: This is critical
#                 CRITICAL:Hello world
#                 INFO: This is an info
#                 ERROR: This is an error
#                 CRITICAL: This is critical"""

import re
with open(r"Python_Interview_Questions/source/file_xyz.txt") as file:
    lines = file.readlines()
    messages = {}
    for line in lines:
        pattern = re.findall(r"CRITICAL|INFO|ERROR",line.strip())
        if pattern:
            for item in pattern:
                if item not in messages:
                    messages[item] = 1
                else:
                    messages[item] += 1
print(messages)

######################################################################################################################

# 34. Write a function to reverse any iterable without using reverse function.


def revv(iterable):
    return iterable[::-1]


a = [1,2,3,4,5]
print(revv(a))
b = (1,2,3,4,5)
print(revv(b))
e = "hello"
print(revv(e))

######################################################################################################################

# 35. Write a function to print the below output.**
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX
def func(string,index):
    if index == 0:
        return string[index+1::2]
    elif index == 1:
        return string[index - 1::2]

print(func("TRACXN",0))
print(func("TRACXN",1))

######################################################################################################################

# 36. Sum all the numbers in the below string.**
s = "Sony12India567Pvt2ltd" # eg.1+2+5+6+7+2
import re
total = 0
matches = re.findall(r"[\d]",s)
print(matches)
for match in matches:
    total += int(match)

print(total)

######################################################################################################################

# 37. Write a program to sum all the numbers in below string.**
s = "Sony12India567Pvt2ltd" # eg.12+567+2
import re

total = 0
matches = re.findall(r"[\d]+", s)
print(matches)
for match in matches:
    total += int(match)

print(total)

######################################################################################################################

# 38. Print all the numbers in the below list**
a = ['abc', '123', 'hello', '23']
for item in a:
    if item.isnumeric():
        print(item)

######################################################################################################################

# 39. Program to print the number of occurrences of characters in a String without using inbuilt functions.**
# >>> s = 'helloworld'
s = "helloworld"
word_count = {}
for char in s:
    if char not in word_count:
        word_count[char] = 1
    else:
        word_count[char] += 1

print(word_count)

######################################################################################################################

# 40. Program to print only the repeated characters and count of the same.**
# >>> s = 'helloworld'
s = "helloworld"
word_count = {i : s.count(i) for i in s if s.count(i) > 1}
print(word_count)

######################################################################################################################

# 41. Write a program to get alternate characters of a string in list format.**
# >>> s = 'helloworld'
s = "helloworld"
res1 = [value for index, value in enumerate(s) if index % 2 == 0]
res2 = [value for index, value in enumerate(s) if index % 2 != 0]
print(res1)
print(res2)

######################################################################################################################

# 42. Write a program to get square of list of number's using lambda function .**
# >>> a = [1, 2, 3, 4, 5]
# a = [1, 2, 3, 4, 5]
# res = list(map(lambda i : i ** 2, a))
# print(res)

######################################################################################################################

# 43. Write a function that accepts two strings and returns True if the two strings are anagrams of each other.
def anagrams(string1,string2):
    if sorted(string1) == sorted(string2):
        print("TRUE")
    else:
        print("FALSE")


anagrams("hello world", "hello world")
anagrams("hello world", "hello universe")

######################################################################################################################

# 44. Write a program to iterate through list and build a new list,
# only if the items of the list has even number of characters.
# >>> names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
new_list = [item for item in names if len(item) % 2 == 0]
print(new_list)

######################################################################################################################

# 45. Write a program to iterate through list and build a new dictionary,
# only if the items of the list has even number of characters.**
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
new_dict = {item: len(item) for item in names if len(item) % 2 == 0}
print(new_dict)

######################################################################################################################

# 46. Write a program which squares the numbers in a list using map object.
a = [1, 2, 3, 4, 5]


def square(i):
    return i ** 2


res = map(square, a)
# print(list(res))

######################################################################################################################

# 47. Count number of lines in a file without loading the file to the memory.
with open(r"Python_Interview_Questions/source/file_xyz.txt") as file:
    total_lines = 0
    for line in file:
        total_lines += 1
print(total_lines)

######################################################################################################################

# 48. Printing line and line no's in a file**
with open(r"Python_Interview_Questions/source/file_xyz.txt") as file:
    for line_no, line in enumerate(file, start=1):
        print(line_no, "----->>>", line.strip())

######################################################################################################################

# 49. Write a Program to print the sum of entire list and sum of only internal list**
l = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
internal = [sum(item) for item in l]
entire = sum(internal)
print(internal)
print(entire)

######################################################################################################################

# 50. Write a program to reverse the list as below**
# # words = ["hi", "hello", "python"]
# # >>> res = ["python", "hello", "hi"]
words = ["hi", "hello", "python"]
print(words[::-1])

res = sorted(words, key=len, reverse=True)
print(res)

######################################################################################################################
