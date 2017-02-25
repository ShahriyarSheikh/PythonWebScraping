import MySQLdb

conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "",db="hcidb", use_unicode=True, charset="utf8" )
cursor = conn.cursor()




#if table is not created then run this query
#cursor.execute("CREATE TABLE `ram` (`company` varchar(100) NOT NULL,`r_memory` varchar(50) NOT NULL,`chipset` varchar(100) DEFAULT NULL) ENGINE=MyISAM DEFAULT CHARSET=latin1;")
#else
cursor.execute("Truncate table ram")




cursor.execute("INSERT INTO `ram` (`company`, `r_memory`, `chipset`) VALUES('Kingston', '2GB', 'DDR3 SDRAM'),('Kingston', '4GB', 'DDR3 SDRAM'),('Kingston', '4GB', 'DDR4 SDRAM'),('Kingston', '8GB', 'DDR3 SDRAM'),('Kingston', '8GB', 'DDR4 SDRAM'),('Corsair', '2GB', 'DDR3 DRAM'),('Corsair', '4GB', 'DDR3 DRAM'),('Corsair', '4GB', 'DDR4 DRAM'),('Corsair', '8GB', 'DDR3 DRAM'),('Corsair', '8GB', 'DDR4 DRAM'),('Corsair', '16GB', 'DDR4 DRAM'),('Corsair', '32GB (2x16 GB)', 'DDR4 DRAM');")



cursor.execute("UPDATE ram set chipset = REPLACE(chipset,'DRAM','')")
cursor.execute("UPDATE ram set chipset = REPLACE(chipset,'SDRAM','')")

conn.commit()
conn.close()