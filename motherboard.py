import MySQLdb

conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "",db="hcidb", use_unicode=True, charset="utf8" )
cursor = conn.cursor()

#if table is not created then run this query
#cursor.execute("CREATE TABLE `motherboard` (`company` varchar(50) NOT NULL,`m_name` varchar(500) NOT NULL,`chipsetSupport` varchar(50) DEFAULT NULL,`genSupport` varchar(50) DEFAULT NULL) ENGINE=MyISAM DEFAULT CHARSET=latin1;")
#else


cursor.execute("Truncate table motherboard")

cursor.execute("INSERT INTO `motherboard` (`company`, `m_name`, `chipsetSupport`, `genSupport`) VALUES('Gigabyte', 'GA-H81M-S2PV (Rev. 3.0) Intel Socket 1150 Motherboard', 'DDR3', '4'),('Gigabyte', 'GA-B150M-D3H-WP Intel B150 Socket 1151 DDR4 Motherboard', 'DDR3', '6'),('Gigabyte', 'GA-H170-HD3 DDR3 Intel LGA1151 Socket Motherboard', 'DDR3', '6'),('Gigabyte', 'G1.Sniper B7 Intel B150 Socket 1151 Motherboard', 'DDR4', '6'),('Gigabyte', 'GA-Z170-HD3 (rev. 1.0) LGA 1151 Intel Z170 HDMI SATA 6Gb/s USB 3.0 ATX Intel Motherboard', 'DDR4', '6'),('Gigabyte', 'GA-Z170XP-SLI (rev. 1.0) Intel Socket LGA1151 Motherboard', 'DDR4', '6'),('Gigabyte', 'GA-Z170X-Gaming 3 (rev. 1.0) Intel Socket LGA1151 G1 Gaming Motherboard', 'DDR4', '6'),('Gigabyte', 'GA-Z170X-Gaming 7 (rev. 1.0) Intel Socket LGA1151 G1 Gaming Motherboard', 'DDR4', '6'),('Asus', 'P5P41T LE Motherboard LGA775 Socket', 'DDR3', '6'),('Asus', 'H61M-E LGA 1155 Intel H61 (B3) Micro ATX Intel Motherboard', 'DDR3', '6'),('Asus', 'H81M-C LGA 1150 Intel H81 SATA 6Gb/s USB 3.0 Micro ATX Intel Motherboard', 'DDR3', '6'),('Asus', 'H110M-K Intel LGA1151 Socket Motherboard', 'DDR4', '6'),('Asus', 'H110M-D Intel Socket 1151 Motherboard', 'DDR4', '6'),('Asus', 'H110M-A LGA1151 Intel Motherboard', 'DDR4', '6'),('Asus', 'B150M-A D3 LGA1151 Intel Motherboard', 'DDR3', '6'),('Asus', 'B150M-K Intel Socket LGA1151 Motherboard', 'DDR3', '6'),('Asus', 'B150M-A LGA 1151 Intel B150 HDMI SATA 6Gb/s USB 3.0 Micro ATX Intel Motherboard', 'DDR3', '6'),('Asus', 'H170M-E D3 LGA 1151 Intel H170 HDMI SATA 6Gb/s USB 3.0 uATX Intel Motherboard', 'DDR3', '6'),('Asus', 'Q87M-E Socket 1150 Motherboard', 'DDR3', '6'),('Asus', 'GRYPHON Z87 LGA 1150 Intel Z87 HDMI SATA 6Gb/s USB 3.0 uATX Intel Motherboard', 'DDR3', '4'),('Asus', 'Z170-K LGA 1151 Intel Z170 HDMI SATA 6Gb/s USB 3.1 USB 3.0 ATX Intel Motherboard', 'DDR4', '6'),('Asus', 'Z170 PRO GAMING LGA 1151 Intel Z170 HDMI SATA 6Gb/s USB 3.1 USB 3.0 ATX Intel Motherboard', 'DDR4', '6'),('Asus', 'ROG MAXIMUS VIII RANGER LGA 1151 Intel Z170 HDMI SATA 6Gb/s USB 3.1 USB 3.0 ATX Intel Motherboard', 'DDR4', '6'),('Asus', 'ROG MAXIMUS VIII FORMULA Intel Z170 LGA1151 Motherboard', 'DDR4', '6'),('Asus', 'RAMPAGE V EXTREME/U3.1 LGA 2011-v3 Intel X99 SATA 6Gb/s USB 3.0 Extended ATX Intel Motherboard', 'DDR4', '6'),('Gigabyte', 'GA-H110M-DS2 (Rev 1.0) Intel Socket 1151 Motherboard', 'DDR4', '6');")

conn.commit()
conn.close()