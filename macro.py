from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from dotenv import load_dotenv
import os

load_dotenv()

def initDriver():
    driver = uc.Chrome()
    driver.get("https://www.youtube.com")

    return driver

def run():
    try:
        driver = initDriver()
        email = os.environ.get("YOUTUBE_EMAIL")
        pw = os.environ.get("YOUTUBE_PW")

        def find_element(by, value, locator: tuple[str, str] = None):
            if locator == None:
                return driver.find_element(by, value)
            return find_element(locator[0], locator[1]).find_element(by, value)

        def click_element(by, value, locator: tuple[str, str] = None):
            if locator == None:
                find_element(by, value).click()
                return
            
            find_element(locator[0], locator[1]).find_element(by, value).click()
        
        def fill_element(by, value, text):
            print("입력 시작")
            find_element(by, value).send_keys(text)
            print("입력 끝")

        # 로그인 페이지로 이동
        click_element(By.LINK_TEXT, "로그인")
        print("로그인 페이지로 이동")

        # 이메일 입력
        fill_element(By.ID, "identifierId", email)
        click_element(By.TAG_NAME, "button", (By.ID, "identifierNext"))
        print("이메일 입력")

        # 패스워드 입력 페이지에 다음 버튼이 나올 때까지 기다림 (타임아웃은 10초)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'passwordNext')))

        # 패스워드 입력
        fill_element(By.CSS_SELECTOR, f"input[aria-label='비밀번호 입력']", pw)
        click_element(By.TAG_NAME, 'button', (By.ID, "passwordNext"))

    except Exception as e:
        print("에러 발생", e)
run()

while True:
    pass