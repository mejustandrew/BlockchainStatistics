import csv
import os

experienceSplitResultsFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\results\\experienceSplitResults.txt'
if os.path.exists(experienceSplitResultsFilePath):
    os.remove(experienceSplitResultsFilePath)

def saveExperienceSplitFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        underTwoYears = 0
        twoToFiveYears = 0
        fiveToTenYears = 0
        overTenYears = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            stringExperience = line[15]

            if stringExperience == 'Less than 1 year':
                underTwoYears += 1
            elif stringExperience == 'More than 50 years':
                overTenYears += 1
            elif stringExperience != 'NA':
                age = float(stringExperience)
                if age < 2:
                    underTwoYears += 1
                elif age < 5:
                    twoToFiveYears += 1
                elif age < 10:
                    fiveToTenYears += 1
                else:
                    overTenYears += 1
            elif stringExperience == 'NA' :
               notMentioned = notMentioned + 1
           

        with open(experienceSplitResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + 
                              '  under two years: ' + str(underTwoYears) + 
                              '  two to five years: ' + str(twoToFiveYears) +
                              '  five to ten years: ' + str(fiveToTenYears) +
                              '  over ten years: ' + str(overTenYears) +
                              '  NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveExperienceSplitFromFile(broadlyUsefulFilePath, 'broadly used')
saveExperienceSplitFromFile(immutabilityUsefulFilePth, 'immutability')
saveExperienceSplitFromFile(passingFudFilePath, 'passing fud')
saveExperienceSplitFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveExperienceSplitFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveExperienceSplitFromFile(noOpinionFilePath, 'no opinion')



        