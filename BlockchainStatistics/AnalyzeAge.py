import csv
import os

ageResultsFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\results\\ageResults.txt'
if os.path.exists(ageResultsFilePath):
    os.remove(ageResultsFilePath)

def saveAverageAgeFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        sum = 0
        numberOfValidEntries = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            stringAge = line[77]

            if stringAge != 'NA':
                age = float(stringAge)
                sum = sum + age
                numberOfValidEntries = numberOfValidEntries + 1
            else:
               notMentioned = notMentioned + 1

        averageAge = sum / numberOfValidEntries
        with open(ageResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + '  average age: ' + str(averageAge) + \
                              '  valid responses: ' + str(numberOfValidEntries) + '  NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveAverageAgeFromFile(broadlyUsefulFilePath, 'broadly used')
saveAverageAgeFromFile(immutabilityUsefulFilePth, 'immutability')
saveAverageAgeFromFile(passingFudFilePath, 'passing fud')
saveAverageAgeFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveAverageAgeFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveAverageAgeFromFile(noOpinionFilePath, 'no opinion')



        