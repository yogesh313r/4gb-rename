import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25393663")
API_HASH = os.environ.get("API_HASH", "46fb840e6cb4b84d582c44ebbf703251")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6475149749:AAEQt9M91pjiNCBF_lkxgVEXdq77S1lT_n0") 

CHANNEL = os.environ.get("CHANNEL", "-1002044312409") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","Renamebott_bot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","BYNF_TamilChat") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","ATL_Univers") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","Yogi_YogiBot")
STRING = os.environ.get("STRING","HI")

DB_NAME = os.environ.get("DB_NAME","renameone")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://karthickjk:karthick@cluster0.vcjskkq.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5324568283').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002121321120"))
