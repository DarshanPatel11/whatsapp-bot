import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_last_message(msg):
    msg = str(msg)
    # convert list of all message to string, split at new line and retrieve sender's name and message by slicing
    msg = msg.split("\n")
    return msg[-2].lower(), msg[-3]


option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:/Users/"Your UserName"/AppData/Local/Google/Chrome/User Data')
#i.e, option.add_argument('--user-data-dir=C:/Users/DARSHAN/AppData/Local/Google/Chrome/User Data')
driver = webdriver.Chrome('E:/project/chromedriver', chrome_options=option) #change chromedriver path
driver.get("http://web.whatsapp.com/")
wait = WebDriverWait(driver, 50)
# wait until webpage loads successfully to prevent any exception
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/header/div[1]/div')))
# List of Greetings. or change it to trigger word like commands
greeting_list = ['happy', 'birthday', 'returns', 'bless', 'hbd']
# reply of the greetings. or change it to response of the triggered event
reply = ['Thanks a lot.', 'Thank You Very Much...', 'Thanks.']
while True:
    try:
        content = driver.find_element_by_css_selector('.chat.unread')
        content.click()  # find the unread chat
        # Retrieve all messages of the person
        all_msgs_text_only = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/div/div[3]')
        message, sender = get_last_message(all_msgs_text_only[0].text)
        if any(message.__contains__(s) for s in greeting_list):
            # Xpath to message box
            input_form = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            if sender.endswith("AM") or sender.endswith("PM") or sender.__contains__("UNREAD"):
                # if it's a personal message sender will be time of the message instead of the name of sender
                input_form.send_keys(random.choice(reply))
                input_form.send_keys(Keys.ENTER)
            else:
                input_form.send_keys(random.choice(reply) + "@" + sender)
                input_form.send_keys(Keys.ENTER)  # 1st time is to select person from the list
                input_form.send_keys(Keys.ENTER)  # 2nd time is to send the reply
        time.sleep(2)
    except Exception as e:
        pass
