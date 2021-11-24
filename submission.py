
def sortSemanticVersion(*s):
    # arguments checking and cleaning
    if type(s[0]) is list:
        processedArgument = s[0]
    else:
        processedArgument = list(s)
    firstList = [elem.split(".") for elem in processedArgument]
    
    # sorted list of integers
    secondList = [list(map(int,x))for x in firstList]
    sortedList = sorted(secondList, reverse=True)
    
    #converting the sorted list back to semantic version format
    finalList = []
    for miniList in sortedList:
        miniList = ".".join(str(var) for var in miniList)
        finalList.append(miniList)
    return(finalList)
print(sortSemanticVersion(["3.9.5", "4.3.11", "1.2.11", "8.1.2", "4.3.6", "4.5.6"]));