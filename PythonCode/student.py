"""
File:student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """ Represents a Student """

    def __init__(self,name,number):
        """ Constructor which creates a Student with the given name
        and number of scores and sets all the scores to 0."""
        self._name=name
        self._scores=[]
        for count in xrange(number):
            self._scores.append(0)

    def getName(self):
        """ Returns the Student's name """
        return self._name
    
    def setScore(self,i,score):
        """ Resets the ith score, counting from 1."""
        self._scores[i-1]=score
    
    def getScore(self,i):
        """ Returns the ith score, counting from i."""
        print len(self._scores)
        if i<len(self._scores):
            return self._scores[i-1]
        else:
            return 0

    def getAverage(self):
        """ Returns the average score."""
        sum=reduce(lambda x,y: x+y, self._scores)
    
    def getHighScore(self):
        """ Returns the highest score."""
        return max(self._scores)
    
    def __str__(self):
        """ Returns the string representation of the students """
        return "Name: {} \nScores: {}".format(self._name,(" ".join(map(str, self._scores))))