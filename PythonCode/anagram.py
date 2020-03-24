def anagram(s1,s2):
    '''
     This function compares 2 strings and returns true 
     if the string is anagram of the other else it returns 
     false (True/False)
    '''
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    # Edge Case
    if len(s1)!=len(s2):
        return False
    
    char_count={}
    for x in s1:
        if x in char_count:
            char_count[x]+=1
        else:
            char_count[x]=1
    for x in s2:
        if x in char_count:
            char_count[x]-=1
        else:
            char_count[x]=1
    for n in char_count:
        if char_count[n]!=0:
            return False
    return True

if __name__=="__main__":
    str1="Madam Curie"
    str2="Radium came"
    x=anagram(str1,str2)
    if x:
        print "{} is anagram of {}".format(str1,str2)
    else:
        print "{} is not anagram of {}".format(str1,str2)
