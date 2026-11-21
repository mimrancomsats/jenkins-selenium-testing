from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_web_form():

    # Configure Chrome for headless execution
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Start WebDriver session
    driver = webdriver.Chrome(options=options)

    try:
        # Open web application
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        # Verify page title
        assert driver.title == "Web form"

        # Find text box and enter text
        text_box = driver.find_element(By.NAME, "my-text")
        text_box.send_keys("Hello Selenium!")

        # Find and click submit button
        submit_button = driver.find_element(By.TAG_NAME, "button")
        submit_button.click()

        # Retrieve resulting message
        message = driver.find_element(By.ID, "message")

        # Verify expected result
        assert message.text == "Received!"

        print("Test Passed!")

    finally:
        # Close browser session
        driver.quit()
