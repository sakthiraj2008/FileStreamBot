from os import environ as env
from dotenv import load_dotenv

load_dotenv()

class Telegram:
    API_ID = int(11472991)
    API_HASH = str("c78c50d54baf2173e8b3f75c359c0c72")
    BOT_TOKEN = str("7754306060:AAGBIJsYxqYe9vUPKuCsg5t7i5xS786ufWk")
    OWNER_ID = int(''1430742022')
    WORKERS = int("6")  # 6 workers = 6 commands at once
    DATABASE_URL = str('mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority')
    UPDATES_CHANNEL = str('tn_botz')
    SESSION_NAME = str('FileStream')
    FORCE_SUB_ID =('-1002450932371')
    FORCE_SUB = ('tn_botz')
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int("60")
    FILE_PIC = ("https://envs.sh/EyO.jpg")
    START_PIC = ("https://envs.sh/EyO.jpg")
    VERIFY_PIC = ("https://envs.sh/EyO.jpg")
    MULTI_CLIENT = False
    FLOG_CHANNEL = int("-1002318167392")   # Logs channel for file logs
    ULOG_CHANNEL = int("-1002318167392")   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))

class Server:
    PORT = int(env.get("PORT", 8080))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )



