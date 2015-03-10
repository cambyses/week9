import random

def sort(items):
    
    
    if(len(items) <= 1):
        return(items)


    while(True):
        

        i = 0
        number_of_swaps = 0


        while(i < len(items)-1):

    
            if(items[i] > items[i+1]):
            
                number_of_swaps += 1

            
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

            
            i += 1

    
        if(number_of_swaps == 0):

            break
        

    return(items)



numbers = list(range(10))
random.shuffle(numbers)

assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")


print("This algorithm is classified as: O(n*n)")
