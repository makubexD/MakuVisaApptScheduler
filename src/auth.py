from selenium.common.exceptions import TimeoutException
from browser.actions import click_element_by_xpath, wait_for_element_by_xpath, wait_for_element_by_name, refresh_page, input_text_by_id, click_element_by_class, click_element_by_name
from config import USERNAME, PASSWORD, COUNTRY_CODE, STEP_TIME, REGEX_CONTINUE_HREF
from driver_instance import driver
from utils.sleep_progress_bar import smart_sleep

def login():
    driver.get(f"https://ais.usvisa-info.com/{COUNTRY_CODE}/niv")
    smart_sleep(STEP_TIME, "Open login page")

    click_element_by_xpath('//a[@class="down-arrow bounce"]')
    smart_sleep(STEP_TIME, "Click bounce")

    print("Login start...")


    click_element_by_xpath('//*[@id="header"]/nav/div[1]/div[1]/div[2]/div[1]/ul/li[3]/a')
    smart_sleep(STEP_TIME, "Click login")
    
    wait_for_element_by_name("commit")

    click_element_by_xpath('//a[@class="down-arrow bounce"]')
    smart_sleep(STEP_TIME, "Click bounce")

    do_login_action()

def do_login_action():    
    input_text_by_id('user_email', USERNAME)    
    smart_sleep((1, 3), "Input email")
    
    input_text_by_id('user_password', PASSWORD)    
    smart_sleep((1, 3), "Input password")
    
    click_element_by_class('icheckbox')
    smart_sleep((1, 3), "Click privacy checkbox")
    
    click_element_by_name('commit')    
    smart_sleep((1, 3), "Click commit button")

    

    try:
        wait_for_element_by_xpath(REGEX_CONTINUE_HREF)
    except TimeoutException as te:
        print("In TimeOutException")        
        print(te)
        print("In TimeOutException")        
        refresh_page()
        smart_sleep((1, 3), "[TimeoutException]: Refresh page...")
    except Exception as e:        
        print("In Exception")
        print(e)
        print("In Exception")
        refresh_page()
        smart_sleep((1, 3), "[Exception]: Refresh page...")
    
    print("Login successful!")