import requests
from bs4 import BeautifulSoup
import sys
import pyodbc
import MySQLdb


def spider(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    dataEntryList = []
    series = None
    i = 1
    for psu_tables in soup.findAll('table', {'border': '0'}, {'dir': 'ltr'}):
        print "**********TABLE#"+str(i)+"**********"
        j = 1
        for table_rows in psu_tables.findAll('tr'):
            if j > 2:
                print "-----ROW#"+str(j)+"-----"
                k = 1
                for data_line in table_rows.findAll('p', {'class': 'MsoNormal'}):
                    data = data_line.find('span', {'lang': 'es'})
                    dataEntryList.append(data.text)
                    #print "cardname " + data.text
                    k += 1
                if(len(dataEntryList) == 5):
                    series = dataEntryList[0]
                    print series
                    print dataEntryList[1]
                    print dataEntryList[2]
                    print dataEntryList[3]
                    print dataEntryList[4]
                    query = "Insert into powerSupply values ('" + series + "','" + dataEntryList[1] + "','" + dataEntryList[2] + "','" + dataEntryList[3] + "','" + dataEntryList[4] + "')"
                else:
                    print series
                    print dataEntryList[0]
                    print dataEntryList[1]
                    print dataEntryList[2]
                    print dataEntryList[3]
                    query = "Insert into powerSupply values ('" + series + "','" + dataEntryList[0] + "','" + dataEntryList[1] + "','" + dataEntryList[2] + "','" + dataEntryList[3] + "')"
                cursor.execute(query)
                del dataEntryList[:]
            j += 1
        i += 1



#conn = pyodbc.connect("DRIVER={SQL Server};SERVER=SHAHRIYAR-PC\SQLEXPRESS;DATABASE=hcidb")
conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "",db="hcidb", use_unicode=True, charset="utf8" )
cursor = conn.cursor()


#if table is not created then run this query
#cursor.execute("CREATE TABLE `powersupply` (`cardSeries` varchar(100) NOT NULL,`cardName` varchar(100) NOT NULL,`wattage` varchar(20) NOT NULL,`sixPin` varchar(20) NOT NULL,`eightPin` varchar(20) NOT NULL) ENGINE=MyISAM DEFAULT CHARSET=latin1;")
#else

cursor.execute("Truncate table powerSupply")

reload(sys)
sys.setdefaultencoding('utf-8')
URL = 'http://www.realhardtechx.com/index_archivos/Page362.htm'
spider(URL)

conn.commit();
conn.close()
