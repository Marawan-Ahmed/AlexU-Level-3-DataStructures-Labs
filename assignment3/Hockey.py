def userInput():
    dimenssions = input("").replace(" ", "").split(',')
    img_row = int(dimenssions[0])
    img_column = int(dimenssions[1])

    raw_img = []

    for row in range(img_row):
        temp=[]
        for col in str(input()):
            temp.append(col)
        raw_img.append(temp)

    color = input("")
    threshold = int(input(""))


    for row in range(img_row):
        for column in range(img_column):
            if (raw_img[row][column] == color):
                raw_img[row][column] = 1
            else:
                raw_img[row][column] = 0
    return (img_row,img_column,threshold,raw_img)

# Function that return true if mat[row][col]
# is valid and hasn't been visited
def isValid(raw_img, row, col, img_row, img_column):                    
    # If row and column are valid and element
    # is matched and hasn't been visited then
    # the cell is safe
    if ((row >= 0 and row < img_row) and (col >= 0 and col < img_column) and raw_img[row][col] and (not numbered_img[row][col])):
        return True
    else:
        return False        
 
# Function for depth first search
def DFS(raw_img, row, col, img_row, img_column) :
    # These arrays are used to get row
    # and column numbers of 4 neighbours
    # of a given cell
    rowNbr = [ -1, 0, 0, 1 ]
    colNbr = [ 0, -1, 1, 0 ]
    global connectedComp
    # Mark this cell as visited
    numbered_img[row][col] = connectedComp
    # Recur for all connected neighbours
    for k in range(4) :
        if (isValid(raw_img, row + rowNbr[k],col + colNbr[k], img_row, img_column)) :
            DFS(raw_img, row + rowNbr[k],col + colNbr[k], img_row, img_column)
    
# Function to return the number of
# connected components in the matrix
def connectedComponents(raw_img, img_row, img_column) :
    global connectedComp
    for row in range(img_row) :
        for column in range(img_column):
            if ((not numbered_img[row][column]) and raw_img[row][column]):
                connectedComp += 1
                DFS(raw_img, row, column, img_row, img_column)
                
def countConnectedComponents(numbered_img, img_row, img_column,connectedComp,threshold):
    possiblePlayers = [[0]*5 for i in range(connectedComp)]  #each element consists of number ofelements min x,,max x,min y max y 
    for row in range (img_row):
        for col in range (img_column):
            if (numbered_img[row][col] != 0):
                if (possiblePlayers[numbered_img[row][col]-1][0] == 0):
                    possiblePlayers[numbered_img[row][col]-1][1] = col
                    possiblePlayers[numbered_img[row][col]-1][2] = col
                    possiblePlayers[numbered_img[row][col]-1][3] = row
                    possiblePlayers[numbered_img[row][col]-1][4] = row
                else:
                    if (possiblePlayers[numbered_img[row][col]-1][1] > col ):
                        possiblePlayers[numbered_img[row][col]-1][1] = col
                    if (possiblePlayers[numbered_img[row][col]-1][2] < col ):
                        possiblePlayers[numbered_img[row][col]-1][2] = col

                    if (possiblePlayers[numbered_img[row][col]-1][3] > row ):
                        possiblePlayers[numbered_img[row][col]-1][3] = row
                    if (possiblePlayers[numbered_img[row][col]-1][4] < row ):
                        possiblePlayers[numbered_img[row][col]-1][4] = row

                possiblePlayers[numbered_img[row][col]-1][0] += 1

    playersPosition = []

    for i in range(connectedComp):
        if ((possiblePlayers[i][0]*4) >= threshold):
            playersPosition.append((possiblePlayers[i][1] + 1 + possiblePlayers[i][2],possiblePlayers[i][3] + 1 + possiblePlayers[i][4]))
    return playersPosition

def printOutput (playersPosition):
    print (sorted(playersPosition, key=lambda element: (element[0], element[1])))
    
# Driver code
if __name__ == "__main__" :
    connectedComp = 0
    img_row,img_column,threshold,raw_img = userInput()
    numbered_img = [[0]*img_column for i in range(img_row)]
    connectedComponents(raw_img, img_row, img_column)
    printOutput(countConnectedComponents(numbered_img, img_row, img_column,connectedComp,threshold))
