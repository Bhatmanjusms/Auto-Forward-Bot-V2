from os import environ 

class Config:
    API_ID = environ.get("API_ID", "977080")
    API_HASH = environ.get("API_HASH", "0c20c4265501492a1513f91755acd42b")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7761446138:AAFALYPeMdVxAdWdD0IN31WVBOGJ91wUGw8") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://abcd:abcd@cluster0.mv320.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '399726799').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
