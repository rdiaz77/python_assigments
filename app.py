# Write a Python function called max_num()to find the maximum of three numbers.

from multiprocessing.pool import ThreadPool


numbers = [1,2,3,45,2]

def max_num(num):
    print(max(num))
    
max_num(numbers)
    

# Write a Python function called mult_list() to multiply all the numbers in a list.

def multi_list(lst):
    value = 1
    for i in lst:
       value *= i
       
    print(value)
multi_list(numbers)

# Write a Python function called rev_string() to reverse a string.

str =  "Welcome to the jungle"

def rev_string(str):
    print(str[::-1])
    

rev_string(str)

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

numbers = [2,5,6,0,10]

def num_within(first,num,last):
    if num in range(first,last):
        print(f"{num} is between the range {first} and {last}")
    else:
        print(f"{num} is not in the range {first} and {last}")
 
num_within(13, 3, 20)       



# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
    trow = [1]
    y = [0]
    for n in range(max(n,0)):
        print(trow)
        trow = [l+r for l,r in zip(trow+y , y+trow)]
    return n >=1

pascal(0)

pascal(5)
                                                    