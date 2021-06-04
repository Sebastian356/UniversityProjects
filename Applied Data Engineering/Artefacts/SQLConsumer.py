from confluent_kafka import Consumer, KafkaError
from config import conf_consumer
import pyodbc
import json

c = Consumer(conf_consumer)

c.subscribe(['COINCAP_TWITTER'])


#connect to SQL-DB
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=141.62.117.239,1433;'
                      'Database=kafka;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

while True:
    msg = c.poll(1.0)

    if msg is None:
       continue
    if msg.error():
       if msg.error().code() == KafkaError._PARTITION_EOF:
           continue
       else:
           print(msg.error())
           break



    datastring = json.loads(msg.value().decode('utf-8'))
    keystring = msg.key().decode('utf-8').split(",")
    #zeit = msg.key().decode('utf-8')
    print('msg.key={}'.format(msg.key().decode('utf-8')))
    print('msg.value={}'.format(msg.value()))

    cursor.execute("INSERT INTO CoinTable(symbol, timestamp,\
                    avg_price, marketCapUsd, volumeUsd24Hr,\
                    changePercent24Hr, Anzahl_Tweets)\
                    VALUES (?, ?, ?, ?, ?, ?, ?)",
                   keystring[0][1:],
                   keystring[1][:-1],
                   datastring['AVG_PRICEUSD'],
                   datastring['AVG_MARKETCAPUSD'],
                   datastring['AVG_VOLUMEUSD24HR'],
                   datastring['AVG_CHANGEPERCENT24HR'],
                   datastring['ANZAHL_TWEETS'])
    conn.commit()
c.close()