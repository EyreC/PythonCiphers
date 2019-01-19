
#function takes a string and returns an encoded string
#encoding function squares the position number of each letter,
#subtracts the largest multiple of 26 such that the number is non-negative
#and maps that number to the position number in the English alphabet
#returns that letter
#punctuation will be given numbers in excess of 26

import string
import numpy as np

def uniqueChecker(listOfNumbers):
    newList = []
    for num in listOfNumbers:
        num2 = num^2
        newList.append(num2)
    if len(newList) == len(set(newList)):
        return True
    else:
        return False

def normalisedSquare(listOfNumbers):
    squareList = [i**2 for i in listOfNumbers]
    print(squareList)
    returnList = []
    for i in squareList:
        while i>26:
            i-=26
        returnList.append(i)
    return returnList

def letterToNumber(inputString):
    #Create dictionary mapping upper and lowercase letters to numbers
    letterToNumDict = {l:n for n,l in enumerate(string.ascii_lowercase)}

    #Generate number encoded list
    outputList = []
    for i in inputString:
        try:
            outputList.append(letterToNumDict[i])
        except KeyError:
            outputList.append(i)
    return outputList


def numberToLetter(numInputList):

    #Create a dictionary mapping numbers to lower and uppercase letters
    numToLetterDict = {n:l for n,l in enumerate(string.ascii_lowercase)}

    #Generate case sensitive list from numbers
    outputList = []
    for i in numInputList:
        try:
            outputList.append(numToLetterDict[i])
        except KeyError:
            outputList.append(i)
    outputString = "".join(outputList)
    return outputString

def caseAdjuster(inputString, caseList):
    returnList = []
    for i,v in enumerate(caseList):
        if v == (False,):
            returnList.append(inputString[i].upper())
        else:
            returnList.append(inputString[i])

    return "".join(returnList)

def encoderSinglelOffset(inputString):
    numberList = letterToNumber(inputString)
    offsetNumberList = []
    for i in numberList:
        try:
            if i < 51:
                offsetNumberList.append(i+1)
            elif i == 51:
                offsetNumberList.append(0)
        except TypeError:
            offsetNumberList.append(i)

    return numberToLetter(offsetNumberList)

def decoderSingleOffset(inputString):
    numberList = letterToNumber(inputString)
    offsetNumberList = []
    for i in numberList:
        try:
            if i > 0:
                offsetNumberList.append(i-1)
            elif i == 0:
                offsetNumberList.append(51)
        except TypeError:
            offsetNumberList.append(i)
    return "".join(numberToLetter(offsetNumberList))

def encoderOffset(inputString, offsetNumber):
        numberList = letterToNumber(inputString.lower())
        offsetNumberList = []

        #Gen list the lenght of the string, with '1' if uppercase, '0'
        #if lowercase

        caseList = [(i.lower() == i,) for i in inputString]

        for i in numberList:
            try:
                if i+offsetNumber<26:
                    offsetNumberList.append(i + offsetNumber)
                else:
                    offsetNumberList.append(i + offsetNumber - 26)
            except TypeError:
                offsetNumberList.append(i)

        return caseAdjuster(numberToLetter(offsetNumberList),caseList)

def decoderOffset(inputString, offsetNumber):
        numberList = letterToNumber(inputString.lower())
        offsetNumberList = []

        #Gen list the lenght of the string, with '1' if uppercase, '0'
        #if lowercase

        caseList = [(i.lower() == i,) for i in inputString]

        for i in numberList:
            try:
                if i-offsetNumber<0:
                    offsetNumberList.append(i - offsetNumber + 26)
                else:
                    offsetNumberList.append(i - offsetNumber)
            except TypeError:
                offsetNumberList.append(i)
        return caseAdjuster(numberToLetter(offsetNumberList),caseList)


