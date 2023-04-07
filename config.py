import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23830477"))
    API_HASH = os.environ.get("API_HASH", "19f8365d98fb11c9cd6c1eaa8b1fa4b8")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6052077988:AAGybcYefy_-Zo_vHACPJvsZKoK_L7SF4Do")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1867884587")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Khrish:12121212@cluster1.gcybfhx.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste1")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQGzyDMAqX6u6kKG0RBwAvUmWUUnFVBijH0Jp79kGJA8Qn_89RGZualZW9AqH9hN11Bnwk1U0m1JSzhw9t0ko1mySuJKC5VH5u-aultQkSGuD6Yvxy01rkQq7ymtuj1GbMF9E3SAGUii9ynAMMeHEMWHKveKNgOr08gb-_aviCxuguVje9duS_3l3Zz-Kc37sLPw0XGflg3jtsNE96d5qpRW8vf25L1qYuW24FmziaYQuCWVzIeU2pjtT6E_91PRL_9kv8aNBH9mp6XS8CM-W5Qkh1hqRZZxivuXS6-KHUJWBBJX9AKo4Sm7nIty6I7S1AIuvPgrU-8bKU5hCxRxE7qaedJ27wAAAAFeaUBpAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626206283"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@leeachhehehehebot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
