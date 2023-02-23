from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

token = os.environ["TOKEN"]
#accent_color = 0x209af8

legionmid = 980844839694381066
legionmnotificationsid = 980844840688427013

rsfid = 646322883555098644
rsfnotificationsid = 646322883555098647

kashtanid = 957592822071050250
kashtannotificationsid = 997505816670244894

ugolokid = 1072512832916160534
ugoloknotificationsid = 1078346261532520579