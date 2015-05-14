import xmldownloader
import xmlconverter
import os

ciks = ["1006438","842322","109694","1350694","868491","1535472","1314588","1056831","1300763","1420192","1079563","1159159","1315309","1061165","1056529","898202","1035674","1336528","1599822","1509842","1047644","1029160","807985","1021944","1040273","1167483","1345472","1351069"]

def main():
	# xmldownloader.getXMLFilingsByCIK(ciks)
	xmlFiles = os.listdir("data/xml/")
	for file in xmlFiles:
		if file.endswith('.xml'):
			inFile = "data/xml/" + file
			outFile = "data/csv/" + os.path.splitext(file)[0] + ".csv"
			xmlconverter.xmlToCsv(inFile, outFile)
	xmlconverter.mergeCSVs("data/csv", "data/combined.csv")

if __name__ == "__main__":
    main()