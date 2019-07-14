import csv
import os

openSourceResultsFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\results\\openSourceResults.txt'
if os.path.exists(openSourceResultsFilePath):
    os.remove(openSourceResultsFilePath)

def saveOpenSourceContributionFromFile(opinionsFilePath, category):
    with open(opinionsFilePath, 'r', encoding="utf-8") as opinionsFile:
        never = 0
        lessThanOncePerYear = 0
        lessThanOncePerMonth = 0
        oncePerMonthOrMore = 0
        notMentioned = 0

        for line in csv.reader(opinionsFile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
            openSource = line[3]

            if openSource == 'Never':
                never += 1
            if openSource == 'Less than once per year':
                lessThanOncePerYear += 1
            if openSource == 'Less than once a month but more than once per year':
                lessThanOncePerMonth += 1
            if openSource == 'Once a month or more often':
                oncePerMonthOrMore += 1
            if openSource == 'NA':
                notMentioned += 1

        with open(openSourceResultsFilePath, 'a') as resultsFile:
            resultsFile.write('category: ' + category + 
            ' Never: ' + str(never) +
            ' Less than 1\year: ' + str(lessThanOncePerYear) +
            ' Less than 1\month: ' + str(lessThanOncePerMonth) +
            ' 1\month or more: ' + str(oncePerMonthOrMore) + 
            ' NAs: ' + str(notMentioned) + '\n')


broadlyUsefulFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv'
immutabilityUsefulFilePth = 'C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv'
passingFudFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv'
irresponsableWasteFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv'
cryptocurrenciesFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv'
noOpinionFilePath = 'C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv'

saveOpenSourceContributionFromFile(broadlyUsefulFilePath, 'broadly used')
saveOpenSourceContributionFromFile(immutabilityUsefulFilePth, 'immutability')
saveOpenSourceContributionFromFile(passingFudFilePath, 'passing fud')
saveOpenSourceContributionFromFile(irresponsableWasteFilePath, 'irresponsable waste')
saveOpenSourceContributionFromFile(cryptocurrenciesFilePath, 'cryptocurrencies')
saveOpenSourceContributionFromFile(noOpinionFilePath, 'no opinion')
        
