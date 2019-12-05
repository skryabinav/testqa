#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import argparse,os,time,csv
from selenium.webdriver.chrome.options import Options


class expsys:
    def __init__(self, debug):
        self.debug=debug
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1366x768')
        if not self.debug:
           chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_window_size(1366, 768)
        if not os.path.exists("/app/report/"):
            os.makedirs("/app/report/")
        self.actions = ActionChains(self.driver)
        self.driver.implicitly_wait(1)

    def info(self,string):
        print(self.OKGREEN+string+self.ENDC)

    def warning(self, string):
        print(self.WARNING + string + self.ENDC)

    def error(self,string):
        print(self.FAIL + string + self.ENDC)
        self.driver.quit()
        exit(111)

    def save_screenshot(self,name):
        basedir="/app/report/step_"
        self.driver.save_screenshot(basedir+name)

    def runner(self):
        self.driver.get("https://google.com/")
        self.save_screenshot("1.png")

        try:
            element = self.driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input")
            element.send_keys("habrahabr")
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("input habrahabr")
        self.save_screenshot("2.png")

        try:
            element = self.driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input")
            element.send_keys(u'\ue007')
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("send enter")
        self.save_screenshot("3.png")

        try:
            for i in self.driver.find_elements_by_tag_name("cite"):
                if "https://habrahabr.ru" in i.text:
                    habr = i.find_element_by_xpath('..').find_element_by_xpath('..')
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("Find habrahabr.ru")

        try:
            self.driver.execute_script("arguments[0].click();", habr)
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("Go habrahabr")
        self.save_screenshot("4.png")

        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[1]/div[2]/div/ul/li[6]/a").click()
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("Go sandbox")
        self.save_screenshot("5.png")

        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[1]/div[3]/div/ul[2]/li[2]/a").click()
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("Go sandbox")
        self.save_screenshot("6.png")

        try:
            Title = self.driver.find_element_by_tag_name("h2")
            titlehref=Title.find_element_by_tag_name("a").get_attribute("href")
            titletext=Title.text
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("Find habrahabr.ru")

        self.driver.get("https://google.com/")
        self.save_screenshot("7.png")

        try:
            element = self.driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input")
            element.send_keys(titletext)
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("input title" +str(inst))
        self.save_screenshot("8.png")

        try:
            element = self.driver.find_element_by_xpath("/html/body/div/div[4]/form/div[2]/div[1]/div[1]/div/div[2]/input")
            element.send_keys(u'\ue007')
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("send enter")
        self.save_screenshot("9.png")

        try:
            self.find=False
            for i in self.driver.find_elements_by_tag_name("a"):
                if titlehref in str(i.get_attribute("href")):
                    self.find=True
                    break
            if self.find:
                self.info("Find on first page google -> " + titlehref)
            else:
                self.warning("Not find on first page google -> " + titlehref)
        except Exception as inst:
            self.save_screenshot("error.png")
            self.error("Find habrahabr.ru"+str(inst))

        self.driver.quit()


def main():
    parser = argparse.ArgumentParser(description='Утилита для тестирования юзабмлити')
    parser.add_argument("-d", "--debug", action='store_true',
                        help="Включаем debug режим - отключаем headless режим браузера")
    args = parser.parse_args()
    if args.debug:
        xpc = expsys(True)
    else:
        xpc = expsys(False)
    xpc.runner()

if __name__ == "__main__":
    main()