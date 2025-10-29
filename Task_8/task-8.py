import math

values = [3, 1, 5, 2, 7, 8, 9, 9]

levels = math.log(len(values), 2)
LEVELS = int(levels)

def minmaxalgo(currDepth, nodeIndex, isMinTurn, values, totalDepth):
   
    if currDepth == totalDepth:
        return values[nodeIndex]

    if isMinTurn:
        return min(
            minmaxalgo(currDepth + 1, nodeIndex * 2, False, values, totalDepth),
            minmaxalgo(currDepth + 1, nodeIndex * 2 + 1, False, values, totalDepth)
        )
    else:
       
        return max(
            minmaxalgo(currDepth + 1, nodeIndex * 2, True, values, totalDepth),
            minmaxalgo(currDepth + 1, nodeIndex * 2 + 1, True, values, totalDepth)
        )

print("The optimal value is:", minmaxalgo(0, 0, True, values, LEVELS))
