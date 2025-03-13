// notes.md
# CSE3110 - Iterative Algorithms
Iterative algorithms are algorithms that use loops to process large amounts of data. This includes while loops and for loops. In contrast, Recursive algorithms- are functions that call the same function over and over again to divide a large set of data into smaller and smaller sets. Once the function has the smallest set possible, it will process the data of the set. Iterative algorithms tend to be easier to program, but the overall efficiency of an algorithm will increase when recursive aspects are applied. 

While sort algorithms can cort a wide variety of entities (i.e. numbers, strings, etc.), these units will focus on sorting integers. 

## Linear Search
Linear search is the easiest to program, but least efficient method of search. It processes the data line-by-line, similar to brute force decryption algorithms.

```python
FOUND = False
for i in range(len(A_LIST)):
    if A_LIST[i] == VALUE: 
    FOUND = True
    break
```

Linear search processing time is dependent on the length of the arrays. Arrays that are 10,000 indices or higher can take a noticeable amount of time to process.

### Measuring processing time
We use ```time.perf_counter()``` as a measuring tool for the efficiency of an algorithm. It will record the approximate process length at the time it is run.

For accurate results, we use the average of thirty trials and then use ```stastics.mean()```.

## Binary Search
Binary search follows the _divide and conquer_ technique of finding a value. It takes an *ordered* set of data and tests the midpoint value. Then it cuts the list in half and reruns the process. 

#### Steps for Binary Search
1. Determine the Midpoint index of the list.
2. Test if the Midpoint value is the same as the searched value.
   1. If the Midpoint value and searched value match, end.
   2. If the midpoint value is greater than the searched value, redefine the highest index value in the range to be one below the midpoint index. 
   3. If the midpoint value is less than the searched value, redefine the lowest index value in the range to be one above the midpoint index.
3. Repeat until the value is found. 

* Advantages of Binary Search
  * It is significantly faster than linear search
* Disadvantages of Binary Search
  * List must already be ordered
  * List must contain the same data type 

## Sorting Data
Just like searching algorithms, sorting algorithms have a varying level of efficiency. There are several types of sort algorithms including bubble, selection, insertion, and merge. (Python uses Timsort, which is a hybrid of merge and insertion sort designed by Tim Peters in 2002).

Sorting algorithms exist to optimize memory usage. Historic computers did not have enough RAM to hold multiple lists in memory. While this limitation does not exist in modern computers, for data storage and management on a global scale, resources are still limited. The efficiency of processing algorithms is still noticeable today. 

### Bubble Sort
Bubble sort compares two adjacent values on the list and arranges them from lowest to highest. Then it moves to the next index pair and repeats until it reaches the end of the unsorted list.

Advantages are that it is easy to program and takes less memory, but the disadvantages are that its processing time is directly proportional to the square of the length of the data set. However, the set is often fully sorted before the last iteration.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3 | 5 | 11 | 17 | 7 | 13 | __19__ |
| 1 | 3 | 5 | 11 | 7 | 13 | __17__ | 19 |
| 1 | 3 | 5 | 7 | 11 | **13** | 17 | 19 |
| 1 | 3 | 5 | 7 | **11** | 13 | 17 | 19 |
| 1 | 3 | 5 | **7** | 11 | 13 | 17 | 19 |
| 1 | 3 | **5** | 7 | 11 | 13 | 17 | 19 |
| 1 | **3** | 5 | 7 | 11 | 13 | 17 | 19 |


### Selection Sort
Selection Sort compares the current index value with the rest of the set. It will store the index of the lowest value and switch its position with the lowest index in the unsorted section of the list.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | **3** | *5* | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | ***5*** | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | **7** | 11 | 17 | *19* | 13 |
| 1 | 3 | 5 | 7 | ***11*** | 17 | 19 | 13 |
| 1 | 3 | 5 | 7 | 11 | **13** | 19 | *17* |
| 1 | 3 | 5 | 7 | 11 | 13 | **17** | *19* |

### Insertion Sort
Insertion Sort splits the list into two sections sorted and unsorted. As it progresses through the list, it takes the value at the lowest index of the unsorted half of the list and places it in the correct relative location in the sorted section of the list.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |__*5*__ | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | _3_ | __5__ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __*19*__ | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | _11_ | __19__ | 17 | 7 | 13 |
| 1 | 3 | 5 | _7_ | 11 | 17 | __19__ | 13 |
| 1 | 3 | 5 | 7 | 11 | _13_ | 17 | __19__ | 

