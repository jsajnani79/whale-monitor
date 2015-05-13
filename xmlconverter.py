# xmlconverter.py
# WhaleKillers
# @Author: Alec Powell
#-------

#OLD WAY, TRIED TO USE XML2CSV PACKAGE --------DOESNT WORK
# import csv
# from xmlutils.xml2csv import xml2csv

# inputs = "data/APPALOOSA_MANAGEMENT_LP_2014-12-31.xml"
# outputs = "output.csv"

# converter = xml2csv(inputs, outputs)
# converter.convert(tag="nameOfIssuer", ignore="votingAuthority")


import sys
import csv
import xml.etree.ElementTree as ET

def xmlToCsv(inFile, outFile):
	NS = 'http://www.sec.gov/edgar/document/thirteenf/informationtable'
	header = ('name', 'class', 'cusip', 'value', 'shares')

	tree = ET.parse(inFile)
	root = tree.getroot()

	with open(outFile, 'w') as f:
	    writer = csv.writer(f)
	    writer.writerow(header)
	    for infoTable in root.iter('{%s}infoTable' % NS):
	        name = infoTable[0].text
	        classNm = infoTable[1].text
	        cusip = infoTable[2].text
	        # NOTE: value in xml table is value in thousands, so we multiply by $1,000
	        value = infoTable[3].text
	        real_value = int(value) * 1000
	        shares = infoTable[4][0].text

	        row = name, classNm, cusip, real_value, shares
	        writer.writerow(row)



