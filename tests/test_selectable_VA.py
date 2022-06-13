import time
import unittest
from selenium.webdriver.common.by import By
from utils.base_test import BaseTest
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--start-maximized")

BASE_URL = 'https://demoqa.com/selectable'


class TestSelectable(BaseTest):
    def setUp(self) -> None:
        self._setUp(BASE_URL)

    def test_selectable_header_is_displayed(self):
        self.assertEqual(self.driver.current_url, "https://demoqa.com/selectable")
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "main-header"))
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[contains(text(),'Selectable')]"))

    def test_selectable_list_is_displayed(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Selectable')]")
        demo_tab_list = self.driver.find_element(By.ID, "demo-tab-list")
        self.assertTrue(demo_tab_list.is_displayed())

    # includes 1st and 2nd sentences
    def test_selectable_text_is_displayed_1(self):
        list_first_button = self.driver.find_element(By.XPATH, "//li[contains(text(),'Cras justo odio')]")
        self.assertTrue(list_first_button.is_displayed(), 'List first button is not shown.')
        # verifies 'change' is not present in class
        self.assertFalse('active' in list_first_button.get_attribute('class'),
                         'List first button is selected by default.')
        list_first_button.click()
        self.assertTrue('active' in list_first_button.get_attribute('class'),    # verifies 'change' in class
                        'List first button is not selected after clicking on it.')
        # asserts background color
        self.assertEqual(list_first_button.value_of_css_property('background-color'), 'rgba(0, 123, 255, 1)')
        # prints color
        print(f"color: {list_first_button.value_of_css_property('background-color')}")

        # second sentence
        list_second_button = self.driver.find_element(By.XPATH, "//li[contains(text(),'Dapibus ac facilisis in')]")
        self.assertTrue(list_second_button.is_displayed(), 'List second button is not shown')
        self.assertTrue('active' not in list_second_button.get_attribute('class'),
                        'List second button is selected by default')
        list_second_button.click()
        self.assertTrue('active' in list_second_button.get_attribute('class'),
                        'List second button is not selected after clicking on it.')

        # asserts background color
        self.assertEqual(list_second_button.value_of_css_property('background-color'), 'rgba(0, 123, 255, 1)')
        # prints color
        print(f"color: {list_second_button.value_of_css_property('background-color')}")

    # includes 3rd and 4th sentences
    def test_selectable_text_is_displayed_2(self):
        list_third_button = self.driver.find_element(By.XPATH, "//li[contains(text(),'Morbi leo risus')]")
        self.assertTrue(list_third_button.is_displayed(), 'List second button is not shown')
        self.assertFalse('active' in list_third_button.get_attribute('class'),
                         'List third button is selected by default.')
        list_third_button.click()
        self.assertFalse('active' not in list_third_button.get_attribute('class'),
                         'List third button is not selected after clicking on it.')
        self.assertEqual(list_third_button.value_of_css_property('background-color'), 'rgba(0, 123, 255, 1)')
        print(f"color: {list_third_button.value_of_css_property('background-color')}")

        # 4th sentence
        list_forth_button = self.driver.find_element(By.XPATH, "//li[contains(text(),'Porta ac consectetur ac')]")
        self.assertTrue(list_forth_button.is_displayed(), 'List second button is not shown')
        self.assertFalse('active' in list_forth_button.get_attribute('class'),
                         'List forth button is selected by default.')
        list_forth_button.click()
        self.assertFalse('active' not in list_forth_button.get_attribute('class'),
                         'List third button is not selected after clicking on it.')
        self.assertEqual(list_forth_button.value_of_css_property('background-color'), 'rgba(0, 123, 255, 1)')
        print(f"color: {list_forth_button.value_of_css_property('background-color')}")

    def test_selectable_grid_1(self):
        demo_tab_grid = self.driver.find_element(By.ID, "demo-tab-grid")
        self.assertTrue(demo_tab_grid.is_displayed())
        self.driver.find_element(By.ID, "demo-tab-grid").click()

        num_1 = self.driver.find_element(By.CSS_SELECTOR, '#row1>li')   # first number
        self.assertTrue(num_1.is_displayed(), 'Number 1 is not diplayed!')
        self.assertTrue('active' not in num_1.get_attribute('class'),
                        'Number 1 button is selected by default.')
        num_1.click()
        self.assertTrue('active' in num_1.get_attribute('class'),  # verifies 'change' in class
                        'Number one button is not selected after clicking on it.')


if __name__ == '__main__':
    unittest.main()
