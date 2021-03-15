# Script by Awais Bhattee written on 13/03/21 for Foo Bar Challenge 1

# A function that givcs us the factors of an integer
list_of_factors = []
def factoriser(x):

   for i in range(1, x + 1):
       if x % i == 0:
           list_of_factors.append(i)

   print("The factors of",x,"are:")
   print(list_of_factors)

# The function that takes the string of sequenced M&Ms on the cake as input and returns the max number of identical slices possible
def solution(s):
    cake = s

    print("")
    print("The cake is..."+cake)
    mnm_count = len(cake)
    print("There are "+str(mnm_count)+" M&Ms on the cake")
    factoriser(mnm_count)

    #loops and checks with the smallest factors first to provide maximum slices
    for factor in list_of_factors:
        print("")
        print("Checking factor..."+str(factor))
        itcuts = True
        all_slices = []
        upto = 0
        slice_count = int(mnm_count / factor)

        #Preparing the slices
        for i in range(1,(slice_count+1)):
            slice=[]
            for j in range(1,(factor+1)):
                print("We are up to M&M..."+cake[upto]+"...on the cake")
                slice.append(cake[upto])
                upto += 1
            print("Plating slice..."+str(slice))
            all_slices.append(slice)
        print("Number of slices made are..."+str(len(all_slices)))

        #Comparing the slices
        for i in range(0,(len(all_slices)-1)):
            if itcuts == True:
                if all_slices[i] != all_slices[i+1]:
                    itcuts = False

        #reporting if factor is valid, and if the cake cuts returning the result of how many cuts
        if itcuts == True:
            print("Yes, we can cut the cake into " + str(slice_count) + " equal slices" )
            return slice_count
        else:
            print("No, we cannot cut the cake into " + str(slice_count) + " equal slices")

#test solution function
solution("abcabcabc")
