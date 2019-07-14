import csv
import os

futureResultsFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\results\\futureResults.txt'
if os.path.exists(futureResultsFilePath):
    os.remove(futureResultsFilePath)

def saveOpinionAboutFutureFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        yes = 0
        no = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            opinionAboutFuture = line[58]

            if opinionAboutFuture == 'Yes':
                yes += 1
            elif opinionAboutFuture == 'No':
                no += 1
            else:
                notMentioned += 1

        with open(futureResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + 
            ' Yes: ' + str(yes) +
            ' No: ' + str(no) +
            ' NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveOpinionAboutFutureFromFile(broadlyUsefulFilePath, 'broadly used')
saveOpinionAboutFutureFromFile(immutabilityUsefulFilePth, 'immutability')
saveOpinionAboutFutureFromFile(passingFudFilePath, 'passing fud')
saveOpinionAboutFutureFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveOpinionAboutFutureFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveOpinionAboutFutureFromFile(noOpinionFilePath, 'no opinion')
        
