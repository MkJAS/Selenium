from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get("https://google.com")

#assert "Google" in driver.title


try:
    

    search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")

    search_bar.clear()
    search_bar.send_keys("youtube")

    search_bar.send_keys(Keys.ENTER)
    
    click_link = driver.find_element(By.PARTIAL_LINK_TEXT, "youtube")
    click_link.click()
    
    
    search_bar = driver.find_element(By.NAME, "search_query")
    search_bar.clear()
    
    search_bar.send_keys("Northerlion")
    search_bar.send_keys(Keys.RETURN)
    
    time.sleep(2)
    
    
    #click_link = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/div/div[2]/a") 
    click_link = driver.find_element(By.ID,  "main-link")
    click_link.click()
    
    driver.maximize_window()
    
    time.sleep(2)
    
    # Scroll down a little using the PAGE_DOWN key
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(0.5)
    actions.send_keys(Keys.ARROW_UP).perform()
    actions.send_keys(Keys.ARROW_UP).perform()
    actions.send_keys(Keys.ARROW_UP).perform()
    time.sleep(0.5)
    
    click_link = driver.find_elements(By.XPATH, "//ytd-grid-video-renderer[1]//a[@id='video-title']")
    click_link[0].click()
    

except NoSuchElementException:
    print("Exception has occured! \nElement not found!")

finally:
    time.sleep(5)

    driver.close()


#assert "No results found." not in driver.page_source



