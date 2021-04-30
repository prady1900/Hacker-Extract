from selenium import webdriver
import urllib.request
import sys

class Downloader:
    def __init__(self):
        url1= str(sys.argv[0])
        n= int(sys.argv[1])
        PATH = "C:\\Program Files (x86)\\chromedriver.exe"
        user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                    "Chrome/90.0.4430.93 Safari/537.36"
        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=800,800")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')

        self.driver = webdriver.Chrome(options=self.options, executable_path=PATH)

        self.driver.get(url1)
        self.images = self.driver.find_elements_by_tag_name("img")
        print(self.images)
        for image in self.images:
            print(image.get_attribute('src'))

        i = 0

        self.sample_input_src = []
        for self.image in self.images:
            i = i + 1
            self.src = self.image.get_attribute('src')
            if "https://s3.amazonaws" in self.src:
                self.sample_input_src.append(self.src)
        j = 0
        for self.src in self.sample_input_src[:-(n+1):-1]:
            j = j + 1
            name = "image" + str(j)+".png"
            urllib.request.urlretrieve(self.src, name)

