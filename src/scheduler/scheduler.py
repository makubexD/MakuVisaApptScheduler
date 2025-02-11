import random
from datetime import datetime
from scraper.scraper import get_date, get_time 
from scraper.parser import get_available_date, print_dates
from notifications.telegram import send_notification
from selenium.webdriver.common.by import By
from config import APPOINTMENT_URL, RETRY_TIME, COOLDOWN_TIME, STEP_TIME, FACILITY_ID, REGEX_CONTINUE_SUBMIT_BTN
from driver_instance import driver
import requests
from utils.sleep_progress_bar import smart_sleep
from browser.actions import click_element_by_class, wait_for_element_by_xpath, check_element_exists

def reschedule(date):
    time_slot = get_time(date)
    driver.get(APPOINTMENT_URL)

    warning_element = driver.find_element(By.XPATH, '//div[@class="callout secondary animate bounce-in"]')
            
    if warning_element:
        print("Warning element found.")
        click_element_by_class('icheckbox')
        
        wait_for_element_by_xpath(REGEX_CONTINUE_SUBMIT_BTN)

    print("After by passing warning message in RESCHEDULE method") 

    data = {
        # "utf8": driver.find_element(by=By.NAME, value='utf8').get_attribute('value'),
        "authenticity_token": driver.find_element(by=By.NAME, value='authenticity_token').get_attribute('value'),
        "confirmed_limit_message": driver.find_element(by=By.NAME, value='confirmed_limit_message').get_attribute('value'),
        "use_consulate_appointment_capacity": driver.find_element(by=By.NAME, value='use_consulate_appointment_capacity').get_attribute('value'),
        "appointments[consulate_appointment][facility_id]": FACILITY_ID,
        "appointments[consulate_appointment][date]": date,
        "appointments[consulate_appointment][time]": time_slot,
    }

    print("After building data in RESCHEDULE method")
    headers = {
        "User-Agent": driver.execute_script("return navigator.userAgent;"),
        "Referer": APPOINTMENT_URL,
        "Cookie": "_yatri_session=" + driver.get_cookie("_yatri_session")["value"]
    }

    print("After building headers in RESCHEDULE method")
    
    r = requests.post(APPOINTMENT_URL, headers=headers, data=data)    

    if 'Successfully Scheduled' in r.text:
        msg = f"✅ Rescheduled Successfully! {date} {time_slot}"
        send_notification(msg)
    else:
        msg = f"❌ Reschedule Failed. {date} {time_slot}"
        send_notification(msg)

def schedule():
    retry_count = 0
    while 1:
        try:
            print("------------------")
            print(datetime.today())
            print(f"Retry count: {retry_count}")
            print()

            driver.get(APPOINTMENT_URL)
            
            warning_element = driver.find_element(By.XPATH, '//div[@class="callout secondary animate bounce-in"]')
            
            if warning_element:
                print("Warning element found.")
                click_element_by_class('icheckbox')
                
                wait_for_element_by_xpath(REGEX_CONTINUE_SUBMIT_BTN)
                smart_sleep(random.randint(1, 3), "Click Understand checkbox")
           

            smart_sleep(4 * STEP_TIME + random.random(), "Waiting for appointment page to load")
            
            dates = get_date()[:5]

            if not dates:
                cool_time = COOLDOWN_TIME + random.randint(1, 30)                
                msg = f"⚠️ No date available... retrying in {cool_time} sec"
                send_notification(msg)                
                smart_sleep(cool_time, "Cooldown before retry") 
                retry_count += 1
            else:
                print_dates(dates)
                date = get_available_date(dates)
                if date:
                    msg = f"📅 Date available: {date}"
                    send_notification(msg)
                    reschedule(date)
                    break
                else:
                    ret_time = RETRY_TIME + random.randint(1, 30)
                    msg = f"⏳ No earlier date available... retrying in {ret_time} sec"
                    send_notification(msg)                    
                    smart_sleep(ret_time, "Waiting before next retry")
                    retry_count += 1
        except Exception as e:
            msg = f"🚨 Help! Script Crashed: {e}"
            send_notification(msg)
            break