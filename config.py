import os

import dotenv

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
REDIS_URL = os.getenv('REDIS_URL')