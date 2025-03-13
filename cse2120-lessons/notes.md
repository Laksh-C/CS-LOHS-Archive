// notes.md

# CSE2120 - Data and Data Structures
Data Structures are organizational, management, and formatting tools for storing large data sets. In programming, these structures are stored in variables or other data structures. There are many different types of data structures: Tuples, Lists, Arrays, Dictionaries, Queues, and Stacks. 

## Types of Data Structures in Python
### Tuple
A _Tuple_ is a static data structure where the data is immutable (cannot be changed). All data is declared when the variable is created. 

```python
# Tuple
A_TUPLE = (1, 3, 5.0, "eleven", 13) # uses parenthesis
A TUPLE = (1, 3, 5.0, "eleven", 17) # updating a single value. (need to change whole tuple) 
# multiple output from a function
# personal information
    # (year, month, day)
    # (firstname, lastname)
NAME = (first_name, last_name)
DATE = (year, month, day)

print(A_TUPLE) # output (1, 3, 5.0, "eleven", 17)
print(A_TUPLE[1]) # output 3
```

When using data structures, each individual data node within the structure is assigned an **index number**. This index number identifies the specific locatino that the data is stored in the structure. Index numbers begin counting at **0** and increases as integers. 

(IB) - in IB, the term tuple is not used because it is a python specific term. Instead, IB will use the term array. 

### Lists
A *List* is a one-dimensional array that is a dynamic data structure, where individual nodes are mutable (can be updated). 

```python
# LIST
A_LIST = [1, 3, 5.0, 7, "eleven", 13]
A_LIST[5] = 17 # update a single value in a list 

print(A_LIST) # output [1, 3, 5.0, 7, "eleven", 17]
print(A_LIST[1]) # output 3
```

NOTE: Despite tuples using parenthesis and lists using brackets, when declaring an index value (node), the index number is *always in brackets*.

NOTE (IB): Lists in Java, which is what IB pseudocode is based upon, calls dynamic lists ArrayLists. 

### Static vs Dynamic Arrays
In most cases, either a static or dynamic array can be used to store data. However, there are instances where one is preferable over another. For data that should not be changed independently, static arrays are preferable. 
* Storing Screen Resolution
* Storing a position on a 2D or 3D plane
* Storing identification information of an individual

Oftentimes, tuples are used to store information that is difficult to change. For example, your name links to your student ID, One should never be changed in a program without changing the other. 

### Data Structure Indexing and Calling
Frequently, calling on a single value within the data structure is needed instead of the entire structure. Therefore, there needs to be a process of identifying a single value. Each value has a positional index number associated with it. 

```python
indexNumber = [0, 1, 2, 3, ...]
```

To reference a specific value, include the list name followed immediately with the index number in brackets. 

```python
A_LIST = ["This", "is", "a", "sentence."]
print(A_LIST[3]) # output "sentence."
```

Array indexing has forward (head-to-tail) indexing and backwards (tail-to-head) indexing. Either index number will call the data value.

```python
A_LIST = ["This", "is", "a", "sentence."]
# index      0      1    2       3
# index     -4     -3   -2      -1

print(A_LIST[-3]) # output "is"
```

To reference a subset of values, include a start index value and an end index value separated by a colon. NOTE: The subset starts at the starting index value, but goes up to, not including, the end index value. 

```python
A_LIST = ["This", "is", "a", "sentence."]
SUBLIST = A_LIST[1:3] # equals ["is", "a"]
```

There are two shortcuts to creating sub-lists from the beginning and the end of the list. When starting a sublist from the beginning of the list, omit the first number; to have a sublist go to the end, omit the last number. 

```python
A_LIST = ["This", "is", "a", "sentence."]
SUBLIST2 = A_LIST[:3] # equals ["This", "is", "a"]
SUBLIST3 = A_LIST[1:] # equals ["is", "a", "sentence."]
```

### List Lengths
All lists also have a length property, where the total number of data values is callable using the ```len(LIST)``` function. 
```python
A_LIST = ["This", "is", "a", "sentence."]
print(len(A_LIST)) # OUTPUT 4

for i in range(len(A_LIST)): 
    print(A_LIST[i])
"""
equals 
print(A_LIST[0])
print(A_LIST[1])
print(A_LIST[2])
print(A_LIST[3])
"""
```


### Manipulating Data in Lists
Data in a dynamic list can undergo many processes. They are often summarized by the acronym CRUD. 
C - Create
R - Read
U - Update 
D - Delete

### Creating Data in Arrays
#### Append data to the end of the list

To add data to the tail of a list, use the ```append(DATA)``` dot function. 

```python
A_LIST = []

A_LIST.append("Hello")
print(A_LIST) # output ["Hello"]

A_LIST.append("World")
print(A_LIST) # output ["Hello", "World"]
```

