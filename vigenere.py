import string

#Cipher function
def vigenere(inputString, keyword, mode):
    """
    Parameters
    ----------
    inputString: string
        The string to be encoded or decoded.

    keyword: string
        The keyword used to encode or decode the inputString.

    mode: "encode" or "decode"
        Specifies whether the function should encode or decode the inputString.

    Returns
    -------
    string
        encoded or decoded inputString

    """



    lowerLetters = string.ascii_lowercase #string containing all lowercase letters of English alphabet
    offsetDict = {l:n for n,l in enumerate(lowerLetters)} #dictionary mapping letters to a number from 0 to 25
    offsetPattern = [offsetDict[letter] for letter in keyword.lower()] #list of numbers by which to offset each letter of inputString
    caseList = [(i.lower() == i,) for i in inputString] #list of all upper case letters in inputString

    conLength = len(keyword) #length of keyword


    numberList = letterToNumber(inputString.lower()) #convert inputString into a list of numbers each from 0 to 25
    encodedNumberList = numberList #create a copy of numberList

    if mode == "encode":
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

    elif mode == "decode":
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

    else:
        print("Check 'mode', should be 'encode' or 'decode'.")
        return

#Helper Functions

def numConstraint(num, conLength):
    """
    Parameters
    ----------
    num: int
        Number to constrain into desired range
    conLength: int
        Upperbound constraint for num variable

    Returns
    -------
    int
        Remainder of num after division by conLength

    """
    return num % conLength



def alphabetRange(numList):
    """
    Parameters
    ----------
    numlist: list,int
        list of numbers

    Returns
    -------
    list,int
        list of numbers each noramlised to range(0,26)
    """

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

#Converts string into a list of numbers by mapping each letter its 'alphabet number'
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

#Converts a list of numbers into a string
#Each letter of the string corresponds to the 'alphabet number' of the list
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

#Capitlises characters in a list based on their position
def caseAdjuster(inputString, caseList):
    """
    Parameters
    ----------
    inputString: string

    caseList: list[bool]
        list of boolean tuples of form (False,) or (True,)
        Pass if (True,)
        Capitlise char if (False,)

    Return
    ------
    string
        inputString with characters capitalised according to specification in
        caseList
    """
    returnList = []
    for i,v in enumerate(caseList):
        if v == (False,):
            returnList.append(inputString[i].upper())
        else:
            returnList.append(inputString[i])

    return "".join(returnList)
