# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class PythonOrgSearch(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Firefox()

#     def test_search_in_python_org(self):
#     	arr = ['a','b','c','d']
#     	for x in range(0, 3):
#     		print arr[x]
#         driver = self.driver
#         driver.get("http://www.insidermonkey.com/hedge-fund/paulson+%26+co/18/holdings/#/offset=10&ffp=2014-12-31&fot=7&fso=1")
#         select_box = driver.find_element_by_id("select-ffp")
#         children = select_box.find_elements_by_tag_name("option")
        
#         for select in children:
#         	select_box.click()
#         	select.click()
# 		# options = [x for x in select_box.find_elements_by_tag_name("option")] 
# 		# print select_box.find_elements_by_tag_name("option")
#         # elem.send_keys("pycon")
#         # print select_box.children
#         # elem.send_keys(Keys.RETURN)
#         # assert "No results found." not in driver.page_source


#     def tearDown(self):
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()
import urllib2

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



ciks = ["1006438","842322","109694","1350694","868491","1535472","1314588","1056831","1300763","1420192","1079563","1159159","1315309","1061165","1056529","898202","1035674","1336528","1599822","1509842","1047644","1029160","807985","1021944","1040273","1167483","1345472","1351069"]
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
			driver.get(filing) #shouldn't i be indexing and going through all docs
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
				file = open("data/"+xmlTable['name']+".xml", 'w')
				file.write(contents)
				file.close()
			# print infoTables


# url = "http://www.sec.gov/Archives/edgar/data/1035674/000114036115007474/form13fInfoTable.xml"
# s = urllib2.urlopen(url)
# contents = s.read()
# file = open("data/export.xml", 'w')
# file.write(contents)
# file.close()

driver.close()





# document.getElementsByClassName('tableFile2')[0].children[0].children













