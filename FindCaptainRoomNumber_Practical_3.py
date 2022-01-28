k = int(input())    #size of each group

room_number = map(int, input().split())     #elements of the list
room_number = sorted(room_number)

for i in range(len(room_number)):
    if(i != len(room_number)-1):
        if(room_number[i]!=room_number[i-1] and room_number[i]!=room_number[i+1]):
            print(room_number[i])
            break;
    else:
        print(room_number[i])