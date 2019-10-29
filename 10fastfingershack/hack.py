from selenium import webdriver
driver = webdriver.Chrome("/home/suryatej/Documents/chromedriver")
driver.get("https://10fastfingers.com/typing-test/english")
driver.maximize_window()
timer_element = driver.find_element_by_xpath('//*[@id="timer"]')
timer = timer_element.get_attribute("innerHTML")
input_element = driver.find_element_by_xpath('//*[@id="inputfield"]')
for i in range(1,350):
	try:
		current_word_element = driver.find_element_by_xpath('//*[@id="row1"]/span[' + str(i) +']' )
		current_word = current_word_element.get_attribute("innerHTML")
		input_element.send_keys(current_word + " ")
		#driver.implicitly_wait(10)
	except:
		break

