from selenium import webdriver
from time import sleep

# driver = webdriver.Chrome(executable_path="./chromedriver")
driver = webdriver.Chrome()
file = open('url_list.txt', 'r')

for line in file:

    driver.get("https://downloader.la/woocrack-downloader.html")
    input = driver.find_element_by_id("codecyan-download-link")
    input.send_keys(line.strip())
    driver.find_element_by_id("codecyan-download-btn-default").click()
    sleep(5)
    driver.find_elements_by_link_text("Download Now")[0].click()

file.close()
