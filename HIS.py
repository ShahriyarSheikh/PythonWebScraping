import requests
from bs4 import BeautifulSoup
import sys
import pyodbc
import MySQLdb


def visit_single_link(url, card_num,title,description):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    products = soup.find('table', {'class': 'producttab'})
    for list_item in products.findAll('td', {'valign': 'top'}):
        print "------------Card # "+str(card_num)+"------------"
        short_description_tag = list_item.find('a', {'class': 'intro clearfix'})
        short_description = short_description_tag.text
        href = list_item.find('a')
        item_link = "http://www.hisdigital.com/us/"+href.get('href')
        img = list_item.find('img')
        img_src = "http://www.hisdigital.com/"+img['src']
        product_table = list_item.find('table', {'class': 'clearfix'})
        product_summary = []
        i = 0
        if (product_table != None):
            single_product_table = product_table.findAll('td')
        for summary_list in single_product_table:
            #summary_list.findAll('td')
            product_summary.append(summary_list.text)
            i += 1
            # key = summary_list.find('td', {'width': '40%'})
            # value = summary_list.find('td', {'width': '60%'})
            # product_summary[key] = value
        print "card item_link = " + item_link
        print "short_description = " + short_description
        print "card img = " + img_src
        print len(product_summary)
        card_num += 1

        queryMaker('AMD',title,short_description,item_link,img_src,description)

    bottom_nav = soup.find('div', {'class': 'bottomnav'})
    if bottom_nav is not None:
        pages = bottom_nav.findAll('a')
        next_page = pages[-1]
        next_page_link = None
        if "Next" in next_page.text:
            next_page_link = "http://www.hisdigital.com/"+pages[-1].get('href')
            print "Next_page_link " + next_page_link
            visit_single_link(next_page_link, card_num,title,description)


def spider(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    products = soup.find('ul', {'class': 'productShow'})
    i = 1
    for list_item in products.findAll('li'):
        href = list_item.find('a')
        item_link = "http://www.hisdigital.com/us/"+href.get('href')
        title = list_item.find('h5')
        description = list_item.find('div', {'class': 'text'})
        print "######################Link number "+str(i)+"######################"
        print "item_link = " + item_link
        print "title = " + title.text
        print "description = " + description.text
        visit_single_link(item_link, 1,title.text,description.text)
        i += 1


def queryMaker(card,title,name,cardlink,imglink,description):
    #print description.replace("'","`")
    query = "Insert into graphics values ('" + card + "','" + title + "','" + name.replace("HIS ","") + "','" + cardlink + "','" + imglink + "','" + description.replace("'","`") + "')"
    print query
    cursor.execute(query)


#conn = pyodbc.connect("DRIVER={SQL Server};SERVER=SHAHRIYAR-PC\SQLEXPRESS;DATABASE=hcidb")
conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "",db="hcidb", use_unicode=True, charset="utf8" )
cursor = conn.cursor()

#if table is not created then run this query
#cursor.execute("CREATE TABLE `graphics` (`card` varchar(50) NOT NULL,`title` varchar(100) NOT NULL,`g_name` varchar(200) NOT NULL,`cardlink` varchar(200) DEFAULT NULL,`imglink` varchar(200) DEFAULT NULL,`description` varchar(500) DEFAULT NULL) ENGINE=MyISAM DEFAULT CHARSET=latin1;")
#else
cursor.execute("Truncate table graphics")


reload(sys)
sys.setdefaultencoding('utf-8')
URL = 'http://www.hisdigital.com/us/product-12.shtml'
spider(URL)



cursor.execute("DELETE from graphics where title not in (select distinct(title) from (select * from graphics) as graph where title like 'R%' or title like 'HD%')")


conn.commit()
conn.close()
