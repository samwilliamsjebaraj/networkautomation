"""
File:lambda_functions.py
Shows the map(),filter(),reduce() function operations using lambda
"""
my_list=range(1,101)
#using map() on lambda
print map((lambda x:x%2==0),my_list)
print map((lambda x:x%2!=0),my_list)

#using filter() on lambda
print filter((lambda x:x%2==0),my_list)
print filter((lambda x:x%2!=0),my_list)

#using reduce() on lambda
print "Total Values:{}".format(reduce((lambda x,y :x+y),my_list))
print "Average:{}".format(reduce((lambda x,y :x+y),my_list)/len(my_list))
print len(my_list)
