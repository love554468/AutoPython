from selenium import webdriver
import time

web = webdriver.Chrome("F:\FOCUS\chromedriver_win32\chromedriver.exe")
web.get("https://docs.google.com/forms/d/e/1FAIpQLSfntQCPINVhD8eGSm87YCgJnS7Q1E_Ec1NLxGLqMbYxqHoUAw/viewform")

time.sleep(2)

# mail = "ngdbinh2@gmail.com"
email = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
email.send_keys("jhghj@gmail.com")
# //*[@id="i13"]/div[3]/div
# //*[@id="i16"]/div[3]/div
# //*[@id="i19"]/div[3]/div
#//*[@id="i22"]/div[3]/div
# //*[@id="i25"]/div[3]/div

radioASM1 = web.find_element_by_xpath('//*[@id="i13"]/div[3]/div')
radioASM1.click()


emailFunix = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
emailFunix.send_keys("jhgj@funix.edu.vn")


skype = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
skype.send_keys("lihkhk48aba0b5509e53")


sdt = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
sdt.send_keys("08972992328")

# btnSend = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div/div/span')
# btnSend.click()