### Insert data to a specif index value within the list
To add data at a specific index position, use the ```insert(index, DATA)``` dot function. This function should be used sparingly because it may result in mis-addressing data. When a value is inserted into a list, it shifts subsequent index values forward by one. 

```python
A_LIST = ["This", "is", "a", "sentence."]
A_LIST.insert(2, "not")
print(A_LIST) # output ["This", "is", "not", "a", "sentence."]
```

### Reading Data in Arrays
ALL examples are found in the introduction above. 

```python
print(A_LIST[1]) # output "is"
```

### Updating Data in Arrays
As a reminder, Tuples cannot update a single value. Instead, the entire tuple must be re-declared in the variable. To update a single value in a list, the list node can be assigned a new value. 

```python
A_LIST = ["this", "is", "a", "sentence."]
A_LIST[0] = "This"
print(A_LIST) # outputs ["This", "is", "a", "sentence."]
```

### Deleting Values in Data Arrays
Deleting data from an array will change the overall length of the array and may re-assign new index values to pre-existing values within the array. 

#### Pop Data Off an Array
To remove a value off an array, the ```pop(INDEX)``` dot function removes the value at the index number. When using .pop(), the data is removed from the list, but not destroyed. If desired the removed data can be stored in a new variable. 
NOTE: If no index value is given ```pop()``` will remove the highest index value data. 

```python
A_LIST = ["This", "is", "a", "sentence."]
A_LIST.pop()
print(A_LIST) # output ["This", "is", "a"]

A_LIST.pop(1)
print(A_LIST) # output ["This", "a"]
VARIABLE = A_LIST.pop(0)
print(A_LIST) # output ["a"]
print(VARIABLE) # output "This"
```

#### Remove Data From an Array
To remove a value off an array, the ```remove(VALUE)``` dot function will remove the first instance of the value while traversing the array from head to tail. 

```python
NEW_LIST = [0, 1, 2, 3, 5, 7, 11, 13, 11, 17]
NEW_LIST.remove(11)
print(NEW_LIST) # output [0, 1, 2, 3, 5, 7, 13, 11, 17]
```

###  What data is stored in an Array?
In python, an array can store any combination of data types; however, in more structured languages, like Java, an array can only store one type of data. 

Furthermore, python cannot create *empty* arrays like other languages. 

NOTE: (IB) follows traditional array limitations of only having one data type in the array. 

## IB Content
### Queueing 
A **queue** is a list of data items, comments, etc., stored so that the information is retrievable in the order they are added to the list. It is often referred to as *LILO (Last In, Last Out)*, or *FIFO (First in, First Out)*. An example of a queue is waiting in line at a water fountain.

IB Pseudocode uses the dot methods ```enqueue``` and ```dequeue```, which cannot be used in python without first importing the queue library. 

```python
A_LIST.enqueu(DATA) # adds items to the end of the list
A_LIST.dequeue() # removes item from the start of the list.

# The above is the same as, 

A_LIST.append(DATA)
A_LIST.pop(0)
```

### Stacking
A **stack** is a list of data, items, comments, etc., stored in a way that the most recently stored data is the first to be retrieved. It is often referred to as *LIFO (Last In, First Out)* or *FILO (First In, Last Out)*. An example of a stack is a pile of books waiting to be returned to a library. The books on the top of the pile were the last ones placed on the pile but the first ones to be returned. Another example is the Undo feature found in most programs.

IB pseudocode uses the dot methods pop and push. Pop is the same as pop in python; push is the same as append in python. 

```python
A_LIST.push(DATA) # adds item to the end of the list
A_LIST.pop() # removes the item from the end of the list
```

## Multi-dimensional Arrays
Arrays can store more than primitive data, they can store additional data structures. An array that stores additional data structures is called a multi-dimensional array. These arrays normally only go two levels deep. Therefore, the most common multi-dimensional arrays are 2D arrays. 

There are three main multi-dimensional arrays and one IB structure: Dictionaries, Parallel Arrays, 2-Dimensional Arrays, and Linked Lists (IB). 

### Dictionary

Dictionaries translate information from one data to another. It takes the key and transforms it into the value found within the dictionary. Keys tend to be primitive data types, but can return advanced data types. 

```python
MY_INFO = {
    "first_name":"Laksh",
    "last_name":"Chopra",
    "email":"Lakshc18@gmail.com",
    "age": 16
}
print(MY_INFO["email"]) # output "Lakshc18@gmail.com
```

ASIDE: Dictionaries are often used to pass data between multiple programming languages within a single program. 

### Parallel Arrays 
Parallel arrays are two independent lists that share information based on their index number. Parallel arrays are not multi-dimensional array in the sense of having multiple layers of data; instead, they are considered individual lists that use the index number to link data together. 

```python
FIRST_NAME = ("Laksh", "Michael")
LAST_NAME = ("Chopra", "Zhang")
print(FIRST_NAME[1], LAST_NAME[1])# output: Michael Zhang
```