# CSE3310 - Recursive Algorithm Notes

A __recursive algorithm__ calls itself with smaller or simpler datasets. Recursive algorithms have a *base case*, which is the simplest input value. Then there are subprocesses that simplify more complex datasets and return the simplified back into a new instance of the same algorithm. 

All iterative algorithms can be written recursively and vice versa; certain functions are easier to write in one form over another.

## Example 3: Testing for the correct input data
```python
def checkInt(VALUE) # recursive
    if VALUE.isnumeric():
        return int(VALUE)
    else: 
        print("You did not enter a number!")
        NEW_VALUE = input("NUMBER: ") # update to the data going into the function
        return checkInt(NEW_VALUE) # calling the function with the new data

def checkInt(VALUE): # iterative
    while True:
        if VALUE.isnumeric():
            return int(VALUE)
        else: 
            print("You did not enter a number!")
            VALUE = input("Number: ")
```

## Iteration vs. Recursion
In general, iterative algorithms require more lines of code and more variables to create. It relies on while and for loops to complete the process. Iterative algorithms work best with consistent changes (i.e. counting, traversing, etc.). Whereas, recursive algorithms do not use as many variables and rely on return values that are re-entered into the function to continue processing the data. Recursion can use more physical memory than iterative algorithms because each instance of the recursive function must stay in memory until the base case is found. Because recursive algorithms can manipulate the data before recurring back into the function, it can change data in ways iteration cannot. Finally, iterative functions tend to be faster than exclusively recursive ones.

Hybrid iterative and recursive algorithms are often faster than exclusively iterative or exclusively recursive algorithms. 

## Example 2: Factorials
### Calculate 7!

```
7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1 = 5040
// BUT
6! = 6 * 5 * 4 * 3 * 2 * 1 * 1 = 
// We can rewrite 7!
7! = 7 * 6!
// EXTEND this reasoning
7! = 7 * (6 * (5 * (4 * (3 * (2 * (1 * (1)))))))
// GENERALIZE the statement
f(x) = x * f(x -1), x > 0
    and 
f(x) = 1, x = 

```

## Sorting 
Recursive sorting uses both recursive and iterative processes. In general, these hybrid sort algorithms are exponentially faster with longer lists. (They are measured on a logarithmic scale). 

### Merge Sort
Merge sort follows a divide and conquer method of sorting, where the array is split into its base length and then rebuilt by combining progressively larger sorted lists together. The recursive portion is the splitting of the list and the iterative process is the actual merging of two smaller sorted lists.

Oftentimes, this function is separated into splitting and merging functions. 

### Quick Sort
Quick sort (or quicksort) is another divide and conquer method of sorting. Quicksort utilizes an arbitrary value as its pivot, which is then used to place the pivot value in the correct index position in the array. It does this by placing all smaller values to the left of the pivot and all larger values to the right of the pivot. Then it places the pivot value where the smaller and larger portions intersect and moves to the next value. It then recurs through the algorithm until the inputted list is one value long. 

NOTE: Quicksort's efficiency is from separating the list into two sections that will never compare values with each other again. 

### Heap Sort
Heap Sort uses a binary tree organization of an array to sort higher values to the top of the tree. The process of moving larger values higher in the binary tree is called **heapifying** (or to heapify). 

To build the binary tree, each index (starting at 0) will have a left child and a right child (hence binary tree). The index values can be calculated from the following:
```
left_child = 2 * parentIndex + 1
right_child = 2 * parentIndex + 2

# sample tree
LIST = [5, 17, 13, 11, 1, 7, 3]

       5[0]
      /    \
   17[1]    13[2]
  /    \      / \
11[3]  1[4] 7[5] 2[6]
```

#### Heapify
To heapify the binary tree, the value of the parent index must be higher than the two children. Therefore, the process starts at the bottom of the tree and works its way to the top. If the parent is smaller than one of the children values, it swaps the highest child with the parent. As heapifying moves through the tree, the higher values will progressively get to the top (lower index values) of the tree.

When the heapifying process reaches the top, the top value swaps with the highest index number in the unsorted tree. Then the heapifying process begins again with the highest number removed from the tree. 

