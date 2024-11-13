import re
import os
from os import environ
from Script import script
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '13305226'))
API_HASH = environ.get('API_HASH', '8cde2475d6b0cb1162b89ebbac71a95d')
BOT_TOKEN = environ.get('BOT_TOKEN', '6375200576:AAGVJdULNUtf1S2qRaZrXvXlVVytXuzJ-OQ')

PICS = (environ.get('PICS', 'https://graph.org/file/2518d4eb8c88f8f669f4c.jpg https://graph.org/file/d6d9d9b8d2dc779c49572.jpg https://graph.org/file/4b04eaad1e75e13e6dc08.jpg https://graph.org/file/05066f124a4ac500f8d91.jpg https://graph.org/file/2c64ed483c8fcf2bab7dd.jpg')).split() #SAMPLE PIC
START_IMG = environ.get('START_IMG', 'https://graph.org/file/208ae1ffacc082167dbc4.jpg')
QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/208ae1ffacc082167dbc4.jpg')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1258310642').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/vis_hnu_bot")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001906470657'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/asianet_surya_zee')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
DATABASE_URI = environ.get('DATABASE_URI', "")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1002122722037').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ MALLU TV SERIALS</b>")
APPROVED = environ.get("APPROVED_WELCOME", "off").lower()

#chatgptAI
AI = is_enabled((environ.get("AI","False")), True)
OPENAI_API = environ.get("OPENAI_API", " ")
DEEP_API = environ.get("DEEP_API", "3ac9b077-654f-45c6-a1f0-a04a5ef6b69e")
GOOGLE_API_KEY = environ.get("GOOGLE_API_KEY", "AIzaSyD214hhYJ-xf8rfaWX044_g1VEBQ0ua55Q")
AI_LOGS = int(environ.get("AI_LOGS", "-1001906470657")) #GIVE YOUR NEW LOG CHANNEL ID TO STORE MESSAGES THAT THEY SEARCH IN BOT PM.... [ i have added this to keep an eye on the users message, to avoid misuse of Bot ]

DATABASE_NAME = environ.get('DATABASE_NAME', "public")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001906470657'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL','-1001906470657'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1001906470657'))
URL = environ.get('URL', '') # your deployment url
STICKERS_IDS = ('CAACAgUAAxkBAAEC5s1mfmbnUx4f7jYODXqmoDo_QltzLQACmw4AAl3VAVYieASlHlskATUE').split()
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001906470657'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/How_to_Download_7x/35")
SHORTENER_API = environ.get("SHORTENER_API", "f2f53890ad92447149ae0361f89b5449d5b24746")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'publicearn.com')
SHORTENER_API2 = environ.get("SHORTENER_API2", "fd85d405b577f2cd524e5d8a185505383d0d4e97")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'inshorturl.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", '')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip","web-dl" ,"bluray", "hdr", "fhd" , "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f'{i}' for i in range(2024 , 2002,-1 )]
SEASONS = [f'season {i}'for i in range (1 , 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002122722037'))
request_channel = environ.get('REQUEST_CHANNEL', '')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPI_PAY_LOGS = int(environ.get('UPI_PAY_LOGS', '-1001906470657'))
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1001906470657'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
    }
DEFAULT_POST_MODE = {
    'singel_post_mode' : False,
    'all_files_post_mode' : False
}
