from selenium.webdriver.common.by import By

def test_form_submission(driver):

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_box = driver.find_element(By.NAME, "my-text")
    text_box.send_keys("Hello Selenium!")

    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    message = driver.find_element(By.ID, "message")

    assert message.text == "Received!"
