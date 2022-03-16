# NAME : ANKIT GANATRA
# ID : 20CE030
# Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


s = Stack()

print('Press 1 for push')
print('Press 2 for pop')
print('Press 3 for exit')
while True:
    choice = input('What would you like to do?\n')
    if choice == '1':
        value = input('Enter data : ')
        s.push(int(value))
    elif choice == '2':
        if s.is_empty():
            print('Stack is empty.')
            break
        else:
            print('Popped value is : ', s.pop())
    else:
        break
    
    
# GITHUB REPO LINK : https://github.com/Ankit-34/Collage-Assignments