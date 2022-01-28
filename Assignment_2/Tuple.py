# Ankit Ganatra - 20CE030

# a. Write a Python program to create a tuple with different data types.
tuple1=(1, 4, 2.3, 'A', "ABC")
print(tuple1)

print("\n--------------------------\n")

# b.Write a Python program to create a tuple with numbers and print one item.
tuple2=(15, 30, 60, 120, 240, 480)
num=tuple2[2]
print(num)
print(tuple2[-2])

print("\n--------------------------\n")

# c.Write a Python program to add an item in a tuple.
# Tuples are immutable 
tuple3=("abc", "pqr")
tuple3=tuple3+("xyz",)  #append an element at the end in tuple
print(tuple3) 

print("\n--------------------------\n")

# d.Write a Python program to convert a tuple to a string.
tuple4=('P', 'Y', 'T', 'H', 'O', 'N')
string=''.join(tuple4)
print("Tuple converted in string :",string)

print("\n--------------------------\n")

# e. Write a Python program to find the length of a tuple.
tuple5=("How", "Are", "You?")
print("Length of tuple:", len(tuple5))
