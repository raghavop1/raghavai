from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 23502611))
API_HASH = getenv("API_HASH", "c90db27ac20cdd45b4f349d21d531a79")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", 6325295720))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "raghavsupport")
UPDATE_CHNL = getenv("UPDATE_CHNL", "LOOK_AT_RAGHAV")
OWNER_USERNAME = getenv("OWNER_USERNAME", "RAGHAV_OP")

# Random Start Images
IMG = [
    "https://telegra.ph/file/fedc0ff4d046c99dea1cb.jp",
    "https://telegra.ph/file/2b4fc8638653e40b18000.jpg",
    "https://telegra.ph/file/709a42905d6b2d68f109d.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0Cd3wFvgABBLQGZfR0L9EcupSy8ZqEAedthfVyWNQAAlYKAAKW27FWtDj77ZoqZnIeBA",
    "CAACAgQAAx0Cd3wFvgABBLQSZfR05BbP1c5kKz0EMEZN5Z12A4AAAgoOAAIXGflQaAioNaP5QkceBA",

]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
