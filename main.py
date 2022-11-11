import json
import math
import logging

from requests import Session
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode
from config import TELEGRAM_API_TOKEN, COINMARKETCAP_API_TOKEN, \
    BUTTON, MESSAGE, URL, KeyboardsBot, KeyboardsCurrencyIDRBot, CURRENCY_FROM_IDR,\
    CURRENCY_FROM_USD, KeyboardsCurrencyUSDBot

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
kb = KeyboardsBot()
kcb_idr = KeyboardsCurrencyIDRBot()
kcb_usd = KeyboardsCurrencyUSDBot()


async def getInfo(from_c, to_c):  # Function to get the info

    url = URL.COINMARKETCAP.API + "/cryptocurrency/quotes/latest"  # Coinmarketcap API url

    parameters = {'slug': from_c, # ex:bitcoin
                  'convert': to_c}  # ex:USD

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_TOKEN
    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=parameters)

        info = json.loads(response.text)

        # logging.info(info['data']['1']['quote'])
        logging.info(info['data'])
        return info['data']
    except Exception:
        logging.info("Error on http request get into coin marketcap")
        return None

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(MESSAGE.START, reply_markup=kb.btn)


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text in ["hi", "hallo", "hello", "halo"]:
        await msg.reply(MESSAGE.START, reply_markup=kb.btn)
    elif msg.text in ["no", "no thanks", "thanks", "bye"]:
        await msg.reply("Alright bye, Thanks")
    elif msg.text in BUTTON.IDR:
        await msg.reply("Alright, you want to fetch into IDR from which currency?",
                        reply_markup=kcb_idr.btn, parse_mode=ParseMode.MARKDOWN)
    elif msg.text in BUTTON.USD:
        await msg.reply("Alright, you want to fetch into USD from which currency?",
                        reply_markup=kcb_usd.btn, parse_mode=ParseMode.MARKDOWN)
    elif msg.text in CURRENCY_FROM_IDR.BTC:
        mes = await getInfo(from_c="bitcoin", to_c="IDR")
        if mes:
            idr_price = math.ceil(mes['1']['quote']['IDR']['price'])
            message = "1 Bitcoin is equal to RP."+str(idr_price)
            await msg.reply(message)
            await msg.reply("is there anything you want to do?")
        else:
            await msg.reply("bot can't connect to coinmarketcap, please retry in a few minutes")
    elif msg.text in CURRENCY_FROM_IDR.ETH:
        mes = await getInfo(from_c="ethereum", to_c="IDR")
        if mes:
            idr_price = math.ceil(mes['1027']['quote']['IDR']['price'])
            message = "1 Ethereum is equal to RP."+str(idr_price)
            await msg.reply(message)
            await msg.reply("is there anything you want to do?")
        else:
            await msg.reply("bot can't connect to coinmarketcap, please retry in a few minutes")
    elif msg.text in CURRENCY_FROM_USD.BTC:
        mes = await getInfo(from_c="bitcoin", to_c="USD")
        if mes:
            idr_price = math.ceil(mes['1']['quote']['USD']['price'])
            message = "1 Bitcoin is equal to $" + str(idr_price)
            await msg.reply(message)
            await msg.reply("is there anything you want to do?")
        else:
            await msg.reply("bot can't connect to coinmarketcap, please retry in a few minutes")
    elif msg.text in CURRENCY_FROM_USD.ETH:
        mes = await getInfo(from_c="ethereum", to_c="USD")
        if mes:
            idr_price = math.ceil(mes['1027']['quote']['USD']['price'])
            message = "1 Ethereum is equal to $" + str(idr_price)
            await msg.reply(message)
            await msg.reply("is there anything you want to do?")
        else:
            await msg.reply("bot can't connect to coinmarketcap, please retry in a few minutes")
    else:
        await msg.reply("Sorry Bot still learning from the input, not understand your word/sentences.")

if __name__ == '__main__':
    executor.start_polling(dp)
