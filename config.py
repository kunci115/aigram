from emoji import emojize
from aiogram.utils.markdown import pre
from dotenv import load_dotenv, dotenv_values
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os


os.environ['TELEGRAM_BOT_KEY'] = dotenv_values('.env')['TELEGRAM_BOT_KEY']
os.environ['COINMARKETCAP_API_KEY'] = dotenv_values('.env')['COINMARKETCAP_API_KEY']
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_BOT_KEY')
COINMARKETCAP_API_TOKEN = os.getenv('COINMARKETCAP_API_KEY')


class BUTTON:
    IDR = ['Convert to IDR', 'Please convert to idr', 'fetch idr price']
    USD = ['Convert to USD', 'Please conver to usd', 'fetch to usd']


class MESSAGE:
    START = "Welcome to fetcher price bot, right now this bot only cover btc, eth to idr or usd to fetch"


class URL:

    class COINMARKETCAP:
        NAME = 'coinmarketcap'
        API = 'https://pro-api.coinmarketcap.com/v1'


class CURRENCY_FROM_IDR:
    BTC = ['BTC TO IDR', 'Please convert btc to idr', 'convert btc to idr']
    ETH = ['ETH TO IDR', 'Please convert eth to idr', 'convert eth to idr']


class CURRENCY_FROM_USD:
    BTC = ['BTC TO USD', 'Please convert btc to usd', 'convert btc to usd']
    ETH = ['ETH TO USD', 'please convert eth to usd', 'convert eth to usd']


class KeyboardsBot(object):

    def __init__(self):
        self.btn_idr = KeyboardButton(BUTTON.IDR[0])
        self.btn_usd = KeyboardButton(BUTTON.USD[0])
        self.btn = ReplyKeyboardMarkup(
            resize_keyboard=True
        ).row(self.btn_idr, self.btn_usd)


class KeyboardsCurrencyIDRBot(object):
    def __init__(self):
        self.btn_btc = KeyboardButton(CURRENCY_FROM_IDR.BTC[0])
        self.btn_eth = KeyboardButton(CURRENCY_FROM_IDR.ETH[0])
        self.btn = ReplyKeyboardMarkup(
            resize_keyboard=True
        ).row(self.btn_btc, self.btn_eth)


class KeyboardsCurrencyUSDBot(object):
    def __init__(self):
        self.btn_btc = KeyboardButton(CURRENCY_FROM_USD.BTC)
        self.btn_eth = KeyboardButton(CURRENCY_FROM_USD.ETH)
        self.btn = ReplyKeyboardMarkup(
            resize_keyboard=True
        ).row(self.btn_btc, self.btn_eth)



