"""
File:function_operations.py
Mapping, Filtering & Reducing
map(),filter(),reduce()
"""
def check_even(x):
    return x%2==0
def check_odd(x):
    return x%2!=0
def add_numbers(x1,x2):
    """
    add's the numbers and returns the value
    """
    return x1+x2
def product(x1,x2):
    '''
    returns the product of the args(x1,x2)
    '''
    return x1*x2

#checking the map() function
my_number_list=range(1,101)
print map(check_even,my_number_list)
print map(check_odd,my_number_list)

#checking the filter() function
print filter(check_even,my_number_list)
print filter(check_odd,my_number_list)

#check reduce() function
print reduce(add_numbers,my_number_list)
print reduce(product,my_number_list)
