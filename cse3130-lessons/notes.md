// notes.md
# Object Oriented Programming 2 Notes
## Inheritance
Inheritance is the process where one class inherits attributes and methods from another class. While some languages, such as Java, prohibit it, classes can inherit from multiple parent classes. However, this process of multiple inheritances is often avoided because of potential conflicts from duplicate attributes and method names. Inheritance improves the efficiency of creating objects as subclasses can use attributes and methods of the parent class. 

* Inheritance describes and _Is-A_ relationship.
  * The _deck_ __is a__ _group of cards_ and the _hand_ __is a__ _group of cards_, but the _deck_ is not a _hand_. Therefore, both the deck and the hand can inherit from a class called _group of cards_. 
  * Cross-curricular link: In biology, phylogeny is where evolutionary traits can be traced back to evolutionary ancestors. Inheritance in programming follows a similar pattern. 
* __Abstract Classes_ (as opposed to concrete classes) are classes that are never instantiated by themselves. These classes are written solely for the purpose of inheritance. Oftentimes, these classes have __abstract methods__ which cannot fully function within the Abstract Class; instead, they rely on data in their respective sub-classes. 
  * In our pygame examples, the abstract sprite class dos not have a working surface object until a subclass creates it. 
* Inheritance, like objects, often reveals itself during the design process when multiple classes have similar attributes or methods. 


```python
class Mammal: #abstract parent class

    def __init__(self, genus, species, common_name):
        self.genus = genus
        self.species = species
        self.name = common_name
        self.cry = ""
        
    def setCry(self, sound):
        """
        updates the sound the mammal makes
        """ 
        self.crySound = sound
        
    def Cry(self):
        return self.crySound
    
    
class Dog(Mammal): #concrete child class

    def __init__(self, cry_cound):
        Mammal.__init__(self, "Canis", "lupis", "dog")
        self.setCry(cry_cound)
        
class Cat(Mammal): #concrete child class
    
        def __init__(self, cry_sound):
            Mammal.__init__(self, "Felis", "catis", "cat")
            self.setCry(cry_sound)

CORGIE = Dog("Bark!")
SIAMESE = Cat("Meow!")

CORGIE.Cry()
SIAMESE.Cry()
```

## Protecting Attributes and Methods with Inheritance
Previously, objects with attributes and methods that begin with two underscores, "\_\_", are private and attributes and methods that begin without an underscore are public. For private attributes and methods, subclasses will not be able to make changes to those attributes or access those methods. To give partial access, called partially-protected attributes/methods, use a __single underscore__ "\_". 

```python

class ParentClass:

    def __init__(self):
        self.__private_attributes = 1
        self._partially_protected_attributes = 2
        self.public_attribute = 3

    def __private_method(self):
        return 4
    
    def _partially_protected_method(self):
        return 5
    
    def public_method(self):
        return 6
    
    def getPartiallyProtectedAttribute(self):
        return self._partially_protected_attributes
    
    def getPrivateAttributes(self):
        return self.__private_attributes

class SubClass(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)
        self.__private_attributes = 7 #different attribute than the parent
        self._partially_protected_attributes = 8
        self.public_attribute = 9

MY_CLASS = SubClass()
print(MY_CLASS.__private_attributes) # ERROR!
print(MY_CLASS._partially_protected_attributes) # ERROR!
print(MY_CLASS.public_attribute) # 9
print(MY_CLASS.__pivate_method()) # ERROR!
print(MY_CLASS._partially_protected_method()) # ERROR!
print(MY_CLASS.public_method()) # 6
print(MY_CLASS.getPartiallyProtectedAttribute()) # 8
print(MY_CLASS.getPrivateAttributes()) # 1
```

# Polymorphism
Polymorphism is the ability to have the same methods in different classes perform different tasks/outcomes.
```python
# Use the classes from above
CORGIE.Cry("Bark!")
SIAMESE.Cry("Meow!")
```
Note that both objects have the same method, but have different outputs.

