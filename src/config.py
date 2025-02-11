import configparser
import os

def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config = load_config(config_path)

USERNAME = config['USVISA']['USERNAME']
PASSWORD = config['USVISA']['PASSWORD']
SCHEDULE_ID = config['USVISA']['SCHEDULE_ID']
MY_SCHEDULE_DATE = config['USVISA']['MY_SCHEDULE_DATE']
COUNTRY_CODE = config['USVISA']['COUNTRY_CODE']
FACILITY_ID = config['USVISA']['FACILITY_ID']

BOT_TOKEN = config['TELEGRAM']['BOT_TOKEN']
USER_ID1 = config['TELEGRAM']['USER_ID1']

SHOW_GUI = config['BROWSEROPTION']['SHOW_GUI']

REGEX_CONTINUE_HREF = "//a[contains(text(),'Continue')]"
REGEX_CONTINUE_SUBMIT_BTN = "//input[@value='Continue']"


STEP_TIME = 0.5
RETRY_TIME = 60 * 7.5
EXCEPTION_TIME = 60 * 30
COOLDOWN_TIME = 60 * 60 * 2

DATE_URL = f"https://ais.usvisa-info.com/{COUNTRY_CODE}/niv/schedule/{SCHEDULE_ID}/appointment/days/{FACILITY_ID}.json?appointments[expedite]=false"
TIME_URL = f"https://ais.usvisa-info.com/{COUNTRY_CODE}/niv/schedule/{SCHEDULE_ID}/appointment/times/{FACILITY_ID}.json?date=%s&appointments[expedite]=false"
APPOINTMENT_URL = f"https://ais.usvisa-info.com/{COUNTRY_CODE}/niv/schedule/{SCHEDULE_ID}/appointment"
EXIT = False