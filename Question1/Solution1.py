# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3
@author: dalalbhargav07
"""

class Solution1(object):
    def replaceWords(self, leet, sentence):
        try:
            if (sentence == ''):
                return ('The input string was null.. Terminating the program')
            for x, y in leet.items():
                sentence = sentence.replace(x,y)
        except:
            return ('Some error/exception occured in manipulateString method of Class Solution1')
        return (sentence)

leet = {
      'a': '4', 'A' : '4',
      'e' : '3', 'E' :'3',
      'i' : '1', 'I' : '1',
      'o' : '0', 'O' : '0',
      't' : '7', 'T' : '7',
      's' : '5', 'S' : '5',
      'b' : '5', 'D' : '5'
}

sentence = input("Please enter a sentence: ")
leetMessage = Solution1().replaceWords(leet,sentence)
print(leetMessage)