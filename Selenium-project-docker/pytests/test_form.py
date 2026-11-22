from selenium.webdriver.common.by import By

def test_text_box(driver):

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_box = driver.find_element(By.NAME, "my-text")

    text_box.send_keys("Hello Selenium!")

    assert text_box.get_attribute("value") == "Hllo Selenium!"
