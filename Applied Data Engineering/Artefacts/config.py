import socket
# Twitter config

consumer_key="0ZFi0cuJrndWAgiobKQPUENQO"
consumer_secret="lHtSo1GQEcjOPyoAwUzq1VizRvWOWIU1OhHSuxBUbmI1xDqRDQ"
access_token_key="1606201596-ftdWg7dhtSTs36Relg6oSmtJ3WVCsb9OoUcuyFH"
access_token_secret="qx3QbhlrxLHLFXd6b6OVAa4H71TPdkOsEEJjbHpdtW8T3"



# kafka configuration

conf = {'bootstrap.servers': "pkc-e8mp5.eu-west-1.aws.confluent.cloud:9092",
        'sasl.mechanisms': "PLAIN",
        'security.protocol':"SASL_SSL",
        'sasl.username': "O7HO5GLID6YXVOBR",
        'sasl.password': "cvkamMbT8wtNd89GgHJVGX4WIhSO+h3HmFGoFJ3kACmWiFLVf9YdZ8+YaMRe0LfT",
        }

conf_consumer = {'bootstrap.servers': "pkc-e8mp5.eu-west-1.aws.confluent.cloud:9092",
        'group.id': 'David2',
        'client.id': socket.gethostname(),
        'sasl.mechanisms': "PLAIN",
        'security.protocol': "SASL_SSL",
        'sasl.username': "O7HO5GLID6YXVOBR",
        'sasl.password': "cvkamMbT8wtNd89GgHJVGX4WIhSO+h3HmFGoFJ3kACmWiFLVf9YdZ8+YaMRe0LfT",
        'auto.offset.reset': 'earliest',}

coin_symbols = ['BTC', 'ETH', 'BNB', 'DOGE', 'XRP',
                'USDT', 'ADA', 'DOT', 'BCH', 'LTC',
                'UNI', 'LINK', 'VET', 'USDC', 'XLM',
                'ETC', 'THETA', 'SOL', 'TRX', 'FIL',
                'WBTC', 'EOS', 'XMR', 'NEO', 'BUSD',
                'BSV', 'ATOM', 'LUNA', 'MIOTA', 'FTT',
                'AAVE', 'XTZ', 'MKR', 'BTT', 'HT',
                'CRO', 'ALGO', 'DAI', 'RUNE', 'DASH',
                'KSM', 'COMP', 'MATIC', 'ZEC', 'XEM',
                'WAVES', 'EGLD', 'LEO', 'CHZ', 'ZIL']




coin_names = ['bitcoin', 'ethereum', 'binance-coin', 'dogecoin', 'xrp',
              'tether', 'cardano', 'polkadot', 'bitcoin-cash', 'litecoin',
              'uniswap', 'chainlink', 'vechain', 'stellar', 'usd-coin',
              'ethereum-classic', 'theta', 'solana', 'tron', 'filecoin',
              'wrapped-bitcoin', 'eos', 'monero', 'neo', 'binance-usd',
              'bitcoin-sv', 'cosmos', 'terra-luna', 'iota', 'ftx-token',
              'aave', 'tezos', 'maker', 'bittorrent', 'crypto-com-coin',
              'huobi-token', 'algorand', 'multi-collateral-dai', 'thorchain',
              'dash', 'compound', 'kusama', 'matic-network', 'zcash',
              'nem', 'waves', 'elrond-egld', 'unus-sed-leo', 'chiliz', 'zilliqa']