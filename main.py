from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
from tweets import tweets_list
import random
from config import username, password, path_to_chrome, profile_directory
from webdriver_manager.chrome import ChromeDriverManager


chrome_profile_path = path_to_chrome 

options = webdriver.ChromeOptions()

options.add_argument(f"user-data-dir={chrome_profile_path}")  

options.add_argument(profile_directory) 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


USERNAME = username
PASSWORD = password


post_messages = tweets_list



driver.get("https://x.com/login")
sleep(2)


try:    
    post_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Post text']"))
    )
    print("Post box found!")
    
    post_text = random.choice(post_messages)
  
    post_box.clear()
    
    post_box.send_keys(post_text)
    print("Post message entered successfully!")
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    
    post_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='tweetButtonInline']"))
    )
    print("Post button located!")
    
    driver.execute_script("arguments[0].click();", post_button)
    print("Post published successfully!")

except TimeoutException:
    print("Timeout while waiting for the post box or post button.")

except NoSuchElementException:
    print("Post box or post button element not found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    sleep(5)
    driver.quit()
