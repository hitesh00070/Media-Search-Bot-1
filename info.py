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
# Messages
START_MSG = """
**Hi, I'm Media Search bot**
Here you can search files in inline mode. Just press follwing buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = 'Please join @.... to use this bot'
