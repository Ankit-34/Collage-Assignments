# Ankit Ganatra - 20CE030

# a.Write a Python script to check whether a given key already exists in a dictionary.
dic = {1: "abc", 2: "xyz", 3: "pqr"}
if 5 in dic:
    print("Yes. 2 is exixts in the dictionary as key.")
else:
    print("This key does not exists in dictionary.")
    
print("\n--------------------------\n");
    
# b.Write a Python script to merge two Python dictionaries.
dic1={1:"A", 3:"B", 5:"C", 7:"D"}
dic2={2:"P", 4:"q", 6:"R"}
dic3={1:"X", 3:"Y", 5:"Z"}
dic1.update(dic2)
print(dic1)
dic1.update(dic3)
print(dic1)

print("\n--------------------------\n")
    
# c. Write a Python program to sum all the items in a dictionary.
dic4={2:100, 4:200, 6:300}
print("Sum of values in dictionary is:",sum(dic4.values()))

print("\n--------------------------\n")

# d. Write a Python script to add a key to a dictionary.

dic5={2:"a", 4:"c", 6:"e"}
dic5.update({8:"g"})
print("Updated dictionary is : ",dic5)


print("\n--------------------------\n")
# e. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)