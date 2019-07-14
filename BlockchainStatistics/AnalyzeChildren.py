import csv
import os

childrenResultsFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\results\\childrenResults.txt'
if os.path.exists(childrenResultsFilePath):
    os.remove(childrenResultsFilePath)

def saveChildrenFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        haveChildren = 0
        doNotHaveChildren = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            children = line[82]

            if children == 'Yes':
                haveChildren += 1
            elif children == 'No':
                doNotHaveChildren += 1
            else:
                notMentioned += 1

        with open(childrenResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + 
            ' have children: ' + str(haveChildren) +
            ' do not have children: ' + str(doNotHaveChildren) +
            ' NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveChildrenFromFile(broadlyUsefulFilePath, 'broadly used')
saveChildrenFromFile(immutabilityUsefulFilePth, 'immutability')
saveChildrenFromFile(passingFudFilePath, 'passing fud')
saveChildrenFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveChildrenFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveChildrenFromFile(noOpinionFilePath, 'no opinion')
        
