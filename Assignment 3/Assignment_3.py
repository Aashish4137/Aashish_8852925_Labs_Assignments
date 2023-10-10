# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to YouTube
driver.get("https://www.youtube.com")

# Wait for the page to load
time.sleep(3)

# Find and click on the menu icon
menu_icon = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[1]/yt-icon-button[2]")
menu_icon.click()

# Wait for the menu to appear
time.sleep(2)

# Find and click on the "Trending" option
trending_option = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item")
trending_option.click()

# Wait for the "Trending" page to load
time.sleep(3)

# Find and click on the "Music" category
music_category = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]")
music_category.click()

# Wait for the "Music" category page to load
time.sleep(3)

# Find and click on the first video in the "Music" category
first_video = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a")
first_video.click()

# To add a delay to wait for potential ad to play and Wait for the video to start playing
time.sleep(15)

# Close the WebDriver
driver.quit()
