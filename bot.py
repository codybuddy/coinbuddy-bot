import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC

def wait_(secs=2):
	time.sleep(secs)

def add_to_db(uname, pwd):
	webdriverwait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[class="modal-content"]')))
	div = webdriverwait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[class="add-fut"]')))
	elem = div.find_element_by_tag_name("a")
	browser.execute_script("arguments[0].click();", elem)
	wait_()
	webdriverwait.until(EC.visibility_of_element_located((By.ID, 'username'))).send_keys(uname)
	wait_(2)
	webdriverwait.until(EC.visibility_of_element_located((By.ID, 'psnID'))).send_keys(uname)
	wait_(1)
	webdriverwait.until(EC.visibility_of_element_located((By.ID, 'psnPass'))).send_keys(pwd)
	wait_(1)
	btn = webdriverwait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/modal-container/div/div/modal-add-fut-form/div[2]/form/div[7]/button')))
	btn.click()

def read_from_csv():
	contents = open(input('Enter name of file: '), 'r').readlines()
	for content in contents:
		raw = content.split(',')
		uname, pwd = raw[2], raw[3]
		if uname != '' and pwd != '':
			print(f'[*] Adding {uname},{pwd}')
			add_to_db(uname, pwd)
			wait_(2)
		
def main():
	change_url = 'https://coinbuddy.pro/home'
	# wait for the user to solve the captcha challenge and click the submit button
	print("[*] Waiting for User to Sign in...")
	WebDriverWait(browser, timeout=180, poll_frequency=1).until(EC.url_to_be(change_url))
	print("[*] Log in Successfull...")
	wait_(5)
	browser.get("https://coinbuddy.pro/fut-account")
	read_from_csv()

if __name__ == '__main__':
	ignored_exceptions = (
		NoSuchElementException, 
		StaleElementReferenceException, 
		ElementNotVisibleException, 
		TimeoutException, 
		ElementClickInterceptedException,
	)
	browser = webdriver.Chrome('')
	webdriverwait = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions)
	main_url = 'https://coinbuddy.pro/login'
	browser.get(main_url)