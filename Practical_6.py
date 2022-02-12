# NAME : ANKIT GANATRA
# ID : 20CE030

# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 

# Sample Input 
# 4 
# bcdef 
# abcdefg 
# bcde 
# bcdef 

# Sample Output 
# 3 
# 2 1 1 


a = int(input())

dict = {}
for i in range(a):  
    str = input()
    if str in dict:
        dict[str] +=1
    else:
        dict[str] = 1
print(len(dict))
for i in dict.values():
    print(i ,end=' ')


# GITHUB REPO LINK : https://github.com/Ankit-34/Collage-Assignments