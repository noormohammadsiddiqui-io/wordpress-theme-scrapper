from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
file = open('url_list.txt', 'r')

for line in file:

    driver.get("https://downloader.la/woocrack-downloader.html")
    input = driver.find_element_by_id("codecyan-download-link")
    input.send_keys(line.strip())
    driver.find_element_by_id("codecyan-download-btn-default").click()
    sleep(5)
    driver.find_elements_by_link_text("Download Now")[0].click()

file.close()
