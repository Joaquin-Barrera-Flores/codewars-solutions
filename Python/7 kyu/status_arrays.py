# DESCRIPTION 
#   The status of each element of an array of integers can be determined by its position 
#   in the array and the value of the other elements in the array. 
#   The status of an element E in an array of size N is determined by adding the position 
#   P, 0 <= P < N, of the element in the array to the number of array elements in the 
#   array that are less than E.
#   For example, consider the array containing the integers: 6 9 3 8 2 3 1. The status of 
#   the element 8 is 8 because its position is 3 and there are 5 elements in the array that 
#   are less than 8. You will return the elements of the original array from low to high 
#   status order. In the event there is a tie for status of two or more elements, you will 
#   output them in order of appearance in the array.

#       EXAMPLE:
#       status([6, 9, 3, 8, 2, 3, 1]) = [6, 3, 2, 1, 9, 3, 8]

x = [6, 9, 3, 8, 2, 3, 1]

def status(nums):

    to_order = []
    nums_sorted = []
    
    for P, E in enumerate(nums):
        C = sum(1 for x in nums if x < E)
        S = P + C
        to_order.append((E,S,P))
        
    to_order = sorted(to_order, key=lambda x: (x[1], x[2]))
    
    for x in to_order:
        nums_sorted.append(x[0])
        
    return nums_sorted

print(status(x))