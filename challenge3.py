# Script by Awais Bhattee written on 13/03/21 for Foo Bar Challenge 3

def solution(x, y):
    distance = int(x)
    height = int(y)
    ID = 0

    next_to_wall = int(((height*(height-1))/2) + 1)
    print("At height..."+str(height)+"...ID next to wall is..."+str(next_to_wall))

    ID = next_to_wall
    print("ID is..."+str(ID))
    add_for_next_id = height + 1


    for i in range (1, distance):
        ID += add_for_next_id
        add_for_next_id +=1
        print("ID is..."+str(ID))

    print("The ID for the worker at distance..."+str(distance)+ "...is..."+str(ID))
    return ID

#test solution function
solution(5,10)
