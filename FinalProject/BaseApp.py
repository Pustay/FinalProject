from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru/"
        
    def find_element(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                         message= f'Cant find element by locator{locator}')

    def get_element_property(self, locator, proper):
        element = self.find_element(locator)
        return element.value_of_css_property(proper)

    def go_to_site(self):
        return self.driver.get(self.base_url)    