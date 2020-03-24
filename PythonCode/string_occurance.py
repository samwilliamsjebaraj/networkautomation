pattern="bob"
count=i=0
s = 'bobobbo'
print (len(s))
print (s[len(s)-1])
while i<(len(s)):
    if s[i]=="b" and i+2<=(len(s)-1):
        print (i,i+2,len(s))
        if s[i+1]=="o":
            if s[i+2]=="b":
                count+=1
    i+=1

print ("Number of times bob occurs is: {}".format(count))


count = 0
maxcount = 0
result = 0

for char in range(len(s) - 1):
    if (s[char] <= s[char + 1]):
        count += 1
        if count > maxcount:
            maxcount = count
            result = char + 1
    else:
        count = 0
sp = result - maxcount
print('Longest substring in alphabetical order is:', s[sp:result + 1])