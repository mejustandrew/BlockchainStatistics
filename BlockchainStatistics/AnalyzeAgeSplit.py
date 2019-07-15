
import csv
import os

ageSplitResultsFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\results\\ageSplitResults.txt'
if os.path.exists(ageSplitResultsFilePath):
    os.remove(ageSplitResultsFilePath)

def saveAgeSplitFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        underTwenty = 0
        twentyToThirty = 0
        thirtyToFourty = 0
        fourtyToFifty = 0
        overFifty = 0
        numberOfValidEntries = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            stringAge = line[77]

            if stringAge != 'NA':
                age = float(stringAge)
                numberOfValidEntries = numberOfValidEntries + 1
                if age < 20:
                    underTwenty += 1
                elif age < 30:
                    twentyToThirty += 1
                elif age < 40:
                    thirtyToFourty += 1
                elif age < 50:
                    fourtyToFifty +=1
                else:
                    overFifty +=1
            else:
               notMentioned = notMentioned + 1

        with open(ageSplitResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + 
                              '  under twenty: ' + str(underTwenty) + 
                              '  twenty to thirty: ' + str(twentyToThirty) +
                              '  thirty to fourty: ' + str(thirtyToFourty) +
                              '  fourty to fifty: ' + str(fourtyToFifty) +
                              '  over fifty: ' + str(overFifty) +
                              '  NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveAgeSplitFromFile(broadlyUsefulFilePath, 'broadly used')
saveAgeSplitFromFile(immutabilityUsefulFilePth, 'immutability')
saveAgeSplitFromFile(passingFudFilePath, 'passing fud')
saveAgeSplitFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveAgeSplitFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveAgeSplitFromFile(noOpinionFilePath, 'no opinion')



        