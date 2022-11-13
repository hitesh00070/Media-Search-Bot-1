import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'LeoMediaSearchBot'
USER_SESSION = 'User_Bot'
API_ID = 1706730
API_HASH = '14a483d10b9191f077e1a954a131c59e'
BOT_TOKEN = '5690605277:AAHYoufns6U8XiYIQP6kSYfIcnYCFV5cfN8'

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = ['@ravi00893']
CHANNELS = [-1001840839823]
AUTH_USERS = []
AUTH_CHANNEL = -1001814578073

# MongoDB information
DATABASE_URI = "mongodb+srv://cinee:cinee@cluster0.vidvag8.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Messages
default_start_msg = """
**Hi, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

BUTTON = environ.get("BUTTON",False)
FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
