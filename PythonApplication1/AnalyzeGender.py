
import csv
import os

genderResultsFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\results\\genderResults.txt'
if os.path.exists(genderResultsFilePath):
    os.remove(genderResultsFilePath)

def saveGenderFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        male = 0
        female = 0
        other = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            gender = line[78]

            if gender == 'Man':
                male += 1
            if gender == 'Woman':
                female += 1
            if gender != 'Man' and gender != 'Woman' and gender != 'NA':
                other += 1
            if gender == 'NA':
                notMentioned += 1

        with open(genderResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + 
            ' Male: ' + str(male) +
            ' Female: ' + str(female) +
            ' Other: ' + str(other) +
            ' NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveGenderFromFile(broadlyUsefulFilePath, 'broadly used')
saveGenderFromFile(immutabilityUsefulFilePth, 'immutability')
saveGenderFromFile(passingFudFilePath, 'passing fud')
saveGenderFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveGenderFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveGenderFromFile(noOpinionFilePath, 'no opinion')
        
