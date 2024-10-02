import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

#Para que este archivo pueda funcionar correctamente es necesario instala las siguientes librerias: selenium y webdriver_manager
"""

pip install selenium
pip install webdriver_manager

"""
# y por si no lo tienes, instala el navegador Chrome (despues se le dará soporte a los demas navegadores)
# Recomendable hacerlo desde su entorno virtual
# Tambien que no te restringan software e interpretes porque luego es molesto no poder actualizar
class WebScrapper:
    def __init__(
        self, 
        dir_dl = fr"C:\Users\{os.getlogin()}\Downloads", 
        usr_agent = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        ):
        self.dl_dir = dir_dl 
        self.usr_agent = usr_agent
        self.driver = self.start()
        self.main_window = self.driver.current_window_handle 
    def start(self):
        try:
            opts = Options()
            prefs = {
                "download.default_directory": self.dl_dir,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True,
                "plugins.always_open_pdf_externally": True,
                "profile.default_content_settings.popups": 0
            }
            opts.add_experimental_option("prefs", prefs)
            opts.add_argument(f"user-agent={self.usr_agent}")
            opts.add_argument('--ignore-certificate-errors')
            opts.add_argument('--ignore-ssl-errors')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
            return driver
        except:
            raise
    def wait_for_element(self, xpath, condition=EC.element_to_be_clickable, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(condition((By.XPATH, xpath)))
        except TimeoutException:
            raise TimeoutException(f"Problema en el xpath: {xpath}")
    def click(self, xpath):
        element = self.wait_for_element(xpath)
        self.driver.execute_script("arguments[0].click();", element)
    def get_text(self, xpath):
        return self.wait_for_element(xpath).text
    def write(self,text, xpath):
        element = self.wait_for_element(xpath)
        self.click(xpath)
        element.clear()
        element.send_keys(text)
    def find_in_select(self,text,xpath):
        element = self.wait_for_element(xpath,EC.presence_of_element_located)
        self.click(xpath)
        element.send_keys(text)
    def go_to(self, new_url):
        self.driver.get(new_url)
    def refr(self):
        self.driver.refresh()
    def switch_iframe(self):
        self.driver.switch_to.frame("hrdIframe")
    def download_by_request(self,filename, url):
        self.driver.get(url)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Levanta una excepción si la respuesta tiene un error
            with open(os.path.join(self.dl_dir, filename), "wb") as file:
                file.write(response.content)
            return f"[+] Archivo {filename} descargado con éxito.\n"
        except requests.RequestException as e:
            return f"[X] Error al descargar archivo {filename}: {e}\n"
    def go_to_popups(self):
        WebDriverWait(self.driver, 60).until(EC.new_window_is_opened)
        all_window_handles = self.driver.window_handles
        popup_window_handle = None
        for handle in all_window_handles:
            if handle != self.main_window:
                popup_window_handle = handle
                break
        self.driver.switch_to.window(popup_window_handle)
    def back_to_main_window(self):
        self.driver.switch_to.window(self.main_window)
    def get_c_url(self):
        return str(self.driver.current_url)
    def close(self):
        self.driver.quit()
    def send_key_enter(self, xpath):
        element = self.wait_for_element(xpath)
        element.send_keys(Keys.ENTER)
    #Experimentales, recomendable usar time.sleep(float) antes de ejecutar esta función
    def get_elements_text(self, xpath):
        self.wait_for_element(xpath, EC.presence_of_element_located, 10)
        elements_str = []
        for element in self.driver.find_elements(By.XPATH, xpath):
            elements_str.append(element.text)
        return elements_str