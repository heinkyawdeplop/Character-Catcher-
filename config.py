class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7887025848"
    sudo_users = "7887025848"
    GROUP_ID = -1003820775782
    TOKEN = "8590198527:AAHQYorkNDHV95GBv8qSW8X2bwcwwXDBnJ4"
    mongo_url = "mongodb://NeoOrinX:OrinX9000@ac-hadowlm-shard-00-00.zpsjvrp.mongodb.net:27017,ac-hadowlm-shard-00-01.zpsjvrp.mongodb.net:27017,ac-hadowlm-shard-00-02.zpsjvrp.mongodb.net:27017/?ssl=true&replicaSet=atlas-y25wtm-shard-0&authSource=admin&appName=Cluster0"
    PHOTO_URL = ["https://files.catbox.moe/7u5o6q.jpg"]
    SUPPORT_CHAT = "orinxwaifu_supchat"
    UPDATE_CHAT = "orinx_updchat"
    BOT_USERNAME = "testorinxbot"
    CHARA_CHANNEL_ID = "-1003070466606"
    api_id = 35078366
    api_hash = "6c5744b9009c3c5b64428259fed1683d"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
