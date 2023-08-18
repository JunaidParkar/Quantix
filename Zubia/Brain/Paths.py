import os

ZUBIA = os.environ.get('Zubia')
TEMP_FOLDER = f"{ZUBIA}\\Zubia\\Temp"

LOCALAPPDATA = os.environ['LOCALAPPDATA']
LOCALFOLDER = f"{LOCALAPPDATA}\\Zubia"

DATABASE_FOLDER = f"{LOCALFOLDER}\\Database"

CHAT_DATA_FOLDER = f"{DATABASE_FOLDER}\\Chats"
CHAT_DATA_FILE = f"{CHAT_DATA_FOLDER}\\Chats.json"

TRAINED_DATA_FOLDER = f"{DATABASE_FOLDER}\\Train"
TRAINED_DATA_FILE = f"{TRAINED_DATA_FOLDER}\\TrainedData.pth"

APPS_FOLDER = f"{DATABASE_FOLDER}\\Apps"
APPS_FILE = f"{APPS_FOLDER}\\AppsList.json"
APPS_USER_FILE = f"{APPS_FOLDER}\\UserApps.json"

LOCAL_COMMUNITY_FOLDER = f"{LOCALFOLDER}\\Community"
LOCALDATA_CONFIG_FILE = f"{LOCAL_COMMUNITY_FOLDER}\\Config.json"
SOFTWARE_CONFIG_FILE = f"{os.environ['Zubia']}\\Zubia\\Data\\Config.json"

DATASET_FOLDER = f"{LOCALFOLDER}\\Dataset"
LOCALDATA_INTENTS_FILE = f"{DATASET_FOLDER}\\Intents.json"
SOFTWARE_INTENTS_FILE = f"{os.environ['Zubia']}\\Zubia\\Brain\\Datasets\\Intents.json"

CHROME_DRIVER_FOLDER = f"{LOCALFOLDER}\\Chrome"
CHROME_DRIVER_FILE = f"{CHROME_DRIVER_FOLDER}\\Driver.exe"

LOG_FOLDER = f"{LOCALFOLDER}\\Logs"
LOG_SETUP = f"{LOG_FOLDER}\\log.txt"


PRIVATE_1 = "Private1.bin"
PRIVATE_2 = "Private2.bin"
PRIVATE_3 = "Private3.bin"