from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from browser.driver import get_driver

driver = get_driver()

def click_element_by_xpath(xpath):
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def click_element_by_class(class_name):
    element = driver.find_element(By.CLASS_NAME, class_name)
    element.click()

def click_element_by_name(name):
    element = driver.find_element(By.NAME, name)
    element.click()

def input_text_by_id(identifier, text):
    element = driver.find_element(By.ID, identifier)
    element.send_keys(text)

def wait_for_element_by_xpath(locator, max_wait=10):
    """
    Wait for an element by XPATH with hybrid smart wait.
    """
    return _wait_for_element(locator, By.XPATH, max_wait, visibility=True)

def wait_for_element_by_name(locator, max_wait=10):
    """
    Wait for an element by NAME with hybrid smart wait.
    """
    return _wait_for_element(locator, By.NAME, max_wait)

def _wait_for_element(locator, by_type, max_wait, visibility=False):
    """
    Abstracted method to handle waiting for elements based on the locator type.
    """
    try:        
        Wait(driver, max_wait).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        print("Page is fully loaded.")
                
        element = Wait(driver, max_wait).until(
            EC.visibility_of_element_located((by_type, locator))
        )
                
        if visibility:
            element.click()
            return element
        else:            
            return element

    except Exception as e:        
        print(f"Exception encountered when waiting for element: {locator}")
        print(f"Error: {str(e)}")
        
        import traceback
        print("Traceback:")
        traceback.print_exc()
        
        return None

def check_element_exists(driver, locator, by=By.XPATH):
    """
    Checks if an element exists using find_elements, which avoids exceptions.
    
    :param driver: Selenium WebDriver instance.
    :param locator: The element locator (e.g., XPath, ID, Class, etc.).
    :param by: Locator type (default: By.XPATH).
    :return: True if the element exists, False otherwise.
    """
    return len(driver.find_elements(by, locator)) > 0

def refresh_page():
    driver.refresh()

