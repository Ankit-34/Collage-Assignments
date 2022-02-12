#  NAME : ANKIT GANATRA
# ID : 20CE030

# AIM: Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome. 

# Sample Input 
# 6 
# gaga 
# abcde 
# rotor 
# xyzxy 
# abbaab 
# ababc  

# Sample Output 
#YES 
# NO 
# YES 
# YES 
# NO 
# NO 


from tokenize import String


def Lapindrome_func(str):

    strlen = len(str)
    if(strlen%2==0):
        a = str[:(strlen//2)]
        b = str[(strlen//2):]
    else: 
        a = str[:(strlen//2)]
        b = str[(strlen//2)+1:]
    list_a = list(a)

    list_a.sort()
    list_b = list(b)

    list_b.sort()
    if (list_a==list_b):
        print("YES")
    else:
        print("NO")

num = int(input())

for i in range(num):
    String =  input()
    Lapindrome_func(String)
    
    
# GITHUB REPO LINK : https://github.com/Ankit-34/Collage-Assignments