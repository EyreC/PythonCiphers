

def stack(inputString, stackLen, mode):
    """
    Paramters
    ---------
    inputString : string

    stackLen : int
        Number of columns in the stacked matrix

    mode: "encode" or "decode"
        Specifies whether the function should encode or decode the inputString.

    Returns
    -------
    string
        (encode) Columns of matrix, formed by stacking every stackLen characters vertically,
        read continuously from left to right.
        (decode) Columns of matrix, formed by stacking every stackLen characters vertically,
        read continuously from left to right.
    """
    if mode == "encode":
        #Split string into list of fours
        iterations = len(inputString)//stackLen
        numLeftover = len(inputString)%stackLen

        mainList = []
        for i in range(iterations):
            mainList.append(list(inputString[stackLen*i:stackLen*i+stackLen]))

        if numLeftover != 0:
            addList = list(inputString[len(inputString)-numLeftover:])
            for i in range(stackLen-numLeftover):
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

    elif mode == "decode":
        numLeftover = len(inputString)%stackLen
        if numLeftover != 0:
            for i in range(numLeftover):
                inputString += " "
        lengthOfList = len(inputString)//stackLen

        mainList = []

        #Generate mainList by splitting string into four lists
        for i in range(stackLen):
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

    else:
        print("Check mode. Select 'encode' or 'decode'.")
        return

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
