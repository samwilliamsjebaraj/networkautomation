def odd_even(x:int) -> int:
    if x%2==0:
        return "EVEN"
    else:
        return "ODD"

print (odd_even(10))
print (odd_even(10.5))