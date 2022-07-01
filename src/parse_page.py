import os
import re
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def pairwise(t):
    it = iter(t)
    return zip(it, it)


class Driver:
    lock = threading.Lock()
    driver = None

    def __init__(self):
        chrome_options = Options()
        chrome_options.binary_location = os.getenv('CHROME_PATH')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument('--remote-debugging-port=9222')
        chrome_options.add_argument('--enable-extension-activity-logging')
        chrome_options.add_argument(
            '--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--auto-open-devtools-for-tabs')
        chrome_options.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=chrome_options)

    def parse_page(self, url: str):
        self.lock.acquire()
        driver = self.driver
        driver.get(url)

        content_key_dict = {}
        try:
            alert = WebDriverWait(driver=driver, timeout=15).until(
                expected_conditions.alert_is_present())
            alert_text = str(alert.text)
            alert.accept()

            content_key_dict = dict(filter(
                lambda pair: pair[0] != 'Session',
                pairwise(re.sub('[:=]', '', alert_text).strip()
                         [len('WidevineDecryptor'):].split())
            ))
        except:
            print("Somehow can not decrypt by widevine")

        # TODO: selector
        iframe = driver.find_element(
            by=By.CSS_SELECTOR, value=".project-player__video.video-player > div > div > iframe")

        driver.switch_to.frame(iframe)

        mpd_elem = driver.find_element(
            by=By.XPATH, value="//script[contains(text(),'mpd')]")

        mpd_to_find = re.compile(pattern='"https:[^"]*\.mpd[^"]*"')
        mpd_url = str(mpd_to_find.findall(
            mpd_elem.get_attribute('innerHTML'))[0]).replace("\"", "")

        self.lock.release()

        return (mpd_url, content_key_dict)
