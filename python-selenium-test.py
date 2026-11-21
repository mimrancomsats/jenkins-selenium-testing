from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure Chrome for headless execution
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 1. Start the WebDriver session
driver = webdriver.Chrome(options=options)

# 2. Open a web application
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 3. Retrieve the page title
print("Page Title:", driver.title)

# 4. Find the text box
text_box = driver.find_element(By.NAME, "my-text")

# 5. Enter text into the text box
text_box.send_keys("Hello Selenium!")

# 6. Find and click the Submit button
submit_button = driver.find_element(By.TAG_NAME, "button")
submit_button.click()

# 7. Retrieve the resulting message
message = driver.find_element(By.ID, "message")
print("Result:", message.text)

# 8. Close the browser session
driver.quit()
