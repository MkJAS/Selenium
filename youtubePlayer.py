from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains




#assert "Google" in driver.title


class YoutubePlayer:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        
        
        
    def searchYoutube(self, searchTerm):
        
        self.driver.get("https://google.com")
        
        search_bar = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        
        search_bar.clear()
        search_bar.send_keys(searchTerm + Keys.ENTER)
        
        click_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, searchTerm)
        click_link.click()
        
        return self.driver.title
    
    
    
    def searchChannel(self,channelName):
        channel_link = self.driver.find_element(By.NAME, "search_query")
        channel_link.send_keys(channelName + Keys.ENTER)
        
        
        try:
            channel_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "main-link")))
            channel_link = self.driver.find_element(By.ID,  "main-link")
            channel_link.click()
        
            return self.driver.current_url
            
        except NoSuchElementException:
            assert False, "Channel link element not found."
        
        
    
    def playVideo(self):
        
        videoXpath = "//ytd-grid-video-renderer[1]//a[@id='video-title']"
        
        try:
            video_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, videoXpath)))
            video_link = self.driver.find_elements(By.XPATH, videoXpath)
            video_link[0].click()
            
            return self.driver.current_url            
            
            
        except NoSuchElementException:
            assert False, "Video link not found."
        except Exception as e:
            assert False, "Some failure occured: " + e
            
            
    def checkChannel(self): #
        
        channelName = self.driver.find_element(By.ID, "channel-name")
        
        return channelName.text
        
        
        
        
        
def main():
     
    player = YoutubePlayer()
    
    player.searchYoutube("youtube")
    
    player.searchChannel("Northernlion")
    
    player.playVideo()
    
    player.checkChannel()
    
    
    
    
main()
    
    
        
        # Scroll down a little using the PAGE_DOWN key
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.PAGE_DOWN).perform()
        # time.sleep(0.5)
        # actions.send_keys(Keys.ARROW_UP).perform()
        # actions.send_keys(Keys.ARROW_UP).perform()
        # actions.send_keys(Keys.ARROW_UP).perform()
        # time.sleep(0.5)
        
        # click_link = self.driver.find_elements(By.XPATH, "//ytd-grid-video-renderer[1]//a[@id='video-title']")
        # click_link[0].click()
        
        
                
        
        
        
        
        


# try:
    

#     search_bar = driver.find_element(By.CLASS_NAME, "gLFyf")

#     search_bar.clear()
#     search_bar.send_keys("youtube")

#     search_bar.send_keys(Keys.ENTER)
    
#     click_link = driver.find_element(By.PARTIAL_LINK_TEXT, "youtube")
#     click_link.click()
    
    
#     search_bar = driver.find_element(By.NAME, "search_query")
#     search_bar.clear()
    
#     search_bar.send_keys("Northerlion")
#     search_bar.send_keys(Keys.RETURN)
    
#     time.sleep(2)
    
    
#     #click_link = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/div/div[2]/a") 
#     click_link = driver.find_element(By.ID,  "main-link")
#     click_link.click()
    
#     driver.maximize_window()
    
#     time.sleep(2)
    
#     # Scroll down a little using the PAGE_DOWN key
#     actions = ActionChains(driver)
#     actions.send_keys(Keys.PAGE_DOWN).perform()
#     time.sleep(0.5)
#     actions.send_keys(Keys.ARROW_UP).perform()
#     actions.send_keys(Keys.ARROW_UP).perform()
#     actions.send_keys(Keys.ARROW_UP).perform()
#     time.sleep(0.5)
    
#     click_link = driver.find_elements(By.XPATH, "//ytd-grid-video-renderer[1]//a[@id='video-title']")
#     click_link[0].click()
    

# except NoSuchElementException:
#     print("Exception has occured! \nElement not found!")

# finally:
#     time.sleep(5)

#     driver.close()


#assert "No results found." not in driver.page_source



