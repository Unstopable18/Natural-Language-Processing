from selenium import webdriver
driver=webdriver.Chrome("D:/Chrome_Driver/chromedriver")
driver.get("https://www.amazon.com/s?k=data+science&crid=1POLP446Z7GVQ&sprefix=data+scie%2Caps%2C339&ref=nb_sb_ss_ts-doa-p_2_9")
elements = driver.find_elements("xpath","//span[@class='a-size-base-plus a-color-base a-text-normal']")
i=0
print(driver.title)

for element in elements:
    i+=1
    print("Book No.:",i," "+element.text)

driver.quit()