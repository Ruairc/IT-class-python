totalNonErroneous=0
countNonErroneous=0
numBS= [1,-19,4,3,-5,2]
print("list with faulty data points",numBS)
for item in numBS:
    if item>=0:
        totalNonErroneous +=item
        countNonErroneous +=1
    
averageNonErroneous=totalNonErroneous/countNonErroneous
print("average of NonErroneous data:",averageNonErroneous)
for counter in range (len(numBS)):
    if numBS[counter]<0:
        numBS[counter]=averageNonErroneous
print("list with faulty data points is replaced with the average of the good data",numBS)