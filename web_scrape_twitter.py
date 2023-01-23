from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
driver=webdriver.Chrome("D:/Chrome_Driver/chromedriver")
driver.get('https://twitter.com/search?q=ChatGPT&src=typeahead_click')

time.sleep(5)

div_elements = driver.find_elements("xpath",'//div[@lang]')

for element in div_elements:
    print(element.text)

"""

# importing the necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# setting up the driver options
chrome_options = Options()
chrome_options.add_argument("--headless")

#creating the driver
driver = webdriver.Chrome(executable_path="D:/Chrome_Driver/chromedriver",options=chrome_options)

# navigating to the page
driver.get('https://twitter.com/search?q=ChatGPT&src=typed_query&f=top')

# maximizing the window
driver.maximize_window()

# waiting 5 seconds
time.sleep(5)

# scrolling till end of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# locating the elements
elements = driver.find_elements("xpath","//div[@lang]")

# printing the text inside the element
for element in elements:
    print(element.text)

# closing the driver
driver.quit()
"""