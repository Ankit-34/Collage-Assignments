# How to use dir() to see all the available magic methods
class employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

e1 = employee("rohan", "shah")
print(dir(employee))


# Simple use of add magic method
num = 10
num = num+10
print(num)  # Output: 20
num = 10
print(num.__add__(10))

# Following code will give same output as above
num = 10
print(num.__add__(10))


# __add__()
class One:
    def __init__(self, a):
        self.a = a
        
    def __add__(self, object2):
        return self.a + object2.a

class Two:
    def __init__(self, a):
        self.a = a

    def __add__(self, object2):
        return self.a + object2.a

a_instance = One(10)
b_instance = Two(20)
print(a_instance + b_instance)
# Output: 30


# __new__()
class A:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print ("__init__ magic method is called")
        self.name='abcd'

obj=A()
#Output:
# __new__ magic method is called
# __init__ magic method is called


# __getitem__()
class A:
    def __init__(self, item):
        self.item = item

    def __getitem__(self, index):
        return self.item[index]

a = A([1, 2, 3])
print(f"First item: {a[0]}")
print(f"Second item: {a[1]}")
print(f"Third item: {a[2]}")
# Output:
# First item: 1
# Second item: 2
# Third item: 3


# __setitem__()
class SetItemExample:
    def __init__(self, item):
        self.item = item
        
    def __setitem__(self, index, item1):
        self.item[index] = item1
    
setitem_instance = SetItemExample([1, 2, 3])
print(f"Items before setting: {setitem_instance.item}")
setitem_instance[1] = 5
print(f"Items after setting: {setitem_instance.item}")
# Output
# Items before setting: [1, 2, 3]
# Items after setting: [1, 5, 3]


# __repr__()
class ReprExample:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __repr__(self):
        return f"ReprExample(a={self.a}, b={self.b}, c={self.c})"

repr_instance = ReprExample(1, 2, 3)
print(repr_instance)
# Output
# ReprExample(a=1, b=2, c=3)


# __len__()
class LenExample:
    def __init__(self, item):
        self.item = item

    def __len__(self):
        return len(self.item)

len_instance = LenExample([1, 2, 3])
print(len(len_instance))
# Output: 3


# __call__()
class CallExample:
    def __init__(self, val):
        self.val = val
    
    def __call__(self, b):
        return self.val * b

call_example = CallExample(5)
print(call_example(6))
# Output: 30


# Magic methods for comparison
class Comparison:
    def __init__(self, a):
        self.a = a
    def __lt__(self, object2):
        return self.a < object2.a
    
    def __gt__(self, object2):
        return self.a > object2.a
    
    def __le__(self, object2):
        return self.a <= object2.a
    
    def __ge__(self, object2):
        return self.a >= object2.a
    
    def __eq__(self, object2):
        return self.a == object2.a
    
    def __ne__(self, object2):  
        return self.a!= object2.a

a = Comparison(1)
b = Comparison(2)
print( a < b, a > b, a <= b, a >= b, a == b, a!= b )
# Output
# True False True False False True



