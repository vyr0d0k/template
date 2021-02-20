import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
owner = int(os.getenv("owner"))
ip = str(os.getenv("ip"))

docker = str(os.getenv("docker"))

PG_USER = str(os.getenv("PG_USER"))
PG_PASSWORD = str(os.getenv("PG_PASSWORD"))
DATABASE = str(os.getenv("DATABASE"))

admins = [owner]

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

if docker:
    db_host = "database"
else:
    db_host = ip

POSTGRES_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{db_host}/{DATABASE}"
