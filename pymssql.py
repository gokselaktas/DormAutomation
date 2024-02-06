import pymssql

# Veritabanı bağlantı bilgileri
server = 'hatayusuluzurna'  # Örneğin, 'localhost' veya bir IP adresi
database = 'YurtOtomasyon'  
username = 'YOUR_USERNAME'  
password = 'YOUR_PASSWORD'  


# Veritabanına bağlan
conn = pymssql.connect(server, username, password, database)

# Cursor objesi oluştur
cursor = conn.cursor()

cursor.execute('SELECT * FROM your_table_name')


# Sonuçları al
for row in cursor:
    print(row)

# İşimiz bittiğinde cursor ve bağlantıyı kapat
cursor.close()
conn.close()
