import requests
import threading
from confluent_kafka import Producer
from config import conf
from config import coin_names

### Create coin string for payload

def coinNameString():
    coinNameString.coin_payload = ""
    i = 0
    for element in coin_names:
        i += 1
        if i == 1:
            coinNameString.coin_payload += "'" + element + ","
        if i > 1 and i < len(coin_names):
            coinNameString.coin_payload += element + ","
        if i == len(coin_names):
            coinNameString.coin_payload += element + "'"
    return coinNameString.coin_payload

coinNameString()

### Setup CoinCap API. Include list for Payload with top50 Coins
url = "http://api.coincap.io/v2/assets"

payload = {'ids': 'bitcoin,ethereum,binance-coin,dogecoin,xrp,tether,cardano,polkadot,bitcoin-cash,litecoin,uniswap,chainlink,vechain,stellar,usd-coin,ethereum-classic,theta,solana,tron,filecoin,wrapped-bitcoin,eos,monero,neo,binance-usd,bitcoin-sv,cosmos,terra-luna,iota,ftx-token,aave,tezos,maker,bittorrent,crypto-com-coin,huobi-token,algorand,multi-collateral-dai,thorchain,dash,compound,kusama,matic-network,zcash,nem,waves,elrond-egld,unus-sed-leo,chiliz,zilliqa'}
headers = {}

### create producer
producer = Producer(conf)

### Loop which runs every 10 seconds and produces to Kafka
def producerLoop():
    threading.Timer(10.0, producerLoop).start()
    response = requests.get(url, headers=headers, params=payload)
    producer.produce("Coin_data", response.text)
    producer.flush()
    print(response.text)

producerLoop()