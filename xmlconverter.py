# xmlconverter.py
# WhaleKillers
# @Author: Alec Powell
#-------

import sys
import csv
import xml.etree.ElementTree as ET

import glob
import os
import time
from itertools import izip_longest
import fnmatch
import datetime
from datetime import timedelta, datetime
import shutil
import time
from sys import argv

import pandas as pd

def xmlToCsv(inFile, outFile):
	NS = 'http://www.sec.gov/edgar/document/thirteenf/informationtable'
	header = ('name', 'class', 'cusip', 'value', 'shares')

	tree = ET.parse(inFile)
	root = tree.getroot()
	fileName = inFile[9:-4]
	filingDate = fileName[-10:]
	fundName = fileName[:-11]
	with open(outFile, 'w') as f:
	    writer = csv.writer(f)
	    # writer.writerow(header)
	    for infoTable in root.iter('{%s}infoTable' % NS):
	        name = infoTable[0].text
	        classNm = infoTable[1].text
	        cusip = infoTable[2].text
	        # NOTE: value in xml table is value in thousands, so we multiply by $1,000
	        value = infoTable[3].text
	        real_value = int(value) * 1000
	        shares = infoTable[4][0].text

	        row = fundName, filingDate, name, classNm, cusip, real_value, shares
	        writer.writerow(row)

def mergeCSVs(readDir, outFile):
	fout=open(outFile,"a")
	allFiles = glob.glob(readDir + "/*.csv")
	for file in allFiles:
	    for line in open(file):
	         fout.write(line)    
	fout.close()



