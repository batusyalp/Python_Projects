# Selenium ile kendi twitterıma otomatik giriş işlemini yapmak istedim.
# bunun için find_element(),send_keys(),click() metodlarını kullanarak gerekli kullanıcı adı ve şifrenin
# html kodundaki xpath'ini kopyalayarak bu metodlara aktardım.Daha sonra import ettiğim username ve password bilgilerini
# bu metodlara send_keys() metoduyla gönderdim.

# !!! Webdriver'ın bazı metodlarında değişiklik olduğundan dolayı kod hata verebilir. Yapı olarak bir sorun yok ama bazı metodların
# kaldırılma söz konusu olduğu için hata vermeleri normal.


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


username = 'dogu1_fb'
password = 'Dodo12345'

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def singIn(self):
        self.browser.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoidHIifQ%3D%3D%22%7D")
        time.sleep(3)

        usernameInput = self.browser.find_element(By.XPATH,("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"))
        usernameInput.send_keys(self.username)

        btnSubmit = self.browser.find_element(By.XPATH,("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"))
        btnSubmit.click()

        passwordInput = self.browser.find_element(By.XPATH,("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"))
        passwordInput.send_keys(self.password)

        btnSubmit_1 = self.browser.find_element(By.XPATH,("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"))
        btnSubmit_1.click()

        self.browser.close()


twitter = Twitter(username,password)
# login
twitter.singIn()