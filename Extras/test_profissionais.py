# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestProfissionais():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_profissionais(self):
    # Test name: Profissionais
    # Step # | name | target | value
    # 1 | open | https://dashboard.plataformabyou.com.br/visao-geral | 
    self.driver.get("https://dashboard.plataformabyou.com.br/visao-geral")
    # 2 | setWindowSize | 1382x784 | 
    self.driver.set_window_size(1382, 784)
    # 3 | runScript | window.scrollTo(0,169) | 
    self.driver.execute_script("window.scrollTo(0,169)")
    # 4 | click | css=#professionals-button > .MuiListItemIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, "#professionals-button > .MuiListItemIcon-root").click()
    # 5 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 6 | click | css=.MuiTableRow-root:nth-child(4) #more-info-button path | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiTableRow-root:nth-child(4) #more-info-button path").click()
    # 7 | click | id=:rn: | 
    self.driver.find_element(By.ID, ":rn:").click()
    # 8 | click | css=.css-he51f8 | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-he51f8").click()
    # 9 | click | id=:rn: | 
    self.driver.find_element(By.ID, ":rn:").click()
    # 10 | click | id=search-input | 
    self.driver.find_element(By.ID, "search-input").click()
    # 11 | type | id=search-input | Henr
    self.driver.find_element(By.ID, "search-input").send_keys("Henr")
    # 12 | click | css=.css-1nujrx4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-1nujrx4").click()
    # 13 | mouseOver | id=add-button | 
    element = self.driver.find_element(By.ID, "add-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 14 | click | id=add-button | 
    self.driver.find_element(By.ID, "add-button").click()
    # 15 | mouseOut | id=add-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 16 | click | id=registry-edit-textfield-0 | 
    self.driver.find_element(By.ID, "registry-edit-textfield-0").click()
    # 17 | type | id=registry-edit-textfield-0 | 480.947.710-03
    self.driver.find_element(By.ID, "registry-edit-textfield-0").send_keys("480.947.710-03")
    # 18 | click | id=email-edit-textfield-2 | 
    self.driver.find_element(By.ID, "email-edit-textfield-2").click()
    # 19 | type | id=email-edit-textfield-2 | teste@gmail
    self.driver.find_element(By.ID, "email-edit-textfield-2").send_keys("teste@gmail")
    # 20 | click | id=email-edit-textfield-2 | 
    self.driver.find_element(By.ID, "email-edit-textfield-2").click()
    # 21 | type | id=email-edit-textfield-2 | teste@gmail.com
    self.driver.find_element(By.ID, "email-edit-textfield-2").send_keys("teste@gmail.com")
    # 22 | type | id=phoneNumber-edit-textfield-3 | (17) 98198-4196
    self.driver.find_element(By.ID, "phoneNumber-edit-textfield-3").send_keys("(17) 98198-4196")
    # 23 | click | id=name-edit-textfield-4 | 
    self.driver.find_element(By.ID, "name-edit-textfield-4").click()
    # 24 | mouseOver | css=.MuiButton-outlined | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-outlined")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 25 | type | id=name-edit-textfield-4 | Teste de novo 
    self.driver.find_element(By.ID, "name-edit-textfield-4").send_keys("Teste de novo ")
    # 26 | click | css=.MuiButton-outlined | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-outlined").click()
    # 27 | mouseOut | css=.MuiButton-outlined | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 28 | click | css=.css-qs1tjg | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg").click()
    # 29 | click | css=.css-qs1tjg | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg").click()
    # 30 | click | css=.css-qs1tjg | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg").click()
    # 31 | click | css=.css-qs1tjg | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg").click()
    # 32 | doubleClick | css=.css-qs1tjg | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 33 | click | css=.MuiGrid-grid-lg-9 | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-grid-lg-9").click()
    # 34 | click | id=name-edit-textfield-4 | 
    self.driver.find_element(By.ID, "name-edit-textfield-4").click()
    # 35 | mouseOver | css=.MuiButton-outlined | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-outlined")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 36 | mouseOut | css=.MuiButton-outlined | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 37 | click | css=.css-w2aeda | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-w2aeda").click()
    # 38 | click | css=.css-qs1tjg | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg").click()
    # 39 | click | css=.css-qs1tjg | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg").click()
    # 40 | click | css=.css-qs1tjg | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg").click()
    # 41 | click | css=.css-qs1tjg | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg").click()
    # 42 | doubleClick | css=.css-qs1tjg | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-qs1tjg")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 43 | mouseOver | id=close-button | 
    element = self.driver.find_element(By.ID, "close-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 44 | click | id=close-button | 
    self.driver.find_element(By.ID, "close-button").click()
    # 45 | mouseOver | css=#more-info-button path | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#more-info-button path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 46 | click | css=#more-info-button path | 
    self.driver.find_element(By.CSS_SELECTOR, "#more-info-button path").click()
    # 47 | mouseOut | css=#more-info-button path | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 48 | click | id=:r14: | 
    self.driver.find_element(By.ID, ":r14:").click()
    # 49 | click | id=:r14: | 
    self.driver.find_element(By.ID, ":r14:").click()
    # 50 | click | id=:r14: | 
    self.driver.find_element(By.ID, ":r14:").click()
    # 51 | doubleClick | id=:r14: | 
    element = self.driver.find_element(By.ID, ":r14:")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 52 | mouseOver | css=.css-1w2t4ga | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-1w2t4ga")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 53 | click | css=.css-1w2t4ga | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-1w2t4ga").click()
    # 54 | mouseOut | css=.css-1w2t4ga | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 55 | click | css=#edit-button > .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, "#edit-button > .MuiSvgIcon-root").click()
    # 56 | click | id=registry-edit-textfield-0 | 
    self.driver.find_element(By.ID, "registry-edit-textfield-0").click()
    # 57 | click | id=registry-edit-textfield-0 | 
    self.driver.find_element(By.ID, "registry-edit-textfield-0").click()
    # 58 | mouseOver | id=submit-button | 
    element = self.driver.find_element(By.ID, "submit-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 59 | type | id=registry-edit-textfield-0 | 480.947.710-03
    self.driver.find_element(By.ID, "registry-edit-textfield-0").send_keys("480.947.710-03")
    # 60 | click | id=submit-button | 
    self.driver.find_element(By.ID, "submit-button").click()
    # 61 | mouseOut | id=submit-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 62 | click | css=.MuiSvgIcon-colorAction | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiSvgIcon-colorAction").click()
    # 63 | mouseOver | css=.MuiButtonBase-root:nth-child(2) .PrivateSwitchBase-input | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) .PrivateSwitchBase-input")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 64 | click | css=.MuiMenuItem-root:nth-child(1) .MuiTypography-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiMenuItem-root:nth-child(1) .MuiTypography-root").click()
    # 65 | click | css=.MuiButtonBase-root:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3)").click()
    # 66 | click | css=.MuiButtonBase-root:nth-child(4) .MuiTypography-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(4) .MuiTypography-root").click()
    # 67 | click | css=.MuiBackdrop-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root").click()
    # 68 | mouseUp | id=search-input | 
    element = self.driver.find_element(By.ID, "search-input")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
  
