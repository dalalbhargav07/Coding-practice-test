# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 
@author: dalalbhargav07
"""

class Solution2(object):
    def manipulateString(self, inputString):
        try:
            prev = inputString[0]
            count = 0
            outputStringList = []
            for i in range(len(inputString)):
                if prev == inputString[i]:
                    count +=1
                else:
                    outputStringList.append(prev)
                    outputStringList.append(count)
                    prev=inputString[i]
                    count = 1
            outputStringList.append(prev)
            outputStringList.append(count)
        except:
            if inputString == '':
                return ('The input string was null.... Terminting the program')
            return ('Some error/exception occured in manipulateString method of Class Solution2')
        return (''.join(map(str, outputStringList)))

inputString = input("Please enter a string: ")
outputString = Solution2().manipulateString(inputString)
print(outputString)