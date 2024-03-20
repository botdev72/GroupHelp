class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 29348046
    API_HASH = "659a930daaba7940fa4905b4adb1d2b9"

    CASH_API_KEY = "LFV7VYUAR39EBD10"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://fzumwcprktqpge:829c92833eac031ce8ea40541fe1a97418b84b0a5b963f729a3f57b456fdcc13@ec2-3-228-158-221.compute-1.amazonaws.com:5432/d24h7fq4skle5d"  # A sql database url from elephantsql.com

    EVENT_LOGS = -1002130458256  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://pablobprem:neulis10@userbotpremium.pundkfy.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/c394b9d3247403031589d.png"

    SUPPORT_CHAT = "mawingsupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6471400122:AAFUTom4hppJTX5sEGS6nMhmg69Iv01lxUQ"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "V7PYDHHRF6QS"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1086365745  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
