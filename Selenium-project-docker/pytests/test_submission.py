from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form_submission(driver):

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_box = driver.find_element(By.NAME, "my-text")
    text_box.send_keys("Hello Selenium!")

    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    # Wait up to 10 seconds for the message to appear
    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert message.text == "Received!"
