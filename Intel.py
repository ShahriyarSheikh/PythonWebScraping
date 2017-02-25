import requests
import sys
from bs4 import BeautifulSoup
import pyodbc
import MySQLdb



def visit_single_link(url,title,description):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    table_div = soup.find('div', {'id': 'tabs-Desktop'})
    if table_div is not None:
        table_body = table_div.find('tbody')
        for list_item in table_body.findAll('tr'):
            i = 1
            for processor in list_item.findAll('td'):
                if i == 2:
                    anchor = processor.find('a')
                    processor_link = anchor.get('href')
                    name = anchor.text
                    print name
                    queryMaker(title,"Intel",name,description)
                i += 1


def spider(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    products = soup.find('div', {'id': 'Processors-DesktopProcessors-scrollpane'})
    i = 1
    for list_item in products.findAll('td'):
        href = list_item.find('a')
        if href is not None:
            title = href.text
            item_link = "http://ark.intel.com"+href.get('href')
            print "######################Link number "+str(i)+"######################"
            print item_link
            print title
            description = "more..."
            if "i3" in title:
                description = i3Description
            if "i5" in title:
                description = i5Description
            if "i7" in title:
                description = i7Description
            visit_single_link(item_link,title,description)
        i += 1

def queryMaker(nameGen,company,processorDesc,description):
    query = "Insert into processors values ('" + processorDesc + "','" + nameGen + "','" + company + "','" + description + "')"
    cursor.execute(query);



conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "",db="hcidb", use_unicode=True, charset="utf8" )
cursor = conn.cursor()






#if table is not created then run this query
#cursor.execute("CREATE TABLE `processors` (`processorDesc` varchar(500) NOT NULL,`nameGen` varchar(500) NOT NULL,`company` varchar(50) NOT NULL,`description` varchar(500) NOT NULL) ENGINE=MyISAM DEFAULT CHARSET=latin1;")
#else







cursor.execute("Truncate table processors")


reload(sys)
sys.setdefaultencoding('utf-8')

URL = 'http://ark.intel.com'
i3Description = "Core i3. A family of dual core, 64-bit, x86 CPUs from Intel intended for entry-level desktop and laptop computers. The Core i3 chips do not include the Turbo Boost feature, which is found in i5 and i7 chips."
i5Description = "Core i5. A family of dual and quad core, 64-bit, x86 CPUs from Intel. The Core i5 chips are the midrange CPUs in the Core i line between the entry-level i3 and the high-performance i7 series."
i7Description = "Core i7. A family of 64-bit x86 CPUs with up to eight cores from Intel. The Core i7 chips are the high-end CPUs in the Core i line. The first models included a graphics processing unit (GPU) in the same chip package as the CPU; however, 2nd Generation Core models integrate a GPU on the same die as the CPU."
spider(URL)



cursor.execute("UPDATE processors set nameGen = Replace(nameGen,'®','')")

cursor.execute("UPDATE processors set nameGen = Replace(nameGen,'™','')")


cursor.execute("UPDATE processors set processorDesc = Replace(processorDesc,'®','')")

cursor.execute("UPDATE processors set processorDesc = Replace(processorDesc,'™','')")

cursor.execute("Insert into processors values ('NA','NA','NA','NA')")

conn.commit();
conn.close()
