import csv

def quoteWhenContainsComma(stringForCsv):
    if ',' in stringForCsv:
        return '\"' + stringForCsv + '\"'
    return stringForCsv

def convertToQuotedCsvLine(csvLine):
    newCsvLine = []
    for element in csvLine:
        newCsvLine.append(quoteWhenContainsComma(element))
    return newCsvLine


with open('C:\\Users\\harry\\Desktop\\statistics\\broadlyUsed.csv', 'a', encoding="utf-8") as broadlyUsefulOpinionsFile, \
open('C:\\Users\\harry\\Desktop\\statistics\\immutabilityUseful.csv', 'a', encoding="utf-8") as immutabilityProviderOpinionsFile, \
open('C:\\Users\\harry\\Desktop\\statistics\\passingFud.csv', 'a', encoding="utf-8") as passingFudOpinionsFile, \
open('C:\\Users\\harry\\Desktop\\statistics\\irresponsableWaste.csv', 'a', encoding="utf-8") as irresponsibleUseOfResourcesOpinionsFile, \
open('C:\\Users\\harry\\Desktop\\statistics\\currenciesUsed.csv', 'a', encoding="utf-8") as usefulForCurrenciesOpinionsFile, \
open('C:\\Users\\harry\\Desktop\\statistics\\noOpinion.csv', 'a', encoding="utf-8") as naOpinionsFile, \
open('C:\\Users\\harry\\Desktop\\statistics\\strange - should be empty.csv', 'a', encoding="utf-8") as errorFile, \
open("C:\\Users\\harry\\Desktop\\statistics\\results.csv", newline='', encoding="utf-8") as mainStatisticsCsv:
    i = 1
    for line in  csv.reader(mainStatisticsCsv, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True):
        print(i)
        i += 1
        quotedLineElements = convertToQuotedCsvLine(line)
        csvLineAsString = ','.join(quotedLineElements) + '\n'
        blockchainOpinion = line[57]
        if blockchainOpinion == 'Useful across many domains and could change many aspects of our lives':
            broadlyUsefulOpinionsFile.write(csvLineAsString)
            broadlyUsefulOpinionsFile.flush()
        elif blockchainOpinion == 'Useful for immutable record keeping outside of currency':
            immutabilityProviderOpinionsFile.write(csvLineAsString)
            immutabilityProviderOpinionsFile.flush()
        elif blockchainOpinion == 'A passing fad':
            passingFudOpinionsFile.write(csvLineAsString)
            passingFudOpinionsFile.flush()
        elif blockchainOpinion == 'An irresponsible use of resources':
            irresponsibleUseOfResourcesOpinionsFile.write(csvLineAsString)
            irresponsibleUseOfResourcesOpinionsFile.flush()
        elif blockchainOpinion == 'Useful for decentralized currency (i.e., Bitcoin)':
            usefulForCurrenciesOpinionsFile.write(csvLineAsString)
            usefulForCurrenciesOpinionsFile.flush()
        elif blockchainOpinion == 'NA':
            naOpinionsFile.write(csvLineAsString)
            naOpinionsFile.flush()
        else:
            errorFile.write(csvLineAsString)
            errorFile.flush()
