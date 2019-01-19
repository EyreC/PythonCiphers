import string

def backwards(inputString):

    wordList = inputString.split(" ") #list of space-separated words in inputString

    backwardsList = [] #list of reversed words

    #Generate list of reversed words
    for word in wordList:
        newWordList=[]
        for index,letter in enumerate(word):
            newWordList.append(word[-(index+1)])
        newWord = "".join(newWordList)
        backwardsList.append(newWord)

    return " ".join(backwardsList).capitalize()
