        for i in range(m):
            oneCntList = getAllLines(i, 0)
            lineCntMatrix[i][0] = oneCntList
        
        for j in range(1, n):
            oneCntList = getAllLines(0, j)
            print(j)
            lineCntMatrix[0][j] = oneCntList
        
        print(getAllLines(0, 0))
        print(getAllLines(0, 0))