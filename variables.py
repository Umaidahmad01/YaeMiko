# @team_society_1
# @Anime_sub_society


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 20718334  # Get this value from my.telegram.org/apps
    API_HASH = "4e81464b29d79c58d0ad8a0c55ece4a5"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://ierjlkr:OG4dxzO67Zret3Zii43Hhvujkg89WVry0n9KsHE@karma.db.elephantsql.com/ierjlkr"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1002078429106
    MESSAGE_DUMP = -1002078429106

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://Umaid:umaid2008@cluster0.4pofs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Support chat and support ID
    SUPPORT_CHAT = "Pika_Discussion"
    SUPPORT_ID = -1002141181899

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "7231833476:AAGSztw37Jk7xZX8E10-DQkp1aN2-y_gVJ0"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 5585016974
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True
