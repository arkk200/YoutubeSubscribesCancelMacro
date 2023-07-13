from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from dotenv import load_dotenv
import os

from utils import Utils

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

        utils = Utils(driver)

        # 로그인 페이지로 이동
        utils.click_element(By.LINK_TEXT, "로그인")
        print("로그인 페이지로 이동")

        # 이메일 입력
        utils.fill_element(By.ID, "identifierId", email)
        utils.click_element(By.TAG_NAME, "button", (By.ID, "identifierNext"))
        print("이메일 입력")

        # 패스워드 입력 페이지에 다음 버튼이 나올 때까지 기다림 (타임아웃은 10초)
        utils.wait_until_element_located(By.ID, 'passwordNext')

        # 패스워드 입력
        utils.fill_element(By.CSS_SELECTOR, f"input[aria-label='비밀번호 입력']", pw)
        utils.click_element(By.TAG_NAME, 'button', (By.ID, "passwordNext"))



    except Exception as e:
        print("에러 발생", e)
run()

while True:
    pass