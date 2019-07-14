
import csv
import os

codesAsHobyContributionFromFile = 'C:\\Users\\harry\\Desktop\\statistics\\results\\codesAsHobbyResults.txt'
if os.path.exists(codesAsHobyContributionFromFile):
    os.remove(codesAsHobyContributionFromFile)

def saveCodesAsHobyFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        yes = 0
        no = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            codesAsHobby = line[2]

            if codesAsHobby == 'Yes':
                yes += 1
            if codesAsHobby == 'No':
                no += 1
            if codesAsHobby == 'NA':
                notMentioned += 1

        with open(codesAsHobyContributionFromFile, 'a') as resultsFile:
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

saveCodesAsHobyFromFile(broadlyUsefulFilePath, 'broadly used')
saveCodesAsHobyFromFile(immutabilityUsefulFilePth, 'immutability')
saveCodesAsHobyFromFile(passingFudFilePath, 'passing fud')
saveCodesAsHobyFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveCodesAsHobyFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveCodesAsHobyFromFile(noOpinionFilePath, 'no opinion')
        
