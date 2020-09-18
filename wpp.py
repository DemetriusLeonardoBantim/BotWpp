from selenium import webdriver
import time

class wppBot:
    def __init__(self):
        self.mensagem = "Coloque a mensagem desejada"
        self.grupos = ["Oi"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="Amoreco" class="_3ko75 _5h6Y_ _3Whw5">Amoreco</span>
        #<div tabindex="-1" class="_3uMse">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupo:
            grupos = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat = self.driver.find_elements_by_class_name('_3uMse')
            time.sleep(3)
            chat.click()
            chat.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            botao_enviar.click()
            time.sleep(5)




bot = wppBot()
bot.EnviarMensagens()        
