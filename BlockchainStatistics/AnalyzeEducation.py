import csv
import os

educationResultsFilePath ='C:\\Users\\harry\\Desktop\\statistics\\results\\educationResults.txt'
if os.path.exists(educationResultsFilePath):
    os.remove(educationResultsFilePath)

def saveEducationLevelFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        undergraduateNumber = 0
        banchelorDegree = 0
        others = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            education = line[8]

            if education == 'Bachelor’s degree (BA, BS, B.Eng., etc.)':
                banchelorDegree += 1
            elif education == 'Associate degree' or \
                education == 'Some college/university study without earning a degree' or \
                education == 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)' or \
                education == 'Primary/elementary school' or \
                education == 'I never completed any formal education':
                undergraduateNumber += 1
            elif education == 'NA':
                notMentioned += 1
            else:
                others += 1

        with open(educationResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + 
            ' Bachelor degree: ' + str(banchelorDegree) +
            ' Undergraduate: ' + str(undergraduateNumber) +
            ' Others: ' + str(others) +
            ' NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveEducationLevelFromFile(broadlyUsefulFilePath, 'broadly used')
saveEducationLevelFromFile(immutabilityUsefulFilePth, 'immutability')
saveEducationLevelFromFile(passingFudFilePath, 'passing fud')
saveEducationLevelFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveEducationLevelFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveEducationLevelFromFile(noOpinionFilePath, 'no opinion')
        