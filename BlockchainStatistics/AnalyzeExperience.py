import csv
import os

experienceResultsFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\results\\experienceResults.txt'
if os.path.exists(experienceResultsFilePath):
    os.remove(experienceResultsFilePath)

def saveAverageExperienceFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        sum = 0
        numberOfValidEntries = 0
        notMentioned = 0
        skippedResponses = 0
        lessThanOneYear = 0
        overFifty = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            stringExperience = line[15]

            if stringExperience == 'Less than 1 year':
                lessThanOneYear += 1
            elif stringExperience == 'More than 50 years':
                overFifty += 1
            elif stringExperience != 'NA' :
                age = float(stringExperience)
                sum = sum + age
                numberOfValidEntries = numberOfValidEntries + 1
            elif stringExperience == 'NA' :
               notMentioned = notMentioned + 1
            

        averageExperience = sum / numberOfValidEntries
        with open(experienceResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + 
                              '  average experience: ' + str(averageExperience) + 
                              '  valid responses: ' + str(numberOfValidEntries) + 
                              '  less than 1 year: ' + str(lessThanOneYear) + 
                              '  over 50 years: ' + str(overFifty) + 
                              '  NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveAverageExperienceFromFile(broadlyUsefulFilePath, 'broadly used')
saveAverageExperienceFromFile(immutabilityUsefulFilePth, 'immutability')
saveAverageExperienceFromFile(passingFudFilePath, 'passing fud')
saveAverageExperienceFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveAverageExperienceFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveAverageExperienceFromFile(noOpinionFilePath, 'no opinion')



        
