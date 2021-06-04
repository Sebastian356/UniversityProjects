import pyodbc

#connect to SQL-DB
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=141.62.117.239,1433;'
                      'Database=kafka;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''
                        CREATE TABLE CoinTable
                        (
                        ID int IDENTITY(1,1) PRIMARY KEY,
                        symbol NVARCHAR(50),
                        timestamp NVARCHAR(50),
                        avg_price FLOAT,
                        marketCapUsd FLOAT,
                        volumeUsd24Hr FLOAT,
                        changePercent24Hr FLOAT,
                        Anzahl_Tweets INT
                        )
                  ''')
conn.commit()

