input_string = input("")[2:-2]

if input_string == "":
    print ("[[]]")
else:
    listOfLists  = input_string.split('], [')
    for i in range(len(listOfLists)):
        listOfLists[i]=listOfLists[i]
        listOfLists[i]=listOfLists[i].split(', ')
        listOfLists[i] = [ int(x) for x in listOfLists[i] ]
    numOfRows=len(listOfLists)
    if (numOfRows!=0):
        numOfColumns=len(listOfLists[0])
    else:
        numOfColumns=0    
    transpose=[[0]*numOfColumns for i in range(numOfRows)]

    for row in range(numOfRows):
        for column in range (numOfColumns):
            transpose[column][row]=listOfLists[row][column]

    print(transpose)
