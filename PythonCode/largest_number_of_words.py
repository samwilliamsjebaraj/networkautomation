import re
def solution(S):
    word_count={}
    # write your code in Python 3.6
    S=re.split('[?!.]',S)
    print ("SENETENCE:{}".format(S))
    for sentence in S:
        print (sentence.split(' '))
        for words in sentence.split(' '):
            print (words)
            if words in word_count.keys():
                word_count[words]+=1
            else:
                word_count[words]=1
    print (word_count)
    return (sum(word_count.values()))


if __name__=="__main__":
    S="We test coders. Give us a try?"
    print solution(S)
