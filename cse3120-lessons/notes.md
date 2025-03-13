// notes.md
# CSE3120 - Object Oriented Programming 1 - Notes
## Definitions
**Object-Oriented Analysis (OOA)** is the process of looking at a problem, system or task and identifying the objects and interactions between those objects. It answers the question, *what needs to be done*.
* This term is often called a **use case** analysis.

**Object-Oriented Design (OOD)** is the process of converting the identified objects and interactions from OOA into object behaviours. It answers the question, *how things need to be done*.  

* This term is often called a *behavioural analysis*

**Object-Oriented Programming (OOP)** is the process of implementing the outcome of OOD into a functioning program. It uses class templates to create objects that have attributes and methods. 

A **Class** is a model of an object. Classes contain *attributes* and *behaviours* which are inherited when objects are *instantiated* from the class. Another definition of a class is a blueprint, template, or mold. 
* An **Attribute** is a property or characteristics an object possesses. (Like Variables). Each object can have different values for the attributes, but all objects instantiated from the class inherits the same attributes from the class template. 
* A **Behaviour** is an action that can be performed on the data within the object. Behaviours are formerly named *Methods* and are written in the same manner as a function. Therefore, methods can accept arguments into parameters and return values. 
  * Methods can accept external data and save it as an attribute within the object, process internal data within the object, and pass internal data within the object to an external source. 
  * Methods always have at least oen parameter, ```self```, which indicates that the function is referencing the current object. 
    * **Constructors** are methods that provide the object with the default set of attributes. 
    
```python
from random import randint

class Die:
    """
    A die object that can be rolled
    """
    # Constructor 
    def __init__(self, SIDES):
        # Attributes of the object
        self.MAX_NUM = SIDES
    # Method
    def getRoll(self):
        return randint(1, self.MAX_NUM)

DIE1 = Die(6)
print(DIE1.getRoll())

DIE2 = Die(20)
```

An **Object** is a unique set of data and functions instantiated from a class. An object accesses attributes and methods using *dot notation*, which identifies the object, then the attribute or method.
```python
OBJECT_NAME.ATTRIBUTE_NAME # --> VALUE
OBJECT_NAME.METHOD_NAME(ARGUMENTS) # --> METHOD
```

# WHY OOP? (This section is really important)
1. __Encapsulation__ is the process of protecting or hiding data and data processes through the implementation of an _interface_. The interface is often a collection of methods such as setter (modifier) methods and getter (accessor) methods that other objects can interact with.
   * NOTE; In most programming languages, attributes are *private* by default; however, in python, they are *public* by default.
   * A television encapsulates all hardware and software into a small box which the user interfaces with through a series of buttons on the device or on a remote control. 
   * It is important to emphasize the need for setter and getter methods and how each of the attributes within a class should only be accessed through these methods. 
   ```python
   class Main:
       def __init__(self):
           self.UNPROTECTED_ATTRIBUTE = 0
           self.__PROTECTED_ATTRIBUTE = 1 # Attributes starting with __ are protected
       def unprotectedMethod(self):
           pass
       def __protectedMethod(self):
           pass
   
   MAIN = Main()
   print(MAIN.UNPROTECTED_ATTRIBUTE) # print 0
   print(MAIN.__PROTECTED_ATTRIBUTE) # ERROR!
   ```
2. __Abstraction__ is the process of setting the level of detail and complexity to what is appropriate for the given task.
   * A driver only needs to interact with the steering, accelerator, brakes, and signals of the car to drive. But a mechanic has a much more complex understanding of the car in order to repair and maintain it. Therefore, the mechanic's abstraction of the car is more complex than the driver. 
   * To calculate a student's average, one requires the student ID, courses taken, and grades received. While a person has many more traits (i.e. height, hair color, ethnicity, postal code, etc.), they are not needed for the purpose of the calculation and are therefore omitted. 
3. __Aggregation__ is the process of grouping objects together. Objects exist independently of each other. 
   * The students in the classroom object are an aggregation of student objects. 
4. __Composition__ is the process of creating a complex object from a collection of several smaller objects.
   * A bicycle is composed of two wheels, chain, handlebars, frame, pedals, seat, gears, breaks. Any one of the objects when broken will affect the performance of the bicycle. If enough objects within the bicycle are missing/damaged, the bicycle will not be able to function. 
   
## Unified Modeling Language
A standardized modeling language that unifies notational systems and approaches for data management and software design. UML focuses on managing _data_ and grouping that data together. It is composed of three main diagram types: structure, behaviour, and interactions. 

NOTE: While software developers require knowledge of all three types, this program will only focus on structure UML Tables. 

A Class diagram is a common structure diagram. It contains the name of the class, the attributes, and methods within the class. 

| Bank Account ||
| --- | --- |
| _Attribute_ | _datatype_ |
| accountNo- | int |
| balance | float |
| _Methods(param)_ | _return-value_ |
| deposit(float) | None |
| withdraw(float) | None |
| getBalance() | float |

Each class within a program can be designed using a UML table. During the design process, developers can determine which classes will have which attributes and behaviours and map out how the objects will interact with each other (in a flowchart). A given program should have multiple types of objects. 








