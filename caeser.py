def caeser(inputString, offsetNumber, mode):
        """
        Parameters
        ----------
        inputString: string
            The string to be encoded or decoded.

        offsetNumber: int
            Number of letters along the alphabet each character is to be transformed by.

        mode: "encode" or "decode"
            Specifies whether the function should encode or decode the inputString.

        Returns
        -------
        string
            encoded or decoded inputString

        """

        numberList = letterToNumber(inputString.lower()) #list of numbers mapping each alphabet character
        offsetNumberList = [] #list of numbers transformed according to the offsetNumber

        caseList = [(i.lower() == i,) for i in inputString] #list of same length as inputString; '1' if char is uppercase, '0' if lowercase

        if mode == "encode":
            for i in numberList:
                try:
                    if i+offsetNumber<26:
                        offsetNumberList.append(i + offsetNumber)
                    else:
                        offsetNumberList.append(i + offsetNumber - 26)
                except TypeError:
                    offsetNumberList.append(i)

            return caseAdjuster(numberToLetter(offsetNumberList),caseList)

        elif mode == "decode":
            for i in numberList:
                try:
                    if i-offsetNumber<0:
                        offsetNumberList.append(i - offsetNumber + 26)
                    else:
                        offsetNumberList.append(i - offsetNumber)
                except TypeError:
                    offsetNumberList.append(i)
            return caseAdjuster(numberToLetter(offsetNumberList),caseList)

        else:
            print("Check mode. Select either 'encode' or 'decode'.")
            return
