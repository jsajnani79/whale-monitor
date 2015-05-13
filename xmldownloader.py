import urllib2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getXMLFilingsByCIK(ciks):
	driver = webdriver.Firefox()
	for cik in ciks:
		driver.get("http://www.sec.gov/edgar/searchedgar/companysearch.html")
		elem = driver.find_element_by_id("cik")
		elem.send_keys(cik)
		elem.send_keys(Keys.RETURN)
		tableItems = driver.find_elements_by_class_name('tableFile2')[0].find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')
		xmlDocs = []
		infoTables = []
		for index in xrange(0, len(tableItems)):
			if("13F-HR" in tableItems[index].text):
				 xmlDocs.append(tableItems[index].find_elements_by_tag_name('a')[0].get_attribute('href'))
		if len(xmlDocs)>0:
			for filing in xmlDocs:
				driver.get(filing)
				companyName = driver.find_elements_by_class_name("companyName")[0].text.split('(Filer)')[0].replace (" ", "_")
				reportDate = driver.find_element_by_id('formDiv').find_elements_by_class_name('formGrouping')[1].find_elements_by_class_name('info')[0].text
				fileName = companyName+reportDate
				docs = driver.find_elements_by_class_name('tableFile')[0].find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')
				for index in xrange(0, len(docs)):
					if("INFORMATION TABLE" in docs[index].text and "xml" in docs[index].text):
						infoTables.append({'href':docs[index].find_elements_by_tag_name('a')[0].get_attribute('href'), 'name': fileName})
				for xmlTable in infoTables:
					s = urllib2.urlopen(xmlTable['href'])		
					contents = s.read()
					file = open("data/xml/"+xmlTable['name']+".xml", 'w')
					file.write(contents)
					file.close()
	driver.close()












