# Main configuration file

# Mandatory Variables
API_ID = 9330561 # Replace with your actual Telegram API ID
API_HASH = "ec6fba589297d16c8c25201908e82412"  # Replace with your actual Telegram API Hash
BOT_TOKEN = "7986169001:AAGTaiQX3oQj3lDCtAWijmYygbupu-hp2k0"  # Replace with your actual Bot Token
OWNER_ID = "8111395095"  # Replace with your actual Owner ID
# Database
DATABASE_URL = "mongodb+srv://mdtahseen7378:IamTahseen730@wallp1.f6rtttp.mongodb.net/?retryWrites=true&w=majority&appName=wallp1"  # Replace with your actual database URL

AUTH_CHAT = "-1002829458686" # Replace with your actual auth chat ID. You can use multiple IDs separated by ( space ).
LOGS_CHAT = -1002780565967 # Replace with your actual logs chat ID
POST_CHAT = -1002780078654 # Replace with your actual post chat ID

ADMIN_USERNAME = "EntStella" # Replace with your admin username
ADMIN_PASSWORD = "Stella07" # Replace with your admin password


SITE_SECRET = "a9X7cB2LmQ8zF1dE" # Replace with your site secret key
TMDB_API_KEY = "a82ab5641c5430d0873025823ca9971b" # Replace with your TMDB API key

# Optional Variables

# If you want to use multiple bot tokens, uncomment the MULTI_TOKENS dictionary and add your tokens. this aditional bots will speed up the process of downloading and streaming files.
MULTI_TOKENS = {
    1: "7882904808:AAEvov1XiBFsg69sXOAwVafNXiGEi_77ukE",
    2: "7986169001:AAGTaiQX3oQj3lDCtAWijmYygbupu-hp2k0",
    3: "7648223117:AAGSe3JZ7HXbpTK61YyLBK53cZRAYtAOBjU",
}
DELETE_AFTER_MINUTES = 10 # Set the number of minutes after which files will be deleted from user message
POST_UPDATES = True # Set to True if you want to post updates in the post chat
USE_CAPTION = True # Set to True if you want to use captions for posts instead of file names.

# Port configuration
import os
PORT = int(os.environ.get("PORT", 6519))
















# (Don't touch this unless you know what you're doing)
SUDO_USERS = [int(x) for x in (OWNER_ID).split()]
AUTH_CHATS = [int(x) for x in (AUTH_CHAT).split()]