Because data must stay aligned so that the index numbers reference the correct values, tuples are often used. 

### 2-Dimensional Arrays

A 2-Dimensional array has a list in another list. Where there are other data structures, like Objects, 2D arrays are often lists/tuples within other lists/tuples. (A list of lists)

Nodes within a sublist are identified after first identifying the node in the main list using square brackets. (NOTE: A node is a position within the list/tuple). 

```python
NUMBERS = ((1, 2), (3, 4), (5, 6))
print(len(NUMBERS)) # output: 3
print(len(NUMBERS[0])) # output: 2 
print(NUMBERS[0]) # output: (1, 2)
print(NUMBERS[1][0]) # output: 3
```

NOTE: 2D arrays can represent tables

```python
NUMBERS = (
    (1, 2),
    (3, 4),
    (5, 6)
)
```

Each inner tuple represents a row and each index of the sub-lists represent a column. 

#### Updating and deleting data in 2D arrays
Updating and deleting data in 2D arrays is similar to 1D arrays. THe program can either update or delete the entire sub-array or a value within the sub-array.

```python
NUMBERS = [[1, 2], [3, 4], [5,6]]
NUMBERS [0][1] = 5 # [[1, 5], [3, 4], ...]
NUMBERS[0] = [4, 5, 6] # [[4, 5, 6], [3, 4], ...]

NUMBERS.pop(1) # output [3, 4]
NUMBERS[0].pop(2) # output 6 --> NOTE for manipulating a sub-array
```

### Using for loops with 2D arrays
For loops are a convenient tool for creating, updating, and reading data within a list. 

```python
# create an empty array of 7 spaces
A_LIST = []
for i in range(7): 
    A_LIST.append(None)
# A_LIST is [None, None, None, None, None, None, None]
```

2D Arrays require nested for loops to create
```python
A_LIST = []
# creating a 2D array that represents a 3x4 table
for i in range(3): # create the row
    A_LIST.append([])
    for j in range(4): # create the columns
        A_LIST[i].append(None)
```

## Traversing Arrays
**Traversing** an array uses a ```for loop``` to access each node in the array. There are two methods of traversing head-to-tail (ascending index number) through the array. 

```python
A_LIST = (1, 2, 3, 5, 7, 11)

# METHOD 1: Uses an intermediate variable, often i, for the index
for i in range(len(A_LIST)):
    print(A_LIST[i])

# METHOD 2: Uses an intermediate variable to store the data in the node

for node in A_LIST:
    print(node)

# NOTE: Method 2 cannot update the information within the list
# NOTE: Method 2 does not store the position of the data within the list.
```
It is possible to traverse an array from tail-to-head. 
```python
for i in range(len(A_LIST)-1, -1, -1):
    print(A_LIST[i])
"""
11
7
5
...
"""
```
Because the range of a for loop is determined at the start of the loop, any changes to the length of the array will not change the  number of iterations for the loop. Therefore, when shortening an array during a for loop, traversing tail-to-head will prevent/reduce *index out of range* errors. 

## Miscellaneous
Arrays can be added together, but they cannot be subtracted, multiplied or divided. (They are not atrices in mathematics)

```python
LIST1 = [1, 2, 3]
LIST2 = [4, 5, 6]
LIST_ADD = LIST1 + LIST2 # [1, 2, 3, 4, 5, 6]
```

Arrays can be assigned multiple variable names. 
```python
LIST =  [1, 2, 3, 5, 11]
NEW_LIST = LIST
NEW_LIST.pop()
print(LIST) # [1, 2, 3, 5]
```

To copy an array, the data has to be appended into a separate empty array by traversing the array that is being copied.

## Working with Strings
All strings are lists in disguise! While you are not able to do all actions with a string as you can with a list, it is possible to create substrings, identify individual characters, and traverse strings. 
```python
STRING = "hello world"
print(STRING[0]) # output h
print(STRING[0:2]) # output he
print(len(STRING)) # output 11 (because the space counts as a character)
```
Strings can be separated into a list using the ```.split()``` dot function. Placing a string inside the parenthesis will split the string using the characters in the .split()
```python
STRING_LIST = STRING.split() # ["hello", "world"]
STRING_LIST2 = STRING.split('l') # ['he', '', 'o wor' 'd']
```
NOTE: When splitting a string, the characters used to identify where the split occurs is called the **delimiter**. 

It is possible to combine a list of *strings* into a string.
```python
STRING_LIST = ['hello', 'world']

NEW_STRING = " ".join(STRING_LIST)
print(NEW_STRING) # 'hello world'
```

NOTE: THe delimiter is specified within quotations with a dot function of ```.join(LIST)```. It is added in between each node of the list. 

An example of using split and join for a string is the "Find and Replace" feature of many word processors. 