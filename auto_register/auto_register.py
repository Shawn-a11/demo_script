from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from imap_tools import MailBox, AND
import os
import time
import re

def setup_driver():
    """设置并返回 Chrome WebDriver"""
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-notifications')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def login_outlook(driver):
    """自动登录 Outlook"""
    # 加载环境变量
    load_dotenv()
    email = os.getenv('OUTLOOK_EMAIL')
    password = os.getenv('OUTLOOK_PASSWORD')
    
    if not email or not password:
        print("请在 .env 文件中设置 OUTLOOK_EMAIL 和 OUTLOOK_PASSWORD")
        return False
    
    try:
        # 访问 Outlook 登录页面
        driver.get('https://outlook.live.com/owa/')
        
        # 等待并点击登录按钮
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-task="signin"]'))
        )
        login_button.click()
        
        # 输入邮箱
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        email_input.send_keys(email)
        
        # 点击下一步
        next_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        next_button.click()
        
        # 输入密码
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        password_input.send_keys(password)
        
        # 点击登录
        sign_in_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        sign_in_button.click()
        
        # 等待登录完成
        time.sleep(5)
        
        print("Outlook 登录成功！")
        return True
        
    except Exception as e:
        print(f"Outlook 登录过程中出现错误: {str(e)}")
        return False

def get_verification_code():
    """从 Outlook 邮箱获取验证码"""
    load_dotenv()
    email = os.getenv('OUTLOOK_EMAIL')
    password = os.getenv('OUTLOOK_PASSWORD')
    imap_server = os.getenv('IMAP_SERVER')
    
    try:
        with MailBox(imap_server).login(email, password) as mailbox:
            # 等待新邮件
            for _ in range(30):  # 最多等待30秒
                for msg in mailbox.fetch(AND(seen=False), limit=1):
                    # 查找验证码（假设验证码是6位数字）
                    code = re.search(r'\b\d{6}\b', msg.text)
                    if code:
                        print(f"找到验证码: {code.group()}")
                        return code.group()
                time.sleep(1)
        print("未找到验证码")
        return None
    except Exception as e:
        print(f"获取验证码时出现错误: {str(e)}")
        return None

def register_account(driver):
    """注册新账号"""
    load_dotenv()
    registration_url = os.getenv('REGISTRATION_URL')
    email = os.getenv('OUTLOOK_EMAIL')
    
    try:
        # 访问注册页面
        driver.get(registration_url)
        
        # 等待页面加载
        time.sleep(3)
        
        # 这里需要根据实际的注册页面元素进行修改
        # 示例：填写邮箱
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        email_input.send_keys(email)
        
        # 点击发送验证码按钮
        send_code_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.send-code'))
        )
        send_code_button.click()
        
        # 等待并获取验证码
        verification_code = get_verification_code()
        if not verification_code:
            print("无法获取验证码")
            return False
        
        # 输入验证码
        code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
        )
        code_input.send_keys(verification_code)
        
        # 点击提交按钮
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit'))
        )
        submit_button.click()
        
        print("注册成功！")
        return True
        
    except Exception as e:
        print(f"注册过程中出现错误: {str(e)}")
        return False

def main():
    driver = setup_driver()
    try:
        # 登录 Outlook
        if not login_outlook(driver):
            return
        
        # 注册新账号
        if not register_account(driver):
            return
        
        # 保持浏览器窗口打开
        input("按回车键关闭浏览器...")
        
    except Exception as e:
        print(f"程序运行过程中出现错误: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main() 