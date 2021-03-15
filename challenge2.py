# Script by Awais Bhattee written on 13/03/21 for Foo Bar Challenge 2

# a function that counts the number of salutes undertaken in a hall
def solution(s):
    print("Looking at hallway..."+s)
    hall_length = len(s)
    print("The hall is..."+str(hall_length)+"...spaces long.")

    moving_right = 0
    interactions = 0

    for i in range (0,hall_length):
        if s[i] == ">":
            print("Space "+str(i)+" has an employee travelling Right >")
            moving_right += 1
        elif s[i] == "<":
            print("Space "+str(i)+" has an employee travelling < Left ")
            interactions += moving_right
        else:
            print("Space "+str(i)+" has nothing noteworthy")

    salutes = interactions * 2

    print("The number of salutes that took place are..."+str(salutes))
    return salutes

#test solution function
solution("<<>>-----<")
