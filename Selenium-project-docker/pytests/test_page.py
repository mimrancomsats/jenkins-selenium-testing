def test_page_title(driver):

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    assert driver.title == "Web form"
