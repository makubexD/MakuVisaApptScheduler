import json
from config import DATE_URL, TIME_URL
from auth import driver

def get_date():
    session = driver.get_cookie("_yatri_session")["value"]
    NEW_GET = driver.execute_script(
        "var req = new XMLHttpRequest();req.open('GET', '"
        + str(DATE_URL)
        + "', false);req.setRequestHeader('Accept', 'application/json, text/javascript, */*; q=0.01');req.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); req.setRequestHeader('Cookie', '_yatri_session="
        + session
        + "'); req.send(null);return req.responseText;"
    )
    return json.loads(NEW_GET)

def get_time(date):
    time_url = TIME_URL % date
    session = driver.get_cookie("_yatri_session")["value"]
    content = driver.execute_script(
        "var req = new XMLHttpRequest();req.open('GET', '"
        + str(time_url)
        + "', false);req.setRequestHeader('Accept', 'application/json, text/javascript, */*; q=0.01');req.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); req.setRequestHeader('Cookie', '_yatri_session="
        + session
        + "'); req.send(null);return req.responseText;"
    )
    data = json.loads(content)
    time = data.get("available_times")[-1]
    print(f"Got time successfully! {date} {time}")
    return time