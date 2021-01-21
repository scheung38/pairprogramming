# Suppose you have an arbitrary natural number (the target) and a set of one or more additional natural numbers (the factors). Write a program that computes the sum of all numbers from 1 up to the target number that are also multiples of one of the factors. 
# For instance, if the target is 20, and the factors are 3 and 5, that gives us the list of 
# multiples 3, 5, 6, 9, 10, 12, 15, 18. The sum of these multiples is 78.
# If no factors are given, use 3 and 5 as the default factors.

# PEDAC
# Create an empty array called multiples that will contain the multiples
# Check whether the list of factors is empty, if there are no factors, set the list to [3,5]
# For every factor in the factors list:
#  Set the current_multiple to factor to keep track of the multiples of factors
#  While current_multiple < target
#    Append the current_multiple to multiples
#    Add factor to current_multiple
# Filter duplicate numbers from multiples
# Compute and return the sum of the numbers in multiples


# How to generate a list of multiples in Python from two numbers?
from icecream import ic

def my_sum(f=3,g=5, target=20):
    list1 = []
    list2 = []
    
    # for i in range(1,21):  
        # ic(i) 
    
    count = target
    [list1.append(i*f) for i in range(1,count+1) if i*f < count ]
    [list2.append(i*g) for i in range(1,count+1) if i*g < count ]

    # ic(list1)   
    # ic(list2)   

    ic(list(set().union(list1,list2)))
    ic(sum(list(set().union(list1,list2))))

    return sum(list(set().union(list1,list2)))


if __name__ == "__main__":     
    ic(my_sum())
    ic(my_sum())