###CaeserStack###
def encoderCaeserStack(inputString):

    #Split string into list of fours
    iterations = len(inputString)//4
    numLeftover = len(inputString)%4

    mainList = []
    for i in range(iterations):
        mainList.append(list(inputString[4*i:4*i+4]))

    if numLeftover != 0:
        addList = list(inputString[len(inputString)-numLeftover:])
        for i in range(4-numLeftover):
            addList.append(" ")

        mainList.append(addList)

    #Generate ndarray of mainList
    ndMainList = np.array(mainList)

    #Transpose mainList
    encMainList = ndMainList.transpose()

    #Combine all lists of four into one long list
    encodedList = []
    for i in encMainList:
        encodedList.extend(i)
    return "".join(encodedList)

def decoderCaeserStack(inputString):
        #Split string into list of fours

    numLeftover = len(inputString)%4
    if numLeftover != 0:
        for i in range(numLeftover):
            inputString += " "
    lengthOfList = len(inputString)//4

    mainList = []

    #Generate mainList by splitting string into four lists
    for i in range(4):
        mainList.append(list(inputString[i*lengthOfList:(i+1)*lengthOfList]))

    #Generate ndarray of mainList
    ndMainList = np.array(mainList)

    #Transpose mainList
    encMainList = ndMainList.transpose()

    #Combine all lists of four into one long list
    encodedList = []
    for i in encMainList:
        encodedList.extend(i)
    return "".join(encodedList)

###CaeserStack End###

###Backwards###

def backwards(inputString):
    wordList = inputString.split(" ")


    backwardsList = []
    for word in wordList:
        newWordList=[]
        for index,letter in enumerate(word):
            newWordList.append(word[-(index+1)])
        newWord = "".join(newWordList)
        backwardsList.append(newWord.capitalize())
    print(backwardsList)
    return " ".join(backwardsList)

#cipher that uses the letter shift according to a keyword e.g. CHAIR

def encoderVigenere(inputString, keyword):
    lowerLetters = string.ascii_lowercase
    offsetDict = {l:n for n,l in enumerate(lowerLetters)}
    offsetPattern = [offsetDict[letter] for letter in keyword.lower()]
    caseList = [(i.lower() == i,) for i in inputString]

    conLength = len(keyword)


    numberList = letterToNumber(inputString.lower())
    encodedNumberList = numberList

    for index, num in enumerate(numberList):
        patternIndex = index
        if index > conLength:
            patternIndex = numConstraint(index, conLength)

        try:
            encodedNumberList[index] += offsetPattern[patternIndex]
        except:
            pass

    normalisedEncodedNumberList = [num for num in alphabetRange(encodedNumberList)]

    return caseAdjuster(numberToLetter(normalisedEncodedNumberList),caseList)

def numConstraint(num, conLength):
    while num >= conLength:
        num -= conLength
    return num



def alphabetRange(numList):
    #numList can contain punctuation strings, so must skip them

    returnNumList = []

    for i in numList:
        if str(i)[-1].isdigit():
            if i > 0:
                while i > 25:
                    i-=25
                returnNumList.append(i)
            else:
                while i < 0:
                    i+=25
                returnNumList.append(i)
        else:
            returnNumList.append(i)
    return returnNumList

def decoderVigenere(inputString, keyword):
    lowerLetters = string.ascii_lowercase
    offsetDict = {l:n for n,l in enumerate(lowerLetters)}
    offsetPattern = [offsetDict[letter] for letter in keyword.lower()]
    caseList = [(i.lower() == i,) for i in inputString]

    conLength = len(keyword)


    numberList = letterToNumber(inputString.lower())
    encodedNumberList = numberList

    for index, num in enumerate(numberList):
        patternIndex = index
        if index > conLength:
            patternIndex = numConstraint(index, conLength)

        try:
            encodedNumberList[index] -= offsetPattern[patternIndex]
        except:
            pass

    normalisedEncodedNumberList = [num for num in alphabetRange(encodedNumberList)]

    return caseAdjuster(numberToLetter(normalisedEncodedNumberList),caseList)


#Build a decoder based on the frequency of letters in the English language
#list ordering the most frequent letters (frequencyList)
#scan text and sort letters by their frequency (encodedList)
#create a dictionary mapping the ith position of encodedList to frequencyList
#explore Counter function "from collections import Counter"
