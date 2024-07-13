from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "24401235"))
API_HASH = getenv("API_HASH", "149f7e13d7d861b27cffc3ab1fd52b22")

BOT_TOKEN = getenv("BOT_TOKEN", "6111967692:AAFEXQo6_5LyA9GNJz-m233iS_57eWr1aBk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))

OWNER_ID = int(getenv("OWNER_ID", "1556830659"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c9edc56d1d48a6be8ff29.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/3b21a54c786b4958f265d.jpg")

SESSION = getenv("SESSION", "BQF0VVMAWuGDiIeWtLh05Gm4G4pDPqkKwmIMlZt4YM_Aw8fGLOB4708EtEbXGnH9BY6rDpWSBpy42RajnLQsD0gd3KopQAdSBzPF5k9ZOfiNbxgSs2qSUaDoS8OV2oOTkaQd0wfEXzFDdJPNfQazEV2otte9NcBT68R72rMADL3jjQ3nI1zwC8ECPngdSL_QknDk2EGEga3XSKTyNcr6d0ZMQuGVKQHJ1kocXNGCJtmrpGcS7WYo_r2NBbJBvePi9ZoOe4p7BcXv5oCadPlLeOCfX6PdKMfq0N-rCz8eKtPSo6wQwC4IrEtefcbn3UZMDO2ZR6eNUmlh8gue0MhnroBHlezJSAAAAAGwd90wAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NekoMenfessChat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NekoLocal")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1556830659").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
